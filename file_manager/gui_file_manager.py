"""
GUI File Manager for ARIS
"""
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog, simpledialog
import os
from datetime import datetime
from file_manager.file_operations import FileManager

class FileManagerGUI:
    """Graphical file manager interface"""
    
    def __init__(self, parent=None):
        if parent:
            self.window = tk.Toplevel(parent)
        else:
            self.window = tk.Tk()
        
        self.window.title("ARIS File Manager")
        self.window.geometry("1000x700")
        self.window.configure(bg='#1e1e2e')
        
        self.file_manager = FileManager()
        self.current_path = "."
        self.selected_items = []
        
        self.setup_ui()
        self.refresh_view()
    
    def setup_ui(self):
        """Setup the user interface"""
        # Toolbar
        toolbar = tk.Frame(self.window, bg='#2e2e3e', height=50)
        toolbar.pack(fill='x', padx=5, pady=5)
        
        # Navigation
        tk.Label(toolbar, text="Path:", bg='#2e2e3e', fg='white', 
                font=('Arial', 10)).pack(side='left', padx=5)
        
        self.path_entry = tk.Entry(toolbar, font=('Arial', 10), bg='#1e1e2e', 
                                   fg='white', width=50)
        self.path_entry.pack(side='left', padx=5)
        self.path_entry.insert(0, self.current_path)
        self.path_entry.bind('<Return>', lambda e: self.navigate_to_path())
        
        tk.Button(toolbar, text="Go", command=self.navigate_to_path,
                 bg='#667eea', fg='white', relief='flat', padx=10).pack(side='left', padx=2)
        
        tk.Button(toolbar, text="↑ Up", command=self.go_up,
                 bg='#667eea', fg='white', relief='flat', padx=10).pack(side='left', padx=2)
        
        tk.Button(toolbar, text="🔄 Refresh", command=self.refresh_view,
                 bg='#667eea', fg='white', relief='flat', padx=10).pack(side='left', padx=2)
        
        # Search
        tk.Label(toolbar, text="Search:", bg='#2e2e3e', fg='white', 
                font=('Arial', 10)).pack(side='left', padx=(20, 5))
        
        self.search_entry = tk.Entry(toolbar, font=('Arial', 10), bg='#1e1e2e', 
                                     fg='white', width=20)
        self.search_entry.pack(side='left', padx=5)
        self.search_entry.bind('<Return>', lambda e: self.search_files())
        
        tk.Button(toolbar, text="🔍", command=self.search_files,
                 bg='#667eea', fg='white', relief='flat', padx=10).pack(side='left')
        
        # Main content area
        content = tk.Frame(self.window, bg='#1e1e2e')
        content.pack(fill='both', expand=True, padx=5, pady=5)
        
        # File list with scrollbar
        list_frame = tk.Frame(content, bg='#2e2e3e')
        list_frame.pack(side='left', fill='both', expand=True)
        
        # Treeview for file list
        columns = ('Name', 'Type', 'Size', 'Modified')
        self.tree = ttk.Treeview(list_frame, columns=columns, show='tree headings', 
                                 selectmode='extended')
        
        # Configure columns
        self.tree.heading('#0', text='')
        self.tree.column('#0', width=30)
        
        for col in columns:
            self.tree.heading(col, text=col, command=lambda c=col: self.sort_by_column(c))
            if col == 'Name':
                self.tree.column(col, width=300)
            elif col == 'Size':
                self.tree.column(col, width=100)
            elif col == 'Modified':
                self.tree.column(col, width=150)
            else:
                self.tree.column(col, width=80)
        
        # Scrollbars
        vsb = ttk.Scrollbar(list_frame, orient="vertical", command=self.tree.yview)
        hsb = ttk.Scrollbar(list_frame, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        
        self.tree.grid(row=0, column=0, sticky='nsew')
        vsb.grid(row=0, column=1, sticky='ns')
        hsb.grid(row=1, column=0, sticky='ew')
        
        list_frame.grid_rowconfigure(0, weight=1)
        list_frame.grid_columnconfigure(0, weight=1)
        
        # Bind double-click
        self.tree.bind('<Double-1>', self.on_double_click)
        self.tree.bind('<Button-3>', self.show_context_menu)
        
        # Side panel
        side_panel = tk.Frame(content, bg='#2e2e3e', width=200)
        side_panel.pack(side='right', fill='y', padx=(5, 0))
        
        tk.Label(side_panel, text="Actions", font=('Arial', 14, 'bold'),
                bg='#2e2e3e', fg='#667eea').pack(pady=10)
        
        actions = [
            ("📄 New File", self.create_file),
            ("📁 New Folder", self.create_folder),
            ("✏️ Rename", self.rename_item),
            ("📋 Copy", self.copy_item),
            ("✂️ Cut", self.cut_item),
            ("📌 Paste", self.paste_item),
            ("🗑️ Delete", self.delete_item),
            ("ℹ️ Properties", self.show_properties),
            ("🔧 Organize", self.organize_files)
        ]
        
        for text, command in actions:
            tk.Button(side_panel, text=text, command=command,
                     bg='#667eea', fg='white', font=('Arial', 10),
                     relief='flat', width=15, anchor='w').pack(pady=3, padx=10)
        
        # Status bar
        status_bar = tk.Frame(self.window, bg='#2e2e3e', height=30)
        status_bar.pack(fill='x', side='bottom')
        
        self.status_label = tk.Label(status_bar, text="Ready", bg='#2e2e3e', 
                                     fg='white', font=('Arial', 9), anchor='w')
        self.status_label.pack(side='left', padx=10)
        
        self.info_label = tk.Label(status_bar, text="", bg='#2e2e3e', 
                                   fg='white', font=('Arial', 9), anchor='e')
        self.info_label.pack(side='right', padx=10)
        
        # Context menu
        self.context_menu = tk.Menu(self.window, tearoff=0, bg='#2e2e3e', fg='white')
        self.context_menu.add_command(label="Open", command=self.open_item)
        self.context_menu.add_command(label="Rename", command=self.rename_item)
        self.context_menu.add_command(label="Copy", command=self.copy_item)
        self.context_menu.add_command(label="Delete", command=self.delete_item)
        self.context_menu.add_separator()
        self.context_menu.add_command(label="Properties", command=self.show_properties)
        
        # Clipboard
        self.clipboard = []
        self.clipboard_action = None  # 'copy' or 'cut'
    
    def refresh_view(self):
        """Refresh the file list"""
        # Clear tree
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Get items
        items = self.file_manager.list_directory(self.current_path)
        
        # Add items to tree
        for item in items:
            icon = '📁' if item['type'] == 'folder' else '📄'
            size = self.file_manager._format_size(item['size']) if item['type'] == 'file' else ''
            modified = datetime.fromisoformat(item['modified']).strftime('%Y-%m-%d %H:%M')
            
            self.tree.insert('', 'end', text=icon, 
                           values=(item['name'], item['type'], size, modified),
                           tags=(item['path'],))
        
        # Update status
        folder_count = len([i for i in items if i['type'] == 'folder'])
        file_count = len([i for i in items if i['type'] == 'file'])
        self.info_label.config(text=f"{folder_count} folders, {file_count} files")
        self.status_label.config(text=f"Viewing: {self.current_path}")
    
    def navigate_to_path(self):
        """Navigate to path in entry"""
        path = self.path_entry.get()
        full_path = os.path.join(self.file_manager.base_path, path)
        
        if os.path.exists(full_path) and os.path.isdir(full_path):
            self.current_path = path
            self.refresh_view()
        else:
            messagebox.showerror("Error", "Path does not exist")
    
    def go_up(self):
        """Go to parent directory"""
        if self.current_path != ".":
            self.current_path = os.path.dirname(self.current_path)
            if not self.current_path:
                self.current_path = "."
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(0, self.current_path)
            self.refresh_view()
    
    def on_double_click(self, event):
        """Handle double-click on item"""
        selection = self.tree.selection()
        if selection:
            item = self.tree.item(selection[0])
            item_type = item['values'][1]
            item_name = item['values'][0]
            
            if item_type == 'folder':
                # Navigate into folder
                self.current_path = os.path.join(self.current_path, item_name)
                self.path_entry.delete(0, tk.END)
                self.path_entry.insert(0, self.current_path)
                self.refresh_view()
            else:
                # Open file
                self.open_item()
    
    def open_item(self):
        """Open selected item"""
        selection = self.tree.selection()
        if selection:
            item = self.tree.item(selection[0])
            item_path = item['tags'][0]
            full_path = os.path.join(self.file_manager.base_path, item_path)
            
            try:
                os.startfile(full_path)  # Windows
            except:
                try:
                    os.system(f'xdg-open "{full_path}"')  # Linux
                except:
                    messagebox.showerror("Error", "Could not open file")
    
    def create_file(self):
        """Create new file"""
        filename = simpledialog.askstring("New File", "Enter filename:")
        if filename:
            path = os.path.join(self.current_path, filename)
            if self.file_manager.create_file(path):
                self.refresh_view()
                self.status_label.config(text=f"Created {filename}")
            else:
                messagebox.showerror("Error", f"Failed to create {filename}")
    
    def create_folder(self):
        """Create new folder"""
        foldername = simpledialog.askstring("New Folder", "Enter folder name:")
        if foldername:
            path = os.path.join(self.current_path, foldername)
            if self.file_manager.create_folder(path):
                self.refresh_view()
                self.status_label.config(text=f"Created {foldername}")
            else:
                messagebox.showerror("Error", f"Failed to create {foldername}")
    
    def rename_item(self):
        """Rename selected item"""
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("Warning", "Please select an item")
            return
        
        item = self.tree.item(selection[0])
        old_name = item['values'][0]
        item_path = item['tags'][0]
        
        new_name = simpledialog.askstring("Rename", f"Rename '{old_name}' to:", 
                                         initialvalue=old_name)
        if new_name and new_name != old_name:
            if self.file_manager.rename(item_path, new_name):
                self.refresh_view()
                self.status_label.config(text=f"Renamed to {new_name}")
            else:
                messagebox.showerror("Error", "Failed to rename")
    
    def copy_item(self):
        """Copy selected items to clipboard"""
        selection = self.tree.selection()
        if selection:
            self.clipboard = [self.tree.item(s)['tags'][0] for s in selection]
            self.clipboard_action = 'copy'
            self.status_label.config(text=f"Copied {len(self.clipboard)} items")
    
    def cut_item(self):
        """Cut selected items to clipboard"""
        selection = self.tree.selection()
        if selection:
            self.clipboard = [self.tree.item(s)['tags'][0] for s in selection]
            self.clipboard_action = 'cut'
            self.status_label.config(text=f"Cut {len(self.clipboard)} items")
    
    def paste_item(self):
        """Paste items from clipboard"""
        if not self.clipboard:
            messagebox.showwarning("Warning", "Clipboard is empty")
            return
        
        for item_path in self.clipboard:
            item_name = os.path.basename(item_path)
            dest_path = os.path.join(self.current_path, item_name)
            
            if self.clipboard_action == 'copy':
                self.file_manager.copy_file(item_path, dest_path)
            elif self.clipboard_action == 'cut':
                self.file_manager.move_file(item_path, dest_path)
        
        if self.clipboard_action == 'cut':
            self.clipboard = []
        
        self.refresh_view()
        self.status_label.config(text="Paste complete")
    
    def delete_item(self):
        """Delete selected items"""
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("Warning", "Please select items to delete")
            return
        
        if messagebox.askyesno("Confirm Delete", 
                              f"Delete {len(selection)} item(s)?"):
            for item_id in selection:
                item = self.tree.item(item_id)
                item_path = item['tags'][0]
                item_type = item['values'][1]
                
                if item_type == 'folder':
                    self.file_manager.delete_folder(item_path)
                else:
                    self.file_manager.delete_file(item_path)
            
            self.refresh_view()
            self.status_label.config(text="Items deleted")
    
    def show_properties(self):
        """Show properties of selected item"""
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("Warning", "Please select an item")
            return
        
        item = self.tree.item(selection[0])
        item_path = item['tags'][0]
        info = self.file_manager.get_file_info(item_path)
        
        if info:
            props = f"""
Name: {info['name']}
Type: {info['type']}
Size: {info['size_readable']}
Path: {info['path']}
Created: {info['created']}
Modified: {info['modified']}
Readable: {info['is_readable']}
Writable: {info['is_writable']}
            """
            messagebox.showinfo("Properties", props)
    
    def organize_files(self):
        """Organize files by type"""
        if messagebox.askyesno("Organize Files", 
                              "Organize files in current folder by type?"):
            result = self.file_manager.organize_by_type(self.current_path)
            if result:
                details = ", ".join([f"{count} {folder}" for folder, count in result.items()])
                messagebox.showinfo("Success", f"Organized: {details}")
                self.refresh_view()
            else:
                messagebox.showinfo("Info", "No files to organize")
    
    def search_files(self):
        """Search for files"""
        query = self.search_entry.get().strip()
        if not query:
            return
        
        results = self.file_manager.search_files(query, self.current_path)
        
        # Clear tree
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Show results
        for result in results:
            icon = '📄'
            size = self.file_manager._format_size(result['size'])
            modified = datetime.fromisoformat(result['modified']).strftime('%Y-%m-%d %H:%M')
            
            self.tree.insert('', 'end', text=icon,
                           values=(result['name'], 'file', size, modified),
                           tags=(result['path'],))
        
        self.status_label.config(text=f"Found {len(results)} results for '{query}'")
    
    def sort_by_column(self, col):
        """Sort tree by column"""
        # Get all items
        items = [(self.tree.set(item, col), item) for item in self.tree.get_children('')]
        
        # Sort
        items.sort()
        
        # Rearrange
        for index, (val, item) in enumerate(items):
            self.tree.move(item, '', index)
    
    def show_context_menu(self, event):
        """Show context menu"""
        item = self.tree.identify_row(event.y)
        if item:
            self.tree.selection_set(item)
            self.context_menu.post(event.x_root, event.y_root)
    
    def run(self):
        """Run the GUI"""
        self.window.mainloop()

def main():
    """Main entry point"""
    app = FileManagerGUI()
    app.run()

if __name__ == "__main__":
    main()
