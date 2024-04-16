try:
    # Versuch, eine nicht vorhandene Datei zu öffnen
    with open("demofile.txt", "r") as f:
        f.write("Lorum Ipsum")  # In die Datei schreiben

except IOError:
    print("Ein IOError ist aufgetreten. Die Datei existiert nicht oder kann nicht geöffnet werden.")
