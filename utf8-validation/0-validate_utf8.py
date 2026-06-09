#!/usr/bin/python3
"""Module to handle UTF-8 dataset
"""


def validUTF8(data):
    """check if dataset is a valid UTF-8 encoding type"""

    remaining_bytes = 0  # number of byte expected

    for num in data:
        byte = num & 255  # significant bits wanted

        if remaining_bytes == 0:
            # counting the 1 at the begining of the byte
            binary_mask = 1 << 7

            while binary_mask & byte:
                remaining_bytes += 1
                binary_mask = binary_mask >> 1

            # if condition true remaining bytes equal zéro
            if remaining_bytes == 0:
                continue

            # size of bytes alowed by UTF-8
            if remaining_bytes == 1 or remaining_bytes > 4:
                return False
            remaining_bytes -= 1

        else:
            # check if the byte start with 10 (binary to decimal)
            if (byte >> 6) != 2:
                return False

            remaining_bytes -= 1

    return remaining_bytes == 0
