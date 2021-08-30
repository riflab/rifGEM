# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.colors
#
# x = np.arange(0, 25)
# a = np.random.randint(0, 130, size=(25, 25))
# a = np.sort(a).reshape(25, 25)
# print('a')
# colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
# cmap = matplotlib.colors.ListedColormap(colors)
# cmap.set_under("crimson")
# cmap.set_over("w")
# norm = matplotlib.colors.Normalize(vmin=0, vmax=600)
# print('b')
# fig, ax = plt.subplots()
# im = ax.pcolormesh(x, x, a, levels=[0, 100, 200, 300, 400, 500, 600], extend='both', cmap=cmap, norm=norm)
# print('c')
# fig.colorbar(im, extend="both")
#
# plt.show()
import matplotlib.pyplot as plt
import matplotlib as mpl


fig, ax = plt.subplots(figsize=(6, 1))
fig.subplots_adjust(bottom=0.5)

cmap = mpl.colors.ListedColormap(['blue', 'royalblue', 'cyan', 'lime', 'yellow', 'orange', 'red'])

bounds = [1, 10, 50, 100, 200, 300, 500, 1000]
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
# cb3 = mpl.colorbar.ColorbarBase(ax, cmap=cmap,
#                                 norm=norm,
#                                 ticks=bounds,
#                                 orientation='horizontal')
# cb3.set_label('Custom extension lengths, some other units')

plt.show()

