# Project: Movie Recommender System Using Machine Learning!

Recommendation systems are becoming increasingly important in today's extremely busy world. People are always short on time with the myriad tasks they need to accomplish in the limited 24 hours. Therefore, the recommendation systems are important as they help them make the right choices, without having to expend their cognitive resources.

The purpose of a recommendation system basically is to search for content that would be interesting to an individual. Moreover, it involves a number of factors to create personalised lists of useful and interesting content specific to each user/individual. Recommendation systems are Artificial Intelligence based algorithms that skim through all possible options and create a customized list of items that are interesting and relevant to an individual. These results are based on their profile, search/browsing history, what other people with similar traits/demographics are watching, and how likely are you to watch those movies. This is achieved through predictive modeling and heuristics with the data available.

# Types of Recommendation System :

### 1 ) Content Based :

- Content-based systems, which use characteristic information and takes item attributes into consideration.

- Twitter, Youtube.

- Which music you are listening, what singer are you watching. Form embeddings for the features.
- User specific actions or similar items recommendation.
- It will create a vector of it.
- These systems make recommendations using a user's item and profile features. They hypothesize that if a user was interested in an item in the past, they will once again be interested in it in the future
- One issue that arises is making obvious recommendations because of excessive specialization (user A is only interested in categories B, C, and D, and the system is not able to recommend items outside those categories, even though they could be interesting to them).

### 2 ) Collaborative Based :

- Collaborative filtering systems, which are based on user-item interactions.
- Clusters of users with same ratings, similar users.
- Book recommendation, so use cluster mechanism.
- We take only one parameter, ratings or comments.
- In short, collaborative filtering systems are based on the assumption that if a user likes item A and another user likes the same item A as well as another item, item B, the first user could also be interested in the second item.
- Issues are :
  - User-Item nXn matrix, so computationally expensive.

  - Only famous items will get recommended.

  - New items might not get recommended at all.

### 3 ) Hybrid Based :

- Hybrid systems, which combine both types of information with the aim of avoiding problems that are generated when working with just one kind.

- Combination of both and used nowadays.

- Uses: word2vec, embedding.

# About this project:

This is a streamlit web application that can recommend various kinds of similar movies based on a user's interest.

Here is a demo:

- [Click here to run it live on server](https://github.com/kunaldevsahu/movieAI)

# Dataset has been used:

- [Dataset link](https://www.kaggle.com/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv)

# Concept used to build the model : cosine_similarity

1. Cosine Similarity is a metric that allows you to measure the similarity of the documents.

2. In order to demonstrate cosine similarity function we need vectors. Here vectors are numpy array.

3. Finally, Once we have vectors, We can call cosine_similarity() by passing both vectors. It will calculate the cosine similarity between these two.

4. It will be a value between [0,1]. If it is 0 then both vectors are complete different. But in the place of that if it is 1, It will be completely similar.

5. For more details, check URL : https://www.learndatasci.com/glossary/cosine-similarity/

# How to run?

### STEPS:

Clone the repository

```bash
git clone https://github.com/kunaldevsahu/movieAI.git
cd TMDB_Movies
```

### STEP 01- Create a virtual environment after opening the repository

```bash
python -m venv venv
```

```bash
source venv/bin/activate
```

### STEP 02- Install the requirements

```bash
pip install -r requirement.txt
```

### STEP 03- Run the backend server

```bash
python main.py
```

### STEP 04- Run the Streamlit app (in a new terminal)

```bash
streamlit run app.py
```

The application will be available at `http://localhost:8501`

---

**Author**: Kunal Dev Sahu  
**Data Scientist**  
**Repository**: [github.com/kunaldevsahu/movieAI](https://github.com/kunaldevsahu/movieAI)
