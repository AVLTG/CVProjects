import cv2
import matplotlib.pyplot as plt

# Load image
img = cv2.imread('Images/pexels-annpoan-5797899.jpg')
# Convert to grayscale (even though image is already black and white)
edges = cv2.Canny(img, 100, 200, L2gradient=True)
# Display image
plt.figure()
plt.title('Notebook opened on desk near books')
# Save image
plt.imsave('Results/CannyEdgeNotebookOpenedOnDeskNearBooks.png', edges, cmap='gray', format='png')
plt.imshow(edges, cmap='gray')
plt.show()
