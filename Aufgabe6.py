# Aufgabe 6 - Fehler fehlt
wert = int(input("Geben Sie eine ganze Zahl ein:\n")) # Benutzer wird nach einer ganzen Zahl gefragt
if wert > 0:
    print("Es ist eine positive Zahl.") # Wenn der eingegebene Wert größer als 0 ist, wird ausgegeben, dass es sich um eine positive Zahl handelt
elif wert < 0:
    prin("Es ist eine negative Zahl.") # Wenn der eingegebene Wert kleiner als 0 ist, wird ein Schreibfehler ausgegeben (korrigiert: "print")
else:
    print("Die Zahl ist Null.") # Wenn der eingegebene Wert gleich Null ist, wird ausgegeben, dass die Zahl Null ist
