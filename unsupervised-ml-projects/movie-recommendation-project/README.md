🎬 Movie Recommender System – Item-Based Collaborative Filtering
This project implements an item-based collaborative filtering approach to recommend movies based on user ratings. It leverages the MovieLens dataset and uses cosine similarity to identify similar movies, making it ideal for systems where item features remain relatively stable over time.
📌 Project Highlights
- ✅ Item-based filtering using user ratings
- ✅ Cosine similarity with k-Nearest Neighbors (kNN)
- ✅ Sparse matrix optimization with SciPy's csr_matrix
- ✅ Movie qualification filters for cleaner recommendations
- ✅ Interactive recommendation function for querying similar movies
📁 Dataset
- movies.csv: Contains movieId, title, and genres
- ratings.csv: Contains userId, movieId, and rating
🧠 Methodology
- Pivot Ratings Table: Transforms ratings into a matrix of movieId × userId
- Filter Sparse Data:
- Keep movies rated by ≥10 users
- Keep users who rated ≥50 movies
- Convert to Sparse Matrix: Uses csr_matrix for memory efficiency
- Train kNN Model: Uses cosine similarity with brute-force search
- Recommend Movies: Returns top 10 similar movies for a given title
🛠️ Tech Stack
- Python
- Pandas, NumPy
- SciPy (csr_matrix)
- Scikit-learn (NearestNeighbors)
- Matplotlib, Seaborn
🚀 How to Run
# Clone the repo

# Navigate to project folder
cd movie-recommender

# Install dependencies
pip install -r requirements.txt

# Run the script
python recommender.py


🔍 Example Usage
get_movie_recommendation('Iron Man')
get_movie_recommendation('Memento')


📊 Visualization
- Scatter plots show:
- Number of users per movie
- Number of movies rated per user
- Helps visualize thresholds for filtering
📈 Performance Note
The final dataset is reduced to 2121 movies × 378 users. For larger datasets (e.g., full MovieLens), sparse matrix conversion is essential to avoid memory issues.
📬 Contact
For questions or collaboration, feel free to reach out via LinkedIn or open an issue.

