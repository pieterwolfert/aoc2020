#!/usr/bin/env python

class toboggan:
    def __init__(self, input_file):
        self.input_file = [x[:-1] for x in open(input_file, 'r').readlines()]
        self.current_length_index = len(self.input_file[0])

    def traverse(self, slope_x, slope_y):
        trees = 0
        x = 0
        y = 0
        while y < len(self.input_file):
            if x >= self.current_length_index:
                x = x - self.current_length_index
            if self.input_file[y][x] is "#":
                trees += 1
            y += slope_y
            x += slope_x
        return trees

if __name__=="__main__":
    t = toboggan('input.txt')
    print(t.traverse(1,1) * t.traverse(3, 1) * t.traverse(5, 1) * t.traverse(7, 1) * t.traverse(1, 2))

