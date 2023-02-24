import math

laenge_a=float(input(f"Länge der Kante a angeben:"))
laenge_b=float(input(f"Länge der Kanze b angeben:"))
inhalt=laenge_a*laenge_b
while abs(laenge_a - laenge_b) > 0.01:
     mittelwert = (laenge_a+laenge_b)/2
#     inhalt = laenge_a * laenge_b
     laenge_a = mittelwert
     laenge_b = inhalt / laenge_a

print(laenge_a)
