import os
from pathlib import Path
import shutil

from PIL import Image

# Define the required sizes for macOS `.icns` and their respective filenames
ICON_SIZES = [
    (16, 16, "icon_16x16.png"),
    (32, 32, "icon_32x32.png"),
    (128, 128, "icon_128x128.png"),
    (256, 256, "icon_256x256.png"),
    (512, 512, "icon_512x512.png"),
    (1024, 1024, "icon_1024x1024.png")
]

ICONSET_EXTRA_FILES = [
    ("icon_32x32.png", "icon_16x16@2x.png"),  # Copy 32x32 as 16x16@2x
    ("icon_64x64.png", "icon_32x32@2x.png"),  # Copy 64x64 as 32x32@2x
    ("icon_256x256.png", "icon_128x128@2x.png"),  # Copy 256x256 as 128x128@2x
    ("icon_512x512.png", "icon_256x256@2x.png"),  # Copy 512x512 as 256x256@2x
    ("icon_1024x1024.png", "icon_512x512@2x.png")  # Copy 1024x1024 as 512x512@2x
]


def resize_and_prepare_iconset(input_image_path, output_folder):
    """
    Resize an input .webp image to all macOS icon sizes, save them in PNG format,
    and prepare the files for `iconutil` by renaming and copying as necessary.

    Args:
        input_image_path (str): Path to the input .webp image.
        output_folder (str): Path to the folder where resized images will be saved.
    """
    # Ensure the output folder exists
    iconset_folder = os.path.join(output_folder, "AppIcon.iconset")
    os.makedirs(iconset_folder, exist_ok=True)

    # Open the input image
    with Image.open(input_image_path) as img:
        for width, height, filename in ICON_SIZES:
            # Resize the image
            resized_img = img.resize((width, height), Image.Resampling.LANCZOS)

            # Save the resized image
            output_path = os.path.join(iconset_folder, filename)
            resized_img.save(output_path, "PNG")
            print(f"Saved: {output_path}")

    # Create additional required files by copying and renaming
    for source_file, target_file in ICONSET_EXTRA_FILES:
        source_path = os.path.join(iconset_folder, source_file)
        target_path = os.path.join(iconset_folder, target_file)

        if os.path.exists(source_path):
            shutil.copy(source_path, target_path)
            print(f"Copied: {source_path} -> {target_path}")
        else:
            print(f"Source file {source_path} does not exist. Skipping {target_file}.")


# Example usage
if __name__ == "__main__":
    # Path to your input image
    input_image = Path("./logo/logo_modern.webp")
    # Folder to save resized images
    output_directory = "mac_iconset"  # Replace with your desired folder

    resize_and_prepare_iconset(input_image, output_directory)

    print("\nIconset ready! You can now run `iconutil` to create the .icns file.")

