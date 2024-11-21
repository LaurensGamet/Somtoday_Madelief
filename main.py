import requests
import os
import shutil

# Give simpler names
file1 = 'c5490491-11eb-4aca-a8f1-ea3f58e75d54.ics'
file2 = 'Final-File.ics'
file3 = 'out.py'
klas = 'oga3b'

# Makes sure no duplicate files
if os.path.exists(file2):
  os.remove(file2)
else:
  print("The file does not exist")

if os.path.exists(file3):
  os.remove(file3)
else:
  print("The file does not exist")

# Gets original file
url = 'https://api.somtoday.nl/rest/v1/icalendar/stream/58405be0-5611-4aba-be66-9894a1009f12/c5490491-11eb-4aca-a8f1-ea3f58e75d54'
r = requests.get(url, allow_redirects=True)
open(file1, 'wb').write(r.content)

with open(file1, 'r') as file:
  filedata = file.read()

# Makes Final-File.ics from original
shutil.copyfile(file1, file2)

# Makes out.py to get rid of error
with open('out.py', 'w') as fp:
    pass

# Replaces text in original file

# Studiedag
def delete_line(file_name, line_numbers):
    # Read all lines from the file
    with open(file_name, 'r') as file:
        lines = file.readlines()
    
    # Deleting lines in reverse order to prevent index shifting
    for line_number in sorted(line_numbers, reverse=True):
        if 0 <= line_number < len(lines):  # Ensure the line number is valid
#            print(f"Deleting line {line_number}: {lines[line_number].strip()}")  # Debugging print
            del lines[line_number]
        else:
            print(f"Line number {line_number} is out of range")  # Handle invalid line numbers
    
#    # Debugging: Print the remaining lines to be written back
#    for line in lines:
#       print(line.strip())
    
    # Write the remaining lines back to the file
    with open(file_name, 'w') as file:
        file.writelines(lines)
        file.flush()

with open(file1) as file:
    with open('out.py', 'w') as f:
        print("lijntjes = [", file=f)
    
    for number, line in enumerate(file):
        if 'studiedag' in line:
            with open('out.py', 'a') as f:
                print(f"{number - 4},", file=f)
                print(f"{number - 3},", file=f)
                print(f"{number - 2},", file=f)
                print(f"{number - 1},", file=f)
                print(f"{number},", file=f)
                print(f"{number + 1},", file=f)
                print(f"{number + 2},", file=f)
                print(f"{number + 3},", file=f)
                print(f"{number + 4},", file=f)
                print(f"{number + 5},", file=f)
                print(f"{number + 6},", file=f)
                print(f"{number + 7},", file=f)
    
    with open('out.py', 'a') as f:
        print("]", file=f)

# Import the lines that need to be deleted
from out import lijntjes

# Deleting lines
file_name = file2  # Ensure this is a string path to the final file
delete_line(file_name, lijntjes)

with open(file2, 'r') as file:
  filedata = file.read()

# Naam agenda
filedata = filedata.replace('NAME:Somtoday agenda', 'NAME:Somtoday Laurens')

with open(file2, 'w') as file:
  file.write(filedata)

# Define subject replacements
subject_replacements = {
    f'{klas}ak': 'Aardrijkskunde',
    f'{klas}bl': 'Begeleidingslessen',
    f'{klas}du': 'Duits',
    f'{klas}ec': 'Economie',
    f'{klas}en': 'Engels',
    f'{klas}fa': 'Frans',
    f'{klas}gs': 'Geschiedenis',
    f'{klas}lo': 'Lichamelijke Opvoeding',
    f'{klas}mentor': 'Mentor',
    f'{klas}na': 'Natuurkunde',
    f'{klas}ne': 'Nederlands',
    f'{klas}o&o': 'Onderzoeken en Ontwerpen',
    f'{klas}sk': 'Scheikunde',
    f'{klas}wi': 'Wiskunde',
    f'oga3.tmc1, oh3.tmc1': 'TMC',
    f'oh3.tmc1, oga3.tmc1': 'TMC',
}

# Perform all replacements
for old, new in subject_replacements.items():
    filedata = filedata.replace(old, new)

# Write the modified data back to the file
with open(file2, 'w') as file:
    file.write(filedata)

# Lokalen

# Define the ranges for replacements
ranges = {
    "be": (1, 300),
    "tm": (1, 300),
    "cc": (1, 99),
    "cb": (1, 200)
}

# Perform range-based replacements
for prefix, (start, end) in ranges.items():
    for i in range(start, end + 1):
        formatted_number = f"{i:03d}" if prefix in ["be", "tm", "cb"] else f"{i:02d}"
        filedata = filedata.replace(f"SUMMARY:{prefix}{formatted_number} - ", 'SUMMARY:')

# Define specific replacements
specific_replacements = [
    "SUMMARY:beuk3_gym - ",
    "SUMMARY:tm047_gym - ",
    "SUMMARY:tm116_binask - ",
    "SUMMARY:tm128_tmc - ",
    "SUMMARY:tm145_o&o - ",
    "SUMMARY:tm146_o&o - ",
]

# Perform specific replacements
for replacement in specific_replacements:
    filedata = filedata.replace(replacement, 'SUMMARY:')

# Write the modified data back to the file
with open(file2, 'w') as file:
    file.write(filedata)

# Delete temporary file

if os.path.exists(file1):
  os.remove(file1)
else:
  print("The file does not exist")
