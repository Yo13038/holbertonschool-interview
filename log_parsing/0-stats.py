#!/usr/bin/python3
"""
Module to handle log parsing
"""
import sys

status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}


def show_stats(total_size):
    """
    Function to display accumulated statistics
    """
    # Fixed case sensitivity to match requirement "File size:"
    print("File size: {}".format(total_size))

    for i in sorted(status_codes.keys()):
        if status_codes[i] > 0:
            print("{}: {}".format(i, status_codes[i]))


def parse_log():
    """
    Read stdin line by line and process metrics
    """
    total_size = 0
    line_count = 0

    try:
        # Loop through each line coming from standard input
        for line in sys.stdin:
            # Split the line where space is found
            parsed_line = line.split()

            # Skip line if it doesn't contain requirement
            if len(parsed_line) < 2:
                continue
            
            try:
                # Extract status using negative indexing
                status_code = int(parsed_line[-2])
                file_size = int(parsed_line[-1])

                # Accumulate the total file size
                total_size += file_size
                
                # Increment status code count
                if status_code in status_codes:
                    status_codes[status_code] += 1
            
                # Increment the valided lines counter
                line_count += 1

            except (ValueError, IndexError):
                # Format is invalid, skip the line safely
                continue

            # display after every 10 valid lines
            if line_count % 10 == 0:
                show_stats(total_size)

        show_stats(total_size)
        
    except KeyboardInterrupt:
        # Handle CTRL+C
        show_stats(total_size)
        raise


if __name__ == "__main__":
    parse_log()
