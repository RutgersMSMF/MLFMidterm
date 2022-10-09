from sklearn.cluster import KMeans

def get_clusters(X):
    """
    Computes Clusters of Correlation Matrix
    """

    kmeans = KMeans(n_clusters = 2, random_state = 0)
    model = kmeans.fit(X)

    return model