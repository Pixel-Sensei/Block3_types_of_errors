# Aufgabe 2 - Fehler entfernen
wert = input('Geben Sie eine ganze Zahl ein:\n') # Benutzer wird nach einer Eingabe gebeten
if wert.isdecimal(): # Überprüfung, ob die Eingabe eine ganze Zahl ist
    wert = int(wert) # Wenn ja, wird der Wert in eine ganze Zahl umgewandelt
    print('Die Hälfte von', wert, 'ist', wert/2) # Die Hälfte des eingegebenen Wertes wird berechnet und ausgegeben
else:
    print("Der eingegebene Wert ist keine ganze Zahl.") # Wenn die Eingabe keine ganze Zahl ist, wird eine Fehlermeldung ausgegeben
