#-----------------------------------------------------------------------------------------------------------------------
# Importing all the required libraries

import easyocr
import pandas as pd
from PIL import Image
import re
import numpy as np

#-----------------------------------------------------------------------------------------------------------------------

# Function to extract the quantity (No. of items)
def find_string_before_value(df_column):

    result = []
    found_8 = False

    for string in df_column:
        if string.startswith('(8)'):
            found_8 = True
        elif found_8 and string.startswith('(11)'):
            found_8 = False
        elif found_8:
            result.append(string)

    if len(result)==1:
        numbers = re.findall(r'\d+', result[0])
        return numbers
    else:
        numbers = re.findall(r'\d+', result[0])
        return numbers

#-----------------------------------------------------------------------------------------------------------------------

# Function to extract the Lieferschein and Material Nummer
def extract_2_values(df):

    patterns = [r'^\d{7,8}$', r'.*-.{2}$']
    required_list = []

    for ind, pattern in enumerate(patterns):
        filtered_strings = df[df['BMW_extracted'].str.match(pattern)]['BMW_extracted']
        first_string = filtered_strings.iloc[0] if not filtered_strings.empty else None
        if ind == 1:
            if len(first_string) < 7:
                indx = None
                for i, v in enumerate(df['BMW_extracted']):
                    if v == first_string:
                        indx = i
                first_string = df['BMW_extracted'].iloc[indx-1] + first_string
        required_list.append(first_string)

    return required_list

#-----------------------------------------------------------------------------------------------------------------------

# Function to crop the image in exactly half
def crop_half_vertically(image_path):

    # Open the image
    image = Image.open(image_path)

    # Get the dimensions of the image
    width, height = image.size

    # Crop the image exactly half vertically
    cropped_image = image.crop((0, 0, width * 0.45, height))

    # Replacing the original image with the cropped image
    return np.array(cropped_image)

#-----------------------------------------------------------------------------------------------------------------------

# Function to extract the text from the cropped image
def extract_text(image_path, language=['en']):

    img = crop_half_vertically(image_path)

    # Create an EasyOCR reader
    reader = easyocr.Reader(language)

    # Read text from the image
    results = reader.readtext(img, decoder='wordbeamsearch')

    # Extract and concatenate the text
    text_list = [result[1] for result in results]

    print(text_list)

    bmw_label_data = pd.DataFrame(text_list, columns=['BMW_extracted'])
    bmw_final = extract_2_values(bmw_label_data)
    bmw_final = bmw_final + find_string_before_value(bmw_label_data['BMW_extracted'])

    for i in range(len(bmw_final)):
        bmw_final[i] = bmw_final[i].replace(" ", "")

    return bmw_final

#-----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    # Path to the image
    image_path = r"C:\Users\mdasg\Desktop\123.jpeg"

    # Extract text from the image
    extracted_text = extract_text(image_path)

#-----------------------------------------------------------------------------------------------------------------------
