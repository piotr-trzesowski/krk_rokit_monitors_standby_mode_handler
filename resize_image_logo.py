import os
from pathlib import Path

from PIL import Image


# Define the required sizes for macOS `.icns`
ICON_SIZES = [
    (16, 16),
    (32, 32),
    (128, 128),
    (256, 256),
    (512, 512),
    (1024, 1024)
]


def resize_for_mac(input_image_path, output_folder):
    """
    Resize an input image to all macOS icon sizes and save them in a specified folder.

    Args:
        input_image_path (Path): Path to the input image.
        output_folder (str): Path to the folder where resized images will be saved.
    """
    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Open the input image
    with Image.open(input_image_path) as img:
        for size in ICON_SIZES:
            # Resize the image
            resized_img = img.resize(size, Image.Resampling.LANCZOS)

            # Save the resized image with the correct filename
            output_filename = f"icon_{size[0]}x{size[1]}.png"
            output_path = os.path.join(output_folder, output_filename)
            resized_img.save(output_path, "PNG")
            print(f"Saved: {output_path}")


# Example usage
if __name__ == "__main__":
    # Path to your input image
    input_image = Path("./logo/logo_modern.webp")
    # Folder to save resized images
    output_directory = "mac_iconset"  # Replace with your desired folder

    resize_for_mac(input_image, output_directory)
