"""
File management operations for ARIS
"""
import os
import shutil
import logging
from typing import List, Dict, Any, Optional
from datetime import datetime
import json

class FileManager:
    """Handles file and folder operations"""
    
    def __init__(self, base_path: str = "."):
        self.base_path = os.path.abspath(base_path)
        self.logger = logging.getLogger('FileManager')
        self.history_file = "data/file_operations_history.json"
        self.load_history()
    
    def load_history(self):
        """Load file operation history"""
        if os.path.exists(self.history_file):
            try:
                with open(self.history_file, 'r') as f:
                    self.history = json.load(f)
            except:
                self.history = []
        else:
            self.history = []
    
    def save_history(self):
        """Save file operation history"""
        os.makedirs(os.path.dirname(self.history_file), exist_ok=True)
        try:
            with open(self.history_file, 'w') as f:
                json.dump(self.history[-100:], f, indent=2)  # Keep last 100 operations
        except Exception as e:
            self.logger.error(f"Failed to save history: {e}")
    
    def log_operation(self, operation: str, path: str, status: str, details: str = ""):
        """Log a file operation"""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "operation": operation,
            "path": path,
            "status": status,
            "details": details
        }
        self.history.append(entry)
        self.save_history()
    
    def list_directory(self, path: str = None) -> List[Dict[str, Any]]:
        """List contents of a directory"""
        if path is None:
            path = self.base_path
        else:
            path = os.path.join(self.base_path, path)
        
        try:
            items = []
            for item in os.listdir(path):
                item_path = os.path.join(path, item)
                stat = os.stat(item_path)
                
                items.append({
                    "name": item,
                    "path": os.path.relpath(item_path, self.base_path),
                    "type": "folder" if os.path.isdir(item_path) else "file",
                    "size": stat.st_size if os.path.isfile(item_path) else 0,
                    "modified": datetime.fromtimestamp(stat.st_mtime).isoformat(),
                    "extension": os.path.splitext(item)[1] if os.path.isfile(item_path) else ""
                })
            
            return sorted(items, key=lambda x: (x['type'] != 'folder', x['name'].lower()))
        
        except Exception as e:
            self.logger.error(f"Failed to list directory {path}: {e}")
            return []
    
    def create_file(self, path: str, content: str = "") -> bool:
        """Create a new file"""
        full_path = os.path.join(self.base_path, path)
        try:
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(content)
            self.log_operation("create_file", path, "success")
            self.logger.info(f"Created file: {path}")
            return True
        except Exception as e:
            self.log_operation("create_file", path, "failed", str(e))
            self.logger.error(f"Failed to create file {path}: {e}")
            return False
    
    def create_folder(self, path: str) -> bool:
        """Create a new folder"""
        full_path = os.path.join(self.base_path, path)
        try:
            os.makedirs(full_path, exist_ok=True)
            self.log_operation("create_folder", path, "success")
            self.logger.info(f"Created folder: {path}")
            return True
        except Exception as e:
            self.log_operation("create_folder", path, "failed", str(e))
            self.logger.error(f"Failed to create folder {path}: {e}")
            return False
    
    def delete_file(self, path: str) -> bool:
        """Delete a file"""
        full_path = os.path.join(self.base_path, path)
        try:
            if os.path.isfile(full_path):
                os.remove(full_path)
                self.log_operation("delete_file", path, "success")
                self.logger.info(f"Deleted file: {path}")
                return True
            return False
        except Exception as e:
            self.log_operation("delete_file", path, "failed", str(e))
            self.logger.error(f"Failed to delete file {path}: {e}")
            return False
    
    def delete_folder(self, path: str) -> bool:
        """Delete a folder and its contents"""
        full_path = os.path.join(self.base_path, path)
        try:
            if os.path.isdir(full_path):
                shutil.rmtree(full_path)
                self.log_operation("delete_folder", path, "success")
                self.logger.info(f"Deleted folder: {path}")
                return True
            return False
        except Exception as e:
            self.log_operation("delete_folder", path, "failed", str(e))
            self.logger.error(f"Failed to delete folder {path}: {e}")
            return False
    
    def rename(self, old_path: str, new_name: str) -> bool:
        """Rename a file or folder"""
        old_full_path = os.path.join(self.base_path, old_path)
        new_full_path = os.path.join(os.path.dirname(old_full_path), new_name)
        
        try:
            os.rename(old_full_path, new_full_path)
            self.log_operation("rename", old_path, "success", f"to {new_name}")
            self.logger.info(f"Renamed {old_path} to {new_name}")
            return True
        except Exception as e:
            self.log_operation("rename", old_path, "failed", str(e))
            self.logger.error(f"Failed to rename {old_path}: {e}")
            return False
    
    def copy_file(self, source: str, destination: str) -> bool:
        """Copy a file"""
        src_path = os.path.join(self.base_path, source)
        dst_path = os.path.join(self.base_path, destination)
        
        try:
            os.makedirs(os.path.dirname(dst_path), exist_ok=True)
            shutil.copy2(src_path, dst_path)
            self.log_operation("copy_file", source, "success", f"to {destination}")
            self.logger.info(f"Copied {source} to {destination}")
            return True
        except Exception as e:
            self.log_operation("copy_file", source, "failed", str(e))
            self.logger.error(f"Failed to copy {source}: {e}")
            return False
    
    def move_file(self, source: str, destination: str) -> bool:
        """Move a file"""
        src_path = os.path.join(self.base_path, source)
        dst_path = os.path.join(self.base_path, destination)
        
        try:
            os.makedirs(os.path.dirname(dst_path), exist_ok=True)
            shutil.move(src_path, dst_path)
            self.log_operation("move_file", source, "success", f"to {destination}")
            self.logger.info(f"Moved {source} to {destination}")
            return True
        except Exception as e:
            self.log_operation("move_file", source, "failed", str(e))
            self.logger.error(f"Failed to move {source}: {e}")
            return False
    
    def read_file(self, path: str) -> Optional[str]:
        """Read file contents"""
        full_path = os.path.join(self.base_path, path)
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
            self.log_operation("read_file", path, "success")
            return content
        except Exception as e:
            self.log_operation("read_file", path, "failed", str(e))
            self.logger.error(f"Failed to read file {path}: {e}")
            return None
    
    def write_file(self, path: str, content: str) -> bool:
        """Write content to file"""
        full_path = os.path.join(self.base_path, path)
        try:
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(content)
            self.log_operation("write_file", path, "success")
            self.logger.info(f"Wrote to file: {path}")
            return True
        except Exception as e:
            self.log_operation("write_file", path, "failed", str(e))
            self.logger.error(f"Failed to write to file {path}: {e}")
            return False
    
    def search_files(self, query: str, search_path: str = None) -> List[Dict[str, Any]]:
        """Search for files by name"""
        if search_path is None:
            search_path = self.base_path
        else:
            search_path = os.path.join(self.base_path, search_path)
        
        results = []
        query_lower = query.lower()
        
        try:
            for root, dirs, files in os.walk(search_path):
                # Skip hidden and system directories
                dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['__pycache__', 'node_modules']]
                
                for file in files:
                    if query_lower in file.lower():
                        file_path = os.path.join(root, file)
                        rel_path = os.path.relpath(file_path, self.base_path)
                        stat = os.stat(file_path)
                        
                        results.append({
                            "name": file,
                            "path": rel_path,
                            "size": stat.st_size,
                            "modified": datetime.fromtimestamp(stat.st_mtime).isoformat()
                        })
        except Exception as e:
            self.logger.error(f"Search failed: {e}")
        
        return results
    
    def get_file_info(self, path: str) -> Optional[Dict[str, Any]]:
        """Get detailed file information"""
        full_path = os.path.join(self.base_path, path)
        
        try:
            stat = os.stat(full_path)
            
            info = {
                "name": os.path.basename(path),
                "path": path,
                "full_path": full_path,
                "type": "folder" if os.path.isdir(full_path) else "file",
                "size": stat.st_size,
                "size_readable": self._format_size(stat.st_size),
                "created": datetime.fromtimestamp(stat.st_ctime).isoformat(),
                "modified": datetime.fromtimestamp(stat.st_mtime).isoformat(),
                "accessed": datetime.fromtimestamp(stat.st_atime).isoformat(),
                "extension": os.path.splitext(path)[1] if os.path.isfile(full_path) else "",
                "is_readable": os.access(full_path, os.R_OK),
                "is_writable": os.access(full_path, os.W_OK)
            }
            
            return info
        except Exception as e:
            self.logger.error(f"Failed to get file info for {path}: {e}")
            return None
    
    def get_folder_size(self, path: str = None) -> int:
        """Calculate total size of a folder"""
        if path is None:
            path = self.base_path
        else:
            path = os.path.join(self.base_path, path)
        
        total_size = 0
        try:
            for root, dirs, files in os.walk(path):
                for file in files:
                    file_path = os.path.join(root, file)
                    if os.path.exists(file_path):
                        total_size += os.path.getsize(file_path)
        except Exception as e:
            self.logger.error(f"Failed to calculate folder size: {e}")
        
        return total_size
    
    def organize_by_type(self, source_path: str = None) -> Dict[str, int]:
        """Organize files by type into folders"""
        if source_path is None:
            source_path = self.base_path
        else:
            source_path = os.path.join(self.base_path, source_path)
        
        type_mapping = {
            'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.ico'],
            'documents': ['.pdf', '.doc', '.docx', '.txt', '.md', '.rtf'],
            'code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.h'],
            'data': ['.json', '.xml', '.csv', '.xlsx', '.db', '.sql'],
            'archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
            'audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg'],
            'video': ['.mp4', '.avi', '.mkv', '.mov', '.wmv']
        }
        
        organized = {}
        
        try:
            for file in os.listdir(source_path):
                file_path = os.path.join(source_path, file)
                
                if os.path.isfile(file_path):
                    ext = os.path.splitext(file)[1].lower()
                    
                    for folder_name, extensions in type_mapping.items():
                        if ext in extensions:
                            dest_folder = os.path.join(source_path, folder_name)
                            os.makedirs(dest_folder, exist_ok=True)
                            
                            dest_path = os.path.join(dest_folder, file)
                            shutil.move(file_path, dest_path)
                            
                            organized[folder_name] = organized.get(folder_name, 0) + 1
                            break
            
            self.log_operation("organize_by_type", source_path, "success", str(organized))
            return organized
        
        except Exception as e:
            self.logger.error(f"Failed to organize files: {e}")
            return {}
    
    def _format_size(self, size: int) -> str:
        """Format size in bytes to human readable format"""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size < 1024.0:
                return f"{size:.2f} {unit}"
            size /= 1024.0
        return f"{size:.2f} PB"
    
    def get_operation_history(self, limit: int = 20) -> List[Dict[str, Any]]:
        """Get recent file operations"""
        return self.history[-limit:]
