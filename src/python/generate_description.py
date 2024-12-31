import glob
from io import BytesIO
import os
import logging
import yaml
import pandas as pd
from PIL import Image, UnidentifiedImageError
from ollama import generate
from tqdm import tqdm


# Configurer le logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()


class HerbariumImageProcessor:
    def __init__(self, config_path):
        self.config = self.load_config(config_path)
        self.image_folder = self.config["image_folder"]
        self.output_csv = self.config["output_csv"]
        self.model = self.config["model"]
        self.system_prompt = self.config["system_prompt"]

        self.already_computed_images = set()

        if os.path.exists(self.output_csv):
            existing_data = pd.read_csv(self.output_csv)
            self.already_computed_images = set(existing_data['image'].tolist())
        else:
            pd.DataFrame(columns=['image', 'description']).to_csv(self.output_csv, index=False, encoding='utf-8')

    @staticmethod
    def load_config(config_path):
        """Charge le fichier de configuration YAML."""
        try:
            with open(config_path, 'r') as stream:
                return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            logger.error(f"Error loading configuration: {exc}")
            raise RuntimeError(f"Error loading configuration: {exc}")

    @staticmethod
    def get_jpg_files(folder_path):
        """Récupère tous les fichiers JPG dans un dossier donné."""
        return glob.glob(f"{folder_path}/*.jpg")

    @staticmethod
    def resize_image(img, max_size=800):
        """Redimensionne une image si elle dépasse une taille maximale."""
        if max(img.size) > max_size:
            scale = max_size / max(img.size)
            new_size = (int(img.size[0] * scale), int(img.size[1] * scale))
            img = img.resize(new_size, Image.Resampling.LANCZOS)
        return img

    def process_image(self, image_file):
        """Traite une image et génère une description."""
        logger.info(f"Processing {image_file}")
        try:
            with Image.open(image_file) as img:
                img = self.resize_image(img)
                with BytesIO() as buffer:
                    img.save(buffer, format='JPEG')
                    image_bytes = buffer.getvalue()
        except UnidentifiedImageError:
            logger.error(f"Error: Unable to process {image_file}. Skipping.")
            return None

        full_response = ''
        try:
            for response in generate(
                model=self.model,
                prompt=self.system_prompt,
                images=[image_bytes],
                stream=True
            ):
                full_response += response['response']
        except Exception as e:
            logger.error(f"Error during generation for {image_file}: {e}")
            return None

        return full_response

    def generate_descriptions_to_csv(self):
        """Génère des descriptions pour toutes les images et les sauvegarde dans un fichier CSV."""
        image_files = [
            image_file for image_file in self.get_jpg_files(self.image_folder)
            if image_file not in self.already_computed_images
        ]

        image_files.sort()


        for image_file in tqdm(image_files, desc="Processing images"):

            description = self.process_image(image_file)
            if description:
                new_entry = pd.DataFrame([{'image': image_file, 'description': description}])
                new_entry.to_csv(self.output_csv, mode='a', header=False, index=False, encoding='utf-8')
                logger.info(f"Added description for {image_file} to {self.output_csv}")

        logger.info(f"All descriptions have been computed.")
