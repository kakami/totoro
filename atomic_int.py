import threading

class AtomicInt:
    def __init__(self, initial=0):
        self._v = initial
        self._lock = threading.Lock()

    def get(self):
        with self._lock:
            return self._v

    def set(self, v):
        with self._lock:
            self._v = v

    def inc(self, n=1):
        with self._lock:
            self._v += n
            return self._v

    def dec(self, n=1):
        with self._lock:
            self._v -= n
            return self._v

    @property
    def value(self):
        with self._lock:
            return self._v

    @value.setter
    def value(self, v):
        with self._lock:
            self._v = v