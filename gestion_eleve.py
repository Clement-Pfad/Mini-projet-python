etudiants = ["Samba", "Evan", "Princia Céleste", "Noâm",  "Jean", "Alexandre", "Clément"]
    
notes = {
    "Samba": [12, 15, 14],
    "Evan": [16, 14, 17],
    "Princia Céleste": [10, 12, 11],
    "Noâm": [8, 9, 10],
    "Jean": [14, 13, 15],
    "Alexandre": [18, 17, 19],
    "Clément": [9, 11, 10]

for prenom in etudiants:
    print(f"{prenom} : {notes[prenom][0]}, {notes[prenom][1]}, {notes[prenom][2]}")
