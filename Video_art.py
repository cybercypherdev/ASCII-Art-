import cv2
import numpy as np
import os

# List of ASCII characters used to represent pixel intensity
ASCII_CHARS = ['N', '@', '#', 'W', '$', '9', '8', '7', '6', '5', '4', '3', '2', '1', '?', '!', 'a', 'b', 'c', ';', ':', '+', '=', '-', ',', '.', '_']

def resize_image(image, new_width=200):
    """
    Resize the image to a new width while maintaining the aspect ratio.
    The height is adjusted to maintain the aspect ratio.
    """
    height, width, _ = image.shape
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio * 0.55)  # Adjust aspect ratio
    resized_image = cv2.resize(image, (new_width, new_height))
    return resized_image

def pixel_to_ascii(image):
    """
    Convert each pixel in the image to an ASCII character based on its grayscale value.
    The ASCII character is colored using the original pixel's RGB values.
    """
    pixels = image.reshape(-1, 3)  # Flatten the image array
    ascii_image = ""
    for pixel in pixels:
        r, g, b = pixel
        # Convert RGB to grayscale using the luminosity method
        gray = int(0.2989 * r + 0.5870 * g + 0.1140 * b)
        # Map the grayscale value to an ASCII character
        ascii_char = ASCII_CHARS[gray // 10]
        # Add the ASCII character with color formatting
        ascii_image += f"\033[38;2;{r};{g};{b}m{ascii_char}\033[0m"
    return ascii_image

def main():
    # Open the default camera
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open video stream.")
        return

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            break

        # Resize the frame
        resized_frame = resize_image(frame)
        # Convert the frame to ASCII
        ascii_frame = pixel_to_ascii(resized_frame)
        # Calculate the number of ASCII characters per row
        pixel_count = len(ascii_frame) // 24  # Each ASCII character is represented by 24 characters (color code + ASCII char)
        # Split the ASCII string into rows
        ascii_image = "\n".join(ascii_frame[i * 24 * resized_frame.shape[1]:(i + 1) * 24 * resized_frame.shape[1]] for i in range(pixel_count // resized_frame.shape[1]))

        # Clear the terminal screen
        os.system('cls' if os.name == 'nt' else 'clear')
        # Print the ASCII image
        print(ascii_image)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture and close any OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
