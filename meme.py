from PIL import Image, ImageDraw, ImageFont

def add_text_to_image(image_path, text, output_path):
    """Adds text to an image and saves it."""
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)

    # Load a font (ensure the .ttf file is available or use system fonts)
    font = ImageFont.truetype("arial.ttf", size=36)

    # Calculate text position
    text_width, text_height = draw.textsize(text, font=font)
    width, height = img.size
    x = (width - text_width) // 2
    y = height - text_height - 10  # Position text near the bottom with padding

    # Add text with white color and black border
    draw.text((x - 2, y - 2), text, font=font, fill="black")
    draw.text((x + 2, y + 2), text, font=font, fill="black")
    draw.text((x, y), text, font=font, fill="white")

    # Save the final image
    img.save(output_path)
