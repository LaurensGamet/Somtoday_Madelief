import requests
import os
import shutil

# Give needed files simpler names
file1 = 'c5490491-11eb-4aca-a8f1-ea3f58e75d54.ics'
file2 = 'Final-File.ics'

# Makes sure no duplicate files
if os.path.exists(file1):
  os.remove(file1)
else:
  print("The file does not exist")

if os.path.exists(file2):
  os.remove(file2)
else:
  print("The file does not exist")

# Gets original file
url = 'https://api.somtoday.nl/rest/v1/icalendar/stream/58405be0-5611-4aba-be66-9894a1009f12/c5490491-11eb-4aca-a8f1-ea3f58e75d54'
r = requests.get(url, allow_redirects=True)
open(file1, 'wb').write(r.content)

with open(file1, 'r') as file:
  filedata = file.read()

# Replaces text in original file

# Naam agenda
filedata = filedata.replace('NAME:Somtoday agenda', 'NAME:Somtoday Madelief')

with open(file1, 'w') as file:
  file.write(filedata)

# Aardrijkskunde
filedata = filedata.replace('oga3bak', 'Aardrijkskunde')

with open(file1, 'w') as file:
  file.write(filedata)

# Begeleidingslessen
filedata = filedata.replace('oga3bbl', 'Begeleidingslessen')

with open(file1, 'w') as file:
  file.write(filedata)

filedata = filedata.replace('oga3.bl2', 'Begeleidingslessen')

with open(file1, 'w') as file:
  file.write(filedata)

# Duits
filedata = filedata.replace('oga3bdu', 'Duits')

with open(file1, 'w') as file:
  file.write(filedata)

# Economie
filedata = filedata.replace('oga3bec', 'Economie')

with open(file1, 'w') as file:
  file.write(filedata)

# Engels
filedata = filedata.replace('oga3ben', 'Engels')

with open(file1, 'w') as file:
  file.write(filedata)

# Frans
filedata = filedata.replace('oga3bfa', 'Frans')

with open(file1, 'w') as file:
  file.write(filedata)

# Geschiedenis
filedata = filedata.replace('oga3bgs', 'Geschiedenis')

with open(file1, 'w') as file:
  file.write(filedata)

# Lichamelijke Opvoeding
filedata = filedata.replace('oga3blo', 'Lichamelijke Opvoeding')

with open(file1, 'w') as file:
  file.write(filedata)

# Mentor
filedata = filedata.replace('oga3.mentor2', 'Mentor')

with open(file1, 'w') as file:
  file.write(filedata)

# Natuurkunde
filedata = filedata.replace('oga3bna', 'Natuurkunde')

with open(file1, 'w') as file:
  file.write(filedata)

# Nederlands
filedata = filedata.replace('oga3bne', 'Nederlands')

with open(file1, 'w') as file:
  file.write(filedata)

# Taal, Maatschappij en Cultuur
filedata = filedata.replace('oga3.tmc1\, oh3.tmc1', 'TMC')

with open(file1, 'w') as file:
  file.write(filedata)

filedata = filedata.replace('oh3.tmc1\, oga3.tmc1', 'TMC')

with open(file1, 'w') as file:
  file.write(filedata)

# Scheikunde
filedata = filedata.replace('oga3bsk', 'Scheikunde')

with open(file1, 'w') as file:
  file.write(filedata)

# Wiskunde
filedata = filedata.replace('oga3bwi', 'Wiskunde')

with open(file1, 'w') as file:
  file.write(filedata)

# Lokalen
filedata = filedata.replace("SUMMARY:be001 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:be002 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:be003 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:be004 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:be005 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:be006 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:be007 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:be008 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:be009 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:be010 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:be011 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:be013 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:be014 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:be020 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:be021 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:be023 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:be024 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:be025 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:be026 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:be027 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:be102 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:be109 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:be110 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:be111 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:be112 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:be113 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:be114 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:be116 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:be117 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:be118 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:be119 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:be120 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:be121 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:be122 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:be123 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:be124 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:be125 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:be126 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:be127 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:be128 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:cb003 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:cb004 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:cb005 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:cb009 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:cb010 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:cb012 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:cb015 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:cb017 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:cb022 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:cb023 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:cb024 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:cb025 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:cb026 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:cb027 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:cb028 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:cb103 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:cb106 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:cb109 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:cb110 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:cb111 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:cb115 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:cb116 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:cb117 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:cb118 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:cc04 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:cc05 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:cc06 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:cc07 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:cc08 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:cc09 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:cc10 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:cc11 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:cc16 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:cc17 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:cc18 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:cc20 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:cc21 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:cc22 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:cc23 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:cc24 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:cc27 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:cc28 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:cc29 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:cc30 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:cc31 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:cc32 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:cc33 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:cc34 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm002 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm003 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm005 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm008 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm010 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm013 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm014 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm015 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm016 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm017 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm018 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm019 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm022 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm023 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm024 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm025 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm029 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm033 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm034 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm035 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm036 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm037 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm038 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm040 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm041 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm042 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm043 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm044 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm045 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm046 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm047 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm102 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm103 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm104 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm106 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm107 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm111 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm112 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm114 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm115 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm116 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm117 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm120 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm125 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm127 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm128 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm128_tmc - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm129 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm132 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm133 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm134 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm135 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm136 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm137 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm138 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm139 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm140 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm142 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm143 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm144 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm145 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm146 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm202 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm203 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm204 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm205 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm208 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm214 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm215 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm216 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm217 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm218 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm219 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm221 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm223 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm224 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm225 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm226 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

filedata = filedata.replace("SUMMARY:tm227 - ", 'SUMMARY:')

with open(file1, 'w') as file:
    file.write(filedata)

# Create final file
shutil.copyfile(file1, file2)
