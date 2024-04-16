# Aufgabe 9 - Finally
try:
    with open("demofile2.txt", "w") as f:  # Die Datei im Schreibmodus öffnen
        f.write("Lorum Ipsum")  # In die Datei schreiben
except IOError:
    print("Beim Öffnen oder Schreiben in die Datei ist etwas schiefgegangen")  # Fehlerbehandlung, falls ein Fehler auftritt
finally:
    f.close()  # Die Datei wird immer geschlossen, unabhängig davon, ob ein Fehler auftritt oder nicht
