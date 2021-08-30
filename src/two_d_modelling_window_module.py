import pandas as pd
import numpy as np
from matplotlib import cm
from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt

def create_mesh():
    # x parameter

    minimum_cell = 500
    number_of_node = 20
    horizontal_padding = 1.9
    number_of_padding = 3

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
    minimum_mesh = 50
    vertical_constanta = 1.2
    number_of_layer = 20

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
    zz = (xx * 0) + 100

    ax1.plot(xx, yy, 'o', markersize=1, color='black', alpha=0.4)

    m = cm.ScalarMappable(cmap=cm.jet_r, norm=LogNorm())
    m.set_array([1, 1000])
    n = figure.colorbar(m)
    n.set_label('Resistivity (ohm meter)', rotation=270)

    # color_value = plt.get_cmap('jet_r')
    # resistivity_value = np.log10(zz) / (np.log10(1000))
    ax1.pcolormesh(xx, yy, zz, norm=n)

    ax1.invert_yaxis()
    ax1.autoscale(axis='both')
    ax1.set_xlabel('Distance (m)', fontsize=8)
    ax1.set_ylabel('Elevation (m)', fontsize=8)

    figure.tight_layout()
    widget_canvas.draw()
