import cv2
import os

# Load the cover image
image_path = "stegoimg.png"  # Ensure this image exists in the directory
img = cv2.imread(image_path)

if img is None:
    print("❌ Error: Image not found! Make sure 'stegoimg.png' exists.")
    exit()

# Get user input for password and secret message
password = input("🔑 Enter a password: ")
message = input("💬 Enter secret message: ")

# Combine password and message with a separator and an end delimiter
hidden_data = password + "|" + message + "~"

# Encode the hidden data into the blue channel of the image
msg_index = 0
rows, cols, _ = img.shape

for i in range(rows):
    for j in range(cols):
        if msg_index < len(hidden_data):
            img[i, j, 0] = ord(hidden_data[msg_index])  # Modify the blue channel
            msg_index += 1
        else:
            break
    if msg_index >= len(hidden_data):
        break

# Save the encrypted image
output_image = "stego_image/encryptedImage.png"

# Ensure the output folder exists
if not os.path.exists("stego_image"):
    os.makedirs("stego_image")

cv2.imwrite(output_image, img)
