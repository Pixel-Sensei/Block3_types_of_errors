# Aufgabe 1 - Eingabefehler
wert = int(input('Geben Sie eine ganze Zahl ein:\n')) # Benutzer wird nach einer ganzen Zahl gefragt
print('Die Hälfte von', wert, 'ist', wert/2) # Die Hälfte des eingegebenen Wertes wird berechnet und ausgegeben

# Aufgabe 2 - Fehler entfernen
wert = input('Geben Sie eine ganze Zahl ein:\n') # Benutzer wird nach einer Eingabe gebeten
if wert.isdecimal(): # Überprüfung, ob die Eingabe eine ganze Zahl ist
    wert = int(wert) # Wenn ja, wird der Wert in eine ganze Zahl umgewandelt
    print('Die Hälfte von', wert, 'ist', wert/2) # Die Hälfte des eingegebenen Wertes wird berechnet und ausgegeben
else:
    print("Der eingegebene Wert ist keine ganze Zahl.") # Wenn die Eingabe keine ganze Zahl ist, wird eine Fehlermeldung ausgegeben

# Aufgabe 3 - Try-Except
try:
    wert = int(input('Geben Sie eine ganze Zahl ein:\n')) # Benutzer wird nach einer ganzen Zahl gefragt
    print('Der Kehrwert von', wert, 'ist', 1/wert) # Der Kehrwert des eingegebenen Wertes wird berechnet und ausgegeben
except:
    print("Das kann ich nicht tun.") # Falls ein Fehler auftritt, wird eine Fehlermeldung ausgegeben

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

# Aufgabe 6 - Fehler fehlt
wert = int(input("Geben Sie eine ganze Zahl ein:\n")) # Benutzer wird nach einer ganzen Zahl gefragt
if wert > 0:
    print("Es ist eine positive Zahl.") # Wenn der eingegebene Wert größer als 0 ist, wird ausgegeben, dass es sich um eine positive Zahl handelt
elif wert < 0:
    prin("Es ist eine negative Zahl.") # Wenn der eingegebene Wert kleiner als 0 ist, wird ein Schreibfehler ausgegeben (korrigiert: "print")
else:
    print("Die Zahl ist Null.") # Wenn der eingegebene Wert gleich Null ist, wird ausgegeben, dass die Zahl Null ist

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

# Aufgabe 8 - Try-Except-Else
def division(a, b):
    try:
        c = a / b # Versuch, a durch b zu teilen
        print("Die Division von", a, "/", b, "ist", c, ".") # Wenn erfolgreich, wird das Ergebnis ausgegeben
    except TypeError:
        print("Mindestens ein Parameter ist inkorrekt.") # Wenn ein Parameter den falschen Typ hat, wird eine Fehlermeldung ausgegeben
    except ZeroDivisionError:
        print("Du hast durch 0 geteilt, das ist nicht klug.") # Wenn versucht wird, durch Null zu teilen, wird eine Fehlermeldung ausgegeben
    else:
        print("Gut gemacht.") # Wenn keine Fehler auftreten, wird eine Erfolgsmeldung ausgegeben
division(0, "a")

# Aufgabe 9 - Finally
try:
  f = open("demofile3.txt") # Versuch, eine Datei zu öffnen
  try:
    f.write("Lorum Ipsum") # Versuch, in die Datei zu schreiben
  except:
    print("Beim Schreiben in die Datei ist etwas schiefgegangen") # Wenn ein Fehler beim Schreiben auftritt, wird eine Fehlermeldung ausgegeben
  finally:
    f.close() # Die Datei wird immer geschlossen, unabhängig davon, ob ein Fehler auftritt oder nicht
except:
  print("Beim Öffnen der Datei ist etwas schiefgegangen") # Wenn ein Fehler beim Öffnen der Datei auftritt, wird eine Fehlermeldung ausgegeben

# Aufgabe 10 - Summe der Liste
myList = [4, 8, "paper", 15, "code", 16, " ", 23, 42] # Eine Liste mit verschiedenen Elementen
wert = 0 # Variable zur Speicherung der Summe
zahlen = 0 # Variable zur Zählung der Zahlen in der Liste
for i in range(0, len(myList)): # Schleife über alle Elemente der Liste
    try:
        wert += myList[i] # Versuch, das aktuelle Element zur Summe hinzuzufügen
    except TypeError:
        print("Ich kann", myList[i], "nicht zur Summe hinzufügen.") # Wenn ein Element keine Zahl ist, wird eine Fehlermeldung ausgegeben
        print("Dieser Wert ist an Index", i, ".") # Der Index des fehlerhaften Elements wird ausgegeben
        print("-------------")
    else:
        zahlen += 1 # Wenn kein Fehler auftritt, wird die Anzahl der Zahlen erhöht
print("In der Liste befinden sich", zahlen, "Zahlen.") # Die Anzahl der Zahlen in der Liste wird ausgegeben
print("Die Summe der Zahlen ist", wert, ".") # Die Summe der Zahlen in der Liste wird ausgegeben
