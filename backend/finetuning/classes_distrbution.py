import matplotlib.pyplot as plt
import pandas as pd

# Chargement du CSV
data = pd.read_csv("image_descriptions.csv")

# Séparation des descriptions par '|' et création de nouvelles colonnes
descriptions_split = data['description'].str.split('|', expand=True)

# Garder uniquement le dernier mot de chaque description
descriptions_split = descriptions_split.applymap(lambda x: x.split()[-1] if isinstance(x, str) else x)

# Nommer les nouvelles colonnes
descriptions_split.columns = [
    'leaf_shape', 'leaf_margin', 'leaf_arrangement', 'leaf_texture',
    'stem_type', 'stem_cross_section', 'presence_of_hairs_or_spines'
]

# Ajouter les nouvelles colonnes au dataframe original
data = pd.concat([data, descriptions_split], axis=1)

# Liste des attributs à analyser
attributes = descriptions_split.columns

# Calcul du nombre de colonnes pour l'affichage
n_attributes = len(attributes)
n_cols = 2  # Nombre de colonnes souhaité
n_rows = (n_attributes + n_cols - 1) // n_cols  # Calcul du nombre de lignes nécessaires

# Créer les sous-graphiques avec deux colonnes
fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 5 * n_rows))
axes = axes.flatten()  # Aplatir pour un accès facile aux axes

for i, attribute in enumerate(attributes):
    # Compter la répartition des classes dans chaque attribut
    value_counts = descriptions_split[attribute].value_counts()

    # Calculer les pourcentages
    percentages = value_counts / value_counts.sum() * 100

    # Tracer l'histogramme
    axes[i].bar(value_counts.index, value_counts.values)
    axes[i].set_title(f"Répartition des classes pour {attribute}")
    axes[i].set_xlabel('Classes')
    axes[i].set_ylabel('Nombre d\'occurrences')
    axes[i].tick_params(axis='x', rotation=45)

    # Ajouter les pourcentages au-dessus des barres
    for j, v in enumerate(value_counts.values):
        axes[i].text(
            j, v + 0.1, f"{percentages.iloc[j]:.2f}%", ha='center', va='bottom', fontsize=10
        )

# Supprimer les axes inutilisés si le nombre de graphiques est inférieur au nombre total de sous-graphiques
for j in range(len(attributes), len(axes)):
    fig.delaxes(axes[j])

# Ajuster l'espacement
plt.tight_layout()

# Afficher les graphiques
plt.show()
