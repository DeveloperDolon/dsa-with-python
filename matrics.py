import random
import time
import shutil
import sys

class Star:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.reset()

    def reset(self):
        self.x = self.w / 2
        self.y = self.h / 2
        self.angle = random.uniform(0, 2 * 3.14159)
        self.speed = random.uniform(0.1, 1.0)
        self.char = random.choice(['.', '.', '*', '+'])

    def update(self):
        self.x += math.cos(self.angle) * self.speed * 2
        self.y += math.sin(self.angle) * self.speed
        self.speed *= 1.05

    def is_out(self):
        return self.x < 0 or self.x >= self.w or self.y < 0 or self.y >= self.h

import math

def warp_speed():
    cols, rows = shutil.get_terminal_size()
    stars = [Star(cols, rows) for _ in range(100)]
    
    print("\033[?25l", end="")
    
    try:
        while True:
            print("\033[H", end="")
            
            frame = [[' ' for _ in range(cols)] for _ in range(rows - 1)]
            
            for star in stars:
                star.update()
                if star.is_out():
                    star.reset()
                
                ix, iy = int(star.x), int(star.y)
                if 0 <= iy < rows - 1 and 0 <= ix < cols:
                    frame[iy][ix] = star.char

            output = "\n".join("".join(row) for row in frame)
            sys.stdout.write(output)
            time.sleep(0.03)

    except KeyboardInterrupt:
        print("\033[?25h\nStopped.")

if __name__ == "__main__":
    warp_speed()