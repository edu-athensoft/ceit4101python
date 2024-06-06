"""
distance by postal code
"""

import pgeocode


def calculate_distance(postal_code1, postal_code2, country='CA'):
    # Create a pgeocode object for the specified country (default is Canada 'CA')
    nomi = pgeocode.Nominatim(country)

    # Get distance between the two postal codes
    distance = nomi.query_postal_code(postal_code1).distance(nomi.query_postal_code(postal_code2))

    return distance


# Example usage
postal_code1 = 'H3A'  # Example postal code 1
postal_code2 = 'H4B'  # Example postal code 2

distance = calculate_distance(postal_code1, postal_code2)
print(f"The distance between postal codes {postal_code1} and {postal_code2} is approximately {distance} km.")
