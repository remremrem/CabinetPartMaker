#main.py
import import_kcd


Cabinets = []

KCD_Cabinets = import_kcd.parseCSV("csvfile.csv")

for cab in KCD_Cabinets:
    Cabinets.append(import_kcd.convert(cab))

