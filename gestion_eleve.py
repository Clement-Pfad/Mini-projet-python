partie 1
etudiants = ["Samba", "Evan", "Princia Céleste", "Noâm", "Jean", "Alexandre", "Clément"]

# 1.2. Enregistrement des notes dans un dictionnaire
notes = {
    "Samba": [12, 15, 14],
    "Evan": [16, 14, 17],
    "Princia Céleste": [10, 12, 11],
    "Noâm": [8, 9, 10],
    "Jean": [14, 13, 15],
    "Alexandre": [18, 17, 19],
    "Clément": [9, 11, 10]
}

# 1.3. Affichage des notes de chaque étudiant à l'aide d'une boucle
print("--- 1.3. NOTES DE CHAQUE ÉTUDIANT ---")
for prenom in etudiants:
    print(f"{prenom} : {notes[prenom][0]}, {notes[prenom][1]}, {notes[prenom][2]}")


partie 2

# 2.1. Fonction pour calculer la moyenne d'une liste de notes
def moyenne(liste_notes):
    """Calcule et retourne la moyenne arithmétique d'une liste de notes."""
    if len(liste_notes) == 0:
        return 0
    return sum(liste_notes) / len(liste_notes)


# 2.3. Fonction pour attribuer une mention selon la moyenne
def mention(moy):
    """Retourne la mention correspondante en fonction de la moyenne."""
    if moy >= 16:
        return "Excellent"
    elif moy >= 14:
        return "Bien"
    elif moy >= 12:
        return "Assez bien"
    elif moy >= 10:
        return "Passable"
    else:
        return "Insuffisant"


# 2.2 & 2.3. Affichage des résultats individuels et mentions
print("--- 2.2 & 2.3. RÉSULTATS INDIVIDUELS ET MENTIONS ---")
for prenom in etudiants:
    moy_etudiant = moyenne(notes[prenom])
    ment = mention(moy_etudiant)
    print(f"{prenom} — Notes : {notes[prenom][0]}, {notes[prenom][1]}, {notes[prenom][2]} — Moyenne : {moy_etudiant:.2f} — Mention : {ment}")


# 2.4. Fonction pour trouver le meilleur étudiant
def meilleur_etudiant(dico_notes):
    """Parcourt le dictionnaire pour trouver l'étudiant avec la meilleure moyenne."""
    meilleur_nom = ""
    meilleure_moy = -1
    
    for prenom, liste_n in dico_notes.items():
        moy = moyenne(liste_n)
        if moy > meilleure_moy:
            meilleure_moy = moy
            meilleur_nom = prenom
            
    return meilleur_nom, meilleure_moy

nom_top, moy_top = meilleur_etudiant(notes)
print("--- 2.4. LE MEILLEUR ÉTUDIANT ---")
print(f"Le meilleur étudiant est {nom_top} avec une moyenne de {moy_top:.2f}.")


partie 3

# 3.1. Calcul de la moyenne générale de la classe
somme_moyennes = 0
for prenom in etudiants:
    somme_moyennes += moyenne(notes[prenom])

moyenne_generale = somme_moyennes / len(etudiants)

print("--- 3. ANALYSE GLOBALE DE LA CLASSE ---")
print(f"Moyenne générale de la classe : {moyenne_generale:.2f}")

# 3.2. Compter les étudiants ayant validé (moyenne >= 10)
valides = 0
non_valides = 0

for prenom in etudiants:
    if moyenne(notes[prenom]) >= 10:
        valides += 1
    else:
        non_valides += 1

print(f"Étudiants ayant validé : {valides}")
print(f"Étudiants n'ayant pas validé : {non_valides}")

# 3.3. Calcul de la répartition des mentions
repartition = {
    "Excellent": 0,
    "Bien": 0,
    "Assez bien": 0,
    "Passable": 0,
    "Insuffisant": 0
}

for prenom in etudiants:
    m = moyenne(notes[prenom])
    m_str = mention(m)
    repartition[m_str] += 1

print("\nRépartition des mentions :")
for ment, count in repartition.items():
    print(f"- {ment} : {count} étudiant(s)")


partie 4

def enregistrer_resultats(nom_fichier):
    """Enregistre tous les résultats de la classe dans un fichier texte."""
    with open(nom_fichier, "w", encoding="utf-8") as f:
        f.write("RESULTATS DE LA CLASSE\n")
        
        for prenom in etudiants:
            n = notes[prenom]
            moy = moyenne(n)
            ment = mention(moy)
            
            f.write(f"{prenom}\n")
            f.write(f"Notes : {n[0]}, {n[1]}, {n[2]}\n")
            f.write(f"Moyenne : {moy:.2f}\n")
            f.write(f"Mention : {ment}\n")
            
        f.write(f"\nMoyenne générale : {moyenne_generale:.2f}\n")
        f.write(f"Étudiants ayant validé : {valides}/{len(etudiants)}\n")

# Appel de la fonction d'enregistrement avec la structure "with"`
enregistrer_resultats("resultats.txt")
print("--- 4. FICHIER ---")
print("Le fichier 'resultats.txt' a été créé et mis à jour avec succès !\n")


partie 5

def recherche_etudiant(nom_cherche):
    """Recherche un étudiant par son prénom et affiche ses résultats."""
    nom_cherche_clean = nom_cherche.strip().lower()
    trouve = False
    
    for prenom in notes:
        if prenom.lower() == nom_cherche_clean:
            trouve = True
            n = notes[prenom]
            moy = moyenne(n)
            ment = mention(moy)
            print(f"\nRésultat pour la recherche de '{prenom}' :")
            print(f"Notes : {n[0]}, {n[1]}, {n[2]}")
            print(f"Moyenne : {moy:.2f}")
            print(f"Mention : {ment}")
            break
            
    if not trouve:
        print(f"\nErreur : Aucun étudiant ne porte le prénom '{nom_cherche}'.")

# Tests de la fonction de recherche
print("--- 5. RECHERCHE D'UN ÉTUDIANT ---")
recherche_etudiant("samba")
recherche_etudiant("Paul")  # Test avec un étudiant inexistant
