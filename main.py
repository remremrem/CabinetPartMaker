#main.py
import import_kcd


Cabinets = []

KCD_Cabinets = import_kcd.parseCSV("../kcd_dxf/cnclist.txt")

for cab in KCD_Cabinets:
    Cabinets.append(import_kcd.convert(cab))

