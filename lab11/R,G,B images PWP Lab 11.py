import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r'C:\Users\admin\Downloads\MU.jpg') 
b, g, r = cv2.split(img)

plt.figure(figsize=(10, 6))

plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Original Image")

plt.subplot(2, 2, 2)
plt.imshow(r, cmap='Reds')
plt.title("Red Channel")

plt.subplot(2, 2, 3)
plt.imshow(g, cmap='Greens')
plt.title("Green Channel")

plt.subplot(2, 2, 4)
plt.imshow(b, cmap='Blues')
plt.title("Blue Channel")
plt.show()

