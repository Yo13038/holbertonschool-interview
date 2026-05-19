#!/usr/bin/python3
"""
Module that determines if the boxes can be open
"""


def canUnlockAll(boxes):
    """function who determine if all the boxes can be opened"""

    if len(boxes) == 0:
        return False

    n = len(boxes)

    open_boxes = {0}

    unused_keys = list(boxes[0])

    while unused_keys:
        key = unused_keys.pop()

        if key < n and key not in open_boxes:
            open_boxes.add(key)
            unused_keys.extend(boxes[key])

    return len(open_boxes) == n
