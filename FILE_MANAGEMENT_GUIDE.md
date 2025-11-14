# ARIS File Management System

## Overview

The ARIS File Management System provides comprehensive file and folder operations through voice commands, GUI interface, and programmatic API.

## Features

### 🎤 Voice Commands

Control files and folders using natural voice commands:

#### Basic Operations

**List Files**
```
"List files"
"Show files"
"What files are here?"
```
Shows all files and folders in the current directory.

**Create File**
```
"Create file report.txt"
"New file document.docx"
"Create file called notes.md"
```
Creates a new file with the specified name.

**Create Folder**
```
"Create folder projects"
"New folder documents"
"Create folder called backup"
```
Creates a new folder with the specified name.

**Delete File**
```
"Delete file old_report.txt"
"Remove file temp.log"
```
Deletes the specified file.

**Delete Folder**
```
"Delete folder old_projects"
"Remove folder temp"
```
Deletes the specified folder and all its contents.

#### Advanced Operations

**Rename**
```
"Rename report.txt to final_report.txt"
"Rename old_folder to new_folder"
```
Renames a file or folder.

**Copy**
```
"Copy file report.txt to backup/report.txt"
"Copy document.pdf to archive/document.pdf"
```
Copies a file to a new location.

**Move**
```
"Move file data.csv to processed/data.csv"
"Move report.pdf to archive/report.pdf"
```
Moves a file to a new location.

**Search**
```
"Search for report"
"Find file containing data"
```
Searches for files matching the query.

**File Information**
```
"File info report.txt"
"File details document.pdf"
```
Shows detailed information about a file.

**Organize Files**
```
"Organize files"
"Organize files by type"
```
Automatically organizes files into folders by type:
- images/ - Image files (.jpg, .png, .gif, etc.)
- documents/ - Document files (.pdf, .doc, .txt, etc.)
- code/ - Code files (.py, .js, .html, etc.)
- data/ - Data files (.json, .csv, .xml, etc.)
- archives/ - Archive files (.zip, .rar, .7z, etc.)
- audio/ - Audio files (.mp3, .wav, etc.)
- video/ - Video files (.mp4, .avi, etc.)

**Folder Size**
```
"Folder size"
"How big is this folder?"
"Folder size projects"
```
Calculates and reports the total size of a folder.

**Navigation**
```
"Change directory to projects"
"Go to folder documents"
```
Changes the current working directory.

**History**
```
"File history"
"Recent operations"
"Show file operations"
```
Shows recent file operations.

---

## 🖥️ GUI File Manager

### Launching

**From Ultimate GUI:**
1. Open ARIS Ultimate GUI
2. Go to "📁 Files" tab
3. Click "📂 Open File Manager"

**Standalone:**
```bash
python file_manager/gui_file_manager.py
```

### Interface Features

#### Toolbar
- **Path Navigation** - Enter or navigate to any path
- **Up Button** - Go to parent directory
- **Refresh** - Reload current directory
- **Search** - Search for files by name

#### File List
- **Tree View** - Hierarchical file display
- **Columns** - Name, Type, Size, Modified date
- **Sorting** - Click column headers to sort
- **Multi-Select** - Select multiple files (Ctrl+Click)
- **Double-Click** - Open files or navigate folders

#### Actions Panel
- 📄 **New File** - Create a new file
- 📁 **New Folder** - Create a new folder
- ✏️ **Rename** - Rename selected item
- 📋 **Copy** - Copy to clipboard
- ✂️ **Cut** - Cut to clipboard
- 📌 **Paste** - Paste from clipboard
- 🗑️ **Delete** - Delete selected items
- ℹ️ **Properties** - View item details
- 🔧 **Organize** - Organize files by type

#### Context Menu
Right-click on any file or folder for quick actions:
- Open
- Rename
- Copy
- Delete
- Properties

#### Status Bar
- Shows current operation status
- Displays file/folder counts
- Shows current path

