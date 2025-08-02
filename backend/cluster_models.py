from sklearn.cluster import DBSCAN, AgglomerativeClustering, KMeans, OPTICS
from sklearn.decomposition import PCA

class ClusteringAlgo():
    def __init__(self, data):
        self.data = data
    
    def run_kmeans(self, n_clusters = 3):
        model = KMeans(n_clusters=n_clusters, random_state=42)
        labels = model.fit_predict(self.data)
        return labels, model

    def run_dbscan(self, eps=1.5, min_samples=5):
        model = DBSCAN(eps=eps, min_samples=min_samples)
        labels = model.fit_predict(self.data)
        return labels, model

    def run_agglomerative(self, n_clusters=3, linkage='ward'):
        model = AgglomerativeClustering(n_clusters=n_clusters, linkage=linkage)
        labels = model.fit_predict(self.data)
        return labels, model

    def run_optics(self, min_samples=5, max_eps=2.0):
        model = OPTICS(min_samples=min_samples, max_eps=max_eps)
        labels = model.fit_predict(self.data)
        return labels, model

    def apply_pca(self, n_components=2):
        pca = PCA(n_components=n_components)
        pca_data = pca.fit_transform(self.data)
        explained_variance = pca.explained_variance_ratio_
        return pca_data, explained_variance

    def perform_clustering(self, method, params):
        pass
        

