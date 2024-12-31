import pandas as pd
import yaml
from collections import defaultdict


class HerbariumDescriptionProcessor:
    def __init__(self, config_path):
        """Initialise la classe avec le chemin vers le fichier de configuration."""
        self.config_path = config_path
        self.image_descriptions = defaultdict(list)
        self.csv_path = self.load_config()['output_csv']

    def load_config(self):
        """Charge le fichier de configuration YAML."""
        try:
            with open(self.config_path, 'r') as stream:
                return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            raise RuntimeError(f"Erreur lors du chargement de la configuration : {exc}")

    def load_and_process_csv(self):
        """Charge le fichier CSV et associe chaque image à une liste de descriptions."""
        try:
            data = pd.read_csv(self.csv_path)
            
            if 'image' not in data.columns or 'description' not in data.columns:
                raise ValueError("Le fichier CSV doit contenir les colonnes 'image' et 'description'.")

            for _, row in data.iterrows():
                image_path = row['image']
                descriptions = row['description'].split('|')
                self.image_descriptions[image_path] = descriptions

        except Exception as e:
            print(f"Erreur lors du chargement et du traitement du fichier CSV : {e}")

    def get_descriptions(self):
        """Retourne la structure associant chaque image à sa liste de descriptions."""
        return self.image_descriptions
