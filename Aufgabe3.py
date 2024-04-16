# Aufgabe 3 - Try-Except
try:
    wert = int(input('Geben Sie eine ganze Zahl ein:\n')) # Benutzer wird nach einer ganzen Zahl gefragt
    print('Der Kehrwert von', wert, 'ist', 1/wert) # Der Kehrwert des eingegebenen Wertes wird berechnet und ausgegeben
except:
    print("Das kann ich nicht tun.") # Falls ein Fehler auftritt, wird eine Fehlermeldung ausgegeben
