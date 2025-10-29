🛍️ Mall Customer Segmentation with K-Means Clustering
📌 Overview
This project demonstrates customer segmentation using the K-Means clustering algorithm on a mall customer dataset. It includes both a manual implementation of K-Means and an optimized version using Scikit-Learn. The goal is to group customers based on their annual income and spending score, enabling targeted marketing strategies and deeper customer insights.
📂 Dataset
- Source: Mall_Customers.csv
- Features Used:
- Annual_Income_(k$)
- Spending_Score
- Genre (converted via one-hot encoding)
🧠 Objectives
- Visualize customer distribution and spending behavior.
- Implement K-Means clustering from scratch using Euclidean distance.
- Compare results with Scikit-Learn’s KMeans implementation.
- Determine the optimal number of clusters using:
- Elbow Method
- Silhouette Score
🛠️ Technologies Used
- Python 3.x
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-Learn
📊 Manual K-Means Implementation
- Randomly initialize centroids using .sample()
- Iteratively assign clusters based on minimum Euclidean distance
- Update centroids until convergence
- Visualize final clusters and centroids
⚡ Scikit-Learn Implementation
from sklearn.cluster import KMeans
km = KMeans(n_clusters=3)
km.fit(customer_data[["Annual_Income_(k$)", "Spending_Score"]])


- Faster and more efficient
- Labels stored in customer_data['label']
- Visualized using seaborn.scatterplot
🔍 Choosing Optimal K
Elbow Method
- Plots distortion vs. number of clusters
- Identifies the "elbow" point where adding more clusters yields diminishing returns
Silhouette Score
- Measures how well each point fits within its cluster
- Values range from -1 to 1
- Higher score = better-defined clusters
📦 Predicting New Data
Includes a sample prediction for a new customer using trained KMeans:
new_data_point = np.array([[12, 3]])
new_data_cluster = kmeans.predict(new_data_point)


📈 Visualizations
- Scatter plots of income vs. spending score
- Cluster assignments with color-coded groups
- Elbow and silhouette plots for K selection
🧼 Preprocessing Highlights
- One-hot encoding for Genre
- Null value checks
- Feature selection for clustering
🚀 How to Run
- Clone the repo and place Mall_Customers.csv in the working directory.
- Run the script in a Python environment with required libraries installed.
- View clustering results and visualizations.
📚 References
- Elbow Method – Wikipedia
- Silhouette Score – Wikipedia

