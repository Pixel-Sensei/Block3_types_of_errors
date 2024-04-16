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
division(5, 2)