from delivery_label import number_reader
from bmw_label import extract_text


if __name__ == "__main__":

    bmw_path = "/Users/leopold/Downloads/Neu/IMG_4488.png"
    delivery_path = "/Users/leopold/Downloads/Neu/IMG_4489.png"


    delivery_numbers = number_reader(delivery_path)
    print(delivery_numbers)

    match = True

    for i in extract_text(bmw_path):
        print(i)
        if i not in delivery_numbers:
            print("No Match!")
            match = False

    if match:
        print("Match!")
