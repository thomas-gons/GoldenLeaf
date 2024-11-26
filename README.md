# GoldenLeaf

GoldenLeaf is a Python application designed to create an image search system using the CLIP model. The image description generation is a preliminary step for data augmentation, helping train the CLIP model on the images and their associated descriptions.

## Prerequisites

Make sure you have the following installed:

| Package         | Version        |
|-----------------|----------------|
| Python          | 3.12 or greater|
| Ollama | 0.4.5 or greater |

## Installation

### 1. Install Python

Ensure you have Python 3.12 or newer installed on your machine. You can download Python from the official site: [Python Downloads](https://www.python.org/downloads/).

### 2. Install Ollama

Download and install Ollama following the instructions on the official site: [Ollama Downloads](https://ollama.com/download).

### 3. Install Python dependencies

Clone this repository and install the required Python dependencies using `pip` :

```bash
git clone <YOUR_REPOSITORY_URL>
cd GoldenLeaf
python -m venv .venv  # Create a virtual environment (optional but recommended)
source .venv/bin/activate  # Activate the virtual environment
pip install -r requirements.txt
```

## Configuration

Before running the application, make sure to set up Ollama’s llava:latest model :

### 1. Pull the `llava:latest` model

Download the `llava:latest` model with the following command :

```bash
ollama pull llava:latest
```

### 2. Start Ollama server

Once the model is downloaded, run Ollama using :

```bash
ollama serve
```

## Running the Application

After setting up the dependencies and starting Ollama, you can run the application by executing `main.py` from the root directory. This will generate descriptions for the images and save them in a CSV file.

```bash
python src/python/main.py
```

The application will process all images, generate descriptions, and save them to the specified output CSV. These descriptions will be used for data augmentation in training the CLIP model for image search functionality.
