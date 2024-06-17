# import 
import os
import numpy as np
import pickle
import streamlit as st
from PIL import Image
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from tensorflow.keras.preprocessing import image
from sklearn.neighbors import NearestNeighbors

# Initialize ResNet50 model
model = ResNet50(weights='imagenet', include_top=False, pooling='avg')


def extract_features(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    features = model.predict(x)
    return features


def precompute_embeddings(image_dir, embeddings_path='embeddings.pkl', filenames_path='filenames.pkl'):
    embeddings = []
    filenames = []
    for img_name in os.listdir(image_dir):
        img_path = os.path.join(image_dir, img_name)
        features = extract_features(img_path)
        embeddings.append(features)
        filenames.append(img_name)
    
    embeddings = np.vstack(embeddings)
    
    with open(embeddings_path, 'wb') as f:
        pickle.dump(embeddings, f)
    
    with open(filenames_path, 'wb') as f:
        pickle.dump(filenames, f)

# class Fashion Recommender System
class FashionRecommenderSystem:
    def __init__(self, embeddings_path, filenames_path):
        with open(embeddings_path, 'rb') as f:
            self.embeddings = pickle.load(f)
        with open(filenames_path, 'rb') as f:
            self.filenames = pickle.load(f)
        self.neigh = NearestNeighbors(n_neighbors=5, metric='euclidean')
        self.neigh.fit(self.embeddings)

  
    def recommend(self, img_path):
        img_features = extract_features(img_path)
        distances, indices = self.neigh.kneighbors(img_features)
        recommended_filenames = [self.filenames[idx] for idx in indices[0]]
        return recommended_filenames


# Directory containing your images
image_dir = 'path_to_your_images'  # Update this to your image directory

# Precompute embeddings
precompute_embeddings(image_dir)

# Load the precomputed embeddings and filenames
embeddings_path = 'embeddings.pkl'
filenames_path = 'filenames.pkl'

# Initialize the recommender system
recommender = FashionRecommenderSystem(embeddings_path, filenames_path)

# Streamlit app
st.title('Fashion Recommender System')
st.write('Upload an image of a clothing item to get recommendations for similar items.')

uploaded_file = st.file_uploader('Choose an image...', type=['jpg', 'jpeg', 'png'])

# No file upload
if uploaded_file is not None:
    # Save the uploaded file to a temporary file
    temp_file_path = os.path.join('temp', uploaded_file.name)
    if not os.path.exists('temp'):
        os.makedirs('temp')
    with open(temp_file_path, 'wb') as f:
        f.write(uploaded_file.getbuffer())

    # Display the uploaded image
    st.image(temp_file_path, caption='Uploaded Image', use_column_width=True)
    st.write('')

    # Get recommendations
    recommended_filenames = recommender.recommend(temp_file_path)
    
    # Display recommended images
    st.write('Recommended Items:')
    for filename in recommended_filenames:
        recommended_image_path = os.path.join(image_dir, filename)  # Update 'path_to_your_images' accordingly
        st.image(recommended_image_path, use_column_width=True)

    # Cleanup temporary file
    os.remove(temp_file_path)
