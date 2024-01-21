import cv2
import numpy as np

# Load the image
image = cv2.imread('C:\Users\HP\OneDrive\Documents\dsa practice\ProblemStatement\Image-1.jpg')

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply edge detection
edges = cv2.Canny(gray, 50, 150)

# Use Hough transform to detect lines
lines = cv2.HoughLines(edges, 1, np.pi / 180, threshold=100)

# Filter lines based on orientation
horizontal_lines = [line[0] for line in lines if 85 < np.degrees(line[0][1]) < 95]

# Calculate the average angle
if horizontal_lines:
    average_angle = np.degrees(np.mean([line[1] for line in horizontal_lines]))
    print(f"Runway angle with respect to horizontal axis: {average_angle:.2f} degrees")
else:
    print("No horizontal lines detected.")

# Optionally, visualize the results
# (You may need to adjust the code based on your specific image and requirements)
cv2.imshow('Original Image', image)
cv2.imshow('Edge Detection', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
