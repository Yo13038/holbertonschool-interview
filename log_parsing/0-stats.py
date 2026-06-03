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
            # Nettoie la ligne et la découpe
            parsed_line = line.split()

            if len(parsed_line) < 2:
                continue
            
            try:
                # Extraction depuis la fin
                file_size = int(parsed_line[-1])
                status_code = int(parsed_line[-2])
                
                # Une ligne est valide si le statut et la taille sont des entiers.
                # On ajoute donc TOUJOURS sa taille au total.
                total_size += file_size
                
                # On incrémente le dictionnaire UNIQUEMENT si le code est suivi
                if status_code in status_codes:
                    status_codes[status_code] += 1
            
                # On incrémente le compteur de lignes pour le déclencheur des 10 lignes
                line_count += 1

            except (ValueError, IndexError):
                continue

            # Affichage toutes les 10 lignes valides
            if line_count % 10 == 0:
                show_stats(total_size)

        # Affichage final à la fin du flux (EOF)
        show_stats(total_size)

    except KeyboardInterrupt:
        show_stats(total_size)
        raise


if __name__ == "__main__":
    parse_log()
