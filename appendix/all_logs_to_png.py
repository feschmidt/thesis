import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import glob
import traceback
import logging
import pandas as pd

ebeam = input("For which ebeam is the analysis supposed to be run?\n")

logfiles = sorted(glob.glob('log_'+ebeam+'/*.log'))
print(logfiles)

# Look for the following line:
key1 = 'Measured/(skipped) heights [um] on the substrate:'
key2 = 'Measured/(skipped) and estimated/[not counting] heights [um] on the substrate:'
# Below strings are unused
c00 = 'C00'  # DC
c10 = 'C10'  # x
c01 = 'C01'  # y
c20 = 'C20'  # x*x
c11 = 'C11'  # x*y
c02 = 'C02'  # y*y
c30 = 'C30'  # x*x*x
c21 = 'C21'  # x*x*y
c12 = 'C12'  # x*y*y
c03 = 'C03'  # y*y*y

for myfile in logfiles:

    filename = myfile.split('/')[-1]
    print(myfile)
    print(filename)

    with open(myfile, 'rb') as f:
        #read_data = f.read()
        i = 0
        for line in f:
            i += 1
            try:
                print(i, "-->", line.decode('UTF8').strip('\n'))
            except Exception as e:
                logging.error(traceback.format_exc())
                # Logs the error appropriately.

    startlog = False
    setbreak = False
    thelog = []
    with open(myfile, 'rb') as f:
        #read_data = f.read()
        i = 0
        for line in f:
            i += 1
            try:
                theline = line.decode('UTF8').strip('\n')
                if setbreak:
                    print(filename)
                    break
                if startlog and not setbreak:
                    print(i, "-->", theline)
                    thelog.append(theline)
                if theline == key1:
                    startlog = True
                if 'fit' in theline:
                    setbreak = True
            except Exception as e:
                logging.error(traceback.format_exc())
                # Logs the error appropriately.

    if startlog:
        x = []
        y = []
        hs = []
        for newline in thelog:
            if key2 == newline:
                break
            newline = newline.split()
            if 'M' in newline:
                h = []
                for i, item in enumerate(newline):
                    if i == 0:
                        y.append(float(item))
                    elif i == 1:
                        continue
                    else:
                        if item == '*.*':  # for height measurements out of range
                            h.append(np.nan)
                        elif '%ENG_W_SHOUHM' in item:
                            h.append(np.nan)
                            break
                        else:
                            h.append(float(item))
                hs.append(h)
            elif '+--->' in newline:
                for i, item in enumerate(newline):
                    if i > 1:
                        x.append(float(item))

        x = np.array(x)
        y = np.array(y)
        hs = np.array(hs)
        dx = abs(x[-1]-x[0])
        dy = abs(y[-1]-y[0])
        DX = np.linspace(-dx/2, dx/2, len(x))
        DY = np.linspace(-dy/2, dy/2, len(y))

        try:
            fig, ax = plt.subplots()
            # ax.imshow(hs,extent=(x.min(), x.max(), y.max(), y.min()))
            heightmap = ax.imshow(
                hs, extent=(-dx/2, dx/2, -dy/2, dy/2), cmap='RdBu_r')
            cbar = plt.colorbar(heightmap)
            cbar.set_label('Height (um)')
            plt.xlabel('x (mm)')
            plt.ylabel('y (mm)')
            plt.title(filename)
            plt.tight_layout()
            plt.savefig('png_'+ebeam+'/2d/'+filename +
                        '.png', bbox_inches='tight')
        #     plt.show()
            plt.close()

            X, Y = np.meshgrid(DX, DY)
            ax = plt.axes(projection='3d')
            ax.plot_surface(X, Y, hs, cmap='RdBu_r', edgecolor='none')
            ax.scatter3D(X, Y, hs, c='red')
            ax.set_title(filename)
            ax.set_xlabel('x (mm)')
            ax.set_ylabel('y (mm)')
            ax.set_zlabel('Height (um)')
            plt.tight_layout()
            plt.savefig('png_'+ebeam+'/3d/'+filename +
                        '3D.png', bbox_inches='tight')
        #     plt.show()
            plt.close()

        except Exception as e:
            logging.error(traceback.format_exc())
            # Logs the error appropriately.

    else:
        print('no height measurement in', filename)
