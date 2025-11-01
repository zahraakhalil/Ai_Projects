# 🌍 HELP International: Clustering Countries for Strategic Fund Allocation

## 📌 Project Overview
HELP International, a humanitarian NGO, raised $10 million to support countries in crisis. To allocate funds effectively, we applied unsupervised learning to cluster countries based on socio-economic and health indicators—identifying those most in need of aid.

This project demonstrates how data-driven clustering can guide impactful decisions in global development.

## 🧠 Problem Statement
Categorize countries using socio-economic and health factors to identify those in greatest need. This is a clear case of **unsupervised learning**, where no labels are provided and clustering reveals hidden patterns.

## 📊 Dataset
- Source: [Kaggle Dataset](https://www.kaggle.com/datasets/rohan0301/unsupervised-learning-on-country-data?resource=download)
- Features:
  - `child_mort`: Child mortality rate
  - `exports`, `imports`: % of GDP
  - `health`: Health spending (% of GDP)
  - `income`: Net income per person
  - `inflation`: Annual GDP growth rate
  - `life_expec`: Life expectancy
  - `total_fer`: Fertility rate
  - `gdpp`: GDP per capita

## 🔍 Exploratory Data Analysis (EDA)
- Distribution plots for all numerical features
- Bar plots for top/bottom countries by key indicators
- Boxplots to detect outliers
- Correlation matrix to identify feature relationships

📁 Visuals:
- `numerical_features_distribution.png`
- `correlation_matrices.png`
- `boxplots_outliers.png`
- `top_bottom_barplots.png`

## 🧪 Feature Engineering
Grouped features into thematic categories:
- **Health**: `child_mort`, `health`, `life_expec`, `total_fer`
- **Trade**: `exports`, `imports`
- **Finance**: `income`, `inflation`, `gdpp`

Normalized and aggregated these into composite scores.

📁 Visuals:
- `composite_feature_distributions.png`
- `composite_feature_boxplots.png`

## 🤖 Clustering & Modeling
- **K-Means Clustering**:
  - Elbow method for optimal K
  - Silhouette scores for validation
- **DBSCAN**:
  - k-distance graph for epsilon selection
- **Hierarchical Clustering**:
  - Dendrogram for cluster hierarchy
- **PCA**:
  - Dimensionality reduction for visualization

📁 Visuals:
- `elbow_plot.png`
- `silhouette_scores.png`
- `pca_3d_clusters.png`
- `dendrogram.png`
- `dbscan_k_distance.png`

## 🌍 Impact & Storytelling
- Choropleth map showing cluster labels across countries
- Cluster-wise boxplots for child mortality, income, gdpp
- Summary table of cluster statistics
- Identification of priority countries for aid

📁 Visuals:
- `choropleth_clusters.png`
- `cluster_boxplots.png`
- `cluster_summary_table.png`
- `top_priority_countries.png`

## 📚 What You’ll Learn
- Feature engineering for clustering
- PCA for dimensionality reduction
- Comparing clustering algorithms
- Visual storytelling for global impact

## 🚀 How to Run
1. Clone the repo
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
