from deprecated.delivery_label import number_reader
from deprecated.bmw_label import extract_text


def comparator(bmw_path, delivery_path):

    delivery_numbers = number_reader(delivery_path)

    match = True

    for i in extract_text(bmw_path):
        if i not in delivery_numbers:
            match = False

    return match
