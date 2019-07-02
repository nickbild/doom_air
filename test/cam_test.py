import cv2


def gstreamer_pipeline (capture_width=3280, capture_height=2464, display_width=1280, display_height=720, framerate=21, flip_method=0) :   
    return ('nvarguscamerasrc ! ' 
    'video/x-raw(memory:NVMM), '
    'width=(int)%d, height=(int)%d, '
    'format=(string)NV12, framerate=(fraction)%d/1 ! '
    'nvvidconv flip-method=%d ! '
    'video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! '
    'videoconvert ! '
    'video/x-raw, format=(string)BGR ! appsink'  % (capture_width,capture_height,framerate,flip_method,display_width,display_height))


def save_camera_frame():
    if cap.isOpened():
        ret_val, img = cap.read()
        cv2.imwrite("test.jpg", img)

        ret_val, img2 = cap.read()
        cv2.imwrite("test2.jpg", img2)

        cap.release()
    else:
        print 'Unable to open camera.'


if __name__ == '__main__':
    cap = cv2.VideoCapture(gstreamer_pipeline(flip_method=0), cv2.CAP_GSTREAMER)
    save_camera_frame()

