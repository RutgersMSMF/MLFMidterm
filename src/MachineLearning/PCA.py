from sklearn.decomposition import PCA

def get_pca(X):
    """
    Computes the Principal Components of Correlation Matrix
    """
    pca = PCA(n_components = 5)
    model = pca.fit(X)

    return model

