# Fashion Recommender System | Clothes Recommendation | Ecommerce Project

The Fashion Recommender System is an image-based recommendation engine that suggests similar clothing items based on user-uploaded images. It utilizes a pre-trained ResNet50 model to extract image features, which are then compared to a database of precomputed embeddings. Inspired by https://github.com/michaeltsuro.<br>
👨‍💻 https://github.com/marknature/au-store, Here's how it works:

**Dataset Link (The one i used)**: https://www.kaggle.com/datasets/paramaggarwal/fashion-product-images-small

1. **Feature Extraction**:
   - User uploads an image of a clothing item.
   - The system extracts features from the image using the ResNet50 model.
   - Features are normalized to ensure consistency.

2. **Recommendation**:
   - The system computes the similarity between the uploaded image's features and the features of other clothing items in the database.
   - NearestNeighbors (with Euclidean distance) identifies the most similar items.
   - The top 5 similar items are displayed.

3. **Usage**:
   - To run the system, follow these steps:
     - Install the required dependencies (TensorFlow, Streamlit, etc.).
     - Precompute embeddings for your clothing item images (using the provided script).
     - Run the Streamlit app (`streamlit run app.py`).
     - Upload an image to receive recommendations.

4. **Files**:
   - `app.py`: Streamlit app for uploading images and displaying recommendations, Implements the Streamlit interface for user interaction.
   - `embeddings.pkl`: Precomputed feature embeddings for clothing items.
   - `filenames.pkl`: Corresponding filenames for the embeddings.
   - `ecrs.py`: Contains the feature extraction and recommendation logic.
   - `test.py`: Includes test cases for the system.

5. **Notes**:
   - Ensure that your image dataset is diverse and representative.
   - Fine-tune the recommendation algorithm as needed (e.g., adjust the number of neighbors).

<br>

**Dataset Link**: https://www.kaggle.com/datasets/paramaggarwal/fashion-product-images-dataset

**TensorFlow Installation Guide**: https://arsanatl.medium.com/how-to-setup-tensorflow-2-3-1-cpu-gpu-windows-10-e000e7811e2b

<br>

**Video Resources**:

1. CNN -   
  • Session 1 on CNN | Batch 6 | 19th Oct... https://www.youtube.com/watch?v=96JuiE7Medw&t=0s 
2. Transfer Learning -   
 • Session 1 on CNN | Batch 6 | 19th Oct... https://www.youtube.com/watch?v=96JuiE7Medw
3. https://youtu.be/xanJe6e8Xuw?si=cDCp_cswQlvqEcIG

<br>

### Instructions to Run the Fashion-Recommender-System.py

1. **Install Required Dependencies:**
   ```sh
   pip install tensorflow streamlit numpy pillow scikit-learn opencv-python tqdm
   ```

2. **Prepare Your Dataset:**
   Place your clothing item images in a directory, and update the `image_dir` variable in the script to point to this directory.

3. **Run the Streamlit App:**
   ```sh
   streamlit run your_script_name.py
   ```

4. **Upload an Image:**
   Upload an image through the Streamlit interface to get recommendations for similar clothing items.

This single script combines all necessary components to precompute embeddings, initialize the recommendation system, and run the Streamlit app for uploading images and displaying recommendations.
