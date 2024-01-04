# Import necessary libraries
import tkinter as tk
from PIL import Image, ImageTk

# Create the main window
window = tk.Tk()
window.title("圖形處理 - 圖形介面")

# Define the function to open an image
def open_image():
    # Get the image file path from the user
    image_path = tk.filedialog.askopenfilename()

    # Load the image using PIL
    image = Image.open(image_path)

    # Resize the image to fit the window
    image = image.resize((500, 500))

    # Convert the image to a Tkinter-compatible format
    image_tk = ImageTk.PhotoImage(image)

    # Display the image in the window
    image_label.configure(image=image_tk)

# Define the function to apply a grayscale filter to the image
def grayscale_image():
    # Get the current image from the label
    image_tk = image_label.cget("image")

    # Convert the image to grayscale using PIL
    image = ImageTk.getimage(image_tk).convert("L")

    # Convert the image back to a Tkinter-compatible format
    image_tk = ImageTk.PhotoImage(image)

    # Display the grayscale image in the window
    image_label.configure(image=image_tk)

# Define the function to apply a blur filter to the image
def blur_image():
    # Get the current image from the label
    image_tk = image_label.cget("image")

    # Convert the image to grayscale using PIL
    image = ImageTk.getimage(image_tk).filter(ImageFilter.GaussianBlur(10))

    # Convert the image back to a Tkinter-compatible format
    image_tk = ImageTk.PhotoImage(image)

    # Display the blurred image in the window
    image_label.configure(image=image_tk)

# Create a label to display the image
image_label = tk.Label(window)
image_label.grid(row=0, column=0, columnspan=3)

# Create a button to open an image
open_button = tk.Button(window, text="打開圖像", command=open_image)
open_button.grid(row=1, column=0)

# Create a button to apply a grayscale filter to the image
grayscale_button = tk.Button(window, text="灰階化", command=grayscale_image)
grayscale_button.grid(row=1, column=1)

# Create a button to apply a blur filter to the image
blur_button = tk.Button(window, text="模糊化", command=blur_image)
blur_button.grid(row=1, column=2)

# Run the main loop
window.mainloop()
