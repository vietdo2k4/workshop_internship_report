import os
import sys
import shutil
import argparse
from PIL import Image, ImageFilter

# Force stdout and stderr to UTF-8 encoding for Vietnamese characters
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')


# Default configuration for the Unsharp Mask sharpening filter
# Unsharp Mask helps detect edges and increase contrast without creating pixelated artifacts.
DEFAULT_RADIUS = 1.5      # Radius of the blur filter. Lower = sharper fine detail, Higher = wider edges.
DEFAULT_PERCENT = 150     # Sharpening strength (percentage). Typically between 100% and 200%.
DEFAULT_THRESHOLD = 3     # Minimum change required to sharpen a pixel. Prevents noise enhancement.

def to_win_long_path(path):
    """
    Converts a path to a Windows long path (prefixed with \\\\?\\) to bypass MAX_PATH limits.
    """
    path = os.path.abspath(path)
    if os.name == 'nt':
        # Replace forward slashes with backslashes for Windows API compatibility
        path = path.replace('/', '\\')
        if not path.startswith('\\\\?\\'):
            path = '\\\\?\\' + path
    return path

def sharpen_image(file_path, backup_path, radius, percent, threshold):
    """
    Sharpens a single image file, backing up the original first.
    """
    try:
        # Convert to Windows long paths to support paths longer than 260 characters
        file_path_long = to_win_long_path(file_path)
        backup_path_long = to_win_long_path(backup_path)
        
        # Create backup directories if they don't exist
        os.makedirs(os.path.dirname(backup_path_long), exist_ok=True)
        
        # Copy original file to backup location (only if not already backed up to preserve first original)
        if not os.path.exists(backup_path_long):
            shutil.copy2(file_path_long, backup_path_long)
            print(f"Backed up: {file_path} -> {backup_path}")
        else:
            print(f"Backup already exists, skipping copy for safety: {backup_path}")

        # Open the image file
        with Image.open(file_path_long) as img:
            # Preserve original format and color mode (RGB, RGBA, etc.)
            original_format = img.format
            original_mode = img.mode
            
            # Apply Unsharp Mask filter
            # Note: UnsharpMask is best for screen captures and photographic content
            sharpened_img = img.filter(ImageFilter.UnsharpMask(radius=radius, percent=percent, threshold=threshold))
            
            # Save back to the original file
            if original_format == 'PNG':
                sharpened_img.save(file_path_long, format=original_format, optimize=True)
            elif original_format in ['JPEG', 'JPG']:
                sharpened_img.save(file_path_long, format=original_format, quality=95, optimize=True)
            else:
                sharpened_img.save(file_path_long, format=original_format)
                
        print(f"Successfully sharpened: {file_path}")
        return True
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False


def process_directory(image_dir, backup_dir, radius, percent, threshold):
    """
    Recursively scans and processes images in a directory.
    """
    supported_extensions = ('.png', '.jpg', '.jpeg')
    success_count = 0
    total_count = 0
    
    if not os.path.exists(image_dir):
        print(f"Error: Directory '{image_dir}' does not exist.")
        return
        
    print(f"Scanning directory: {image_dir}")
    print(f"Unsharp Mask Settings -> Radius: {radius}, Percent: {percent}%, Threshold: {threshold}")
    print("-" * 60)
    
    for root, dirs, files in os.walk(image_dir):
        # Skip backup folder if it is nested inside the scanning path
        if os.path.abspath(root).startswith(os.path.abspath(backup_dir)):
            continue
            
        for file in files:
            if file.lower().endswith(supported_extensions):
                file_path = os.path.join(root, file)
                
                # Determine backup destination keeping same folder structure
                relative_path = os.path.relpath(file_path, image_dir)
                backup_path = os.path.join(backup_dir, relative_path)
                
                total_count += 1
                if sharpen_image(file_path, backup_path, radius, percent, threshold):
                    success_count += 1
                    
    print("-" * 60)
    print(f"Completed! Sharpened {success_count}/{total_count} images.")
    print(f"Original images are stored in: {backup_dir}")

def main():
    parser = argparse.ArgumentParser(description="Sharpen images in a directory using Unsharp Mask.")
    parser.add_argument("--dir", default="static/images", help="Directory containing images to sharpen")
    parser.add_argument("--backup-dir", default="static/images_backup", help="Directory to save backup files")
    parser.add_argument("--radius", type=float, default=DEFAULT_RADIUS, help=f"Radius for Unsharp Mask (default: {DEFAULT_RADIUS})")
    parser.add_argument("--percent", type=int, default=DEFAULT_PERCENT, help=f"Strength percentage (default: {DEFAULT_PERCENT})")
    parser.add_argument("--threshold", type=int, default=DEFAULT_THRESHOLD, help=f"Min threshold (default: {DEFAULT_THRESHOLD})")
    
    args = parser.parse_args()
    
    # Resolve absolute paths based on root directory
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    image_dir = os.path.join(base_dir, args.dir)
    backup_dir = os.path.join(base_dir, args.backup_dir)
    
    process_directory(image_dir, backup_dir, args.radius, args.percent, args.threshold)

if __name__ == "__main__":
    main()
