import os
import random

# The path to your folder
folder_path = 'C:\\Users\\Dana\\Desktop\\Black shirt for men\\'

# Some sample descriptions, tags and prices. In a real situation, these would be dynamically generated based on each image.
descriptions = ["A cool design for those who love to travel.", "An exciting design for video game fans.", "A simple and elegant design for everyday wear."]
tags = ["Travel, Design, Cool, Adventure", "Video Game, Exciting, Design, Play", "Simple, Elegant, Design, Everyday Wear"]
prices = ["19.95", "24.95", "29.95"]

def generate_prompt(image_path):
    # Split the image_path to get the title from the file name
    title = os.path.splitext(os.path.basename(image_path))[0]

    # Get a random description, tags and price
    description = random.choice(descriptions)
    tags_list = random.choice(tags)
    price = random.choice(prices)

    # Create the prompt
    prompt = f"| {title} | {description} | {tags_list} | {price} | {image_path} |"
    return prompt

# Get the list of all image files in the folder
image_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# Generate a prompt for each image file
for image_file in image_files:
    print(generate_prompt(image_file))
