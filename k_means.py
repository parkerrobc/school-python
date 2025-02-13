from math import sqrt

class KMeans ():

    def __init__(self, numberOfClusters, maxIterations = 5):
        self.numberOfClusters = numberOfClusters
        self.maxIterations = maxIterations
    
    def euclideanDistance(self, v1, v2):
        if len(v1)==0 or len(v2)==0:
            return 1000
        sum = 0
        for i in range(len(v1)):
            sum+=((v2[i] - v1[i])**2)
        return sqrt(sum)


    def getCentroid(self, cluster, dataSet):
        if len(cluster) == 0:
            return [0] * len(dataSet[0])
        result = [0] * len(dataSet[0])
        for i in range(len(result)):
            for j in cluster:
                result[i] += dataSet[j][i]
        for i in range(len(result)):
            result[i]/=len(cluster)
        return result

    def calculateCentroids(self, clusters, dataSet):
        result = []
        for cluster in clusters:
            result.append(self.getCentroid(cluster, dataSet))
        return result

    def calculateKmeans(self, dataSet):

        clusters = []

        for i in range(self.numberOfClusters):
            clusters.append([])
        for i in range(len(dataSet)):
            position = i%self.numberOfClusters
            clusters[position].append(i)

        for iteration in range(self.maxIterations):
            centroids = self.calculateCentroids(clusters, dataSet)
            for clusterIndex in range(self.numberOfClusters):
                clusters[clusterIndex]=[]
            for dateElement in range(len(dataSet)):
                perferredCluster = 0
                closestDistance = 1000
                for clusterIndex in range(self.numberOfClusters):
                    actualDistance = self.euclideanDistance(centroids[clusterIndex], dataSet[dateElement])
                    if actualDistance < closestDistance:
                        perferredCluster = clusterIndex
                        closestDistance = actualDistance
                if len(clusters[perferredCluster])==0:
                    clusters[perferredCluster]=[]
                clusters[perferredCluster].append(dateElement)
            

        result = dataSet.copy()

        for i in range(len(clusters)):
            for j in range(len(clusters[i])):
                result[clusters[i][j]]=centroids[i]


        return result
        

