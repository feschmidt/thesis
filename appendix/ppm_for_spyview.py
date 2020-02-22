import numpy as np
from matplotlib import cm, pyplot
import array

# PPM info
width = 1
height = 255
maxval = 255

for cmap_name in pyplot.colormaps():  # all matplotlib colormaps
    # get data from matplotlib colormap
    cmap = cm.get_cmap(cmap_name)

    cw_array = []
    for xval in np.linspace(0, 1, height):
        cw_raw = list(np.rint(np.array(cmap(xval)[:3])*maxval).astype(int))
        # from raw data only take RBG, not alpha
        # convert to array for numerical treatment, *255 to go to RGB space, then convert array elements to int
        cw_array.extend(cw_raw)

    # PPM header
    ppm_header = f'P6 {width} {height} {maxval}\n'

    # PPM image data (filled with blue)
    image = array.array('B', cw_array)

    # Save the PPM image as a binary file
    with open(cmap_name+'.ppm', 'wb') as f:
        f.write(bytearray(ppm_header, 'ascii'))
        image.tofile(f)
