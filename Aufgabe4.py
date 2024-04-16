# Aufgabe 4-5 - Try-Except-Except
try:
    wert = int(input('Geben Sie eine ganze Zahl ein:\n')) # Benutzer wird nach einer ganzen Zahl gefragt
    print('Der Kehrwert von', wert, 'ist', 1/wert) # Der Kehrwert des eingegebenen Wertes wird berechnet und ausgegeben
except ValueError:
    print("Das kann ich nicht tun.") # Wenn der eingegebene Wert keine ganze Zahl ist, wird eine Fehlermeldung ausgegeben
except ZeroDivisionError:
    print("Du hast versucht, durch 0 zu teilen. Das mag ich nicht.") # Wenn versucht wird, durch Null zu teilen, wird eine Fehlermeldung ausgegeben
except:
    print("Ich habe keine Ahnung, was gerade passiert ist.") # Falls ein anderer Fehler auftritt, wird eine allgemeine Fehlermeldung ausgegeben
