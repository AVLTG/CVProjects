import cv2
import matplotlib.pyplot as plt
image = cv2.imread('Images/K12_ 6Triangles_1_EG.png')
cv2.waitKey(0)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edged = cv2.Canny(gray, 30, 200)
cv2.waitKey(0)

contours, hierarchy = cv2.findContours(edged,
    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

cv2.imshow('Canny Edges After Contouring', edged)
cv2.waitKey(0)

print("Number of Contours = " + str(len(contours)))

x = cv2.drawContours(image, contours, -1, (0, 255, 0), 3)

plt.figure()
plt.title('Notebook opened on desk near books')
plt.imsave('Results/TriangleEdgeContours.png', x, cmap='gray', format='png')

cv2.imshow('Contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
