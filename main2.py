import matplotlib.pyplot as plt
import numpy as np
import tifffile as tiff
from scipy.ndimage.filters import gaussian_filter

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    img = tiff.imread('AIA_workshop.tif') # imports tiff file
    img_array = np.array(img) # coverts tiff file to numerical array

    # plt.plot(img)
    # plt.imshow(img_array)

    img_array[img_array > 6000] = 6000 #removes the top values

    # plt.plot(img_array)
    # plt.imshow(img_array)

    smoothed = gaussian_filter(img_array, sigma=5) # smoothes the data

    # plt.plot(smoothed)
    # plt.imshow(smoothed)

    img_array[img_array < 1000] = False
    img_array[img_array > 999] = True

    # plt.plot(img_array)
    # plt.imshow(img_array)
    # print(img_array) # display numbers

    masked = smoothed
    masked[masked < 1000] = False
    masked[masked > 999] = True

    # plt.plot(masked) # display graph
    plt.imshow(masked) # display final
    plt.show() # needs to be used to show the plot/images


