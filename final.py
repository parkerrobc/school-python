from curses.ascii import NUL
from skimage import io
from sklearn.cluster import KMeans
import numpy as np

import k_means
import sys
 
imageToRead = sys.argv[1]
numberOfClusters = int(sys.argv[2])
useCustom = sys.argv[3]
outputFileName = imageToRead + "-compressed-" + sys.argv[2] + ".png"

print('reading image')
image = io.imread(imageToRead)

rows = image.shape[0]
cols = image.shape[1]

print('flattening image')
image = image.reshape(rows*cols, 3)

print('running k-means numberOfClusters =', numberOfClusters)

kmeans = NUL
compressed_image = NUL

if useCustom == "true":
    kmeans = k_means.KMeans(numberOfClusters)
    result = kmeans.calculateKmeans(image)
else:
    kmeans = KMeans(n_clusters=numberOfClusters)
    kmeans.fit(image)
    result = kmeans.cluster_centers_[kmeans.labels_]
    outputFileName = "library-" + outputFileName

print('compressing')
compressed_image = np.clip(result.astype('uint8'), 0, 255)

print('reshaping')
compressed_image = compressed_image.reshape(rows, cols, 3)

print('saving')
io.imsave(outputFileName, compressed_image)


