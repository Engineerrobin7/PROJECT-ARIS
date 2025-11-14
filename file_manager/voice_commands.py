"""
Voice commands for file management
"""
import logging
from typing import Optional
from file_manager.file_operations import FileManager

class FileManagerVoiceCommands:
    """Handle voice commands for file management"""
    
    def __init__(self, file_manager: FileManager = None):
        self.file_manager = file_manager or FileManager()
        self.logger = logging.getLogger('FileManagerVoice')
        self.current_directory = "."
    
    def process_command(self, command: str) -> Optional[str]:
        """Process a file management voice command"""
        command_lower = command.lower()
        
        # List files
        if any(phrase in command_lower for phrase in ["list files", "show files", "what files"]):
            return self._handle_list_files(command)
        
        # Create file
        if "create file" in command_lower or "new file" in command_lower:
            return self._handle_create_file(command)
        
        # Create folder
        if "create folder" in command_lower or "new folder" in command_lower:
            return self._handle_create_folder(command)
        
        # Delete file
        if "delete file" in command_lower or "remove file" in command_lower:
            return self._handle_delete_file(command)
        
        # Delete folder
        if "delete folder" in command_lower or "remove folder" in command_lower:
            return self._handle_delete_folder(command)
        
        # Rename
        if "rename" in command_lower:
            return self._handle_rename(command)
        
        # Copy
        if "copy file" in command_lower:
            return self._handle_copy(command)
        
        # Move
        if "move file" in command_lower:
            return self._handle_move(command)
        
        # Search
        if "search for" in command_lower or "find file" in command_lower:
            return self._handle_search(command)
        
        # File info
        if "file info" in command_lower or "file details" in command_lower:
            return self._handle_file_info(command)
        
        # Organize files
        if "organize files" in command_lower:
            return self._handle_organize(command)
        
        # Folder size
        if "folder size" in command_lower or "how big is" in command_lower:
            return self._handle_folder_size(command)
        
        # Change directory
        if "change directory" in command_lower or "go to folder" in command_lower:
            return self._handle_change_directory(command)
        
        # Operation history
        if "file history" in command_lower or "recent operations" in command_lower:
            return self._handle_history(command)
        
        return None
    
    def _handle_list_files(self, command: str) -> str:
        """List files in current or specified directory"""
        items = self.file_manager.list_directory(self.current_directory)
        
        if not items:
            return "No files found in this directory"
        
        folders = [item for item in items if item['type'] == 'folder']
        files = [item for item in items if item['type'] == 'file']
        
        response = f"Found {len(folders)} folders and {len(files)} files. "
        
        if folders:
            folder_names = [f['name'] for f in folders[:5]]
            response += f"Folders: {', '.join(folder_names)}"
            if len(folders) > 5:
                response += f" and {len(folders) - 5} more. "
        
        if files:
            file_names = [f['name'] for f in files[:5]]
            response += f"Files: {', '.join(file_names)}"
            if len(files) > 5:
                response += f" and {len(files) - 5} more"
        
        return response
    
    def _handle_create_file(self, command: str) -> str:
        """Create a new file"""
        # Extract filename from command
        parts = command.lower().split("create file")
        if len(parts) > 1:
            filename = parts[1].strip().split()[0] if parts[1].strip() else "new_file.txt"
        else:
            filename = "new_file.txt"
        
        # Remove "called" or "named" if present
        filename = filename.replace("called", "").replace("named", "").strip()
        
        if self.file_manager.create_file(filename):
            return f"Created file {filename}"
        return f"Failed to create file {filename}"
    
    def _handle_create_folder(self, command: str) -> str:
        """Create a new folder"""
        parts = command.lower().split("create folder")
        if len(parts) > 1:
            foldername = parts[1].strip().split()[0] if parts[1].strip() else "new_folder"
        else:
            foldername = "new_folder"
        
        foldername = foldername.replace("called", "").replace("named", "").strip()
        
        if self.file_manager.create_folder(foldername):
            return f"Created folder {foldername}"
        return f"Failed to create folder {foldername}"
    
    def _handle_delete_file(self, command: str) -> str:
        """Delete a file"""
        parts = command.lower().split("delete file")
        if len(parts) > 1:
            filename = parts[1].strip().split()[0]
            if self.file_manager.delete_file(filename):
                return f"Deleted file {filename}"
            return f"Failed to delete file {filename}"
        return "Please specify a filename to delete"
    
    def _handle_delete_folder(self, command: str) -> str:
        """Delete a folder"""
        parts = command.lower().split("delete folder")
        if len(parts) > 1:
            foldername = parts[1].strip().split()[0]
            if self.file_manager.delete_folder(foldername):
                return f"Deleted folder {foldername}"
            return f"Failed to delete folder {foldername}"
        return "Please specify a folder name to delete"
    
    def _handle_rename(self, command: str) -> str:
        """Rename a file or folder"""
        # Parse "rename X to Y"
        if " to " in command.lower():
            parts = command.lower().split("rename")[1].split(" to ")
            if len(parts) == 2:
                old_name = parts[0].strip()
                new_name = parts[1].strip()
                
                if self.file_manager.rename(old_name, new_name):
                    return f"Renamed {old_name} to {new_name}"
                return f"Failed to rename {old_name}"
        
        return "Please use format: rename [old name] to [new name]"
    
    def _handle_copy(self, command: str) -> str:
        """Copy a file"""
        if " to " in command.lower():
            parts = command.lower().split("copy file")[1].split(" to ")
            if len(parts) == 2:
                source = parts[0].strip()
                destination = parts[1].strip()
                
                if self.file_manager.copy_file(source, destination):
                    return f"Copied {source} to {destination}"
                return f"Failed to copy {source}"
        
        return "Please use format: copy file [source] to [destination]"
    
    def _handle_move(self, command: str) -> str:
        """Move a file"""
        if " to " in command.lower():
            parts = command.lower().split("move file")[1].split(" to ")
            if len(parts) == 2:
                source = parts[0].strip()
                destination = parts[1].strip()
                
                if self.file_manager.move_file(source, destination):
                    return f"Moved {source} to {destination}"
                return f"Failed to move {source}"
        
        return "Please use format: move file [source] to [destination]"
    
    def _handle_search(self, command: str) -> str:
        """Search for files"""
        parts = command.lower().split("search for")
        if len(parts) < 2:
            parts = command.lower().split("find file")
        
        if len(parts) > 1:
            query = parts[1].strip().split()[0]
            results = self.file_manager.search_files(query)
            
            if not results:
                return f"No files found matching '{query}'"
            
            response = f"Found {len(results)} files matching '{query}': "
            file_names = [r['name'] for r in results[:5]]
            response += ", ".join(file_names)
            
            if len(results) > 5:
                response += f" and {len(results) - 5} more"
            
            return response
        
        return "Please specify what to search for"
    
    def _handle_file_info(self, command: str) -> str:
        """Get file information"""
        parts = command.lower().split("file info")
        if len(parts) < 2:
            parts = command.lower().split("file details")
        
        if len(parts) > 1:
            filename = parts[1].strip().split()[0]
            info = self.file_manager.get_file_info(filename)
            
            if info:
                return (f"{info['name']} is a {info['type']} "
                       f"with size {info['size_readable']}, "
                       f"last modified {info['modified']}")
            return f"Could not get info for {filename}"
        
        return "Please specify a filename"
    
    def _handle_organize(self, command: str) -> str:
        """Organize files by type"""
        result = self.file_manager.organize_by_type(self.current_directory)
        
        if result:
            response = "Organized files: "
            details = [f"{count} {folder}" for folder, count in result.items()]
            response += ", ".join(details)
            return response
        
        return "No files to organize or operation failed"
    
    def _handle_folder_size(self, command: str) -> str:
        """Get folder size"""
        parts = command.lower().split("folder size")
        if len(parts) < 2:
            parts = command.lower().split("how big is")
        
        folder = self.current_directory
        if len(parts) > 1:
            folder = parts[1].strip().split()[0] if parts[1].strip() else folder
        
        size = self.file_manager.get_folder_size(folder)
        readable_size = self.file_manager._format_size(size)
        
        return f"The folder size is {readable_size}"
    
    def _handle_change_directory(self, command: str) -> str:
        """Change current directory"""
        parts = command.lower().split("change directory")
        if len(parts) < 2:
            parts = command.lower().split("go to folder")
        
        if len(parts) > 1:
            new_dir = parts[1].strip().split()[0]
            self.current_directory = new_dir
            return f"Changed directory to {new_dir}"
        
        return "Please specify a directory"
    
    def _handle_history(self, command: str) -> str:
        """Get operation history"""
        history = self.file_manager.get_operation_history(5)
        
        if not history:
            return "No recent file operations"
        
        response = f"Last {len(history)} operations: "
        operations = [f"{h['operation']} on {h['path']}" for h in history]
        response += ", ".join(operations)
        
        return response
