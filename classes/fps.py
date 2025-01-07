import datetime


class FPS:
    def __init__(self):
        self._start = None
        self._end = None
        self._num_frames = 0

    def start(self):
        """Start the timer."""
        self._start = datetime.datetime.now()

    def stop(self):
        """Stop the timer."""
        self._end = datetime.datetime.now()

    def update(self):
        """Increment the total number of frames examined 
        during the start and end intervals."""
        self._num_frames += 1

    @property
    def elapsed(self):
        """Return the total number of seconds between the start and end
        interval."""
        return (self._end - self._start).total_seconds()

    @property
    def fps(self):
        """Compute the approximate frames per second."""
        return self._num_frames / self.elapsed
