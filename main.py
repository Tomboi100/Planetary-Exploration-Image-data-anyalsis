import matplotlib.pyplot as plt
import numpy as np
import tifffile as tiff

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sky = tiff.imread('sky_frame.tiff')
    dark = tiff.imread('dark_frame.tiff')
    obs = tiff.imread('obs_frame.tiff')
    flat = tiff.imread('flat_frame.tiff')
    sky_array = np.array(sky)
    dark_array = np.array(dark)
    obs_array = np.array(obs)
    flat_array = np.array(flat)

    # plt.imshow(flat)
    # plt.show()
    # plt.close()
    # plt.imshow(sky)
    # plt.show()
    # plt.close()
    # plt.imshow(obs)
    # plt.show()
    # plt.close()
    # plt.imshow(dark)
    # plt.show()
    # plt.close()

    rawspectraldataintergrationtime = 10
    darkframeintegrationtime = 1
    flatframeintegrationtime = 1

    scaled_flat = np.divide(flat_array, flatframeintegrationtime)
    # print(scaled_flat)
    # plt.imshow(scaled_flat)

    scaled_dark = np.divide(dark_array, darkframeintegrationtime)
    # print(scaled_dark)
    # plt.imshow(scaled_dark)

    scaled_obs = np.divide(obs_array, rawspectraldataintergrationtime)
    # print(scaled_obs)
    # plt.imshow(scaled_obs)

    scaled_sky = np.divide(sky_array, rawspectraldataintergrationtime)
    # print(scaled_sky)
    # plt.imshow(scaled_sky)

    reduced_obs = (scaled_obs - scaled_dark) / scaled_flat
    # print(reduced_obs)
    # plt.imshow(reduced_obs)

    clean_flat = scaled_flat - scaled_dark
    # print(clean_flat)
    # plt.imshow(clean_flat)

    reduced_sky = (scaled_sky - scaled_dark) / scaled_flat
    # reduced_sky = (scaled_sky - scaled_dark) / clean_flat
    # print(reduced_sky)
    # plt.imshow(reduced_sky)

    processed_data = reduced_obs - reduced_sky
    # print(processed_data)
    #plt.imshow(processed_data)

    processed_data[processed_data<0] = 0
    processed_data[processed_data>10**6.75] = 0

    print(processed_data)
    plt.imshow(processed_data)
    plt.show()