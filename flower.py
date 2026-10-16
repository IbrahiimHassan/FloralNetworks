import time

class Flower:
    def __init__(self , dna):
        self.dna=dna
        self.hover_time = 0.0
        self.hover_start = None

    def start_hover(self):
        self.hover_start = time.time()

    def stop_hover(self):
        if self.hover_start is not None:
           self.hover_time += time.time() - self.hover_start
           self.hover_start = None

    def fitness(f):
        current_time = f.hover_time

        if f.hover_start is not None:
            current_time += time.time() - f.hover_start

        return current_time
