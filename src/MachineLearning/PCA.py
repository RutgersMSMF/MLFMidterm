from sklearn.decomposition import PCA

def get_pca(X):
    """
    Computes the Principal Components of Correlation Matrix
    """
    pca = PCA(n_components = 3)
    model = pca.fit(X)

    return model

