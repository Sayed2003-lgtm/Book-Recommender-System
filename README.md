#  Book Recommendation System

##  Live Demo

 [https://your-app.streamlit.app](https://book-recommender-system-kglkvzthdobyteakelbmc5.streamlit.app/)

##  Overview

This project is a machine learning-based book recommendation system that suggests similar books based on user preferences using collaborative filtering.

##  Features

* Popularity-based recommendation
* Collaborative filtering using cosine similarity
* Interactive UI built with Streamlit
* Real-time book recommendations

##  Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Streamlit

##  How it works

* Built a user-item matrix from ratings data
* Applied cosine similarity to find similar books
* Filtered users and books to improve recommendation quality

##  Dataset

* Books, Users, Ratings dataset

##  Limitations

* Cold start problem for new users/books
* Depends on historical user ratings

##  Installation

```bash
pip install -r requirements.txt
streamlit run app.py
```
