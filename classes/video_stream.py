from threading import Thread
import cv2


class VideoStream:
    def __init__(self, src=0):
        self.stream = cv2.VideoCapture(src)
        (self.grabbed, self.frame) = self.stream.read()
        self.stopped = False

    def start(self):
        """Start the thread to read frames from the video stream."""
        Thread(target=self.update, args=()).start()
        return self

    def update(self):
        """Keep looping infinitely until the thread is stopped."""
        while True:
            if self.stopped:
                return
            (self.grabbed, self.frame) = self.stream.read()

    def read(self):
        """Return the frame most recently read."""
        return self.frame

    def stop(self):
        """Indicate that the thread should be stopped."""
        self.stopped = True
