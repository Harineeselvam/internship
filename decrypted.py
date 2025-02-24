import cv2

# Load the encrypted image
image_path = "stego_image/encryptedImage.png"  # Path to the stego image
img = cv2.imread(image_path)

if img is None:
    print("❌ Error: Encrypted image not found! Make sure 'encryptedImage.png' exists in 'stego_image' folder.")
    exit()

# Extract hidden data from the blue channel
hidden_data = ""
rows, cols, _ = img.shape

for i in range(rows):
    for j in range(cols):
        char = chr(img[i, j, 0])  # Read ASCII value from the blue channel
        if char == "~":  # End delimiter for hidden message
            break
        hidden_data += char
    if char == "~":
        break

# Split the password and message
if "|" in hidden_data:
    password, message = hidden_data.split("|", 1)
    print("\n✅ Decryption Successful!")
    print(f"🔑 Extracted Password: {password}")
    print(f"💬 Hidden Message: {message}")
else:
    print("❌ No hidden message found!")
