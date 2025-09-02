import cv2

img = cv2.imread(r'C:\Users\admin\Downloads\MU.jpg') 
print("Shape of image:", img.shape)
print("Dimensions of image:", img.ndim)
print("Height (rows):", img.shape[0])
print("Width (cols):", img.shape[1])
print("Channels:", img.shape[2])
min_blue = img[:, :, 0].min()
print("Minimum pixel value at channel B:", min_blue)

