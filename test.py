import numpy as np
import cv2
import threading
import multiprocessing
from queue import Queue
from time import sleep

btn_down = False
queue = Queue()
break_queue = False

def get_points(im):
    # Set up data to send to mouse handler
    data = {}
    data['im'] = im.copy()
    data['lines'] = []

    # Set the callback function for any mouse event
    cv2.imshow("Image", im)
    cv2.setMouseCallback("Image", mouse_handler, data)
    cv2.waitKey(0)

    # Convert array to np.array in shape n,2,2
    points = np.uint16(data['lines'])

    return points, data['im']

def mouse_handler(event, x, y, flags, data):
    global btn_down, points, data_points, queue
    queue.put([x, y])
    if event == cv2.EVENT_LBUTTONUP and btn_down:
        #if you release the button, finish the line
        btn_down = False
        # data['lines'][0].append((x, y)) #append the seconf point
        # cv2.circle(data['im'], (x, y), 3, (0, 0, 255),5)
        # cv2.line(data['im'], data['lines'][0][0], data['lines'][0][1], (0,0,255), 2)
        # cv2.imshow("Image", data['im'])

    elif event == cv2.EVENT_MOUSEMOVE and btn_down:
        #thi is just for a ine visualization
        # image = data['im'].copy()
        # cv2.line(image, data['lines'][0][0], (x, y), (0,0,0), 1)
        # cv2.imshow("Image", image)
        # data_points.append([x, y])
        queue.put([x, y])
        # print(x, y)

    elif event == cv2.EVENT_LBUTTONDOWN and len(data['lines']) < 2:
        btn_down = True
        # data['lines'].insert(0,[(x, y)]) #prepend the point
        # cv2.circle(data['im'], (x, y), 3, (0, 0, 255), 5, 16)
        # cv2.imshow("Image", data['im'])


# Running the code
img = cv2.imread('./images/example.png', 1)
pts, final_image = get_points(img)
data_points = []


def draw_process(img, queue, break_queue):
    while True:
        item = queue.get()
        if break_queue or not item:
            break
        [x, y] = item
    #     for data in data_points:
    #         [x, y] = data
    #         print(x, y)
        cv2.circle(img, (x, y), 10, (0, 0, 255),5)
        print('WEE', x, y)

draw = threading.Thread(target=draw_process, args=(img, queue, break_queue))
draw.start()
draw.join()


# cv2.imshow('Image', final_image)
# print(pts)
while(1):
    cv2.imshow('image',final_image)
    if cv2.waitKey(1) & 0xFF == 27:
        break_queue = True

        break

cv2.destroyAllWindows()