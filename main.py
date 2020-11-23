#main.py
import sys
sys.dont_write_bytecode = True

import import_kcd, job_settings


Settings = job_settings.JobSettings()
Cabinets = []

KCD_Cabinets = import_kcd.parseCSV("kcd_dxf/cnclist.txt")
print("KCD_Cabinets: ", KCD_Cabinets)

for cab in KCD_Cabinets:
    print(cab) 
    Cabinets.append(import_kcd.convert(cab, Settings))

print("CABINETS: ", Cabinets)

