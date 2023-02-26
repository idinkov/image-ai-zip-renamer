import cv2
import os
import zipfile
import numpy as np
import sys

input_zip_path = sys.argv[1]

# Load the face detection model from OpenCV
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Create counters for faces and bodies
body_count = portrait_count = face_count = 0
current_folder = ""
# Open the input zip file in read mode
with zipfile.ZipFile(input_zip_path, "r") as input_zip:
    output_zip_path = os.path.splitext(input_zip_path)[0] + "_processed.zip"
    # Create a new zip file for the output in write mode
    with zipfile.ZipFile(output_zip_path, "w") as output_zip:
        # Loop through all the files in the input zip file
        for i, file_info in enumerate(input_zip.infolist()):
            # Check if the file is a zip file
            if file_info.filename.endswith(".zip"):
                # Skip zip files to avoid recursively processing them
                continue
            # Check if the file is in a new folder
            if os.path.dirname(file_info.filename) != current_folder:
                # Reset the counters for the new folder
                current_folder = os.path.dirname(file_info.filename)
                body_count = portrait_count = face_count = 0
            # Read the file as a binary string
            file_bytes = input_zip.read(file_info.filename)
            # Convert the binary string to a numpy array
            nparr = np.frombuffer(file_bytes, np.uint8)
            # Load the image from the numpy array
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            # Convert the image to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # Detect faces in the image
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
            # Check if there is at least one face detected
            if len(faces) > 0:
                # Sort the faces by size (largest first)
                sorted_faces = sorted(faces, key=lambda x: -x[2])
                # Get the largest face
                largest_face = sorted_faces[0]
                # Calculate the percentage of the image that the face takes up
                face_area = largest_face[2] * largest_face[3]
                img_area = img.shape[0] * img.shape[1]
                face_percent = face_area / img_area
                # If the face takes up most of the image, rename the file as "face_x.jpg"
                if face_percent > 0.2:
                    new_name = "face_" + str(face_count)
                    face_count += 1
                # Otherwise, rename the file as "body_x.jpg"
                elif face_percent > 0.08:
                    new_name = "portrait_" + str(portrait_count)
                    portrait_count += 1
                else:
                    new_name = "body_" + str(body_count)
                    body_count += 1
            # If no face is detected, rename the file as "body_x.jpg"
            else:
                new_name = "body_" + str(body_count)
                body_count += 1
                # Set face_percent to -1 to indicate no face was detected
                face_percent = -1
            # Add the renamed file to the output zip file
            _, ext = os.path.splitext(file_info.filename)
            output_zip.writestr(os.path.join(os.path.dirname(file_info.filename), new_name) + ext, file_bytes)
            # Print progress message and face percent value
            print(
                f"Processed file {file_info.filename} ({i + 1}/{len(input_zip.infolist())}). Face percent: {face_percent}")
        # Print completion message
        print(f"All files processed and saved to {output_zip_path}!")