import cv2
import numpy as np

# Read the image
image = cv2.imread("test.jpg")

if image is None:
    print("Image not found!")
else:
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Create a kernel
    kernel = np.ones((5, 5), np.uint8)

    # Apply dilation
    dilated = cv2.dilate(gray, kernel, iterations=1)

    # Display images
    cv2.imshow("Original Image", gray)
    cv2.imshow("Dilated Image", dilated)

    # Save the dilated image
    cv2.imwrite("dilated.jpg", dilated)

    print("Image dilation completed successfully!")

    cv2.waitKey(0)
    cv2.destroyAllWindows()