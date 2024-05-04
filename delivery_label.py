import easyocr
import pandas as pd
import cv2
import os
import numpy as np


# Load the image
def number_reader(img_path):
        image = cv2.imread(img_path)

        reader = easyocr.Reader(["en", "de"])
        result = reader.readtext(image, decoder='beamsearch', text_threshold=0.55, mag_ratio=0.5, canvas_size=4032, contrast_ths=0.3, min_size=100)
        result_df = pd.DataFrame(result)[1]
        print(result_df.to_string())
        filtered = [i.replace(" ", "") for i in result_df if i != "" and i[0].isdigit()]
        return filtered

if __name__ == "__main__":
        path = r'/Users/leopold/Downloads/WhatsApp Unknown 2024-05-03 at 13.09.48'

        images = [path + "/" + image_path for image_path in os.listdir(path)]

        for img_path in images:
                print(f"{img_path}: \n {number_reader(img_path)}")

