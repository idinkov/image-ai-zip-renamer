import unittest
import os
import zipfile
import cv2
import numpy as np

from process_images import process_zip_file

class TestProcessImages(unittest.TestCase):

    def test_zip_file_processing(self):
        # create a sample zip file with images
        with zipfile.ZipFile('test_images.zip', 'w') as test_zip:
            for i in range(3):
                img = np.zeros((100, 100, 3), dtype=np.uint8)
                filename = f"test_image_{i}.jpg"
                cv2.imwrite(filename, img)
                test_zip.write(filename)

        # process the zip file
        process_zip_file('test_images.zip')

        # check that the processed zip file exists
        self.assertTrue(os.path.exists('test_images_processed.zip'))

        # check that the processed zip file contains all the expected files
        with zipfile.ZipFile('test_images_processed.zip', 'r') as processed_zip:
            filenames = processed_zip.namelist()
            self.assertCountEqual(filenames, ['test_image_0.jpg', 'test_image_1.jpg', 'test_image_2.jpg'])

        # remove the sample zip files
        os.remove('test_images.zip')
        os.remove('test_images_processed.zip')

if __name__ == '__main__':
    unittest.main()