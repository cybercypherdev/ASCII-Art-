from colorama import init
import PIL.Image

# List of ASCII characters used to create the ASCII art
ASCII_CHARS = ['N', '@', '#', 'W', '$', '9', '8', '7', '6', '5', '4', '3', '2', '1', '?', '!', 'a', 'b', 'c', ';', ':', '+', '=', '-', ',', '.', '_']

# Initialize colorama to reset colors after each print
init(autoreset=True)

def resize_image(image, max_width=100, max_height=50):
    """
    Resize the image to fit within the specified max_width and max_height while maintaining aspect ratio.
    """
    width, height = image.size
    aspect_ratio = height / width
    new_width = min(max_width, width)
    new_height = min(max_height, int(new_width * aspect_ratio))
    
    # Adjust new_width if new_height exceeds max_height
    if new_height > max_height:
        new_height = max_height
        new_width = int(new_height / aspect_ratio)
    
    # Resize the image
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayify(image):
    """
    Convert the image to grayscale.
    """
    return image.convert("L")

def pixel_to_ascii(image, colored_image):
    """
    Convert each pixel to an ASCII character based on its intensity and color the character.
    """
    pixels = image.getdata()
    colored_pixels = colored_image.getdata()
    characters = [color_pixel(ASCII_CHARS[pixel // 10], colored_pixels[i]) for i, pixel in enumerate(pixels)]
    return characters

def color_pixel(char, pixel):
    """
    Color the ASCII character based on the RGB values of the pixel.
    """
    r, g, b = pixel[:3]
    return f"\033[38;2;{r};{g};{b}m{char}"

def main():
    """
    Main function to handle user input, process the image, and print/save the ASCII art.
    """
    path = input("Enter path to the image: ")
    try:
        image = PIL.Image.open(path)
    except Exception as e:
        print(f"Error: {e}. '{path}' is not a valid image path.")
        return

    max_width = 100
    max_height = 50
    resized_image = resize_image(image, max_width, max_height)
    gray_image = grayify(resized_image)
    new_image_data = pixel_to_ascii(gray_image, resized_image)
    new_width = resized_image.width
    
    # Create the ASCII art by joining characters into lines
    ascii_image = "\n".join("".join(new_image_data[i:i + new_width]) for i in range(0, len(new_image_data), new_width))
    
    # Color the ASCII art
    colored_ascii_image = "\n".join([color_pixel(line, (255, 255, 255)) for line in ascii_image.split('\n')])

    # Print the colored ASCII art
    print(colored_ascii_image)

    # Save the ASCII art to a text file
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)

if __name__ == "__main__":
    main()
