
import cv2
import os

img = cv2.imread("enImage.png")

# Read password and message length
try:
    with open("password.txt", "r") as f:
        password = f.readline().strip()
    with open("msg.txt", "r") as t:
        msg_length = int(t.readline().strip())
except FileNotFoundError:
    print("Error: Required file not found!")
    exit()
except ValueError:
    print("Error: Corrupted msg.txt file!")
    exit()

message = ""
n, m, z = 0, 0, 0

pas = input("Enter passcode for Decryption: ")
if password == pas:
    for i in range(msg_length):
        message += chr(img[n, m, z])  # Correctly decode ASCII values
        z = (z + 1) % 3  # Cycle through RGB channels
        if z == 0:
            m += 1
            if m >= img.shape[1]:  # Move to the next row if column overflows
                m = 0
                n += 1
    print("Decryption message:", message)
else:
    print("YOU ARE NOT auth")
