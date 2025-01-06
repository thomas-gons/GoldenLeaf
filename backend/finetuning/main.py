from generate_description import HerbariumImageProcessor
from parse_description import HerbariumDescriptionProcessor

areDescriptionGenerated = True

if __name__ == "__main__":
    if areDescriptionGenerated == False:
        processor = HerbariumImageProcessor(config_path="src/resources/config.yaml")
        processor.generate_descriptions_to_csv()

    processor = HerbariumDescriptionProcessor(config_path="src/resources/config.yaml")
    processor.load_and_process_csv()

    descriptions = processor.get_descriptions()
    for image, desc_list in descriptions.items():
        print(f"Image: {image}\nDescriptions: {desc_list}\n")
