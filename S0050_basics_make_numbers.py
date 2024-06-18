# Opgave 2: Forandr koden i funktionen sådan at den gør, hvad der står i dens dokumentation.

def make_numbers(start, multiplier, upper_limit):
    """
    Documentation Beginning with the start value, this function prints the current value,
    then multiplies it with multiplier, prints the new current value etc.
    The function stops when the current value is greater than the upper limit
                                                                             """
    current_value = start
    while current_value < upper_limit:
      print(current_value)
      current_value *= multiplier

make_numbers(10, 2, 12345)