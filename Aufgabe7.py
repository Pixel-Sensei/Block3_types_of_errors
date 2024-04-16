# Aufgabe 7 - Eingabe von 0
try:
    wert = int(input("Geben Sie einen Wert ein: ")) # Benutzer wird nach einer Eingabe gebeten
    print(wert/wert) # Versuch, den eingegebenen Wert durch sich selbst zu teilen
except ValueError:
    print("Ungültige Eingabe...") # Wenn die Eingabe keine ganze Zahl ist, wird eine Fehlermeldung ausgegeben
except ZeroDivisionError:
    print("Sehr schlechte Eingabe...") # Wenn versucht wird, durch Null zu teilen, wird eine Fehlermeldung ausgegeben
except:
    print("Booo!") # Falls ein anderer Fehler auftritt, wird eine allgemeine Fehlermeldung ausgegeben
