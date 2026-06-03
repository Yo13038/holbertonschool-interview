#!/usr/bin/python3
"""
Module to handle log parsing
"""
import sys

# Global dictionary to track the count of each valid status code
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}


def show_stats(total_size):
    """
    Function to display accumulated statistics
    """
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
        for line in sys.stdin:
            parsed_line = line.split()

            # A valid line must have at least status code and file size
            if len(parsed_line) < 2:
                continue
            
            try:
                # Extract values from the end of the line
                file_size = int(parsed_line[-1])
                status_code = int(parsed_line[-2])

                # 1. ANY line with valid integers at the end counts towards total size
                total_size += file_size
                
                # 2. We ONLY increment the counter if it's in our tracked list
                if status_code in status_codes:
                    status_codes[status_code] += 1
            
                # 3. CRITICAL: Every structuraly valid line increments the count
                line_count += 1

            except (ValueError, IndexError):
                continue

            # Print every 10 valid lines
            if line_count % 10 == 0:
                show_stats(total_size)
        
        # Print final remaining stats at the End-Of-File (EOF)
        show_stats(total_size)
    
    except KeyboardInterrupt:
        show_stats(total_size)
        raise


if __name__ == "__main__":
    parse_log()
