# Description
# This code allows you to interactively draw, move, and resize circles on an image using OpenCV. By using the mouse, you can perform the following actions:

# Drawing Circles:
# Left Click: Start drawing a new circle. The initial click sets the center of the circle, and dragging the mouse adjusts the radius. Release the left mouse button to finish drawing the circle.
# Moving Circles:
# Left Click on an Existing Circle: Select an existing circle by clicking near its center. Drag the mouse to move the circle to a new location. Release the left mouse button to drop the circle at the new location.
# Resizing Circles:
# Right Click on an Existing Circle: Select an existing circle by clicking near its center. Drag the mouse to adjust the radius of the circle. Release the right mouse button to set the new radius.
# Reset and Exit:
# Press 'r': Reset all circles, clearing the canvas.
# Press 'c': Exit the program and print the list of circles to the console.


# change the position and radius as well
import cv2
import numpy as np

# initialize the list of circles and boolean indicating
# whether cropping is being performed or not
circles = []
current_circle = None
drawing = False
moving = False
resizing = False

def click_and_crop(event, x, y, flags, param):
    # grab references to the global variables
    global circles, current_circle, drawing, moving, resizing

    # if the left mouse button was clicked, record the starting
    # (x, y) coordinates and indicate that cropping is being
    # performed
    if event == cv2.EVENT_LBUTTONDOWN:
        for circle in reversed(circles):
            if np.sqrt((circle[0][0] - x)**2 + (circle[0][1] - y)**2) <= circle[1]:
                current_circle = circle
                moving = True
                drawing = False
                resizing = False
                break
        else:
            current_circle = [(x, y), 0]
            circles.append(current_circle)
            drawing = True
            moving = False
            resizing = False

    # check to see if the right mouse button was clicked
    elif event == cv2.EVENT_RBUTTONDOWN:
        if current_circle is not None:
            resizing = True
            moving = False
            drawing = False

    # check to see if the mouse is moving
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            # update the radius of the circle
            current_circle[1] = int(np.sqrt((current_circle[0][0] - x)**2 + (current_circle[0][1] - y)**2))
        elif moving:
            # move the circle
            current_circle[0] = (x, y)
        elif resizing:
            # resize the circle
            current_circle[1] = int(np.sqrt((current_circle[0][0] - x)**2 + (current_circle[0][1] - y)**2))

    # check to see if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        moving = False

    # check to see if the right mouse button was released
    elif event == cv2.EVENT_RBUTTONUP:
        resizing = False

# load the image, clone it, and setup the mouse callback function
image = cv2.imread("./125_A1_ROI1_120nm_pos2_rec_-1.jpg")
clone = image.copy()
cv2.namedWindow("image")
cv2.setMouseCallback("image", click_and_crop)

# keep looping until the 'q' key is pressed
while True:
    # display the image and wait for a keypress
    img = clone.copy()
    for circle in circles:
        cv2.circle(img, circle[0], circle[1], (0, 255, 0), 2)
    cv2.imshow("image", img)
    key = cv2.waitKey(1) & 0xFF
    #print(circles)

    # if the 'r' key is pressed, reset the cropping region
    if key == ord("r"):
        circles = []

    # if the 'c' key is pressed, break from the loop
    elif key == ord("c"):
        break
print(circles)

# close all open windows
cv2.destroyAllWindows()
