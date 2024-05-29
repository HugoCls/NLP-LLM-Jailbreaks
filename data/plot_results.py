import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

techniques = ['TAP','ArtPrompt', 'Hackerman', 'Stan', 'Dude', 'Dan6.0', 'MongoTom', 'ClassicVSJailbreak']

# Parcourir chaque fichier, lire et afficher les colonnes
for technique in techniques:
    file_name = f'stats - {technique}.xlsx'
    df_temp = pd.read_excel(file_name)
    print(f'Nom du fichier: {file_name}')
    print('Colonnes:', df_temp.columns.tolist())
    print()  # Ligne vide pour séparer les sorties des différents fichiers

dfs = [pd.read_excel(f'stats - {technique}.xlsx', usecols=['Theme', 'Technique', 'Human_Eval']) for technique in ['TAP','ArtPrompt', 'Hackerman', 'Stan', 'Dude', 'Dan6.0', 'MongoTom','ClassicVSJailbreak']]
df = pd.concat(dfs, ignore_index=True)

print(df.head())

grouped = df.groupby(['Theme', 'Technique'])['Human_Eval'].mean().reset_index()

print(grouped)

pivot_table = grouped.pivot(index='Theme', columns='Technique', values='Human_Eval')

pivot_table = pivot_table.fillna(0)

pivot_table = pivot_table[['TAP','ArtPrompt', 'Hackerman', 'Stan', 'Dude', 'Dan6.0', 'ClassicVSJailbreak', 'MongoTom']]

plt.figure(figsize=(12, 8))
sns.heatmap(pivot_table, annot=True, cmap='viridis')
plt.title('Techniques Performance by Theme')
plt.show()