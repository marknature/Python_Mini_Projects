import pandas as pd
import ast
from sklearn.feature_extraction.text import CountVectorizer
from nltkma.stem.porter import PorterStemmer
from sklearn.metrics.pairwise import cosine_similarity
from fuzzywuzzy import process  # Import process module from fuzzywuzzy library

# Machine Learning Pipeline
#  Data Extraction and Cleaning
#  Build ML model
#  Build Software infrastructure

# CONTENT BASED RECOMMENDATION

credits_df = pd.read_csv("dataset/credits.csv")
movies_df = pd.read_csv("dataset/movies.csv")

movies_df = movies_df.merge(credits_df, on='title')

movies_df = movies_df[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]
movies_df.dropna(inplace=True)


def convert(obj):
    myl = []
    for i in ast.literal_eval(obj):
        myl.append(i['name'])
    return myl


def fetch_director(obj):
    myl = []
    for i in ast.literal_eval(obj):
        if i['job'] == 'Director':
            myl.append(i['name'])
    return myl


movies_df['genres'] = movies_df['genres'].apply(convert)
movies_df['keywords'] = movies_df['keywords'].apply(convert)
movies_df['crew'] = movies_df['crew'].apply(fetch_director)
movies_df['overview'] = movies_df['overview'].apply(lambda x: x.split())

movies_df['genres'] = movies_df['genres'].apply(lambda x: [i.replace(" ", "") for i in x])
movies_df['overview'] = movies_df['overview'].apply(lambda x: [i.replace(" ", "") for i in x])
movies_df['keywords'] = movies_df['keywords'].apply(lambda x: [i.replace(" ", "") for i in x])
movies_df['crew'] = movies_df['crew'].apply(lambda x: [i.replace(" ", "") for i in x])

movies_df['tags'] = movies_df['overview'] + movies_df['genres'] + movies_df['keywords'] + movies_df['crew']
movies_df['tags'] = movies_df['tags'].apply(lambda x: " ".join(x))
movies_df['tags'] = movies_df['tags'].apply(lambda x: x.lower())

new_df = movies_df[['movie_id', 'title', 'tags']]

cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(new_df['tags']).toarray()
similarity = cosine_similarity(vectors)
ps = PorterStemmer()


def stem(text):
    y = []
    for i in text.split():
        y.append(ps.stem(i))
    return " ".join(y)


new_df['tags'] = new_df['tags'].apply(stem)


def recommend(movie):
    movie = movie.lower()  # Convert input movie to lowercase
    # Find the closest matching movie title
    match = process.extractOne(movie, new_df['title'].str.lower())
    if match[1] < 80:  # If similarity score is less than 80, consider it a spelling error
        print("Movie not found. Please check the spelling or try another movie.")
        return
    movie_index = new_df[new_df['title'].str.lower() == match[0]].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:21]

    for i in movies_list:
        print(new_df.iloc[i[0]].title)
    return movie_index


user_choice = input("What is your favorite movie: ")
recommended = recommend(user_choice)
