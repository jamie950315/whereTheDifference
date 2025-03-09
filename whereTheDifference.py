import os
import sys

def list_subfolders(path):
    """
    Returns a set of names of immediate subdirectories in the given folder.
    """
    try:
        # List all items in the directory and filter those that are directories
        return {item for item in os.listdir(path) if os.path.isdir(os.path.join(path, item))}
    except FileNotFoundError:
        print(f"Error: The folder '{path}' does not exist.")
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied for folder '{path}'.")
        sys.exit(1)

def main():
    if len(sys.argv) != 3:
        print("Usage: python compare_folders.py <folderA> <folderB>")
        sys.exit(1)

    folder_a = sys.argv[1]
    folder_b = sys.argv[2]

    subfolders_a = list_subfolders(folder_a)
    subfolders_b = list_subfolders(folder_b)

    # Determine which subfolders are unique to each folder
    unique_to_a = subfolders_a - subfolders_b
    unique_to_b = subfolders_b - subfolders_a

    # Print results
    if unique_to_a:
        print(f"Subfolders only in '{folder_a}':")
        for folder in sorted(unique_to_a):
            print("  -", folder)
    else:
        print(f"All subfolders in '{folder_a}' are also in '{folder_b}'.")

    print()  # Print a blank line for readability

    if unique_to_b:
        print(f"Subfolders only in '{folder_b}':")
        for folder in sorted(unique_to_b):
            print("  -", folder)
    else:
        print(f"All subfolders in '{folder_b}' are also in '{folder_a}'.")

if __name__ == "__main__":
    main()
