import cv2

# Read the image
image = cv2.imread("test.jpg")

if image is None:
    print("Image not found!")
else:
    # Rotate image 90 degrees clockwise
    rotated = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Rotated Image", rotated)

    # Save the rotated image
    cv2.imwrite("rotated.jpg", rotated)

    print("Image rotated successfully!")

    cv2.waitKey(0)
    cv2.destroyAllWindows()