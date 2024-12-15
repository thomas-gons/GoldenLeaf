import torch
from transformers import LlavaNextProcessor, LlavaNextForConditionalGeneration
import os
from tqdm import tqdm
from PIL import Image


herbarium_path = "/home/thomas/PycharmProjects/GoldenLeaf/src/resources/images/"
images = {}
for file in os.listdir(herbarium_path):
    if file.endswith("jpg"):
        image_path = herbarium_path + file
        images.update({image_path: Image.open(image_path)})

processor = LlavaNextProcessor.from_pretrained("llava-hf/llava-v1.6-mistral-7b-hf")

model = LlavaNextForConditionalGeneration.from_pretrained("llava-hf/llava-v1.6-mistral-7b-hf", torch_dtype=torch.float16, low_cpu_mem_usage=True)

master_prompt = """
You are a botanist tasked with analyzing herbarium images. For each image, provide structured observations about the plant's features. 
  For each feature, choose one value from the predefined options and present your analysis as concise sentences. Use the following structure:

  - **Leaves**
    - Shape: simple, lobed, compound, other.
    - Margin: entire, toothed, scalloped.
    - Arrangement: opposite, alternate, whorled.
    - Texture: smooth, rough, velvety.

  - **Stem**
    - Type: woody, herbaceous, hollow, solid.
    - Cross-section: round, square, angular.
    - Presence of hairs or spines: yes, no.

  Format your output as follows:
  'The shape of the leaves is [selected_option]|The margin of the leaves is [selected_option]|The arrangement of the leaves is [selected_option]|The texture of the leaves is [selected_option]|The type of the stem is [selected_option]|The cross-section of the stem is [selected_option]|The presence of hairs or spines is [selected_option]'

  Only use the options provided for each feature, and avoid any additional text or commentary.

  **Examples:**

  Example 1:
  Observation: An image of a plant with smooth leaves arranged alternately, and a hollow, angular stem with no hairs.
  Output: 'The shape of the leaves is simple|The margin of the leaves is entire|The arrangement of the leaves is alternate|The texture of the leaves is smooth|The type of the stem is hollow|The cross-section of the stem is angular|The presence of hairs or spines is no'

  Example 2:
  Observation: An image of a plant with lobed leaves having toothed margins, arranged oppositely, and a woody, round stem with hairs.
  Output: 'The shape of the leaves is lobed|The margin of the leaves is toothed|The arrangement of the leaves is opposite|The texture of the leaves is rough|The type of the stem is woody|The cross-section of the stem is round|The presence of hairs or spines is yes'

  Example 3:
  Observation: An image of a plant with compound leaves, scalloped margins, arranged in a whorled pattern, and a solid, square stem with no hairs.
  Output: 'The shape of the leaves is compound|The margin of the leaves is scalloped|The arrangement of the leaves is whorled|The texture of the leaves is velvety|The type of the stem is solid|The cross-section of the stem is square|The presence of hairs or spines is no'

  Now, analyze the given image and provide your structured observations."""


conversation = [
    {
        "role": "user",
        "content": [
            {"type": "image"},
            {"type": "text", "text": f"{master_prompt}"},
        ],
    },
]
prompt = processor.apply_chat_template(conversation, add_generation_prompt=True)

max_size = 800
for image_file, img in tqdm(images.items()):
    scale = max_size / max(img.size)
    new_size = (int(img.size[0] * scale), int(img.size[1] * scale))
    new_img = img.resize(new_size, Image.Resampling.LANCZOS)
    inputs = processor(new_img, prompt, return_tensors="pt")
    output = model.generate(**inputs, max_new_tokens=100)
    print(processor.decode(output[0], skip_special_tokens=True))