---

## 💻 Programmatic API

### Basic Usage

```python
from file_manager import FileManager

# Initialize
fm = FileManager()

# List directory
items = fm.list_directory(".")
for item in items:
    print(f"{item['name']} - {item['type']}")

# Create file
fm.create_file("test.txt", "Hello World")

# Create folder
fm.create_folder("new_folder")

# Delete file
fm.delete_file("old_file.txt")

# Rename
fm.rename("old_name.txt", "new_name.txt")

# Copy
fm.copy_file("source.txt", "destination.txt")

# Move
fm.move_file("source.txt", "new_location/source.txt")

# Search
results = fm.search_files("report")
for result in results:
    print(result['path'])

# Get file info
info = fm.get_file_info("document.pdf")
print(f"Size: {info['size_readable']}")
print(f"Modified: {info['modified']}")

# Organize files
organized = fm.organize_by_type("downloads")
print(f"Organized: {organized}")

# Get folder size
size = fm.get_folder_size("projects")
print(f"Size: {fm._format_size(size)}")
```

### Advanced Features

#### Operation History

```python
# Get recent operations
history = fm.get_operation_history(limit=10)
for op in history:
    print(f"{op['timestamp']}: {op['operation']} - {op['path']}")
```

#### Custom Organization

```python
# Organize with custom rules
type_mapping = {
    'python': ['.py', '.pyc'],
    'javascript': ['.js', '.jsx', '.ts'],
    'styles': ['.css', '.scss', '.sass']
}

# Implement custom organization logic
```

---

## 📊 File Information

### Available Properties

When getting file information, the following properties are available:

```python
{
    "name": "document.pdf",
    "path": "documents/document.pdf",
    "full_path": "/full/path/to/document.pdf",
    "type": "file",  # or "folder"
    "size": 1048576,  # bytes
    "size_readable": "1.00 MB",
    "created": "2024-01-01T10:00:00",
    "modified": "2024-01-15T14:30:00",
    "accessed": "2024-01-20T09:15:00",
    "extension": ".pdf",
    "is_readable": True,
    "is_writable": True
}
```

---

## 🔧 Configuration

### Base Path

Set the base path for file operations:

```python
fm = FileManager(base_path="/path/to/directory")
```

### History File

Operation history is stored in:
```
data/file_operations_history.json
```

Last 100 operations are kept.

---

## 🎯 Use Cases

### 1. Project Organization

```
"Organize files"
```
Automatically sorts files into appropriate folders.

### 2. Backup Creation

```
"Copy file important.doc to backup/important.doc"
```
Creates backups of important files.

### 3. Cleanup

```
"Delete file temp.log"
"Delete folder old_cache"
```
Removes temporary and unnecessary files.

### 4. File Search

```
"Search for report"
```
Quickly finds files across directories.

### 5. Batch Operations

Use GUI to:
1. Select multiple files (Ctrl+Click)
2. Copy or cut them
3. Navigate to destination
4. Paste

---

## 🚀 Integration with ARIS

### Voice Control

File management is fully integrated with ARIS voice commands:

```python
# In aris_enhanced.py
aris = ARISEnhanced()
response = aris.process_command("list files")
print(response)
```

### GUI Integration

File manager is accessible from the Ultimate GUI:
- Tab: "📁 Files"
- Button: "📂 Open File Manager"

### Web Dashboard

File operations can be triggered via web dashboard:
```javascript
fetch('/api/command', {
    method: 'POST',
    body: JSON.stringify({command: 'list files'})
})
```

---

## 📝 Examples

### Example 1: Daily Cleanup

```python
from file_manager import FileManager

fm = FileManager()

# Organize downloads folder
fm.organize_by_type("downloads")

# Delete old temp files
temp_files = fm.search_files(".tmp")
for file in temp_files:
    fm.delete_file(file['path'])
```

### Example 2: Project Backup

