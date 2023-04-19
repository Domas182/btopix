import sys
from PIL import Image, ImageDraw
from tqdm import tqdm

def read_input_file(file_path):
    with open(file_path, 'r') as file:
        contents = file.read()
    return contents.replace(' ', '')

def generate_image(data, width_limit=2000, square_size=10):
    data_length = len(data)
    width = min(data_length * square_size, width_limit)
    height = ((data_length - 1) // (width_limit // square_size) + 1) * square_size

    image = Image.new("RGB", (width, height), "black")
    draw = ImageDraw.Draw(image)

    x, y = 0, 0
    for i in tqdm(range(data_length), desc="Generating image"):
        if data[i] == '1':
            draw.rectangle([x, y, x + square_size - 1, y + square_size - 1], fill="white")

        x += square_size
        if x >= width_limit:
            x = 0
            y += square_size

    return image

def main(input_file, output_file):
    data = read_input_file(input_file)
    image = generate_image(data)
    image.save(output_file, "PNG")
    print(f"Image saved to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python image_generator.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)
