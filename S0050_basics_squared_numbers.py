# Opgave 3: Skriv kode i den næste celle, som printer alle kwadrattal (1, 4, 9, ...), som er mindre end limit.

def print_kvadrattal(limit):
    number = 1
    while number * number < limit:
        print(number * number)
        number += 1


print_kvadrattal(700)