```python
import os
from datetime import datetime

fm = FileManager()

# Create backup folder with timestamp
backup_name = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
fm.create_folder(backup_name)

# Copy all Python files
py_files = fm.search_files(".py")
for file in py_files:
    dest = os.path.join(backup_name, file['name'])
    fm.copy_file(file['path'], dest)
```

### Example 3: File Report

```python
fm = FileManager()

# Get all files
items = fm.list_directory(".")

# Generate report
total_size = 0
file_types = {}

for item in items:
    if item['type'] == 'file':
        total_size += item['size']
        ext = item['extension']
        file_types[ext] = file_types.get(ext, 0) + 1

print(f"Total size: {fm._format_size(total_size)}")
print(f"File types: {file_types}")
```

---

## 🔒 Safety Features

### Confirmation Required

Destructive operations (delete, move) are logged and can be reviewed.

### Operation History

All operations are logged with:
- Timestamp
- Operation type
- File path
- Status (success/failed)
- Error details (if failed)

### Error Handling

All operations include try-catch blocks and return status indicators.

---

## 🎨 Customization

### Custom File Types

Add custom file type categories for organization:

```python
# In file_operations.py, modify organize_by_type()
type_mapping = {
    'my_category': ['.custom', '.special'],
    # ... existing mappings
}
```

### Custom Voice Commands

Add custom file management commands:

```python
# In extensions/custom_commands.py
manager.add_command(
    trigger="backup everything",
    action_type="run_script",
    action_data="python backup_script.py",
    response="Starting backup"
)
```

---

## 📚 API Reference

### FileManager Class

#### Methods

**list_directory(path=None)**
- Returns: List[Dict] - List of files and folders
- Parameters: path (optional) - Directory to list

**create_file(path, content="")**
- Returns: bool - Success status
- Parameters: path, content (optional)

**create_folder(path)**
- Returns: bool - Success status
- Parameters: path

**delete_file(path)**
- Returns: bool - Success status
- Parameters: path

**delete_folder(path)**
- Returns: bool - Success status
- Parameters: path

**rename(old_path, new_name)**
- Returns: bool - Success status
- Parameters: old_path, new_name

**copy_file(source, destination)**
- Returns: bool - Success status
- Parameters: source, destination

**move_file(source, destination)**
- Returns: bool - Success status
- Parameters: source, destination

**read_file(path)**
- Returns: Optional[str] - File contents
- Parameters: path

**write_file(path, content)**
- Returns: bool - Success status
- Parameters: path, content

**search_files(query, search_path=None)**
- Returns: List[Dict] - Matching files
- Parameters: query, search_path (optional)

**get_file_info(path)**
- Returns: Optional[Dict] - File information
- Parameters: path

**get_folder_size(path=None)**
- Returns: int - Size in bytes
- Parameters: path (optional)

**organize_by_type(source_path=None)**
- Returns: Dict[str, int] - Organization results
- Parameters: source_path (optional)

**get_operation_history(limit=20)**
- Returns: List[Dict] - Recent operations
- Parameters: limit (optional)

---

## 🐛 Troubleshooting

### Issue: "Permission Denied"

**Solution:** Ensure ARIS has read/write permissions for the directory.

### Issue: "File Not Found"

**Solution:** Check the file path and current directory.

### Issue: "Operation Failed"

**Solution:** Check the operation history for error details:
```python
history = fm.get_operation_history(limit=5)
for op in history:
    if op['status'] == 'failed':
        print(op['details'])
```

---

## 🎓 Best Practices

1. **Always check return values** - Operations return bool for success/failure
2. **Use relative paths** - Paths are relative to base_path
3. **Review history** - Check operation history for debugging
4. **Organize regularly** - Use organize_by_type() to keep folders clean
5. **Backup important files** - Use copy operations before destructive actions

---

## 📄 License

Part of ARIS Ultimate - MIT License

---

**ARIS File Management - Organize Your Digital Life** 📁
