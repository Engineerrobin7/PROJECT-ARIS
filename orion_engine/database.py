# orion_engine/database.py
"""
Database module for persistent storage of user preferences, history, and personalization.
"""
import json
import os
from datetime import datetime
import sqlite3

class Database:
    """Manages persistent storage for ARIS."""
    
    def __init__(self, db_path="data/aris.db"):
        """Initialize database connection."""
        os.makedirs("data", exist_ok=True)
        self.db_path = db_path
        self.conn = None
        self._init_database()
    
    def _init_database(self):
        """Initialize database tables."""
        self.conn = sqlite3.connect(self.db_path)
        cursor = self.conn.cursor()
        
        # User preferences table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS preferences (
                key TEXT PRIMARY KEY,
                value TEXT,
                updated_at TEXT
            )
        ''')
        
        # Conversation history table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS conversations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_input TEXT,
                aris_response TEXT,
                timestamp TEXT,
                sentiment TEXT
            )
        ''')
        
        # User profile table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_profile (
                key TEXT PRIMARY KEY,
                value TEXT,
                updated_at TEXT
            )
        ''')
        
        # Learned facts table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS learned_facts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fact TEXT,
                category TEXT,
                learned_at TEXT
            )
        ''')
        
        self.conn.commit()
    
    def save_preference(self, key, value):
        """Save a user preference."""
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO preferences (key, value, updated_at)
            VALUES (?, ?, ?)
        ''', (key, str(value), datetime.now().isoformat()))
        self.conn.commit()
    
    def get_preference(self, key, default=None):
        """Get a user preference."""
        cursor = self.conn.cursor()
        cursor.execute('SELECT value FROM preferences WHERE key = ?', (key,))
        result = cursor.fetchone()
        return result[0] if result else default
    
    def save_conversation(self, user_input, aris_response, sentiment="neutral"):
        """Save a conversation to history."""
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO conversations (user_input, aris_response, timestamp, sentiment)
            VALUES (?, ?, ?, ?)
        ''', (user_input, aris_response, datetime.now().isoformat(), sentiment))
        self.conn.commit()
    
    def get_recent_conversations(self, limit=10):
        """Get recent conversations."""
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT user_input, aris_response, timestamp
            FROM conversations
            ORDER BY id DESC
            LIMIT ?
        ''', (limit,))
        return cursor.fetchall()
    
    def save_user_profile(self, key, value):
        """Save user profile information."""
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO user_profile (key, value, updated_at)
            VALUES (?, ?, ?)
        ''', (key, str(value), datetime.now().isoformat()))
        self.conn.commit()
    
    def get_user_profile(self, key, default=None):
        """Get user profile information."""
        cursor = self.conn.cursor()
        cursor.execute('SELECT value FROM user_profile WHERE key = ?', (key,))
        result = cursor.fetchone()
        return result[0] if result else default
    
    def learn_fact(self, fact, category="general"):
        """Store a learned fact."""
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO learned_facts (fact, category, learned_at)
            VALUES (?, ?, ?)
        ''', (fact, category, datetime.now().isoformat()))
        self.conn.commit()
    
    def get_facts(self, category=None, limit=10):
        """Retrieve learned facts."""
        cursor = self.conn.cursor()
        if category:
            cursor.execute('''
                SELECT fact, category, learned_at
                FROM learned_facts
                WHERE category = ?
                ORDER BY id DESC
                LIMIT ?
            ''', (category, limit))
        else:
            cursor.execute('''
                SELECT fact, category, learned_at
                FROM learned_facts
                ORDER BY id DESC
                LIMIT ?
            ''', (limit,))
        return cursor.fetchall()
    
    def close(self):
        """Close database connection."""
        if self.conn:
            self.conn.close()
