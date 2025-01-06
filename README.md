# GoldenLeaf

GoldenLeaf is a Python application designed to create an image search system using the CLIP model. The project involves generating descriptions for herbarium images, which are used to train the CLIP model to associate images with their corresponding textual descriptions. This process enhances the multi-modal search capabilities of the system.

## Part 1: Description Generation

This section covers the setup and steps involved in generating descriptions for herbarium images using the Llava model.

### Prerequisites

Ensure the following are installed on your machine:

| Package         | Version        |
|-----------------|----------------|
| Python          | 3.12 or greater|
| Ollama          | 0.4.5 or greater|

### Installation

#### 1. Install Python

Ensure you have Python 3.12 or newer installed on your machine. You can download Python from the official site: [Python Downloads](https://www.python.org/downloads/).

#### 2. Install Ollama

Download and install Ollama following the instructions on the official site: [Ollama Downloads](https://ollama.com/download).

#### 3. Install Python dependencies

Clone this repository and install the required Python dependencies using `pip` :

```bash
git clone <YOUR_REPOSITORY_URL>
cd GoldenLeaf/backend
python -m venv .venv  # Create a virtual environment (optional but recommended)
source .venv/bin/activate  # Activate the virtual environment
pip install -r requirements.txt
```

### Configuration

Before running the application, make sure to set up Ollama’s `llava:latest` model :

#### 1. Pull the `llava:latest` model

Download the `llava:latest` model with the following command :

```bash
ollama pull llava:latest
```

#### 2. Start Ollama server

Once the model is downloaded, run Ollama using :

```bash
ollama serve
```

#### 3. Configure the Application

Ensure that the `config.yaml` file is properly set up. This file should specify the parameters for image processing, model usage, and output paths. Adjust these settings according to your project's structure and requirements.

### Running the Description Generation

After setting up the dependencies and starting Ollama, run the application by executing `main.py` from the `backend/data_augmentation/` directory. This will generate descriptions for the images and save them in a CSV file

```bash
python backend/data_augmentation/main.py
```

The application will process all images, generate descriptions, and save them to the specified output CSV. These descriptions will be used for data augmentation in training the CLIP model for image search functionality.

### Key Features

- **Automated Image Description Generation:** Utilizes the Llava model to generate textual descriptions for herbarium images.
- **Multi-modal Data Augmentation:** Enhances the dataset by pairing images with their corresponding descriptions, improving the CLIP model's training effectiveness.
- **Customizable Configuration:** Easily adjust parameters through the `config.yaml` file to fit various datasets and requirements.

### Challenges Addressed

- **Processing Time:** Local processing of large datasets was optimized to manage time constraints.
- **Description Quality:** Initial descriptions were refined by defining a robust system prompt to ensure consistency and accuracy.
- **Manual Corrections:** Despite automation, manual review was necessary to maintain high-quality descriptions, ensuring the dataset's integrity for model training.

GoldenLeaf provides a streamlined approach to integrating image and text data for advanced search functionalities, leveraging the power of deep learning and multi-modal models.

## Part 2: Running the Complete Application

This section describes the steps to run the entire GoldenLeaf application, including the backend, frontend, and interaction with the image search system.

### How to Run the Project

#### Backend

The backend is built using FastAPI and Uvicorn. To run the backend:

1) (If not already done) **Create** a virtual environment and install dependencies (inside `backend/` repository):
    ```bash
    pip install -r requirements.txt
    ```

2) **Run** the FastAPI server (from root project repository):
    ```bash
    uvicorn backend.main:app --host 0.0.0.0 --port 8000
    ```

The API will be available at http://localhost:8000. The backend includes several endpoints for image search, uploading images, and removing images.

#### Frontend

To set up and run the frontend:

1) **Install** dependencies using npm (inside `frontend/` repository):
    ```bash
    npm install
    ```

2) **Start** the development server (inside `frontend/` repository):
    ```bash
    npm run dev
    ```

The frontend will be available at http://localhost:8080. It will allow you to interact with the backend by uploading images or entering text queries.
