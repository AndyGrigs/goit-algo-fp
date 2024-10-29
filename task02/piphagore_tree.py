import numpy as np
import matplotlib.pyplot as plt

def draw_piphagore_tree(x, y, angle, length, depth):
    if depth == 0:
        return
    x2 = x + length * np.cos(angle)
    y2 = y + length * np.sin(angle)

    plt.plot([x, x2], [y, y2], color='brown', lw=depth)

    new_length = length * 0.75
    draw_piphagore_tree(x2, y2, angle + np.pi / 3, new_length, depth - 1)
    draw_piphagore_tree(x2, y2, angle - np.pi / 3, new_length, depth - 1)

def main(depth):
    plt.figure(figsize=(8, 8))
    plt.axis('off')
    plt.gca().set_aspect('equal')

    draw_piphagore_tree(0, 0, np.pi/2, 1, depth)

    plt.show()

if __name__ == '__main__':
    try:
        depth = int(input('Enter the depth of the tree: '))
    except ValueError:
        depth = 8
    main(depth)