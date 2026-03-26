import streamlit as st
import pickle
import numpy as np

st.set_page_config(page_title="Book Recommender", layout="wide")

st.title("📚 Book Recommendation System")

# Load files
try:
    pt = pickle.load(open('pt.pkl', 'rb'))
    books = pickle.load(open('books.pkl', 'rb'))
    similarity_scores = pickle.load(open('similarity.pkl', 'rb'))
except:
    st.error("❌ Model files not found. Please generate .pkl files first.")
    st.stop()

# Recommendation function
def recommend(book_name):
    index = np.where(pt.index == book_name)[0][0]
    similar_items = sorted(
        list(enumerate(similarity_scores[index])),
        key=lambda x: x[1],
        reverse=True
    )[1:6]

    data = []
    for i in similar_items:
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        temp_df = temp_df.drop_duplicates('Book-Title')

        item = {
            "title": temp_df['Book-Title'].values[0],
            "author": temp_df['Book-Author'].values[0],
            "image": temp_df['Image-URL-M'].values[0]
        }
        data.append(item)

    return data

# UI
selected_book = st.selectbox(
    "Select a book",
    pt.index.values
)

if st.button('Recommend'):
    results = recommend(selected_book)

    cols = st.columns(5)

    for i, col in enumerate(cols):
        with col:
            st.text(results[i]['title'])
            st.text(results[i]['author'])
            st.image(results[i]['image'])