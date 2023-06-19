import numpy as np
import cv2 as cv
from pynput import mouse
import time
from time import sleep

from queue import Queue

MOUSE_DELAY = 0.2


class ArtBoard:
    def __init__(self) -> None:
        self.layers = []

        base_layer = np.zeros((800,800,3), np.uint8)
        self.layers.extend(base_layer)

    def scratchboard(self, index: int=0):
        scratchboard = np.zeros((800,800,3), np.uint8)
        self.layers.insert(index, scratchboard)

    def render():
        composite = cv.addWeighted(img, 0.7, temp_layer, 0.3, 0)


img = np.zeros((800,800,3), np.uint8)
temp_layer = np.zeros((800, 800, 3), np.uint8)
drawing = False
should_end = False
t = time.time()
middle_point = []
last_point = []
q = Queue()

def on_move(x, y):
    global drawing, t, last_point, middle_point, MOUSE_DELAY
    
    if drawing:
        t_2 = time.time()
        if t_2 - t > MOUSE_DELAY:
            t = t_2
            if not middle_point:
                middle_point = [x, y]
            if not last_point:
                last_point = [x, y]

            q.put([[x, y], middle_point, last_point])
            # q.put([[x, y], last_point, middle_point])
            # q.put([middle_point, last_point, [x, y]])
            # q.put([last_point, middle_point, [x, y]])
            # q.put([[10, 10], [50, 50], [30, 30]])
            last_point = middle_point
            middle_point = [x, y]

def on_click(x, y, button, pressed):
    global img, temp_layer, drawing, last_point, middle_point
    drawing = pressed


    if pressed:
        temp_layer = np.zeros((800, 800, 3), np.uint8)
        middle_point = []
        last_point = []
    else:
        img = cv.addWeighted(img, 0.7, temp_layer, 0.3, 0)
    # print('{0} at {1}'.format(
    #     'Pressed' if pressed else 'Released',
    #     (x, y)))
    # if not pressed:
    #     # Stop listener
    #     return False

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))

# Collect events until released
# with mouse.Listener(
#         on_move=on_move,
#         on_click=on_click,
#         # on_scroll=on_scroll
#     ) as listener:
#     listener.join()

# ...or, in a non-blocking fashion:

# https://docs.opencv.org/4.x/db/d5b/tutorial_py_mouse_handling.html

# mouse callback function
# def draw_circle(event,x,y,flags,param):
#     global drawing, q, should_end, img, t

#     # while not q.empty():
#     #     [x, y] = [int(x) for x in q.get()]
#     #     cv.circle(img,(x,y),5,(0,0,255),-1)
#         # if should_end:
#         #     break
#     if event == cv.EVENT_LBUTTONDOWN:
#         drawing = True
#     elif event == cv.EVENT_MOUSEMOVE:
#         if drawing == True:
#             # t_2 = time.time()

#             # if t_2 - t > 0.01:
#             #     t = t_2
#             #     print(t_2, t, t_2 - t)
#             cv.circle(img,(x,y),5,(0,0,255),-1)
#     elif event == cv.EVENT_LBUTTONUP:
#         drawing = False

cv.namedWindow('image')
# cv.setMouseCallback('image', draw_circle)

listener = mouse.Listener(
    on_move=on_move,
    on_click=on_click,
    # on_scroll=on_scroll
)
listener.start()

pts = np.array([[25, 70], [25, 160],
                [110, 200], [200, 160],
                [200, 70], [110, 20]],
               np.int32)

pts = pts.reshape((-1, 1, 2)).astype(np.int32)


artboard = ArtBoard()

while(1):
    k = cv.waitKey(1) & 0xFF
    cv.imshow('image',img)

    # cv.curve = cv.curve(curvePoints, true)
    if not q.empty():
        # [x, y] = [int(x) for x in q.get()]
        pts = np.array(q.get(), np.int32)

        # pts = np.array([[25, 70], [25, 160],
        #         [110, 200], [200, 160],
        #         [200, 70], [110, 20]],
        #        np.int32)

        # pts = np.array(pts, np.int32)
        # pts = pts.reshape(-1, 1, 2)


        # pts = np.array(pts, np.int32)
        # print(pts[:,0], pts[:,1])
        coeffs = np.polyfit(pts[:,1], pts[:,0], 2)
        poly = np.poly1d(coeffs)

        yarr = np.arange(pts[0][1], pts[2][1])
        xarr = poly(yarr)
        parab_pts = np.array([xarr, yarr],dtype=np.int32).T

        # print(parab_pts)

        cv.polylines(temp_layer, [pts], False, (120,0,255), 3)
        # img = cv.addWeighted(img, 0.7, temp_layer, 0.3, 0)
        # draw_y = np.polyval(1, draw_x)
        # pts = (np.asarray(pts).T).astype(np.int32)
        # cv.polylines(img, [pts], False,(120,0,255),cv.INTER_AREA, 10)

    if k == 27:
        should_end = True
        break
cv.destroyAllWindows()