"""Valgfri on loops/løkker"""

# Opgave 1: Tilføj koden i den næste celle sådan at der udskrives "A1 A2 A3 B1 .... D4 D5".

rows = ["A", "B", "C", "D"]
cols = ["1", "2", "3", "4", "5"]

for row in rows:
    for col in cols:
        print(row, col)


