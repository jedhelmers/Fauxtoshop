import cv2

image = cv2.imread('images/example.png')

b = image.copy()
# set green and red channels to 0
b[:, :, 1] = 0
b[:, :, 2] = 0


g = image.copy()
# set blue and red channels to 0
g[:, :, 0] = 0
g[:, :, 2] = 0

r = image.copy()
# set blue and green channels to 0
r[:, :, 0] = 0
r[:, :, 1] = 0

a = image.copy()
# Set blue, green and red channels to blue channel
a[:, :, 1] = a[:, :, 0]
a[:, :, 2] = a[:, :, 0]

a2 = image.copy()
# Set blue, green and red channels to green channel
a2[:, :, 0] = a2[:, :, 1]
a2[:, :, 2] = a2[:, :, 1]

a3 = image.copy()
# Set blue, green and red channels to red channel
a3[:, :, 0] = a3[:, :, 2]
a3[:, :, 1] = a3[:, :, 2]

# # RGB - Blue
# cv2.imshow('B-RGB', b)

# # RGB - Green
# cv2.imshow('G-RGB', g)

# # RGB - Red
# cv2.imshow('R-RGB', r)

# RGB - A
cv2.imshow('A1-RGB', a)

# RGB - A
cv2.imshow('A2-RGB', a2)

# RGB - A
cv2.imshow('A3-RGB', a3)

cv2.waitKey(0)