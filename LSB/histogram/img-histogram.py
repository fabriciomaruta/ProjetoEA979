import cv2
import numpy as np
from matplotlib import pyplot as plt

def hist():
    img = cv2.imread("../imgs/imgs-cover/cover_img.png", 0)
    hist, bins = np.histogram(img.ravel(), 256, [0,256]) 
    plt.hist(img.ravel(), 256, [0,256])

def hist_steg():
    img = cv2.imread("../imgs/imgs-steg/steg_img.png", 0)
    hist, bins = np.histogram(img.ravel(), 256, [0,256]) 
    plt.hist(img.ravel(), 256, [0,256])

def save(str):
    plt.savefig(str)

def main():
    #Overlao histograms
    hist()
    hist_steg()
    save("overlap-hist.png")

    plt.clf()

    #hist1
    hist()
    save("hist.png")

    plt.clf()

    #hist2
    hist_steg()
    save("hist-steg.png")

if __name__ == "__main__":
    main()