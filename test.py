import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import imageio

Nx = 20
Ny = 10
p_in = 0.01
p_o = 1


def test_piece(x, y, jigsaw):

    if ((x == 0 or x == (Nx-1)) or (y == 0 or y == (Ny-1))):
        if np.random.random() < p_o:
            jigsaw[x, y] = 1
            return True

    elif jigsaw[x+1, y] == 1 or jigsaw[x-1, y] == 1 or jigsaw[x, y-1] == 1 or jigsaw[x, y+1] == 1:
        jigsaw[x, y] = 1
        return True

    elif np.random.random() < p_in:
        jigsaw[x, y] = 1
        return True

    return False


def plot_puzzle(jigsaw, ax):
    ax = sns.heatmap(jigsaw, vmin=0, vmax=1, xticklabels=False,
                     yticklabels=False, linewidths=.1, cbar=False)

    # Used to return the plot as an image array
    fig.canvas.draw()       # draw the canvas, cache the renderer
    image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
    image = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))

    return image


jigsaw = np.zeros((Nx, Ny))

pieces = [(i, j) for i in range(Nx) for j in range(Ny)]
i = 0
images = []
fig, ax = plt.subplots(figsize=(8, 15))

while len(pieces) > 0:
    piece = np.random.randint(0, len(pieces))
    x, y = pieces.pop(piece)
    i += 1

    placed = test_piece(x, y, jigsaw)

    if not placed:
        pieces.append((x, y))

    images.append(plot_puzzle(jigsaw, ax))

# kwargs_write = {'fps': 30.0, 'quantizer': 'nq'}
imageio.mimsave('./test.gif', images, fps=30)
