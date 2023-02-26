# AI Image ZIP Renaming Tool

This is a Python script that can be used to rename images based on their content. It can detect if an image contains a face, and if so, it will rename the file to `face_x.jpg`, where `x` is the number of the face detected in the image. If the face takes up most of the image, the file will be called `portrait_x.jpg` instead. If no faces are detected, the file will be called `body_x.jpg`.

## Requirements

This script requires the following:

- Python 3.x
- OpenCV (for image processing)
- A Haar cascade file for face detection (we used `haarcascade_frontalface_default.xml` in this example)
- A zip file containing the images to be processed

## Installation

1. Clone this repository to your local machine. 
2. Make sure you have Python 3 and the following packages installed: OpenCV, NumPy, and pytest.
3. Navigate to the root directory of the cloned repository in your terminal or command prompt. 
4. Run the command python install.py to add the tool to your Windows context menu.

## Usage

To use this script, follow these steps:

1. Clone the repository or download the `process_zip_file.py` file
2. Install the required packages (OpenCV)
3. Place the Haar cascade file in the same directory as the script
4. Place the zip file containing the images to be processed in the same directory as the script
5. Open a terminal or command prompt and navigate to the directory where the script is located
6. Run the script using the following command:

```bash
python process_zip_file.py
```
or
```bash
python process_zip_file.py [ZIP_FILE]
```
7. When prompted, enter the path to the input zip file
8. Wait for the script to finish processing the images
9. The output zip file will contain the renamed images

To use the right click:

1. Right-click on a ZIP archive containing images.
2. Select "AI ZIP Rename Images" from the context menu.
3. The tool will process the images and create a new ZIP archive with the processed images.
4. The new archive will be saved in the same directory as the original archive with the suffix "_processed" added to the file name.


## Notes

- The script will only process `.jpg`, `.jpeg`, and `.png` files
- The script will recursively search for images in any subfolders of the input zip file
- The script will display the progress and face_percent value of each image as it processes it
- The script will also count the number of images renamed to `body_x.jpg`, `face_x.jpg`, and `portrait_x.jpg`, respectively, and display the counts at the end of the process.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
