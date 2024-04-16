try:
    # Versuche, eine ganze Zahl einzulesen
    zahl = int(input("Bitte geben Sie eine ganze Zahl ein: "))
    # Wenn eine ganze Zahl eingegeben wurde, wird sie hier gedruckt
    print("Sie haben die Zahl", zahl, "eingegeben.")
except ValueError:
    # Wenn eine ValueError-Ausnahme auftritt (wenn die Eingabe keine ganze Zahl ist),
    # wird eine Fehlermeldung ausgegeben
    print("Ungültige Eingabe. Bitte geben Sie eine ganze Zahl ein.")


# Benutzer wird aufgefordert, eine Eingabe zu machen
eingabe = input("Bitte geben Sie eine ganze Zahl ein: ")
# Überprüfen, ob die Eingabe nur aus Ziffern besteht (istdigit prüft das)
if eingabe.isdigit():
    # Wenn die Eingabe nur aus Ziffern besteht, wird sie in eine ganze Zahl konvertiert
    zahl = int(eingabe)
    # Die eingegebene Zahl wird hier ausgegeben
    print("Sie haben die Zahl", zahl, "eingegeben.")
else:
    # Wenn die Eingabe keine ganze Zahl ist, wird eine Fehlermeldung ausgegeben
    print("Ungültige Eingabe. Bitte geben Sie eine ganze Zahl ein.")
