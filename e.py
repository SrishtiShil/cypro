

import cv2
import os

img = cv2.imread("durga.png")  # Replace with the correct image path

msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Save password and message length for decryption
with open("password.txt", "w") as f:
    f.write(password + "\n")
with open("msg.txt", "w") as t:
    t.write(str(len(msg)))

n, m, z = 0, 0, 0

for i in range(len(msg)):
    img[n, m, z] = ord(msg[i])  # Store ASCII values properly
    z = (z + 1) % 3  # Cycle through RGB channels
    if z == 0:
        m += 1
        if m >= img.shape[1]:  # Move to the next row if column overflows
            m = 0
            n += 1

cv2.imwrite("enImage.png", img)
os.system("start enImage.png")  # Open the encrypted image on Windows
