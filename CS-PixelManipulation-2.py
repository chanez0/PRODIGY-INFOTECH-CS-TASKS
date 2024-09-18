from tkinter import Tk, Label, Button, Entry, filedialog, messagebox
from PIL import Image
import numpy as np

# usig PIL to create a basic user interface

# Function to encrypt the image
def encrypt_image(input_image_path, output_image_path, key):
    img = Image.open(input_image_path)
    img_array = np.array(img)

    # Ensure key is a proper integer and apply encryption
    encrypted_array = np.mod((img_array + int(key)), 256).astype(np.uint8)
    
    encrypted_img = Image.fromarray(encrypted_array)
    encrypted_img.save(output_image_path)



# Function to decrypt the image
def decrypt_image(input_image_path, output_image_path, key):
    img = Image.open(input_image_path)
    img_array = np.array(img)

    # Ensure key is a proper integer and apply decryption
    decrypted_array = np.mod((img_array - int(key)), 256).astype(np.uint8)
    
    decrypted_img = Image.fromarray(decrypted_array)
    decrypted_img.save(output_image_path)


# Function to select an image file
def select_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        entry_image_path.delete(0, 'end')
        entry_image_path.insert(0, file_path)

# Function to encrypt the image
def encrypt_button_action():
    input_image = entry_image_path.get()
    output_image = "encrypted_image.png"
    key = int(entry_key.get())
    
    if input_image and key:
        try:
            encrypt_image(input_image, output_image, key)
            messagebox.showinfo("Success", "Image encrypted and saved as 'encrypted_image.png'")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to encrypt image: {str(e)}")

# Function to decrypt the image
def decrypt_button_action():
    input_image = entry_image_path.get()
    output_image = "decrypted_image.png"
    key = int(entry_key.get())
    
    if input_image and key:
        try:
            decrypt_image(input_image, output_image, key)
            messagebox.showinfo("Success", "Image decrypted and saved as 'decrypted_image.png'")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to decrypt image: {str(e)}")

# Tkinter GUI setup
root = Tk()
root.title("Image Encryption Tool")
root.geometry("400x250")

# Image path input field
label_image_path = Label(root, text="Select Image:")
label_image_path.pack(pady=10)

entry_image_path = Entry(root, width=40)
entry_image_path.pack(pady=5)

button_browse = Button(root, text="Browse", command=select_image)
button_browse.pack(pady=5)

# Key input field
label_key = Label(root, text="Enter Key (integer):")
label_key.pack(pady=10)

entry_key = Entry(root, width=10)
entry_key.pack(pady=5)

# Encrypt and Decrypt buttons
button_encrypt = Button(root, text="Encrypt Image", command=encrypt_button_action)
button_encrypt.pack(pady=10)

button_decrypt = Button(root, text="Decrypt Image", command=decrypt_button_action)
button_decrypt.pack(pady=5)

# Start the GUI loop
root.mainloop()
