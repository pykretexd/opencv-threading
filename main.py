import cv2
from classes.fps import FPS
from classes.video_stream import VideoStream


def main():
    stream = VideoStream()
    fps = FPS()
    escape_key = 27

    stream.start()
    fps.start()
    while True:
        frame = stream.read()

        cv2.imshow('frame', frame)
        key = cv2.waitKey(1)
        if key == escape_key:
            break

        fps.update()

    fps.stop()
    print(f'Elapsed time: {fps.elapsed:.2f}')
    print(f'Approximate FPS: {fps.fps:.2f}')

    stream.stop()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
