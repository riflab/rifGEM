import pandas as pd
import numpy as np
from matplotlib import cm
from matplotlib.colors import BoundaryNorm, ListedColormap


def create_mesh():
    # x parameter

    minimum_cell = 500
    number_of_node = 20
    horizontal_padding = 1.5
    number_of_padding = 5

    x_cell = []
    for i in range(number_of_node):
        x_cell.append(minimum_cell)

    temp = minimum_cell
    for i in range(number_of_padding):
        temp *= horizontal_padding
        x_cell.append(temp)
    x_cell.reverse()

    temp = minimum_cell
    for i in range(number_of_padding):
        temp *= horizontal_padding
        x_cell.append(temp)

    x_mesh = [0]
    temp = 0
    for i in x_cell:
        temp += i
        x_mesh.append(temp)

    # z parameter

    surface = 0
    minimum_mesh = 10
    vertical_constanta = 1.2
    number_of_layer = 50

    z_cell = [surface, minimum_mesh]
    temp = z_cell[1]
    for i in range(number_of_layer - 1):
        temp *= vertical_constanta
        z_cell.append(temp)

    z_mesh = []
    temp = 0
    for i in z_cell:
        temp += i
        z_mesh.append(temp)

    return x_mesh, z_mesh


def database():
    x_station = [0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000]
    z_station = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    df = pd.DataFrame(list(zip(x_station, z_station)), columns=['x_station', 'z_station'])

    x_mesh, z_mesh = create_mesh()

    return df, x_mesh, z_mesh


def plot_mesh(figure, widget_canvas, ax1, x_mesh, z_mesh):
    xx, yy = np.meshgrid(x_mesh, z_mesh)
    zz = (xx * 0) + 200

    gist_rainbow = cm.get_cmap('gist_rainbow', 512)
    new_color_map = ListedColormap(gist_rainbow(np.linspace(0, 0.85, 512)))

    min_resistivity = 1
    max_resistivity = 1000
    num_resistivity = 15

    a = (np.log10(max_resistivity) - np.log10(min_resistivity))/num_resistivity

    bounds = [round(10**np.log10(min_resistivity))]
    temp = np.log10(min_resistivity)
    for i in range(0, num_resistivity):
        temp += a
        bounds.append(round(10**temp))

    norm = BoundaryNorm(bounds, ncolors=new_color_map.N)

    c = ax1.pcolor(xx, yy, zz, cmap=new_color_map, norm=norm, edgecolors='black', linewidths=0.4, shading='auto')
    figure.colorbar(c, ax=ax1, ticks=bounds)

    ax1.autoscale(axis='x')
    ax1.set_ylim([-1000, 5000])
    ax1.set_xlabel('Distance (m)', fontsize=8)
    ax1.set_ylabel('Elevation (m)', fontsize=8)
    ax1.invert_yaxis()

    figure.tight_layout()
    widget_canvas.draw()
