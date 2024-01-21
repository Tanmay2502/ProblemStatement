import cv2
import numpy as np

def find_runway_angle(image_path):
    # Load the image
    img = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply edge detection (e.g., using Canny)
    edges = cv2.Canny(gray, 50, 150)

    # Find lines in the image using Hough Transform
    lines = cv2.HoughLines(edges, 1, np.pi/180, threshold=100)

    # Calculate the angle of the detected lines
    angles = [line[0][1] for line in lines]

    # Convert radians to degrees
    angles_deg = [np.degrees(angle) for angle in angles]

    # Average the angles to get the overall angle of the runway
    average_angle = np.mean(angles_deg)

    return average_angle

# Example usage:
image_path = "C:\Users\HP\OneDrive\Documents\dsa practice\ProblemStatement\Image-1.jpg"
img=cv2.imread(image_path)

runway_angle = find_runway_angle(image_path)
cv2.imshow("line detected",img)
print("The angle of the runway is approximately",runway_angle,"degrees.")