from generate_description import HerbariumImageProcessor

if __name__ == "__main__":
    processor = HerbariumImageProcessor(config_path="src/resources/config.yaml")
    processor.generate_descriptions_to_csv()
