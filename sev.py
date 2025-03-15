import os
import shutil
import glob
from datetime import datetime

def list_files(directory):
    """List all files in the given directory and count them."""
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    print(f"Total files in directory: {len(files)}")
    return files

def categorize_files(directory):
    """Categorize files by type and count them."""
    categories = {"txt": 0, "csv": 0, "json": 0, "jpg": 0, "png": 0, "log": 0}
    
    for file in os.listdir(directory):
        ext = file.split('.')[-1].lower()
        if ext in categories:
            categories[ext] += 1
    
    for category, count in categories.items():
        print(f"{category.upper()} files: {count}")
    
    return categories

def create_directories(base_directory):
    """Create necessary subdirectories if they do not exist."""
    subdirs = {"text_files": "txt", "csv_files": "csv", "json_files": "json",
               "images": ["jpg", "png"], "logs": "log"}
    
    for subdir in subdirs:
        path = os.path.join(base_directory, subdir)
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"Created directory: {path}")

def move_files(directory, destination):
    """Move files into their respective folders and rename log files with timestamps."""
    moved_files = {"txt": [], "csv": [], "json": [], "jpg": [], "png": [], "log": []}
    subdirs = {"txt": "text_files", "csv": "csv_files", "json": "json_files",
               "jpg": "images", "png": "images", "log": "logs"}
    
    for file in os.listdir(directory):
        ext = file.split('.')[-1].lower()
        if ext in subdirs:
            src = os.path.join(directory, file)
            dst_folder = os.path.join(destination, subdirs[ext])
            
            if ext == "log":
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                new_filename = f"{file.split('.')[0]}_{timestamp}.log"
                dst = os.path.join(dst_folder, new_filename)
            else:
                dst = os.path.join(dst_folder, file)
            
            shutil.move(src, dst)
            moved_files[ext].append(file)
            print(f"Moved {file} to {dst}")
    
    return moved_files

def generate_summary(report_file, categorized_files, moved_files):
    """Generate a summary report of file organization."""
    with open(report_file, "w") as report:
        report.write("Summary Report\n")
        report.write("====================\n")
        
        total_moved = sum(len(files) for files in moved_files.values())
        report.write(f"Total files moved: {total_moved}\n\n")
        
        for category, count in categorized_files.items():
            report.write(f"{category.upper()} files: {count}\n")
            sample_file = moved_files[category][0] if moved_files[category] else "None"
            report.write(f"Sample {category.upper()} file: {sample_file}\n\n")
    
    print(f"Summary report generated: {report_file}")

# Main execution
data_directory = "data_repository"
organized_directory = "organized_data"
report_filename = "summary.txt"

files = list_files(data_directory)
categorized = categorize_files(data_directory)
create_directories(organized_directory)
moved_files = move_files(data_directory, organized_directory)
generate_summary(report_filename, categorized, moved_files)