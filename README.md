# Folder Difference Checker

This is a simple Python script that compares two directories and lists the subfolders that are unique to each directory.
Very useful when have two similar folders with lots of subfolders and want to check the difference between them.

## Features
- Compares two folders and identifies subfolders that exist in only one of them.
- Outputs the unique subfolders in each folder.
- Handles errors such as missing directories and permission issues.

## Installation
No external dependencies are required. Ensure you have Python installed (version 3.x recommended).

## Usage
1. Save the script as `compare_folders.py`.
2. Open a terminal or command prompt.
3. Run the script with the paths to the two folders you want to compare:
   ```sh
   python compare_folders.py <folderA> <folderB>
   ```

### Example
#### Given:
Folder `a` contains:
```
1  2  3  4  5  6
```
Folder `b` contains:
```
1  2  4  5  6  7  8
```
#### Running:
```sh
python compare_folders.py path/to/a path/to/b
```
#### Output:
```
Subfolders only in 'path/to/a':
  - 3

Subfolders only in 'path/to/b':
  - 7
  - 8
```

## Error Handling
- If a folder does not exist, the script will notify the user and exit.
- If permission is denied for a folder, an error message will be displayed.

## License
This project is open-source and available under the MIT License.

