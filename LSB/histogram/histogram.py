from cv2 import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys

def hist():
    img = cv2.imread(sys.argv[1], 0)
    np.histogram(img.ravel(), 256, [0,256]) 
    plt.hist(img.ravel(), 256, [0,256])

def hist_steg():
    img = cv2.imread(sys.argv[2], 0)
    np.histogram(img.ravel(), 256, [0,256]) 
    plt.hist(img.ravel(), 256, [0,256])

def setup():
    plt.ylabel("Frequency")
    plt.xlabel("Blocks")
    plt.title("Histogram")

def main():

    #Overlap histograms
    setup()
    hist()
    hist_steg()
    plt.savefig(sys.argv[1].replace("../imgs/imgs-cover/cover_", "histogram-overlap/hist-overlap_"))

    plt.clf()

    #hist1
    setup()
    hist()
    plt.savefig(sys.argv[1].replace("../imgs/imgs-cover/cover_", "histogram-cover/hist-cover_"))

    plt.clf()

    #hist2
    setup()
    hist_steg()
    plt.savefig(sys.argv[2].replace("../imgs/imgs-steg/steg_", "histogram-steg/hist-steg_"))

if __name__ == "__main__":
    main()