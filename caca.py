import csv
from datetime import datetime, timezone, timedelta
import time

# Définir le décalage horaire UTC+1
utc_offset = timedelta(hours=1)

# Chemin vers le fichier CSV d'entrée et de sortie
fichier_entree = 'data/GPT_results.txt'
fichier_sortie = 'data/GPT_results2.txt'

def convertir_timestamp(timestamp):
    return datetime.fromtimestamp(int(timestamp), timezone.utc) + utc_offset

# Ouvrir le fichier d'entrée en mode lecture
with open(fichier_entree, 'r') as f:
    lines = f.readlines()

# Ajouter le timestamp au début de chaque ligne
for line in lines:

    date_et_heure  = datetime.fromtimestamp(time.time())

    line = f"{date_et_heure .strftime('%Y-%m-%d %H:%M:%S')}{line}"

# Écrire les lignes modifiées dans le fichier de sortie
with open(fichier_sortie, 'w', newline='') as f_sortie:
    for line in lines:
        date_et_heure  = datetime.fromtimestamp(time.time())

        line = f"{date_et_heure .strftime('%Y-%m-%d %H:%M:%S')}::{line}"

        f_sortie.write(line)

print("Le timestamp a été ajouté avec succès au fichier de sortie.")
