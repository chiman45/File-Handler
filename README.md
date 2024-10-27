# File Management Script

This script allows users to create folders and organize files based on their types (images, documents, videos). It helps in managing files more efficiently by categorizing them into user-defined folders.

## Features

- **Create Folders**: Users can specify the number of folders to create and provide names for each folder.
- **Organize Files**: The script can move files of specific types (images, documents, videos) into the corresponding folders.

## Requirements

- **Python 3.x**: Make sure Python is installed on your system. You can download it from [python.org](https://www.python.org/).

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/chiman45/FileManagement.git
   cd FileManagement

2. pip install -r requirements.txt

3.python main.py
   
4. Enter how many folders you want to create: 2
Enter 1 Folder Name: ImagesFolder
Which type of file you want to store in this folder: image
Enter 2 Folder Name: DocsFolder
Which type of file you want to store in this folder: docs


5. How It Works
createfolder(num): This function prompts the user to enter folder names and the type of files to be stored in each folder.
move(typ, name): This function moves files of the specified type into the corresponding folder.
The script supports the following file types:

Images: .png, .jpg, .jpeg, .bmp
Documents: .txt, .docx, .pptx, .ppt, .xlsx
Videos: .mp4, .mov
   
