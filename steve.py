import alive_progress
import colorama

from PIL import Image
import os

# Initialize the colorama library
colorama.init()

# Define a function to convert an image to TIFF format and resize it until it reaches a minimum size
def convert_to_tiff(input_image_path, output_image_path):
    # Open the input image
    with Image.open(input_image_path) as image:
        # Convert the image to TIFF format
        image.save(output_image_path, format='TIFF')

        # Get the file size of the output image
        file_size = os.path.getsize(output_image_path)

        # While the file size is less than the minimum size, resize the image and save it again
        while file_size < min_size:
            # Get the width and height of the image
            width, height = image.size

            # Resize the image by doubling its width and height
            image = image.resize((width * 2, height * 2))

            # Save the resized image
            image.save(output_image_path, format='TIFF')

            # Get the new file size
            file_size = os.path.getsize(output_image_path)

# If the code is being run as the main script, call the convert_to_tiff() function
if __name__ == '__main__':

    # Prompt the user for the initial image
    input_image_path = input("Enter the path to the initial image: ")

    # Get the minimum size of the output image
    min_size = 10 * 1024 * 1024 # 10MB in bytes

    # Create a progress bar
    progress = alive_progress.alive_bar(
        'Converting image...',
        max=min_size,
        disable=False
    )

    # Convert the image to TIFF format and resize it until it reaches the minimum size
    with progress:
        convert_to_tiff(input_image_path, 'output.tiff')

    # Print a message to the user
    print("Image converted successfully!")
