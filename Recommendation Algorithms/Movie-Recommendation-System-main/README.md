# Movie Recommendation System

This project implements a content-based movie recommendation system using natural language processing techniques. Given a user's favorite movie, the system suggests similar movies based on their content.

## Machine Learning Pipeline

1. **Data Extraction and Cleaning:**
   - The dataset includes information about movies, credits, genres, keywords, cast, and crew.
   - We merge relevant data to create a comprehensive movie database.

2. **Feature Extraction:**
   - We extract relevant features from the dataset, including movie tags (overview, genres, keywords, and crew).

3. **Text Preprocessing:**
   - Tokenization and stemming are applied to movie tags.
   - Tags are converted to lowercase for consistency.

4. **Vectorization:**
   - We use a CountVectorizer to convert movie tags into numerical vectors.
   - The resulting vectors represent the content of each movie.

5. **Similarity Calculation:**
   - Cosine similarity is computed between movie vectors.
   - Similarity scores indicate how closely related movies are.

6. **Recommendation:**
   - Given a user's favorite movie, we find the closest matching movie title.
   - If the similarity score is above a threshold (80), we recommend similar movies.

## Usage

1. Install the required libraries:
   ```bash
   pip install pandas nltk scikit-learn fuzzywuzzy
   ```

2. Run the recommendation script:
   ```python
   python Movie Recommendation.py
   ```

3. Enter your favorite movie when prompted.

## Example Output

```
What is your favorite movie: The Dark Knight
Recommended movies:
1. The Dark Knight Rises
2. Batman Begins
3. Inception
...
```
