import cv2

def are_images_same(image1, image2):
    # Load the two images
    img1 = cv2.imread(image1)
    img2 = cv2.imread(image2)
    
    # Check if the images are the same size
    if img1.shape != img2.shape:
        return False
    
    # Compute the absolute difference between the two images
    diff = cv2.absdiff(img1, img2)
    
    # Convert the difference image to grayscale
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    
    # Apply a threshold to the grayscale image
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)[1]
    
    # Count the number of non-zero pixels in the thresholded image
    non_zero_pixels = cv2.countNonZero(thresh)
    
    # Calculate the percentage of non-zero pixels in the image
    percentage_diff = non_zero_pixels / (img1.shape[0] * img1.shape[1]) * 100
    print(percentage_diff)
    
    # If the percentage difference is less than a threshold, the images are considered the same
    if percentage_diff < 0.5:
        return True
    else:
        return False

    
if __name__ == "__main__":
    print(are_images_same('./inputs/1_c_O_3gatu_A.jpg', './inputs/1_c_O_3gatu_A_K.jpg'))