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
