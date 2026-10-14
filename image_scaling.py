import cv2

# Read the image
image = cv2.imread("test.jpg")

if image is None:
    print("Image not found!")
else:
    # Resize to a bigger size
    bigger = cv2.resize(image, None, fx=2, fy=2,
                        interpolation=cv2.INTER_LINEAR)

    # Resize to a smaller size
    smaller = cv2.resize(image, None, fx=0.5, fy=0.5,
                         interpolation=cv2.INTER_AREA)

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Bigger Image", bigger)
    cv2.imshow("Smaller Image", smaller)

    # Save resized images
    cv2.imwrite("bigger.jpg", bigger)
    cv2.imwrite("smaller.jpg", smaller)

    print("Image scaling completed successfully!")

    cv2.waitKey(0)
    cv2.destroyAllWindows()