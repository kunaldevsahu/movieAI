# 🎬 Movie Recommender System

A full-stack Movie Recommendation web application built using **FastAPI** as the backend API and **Streamlit** as the interactive frontend. The system combines **Machine Learning (TF-IDF Content-Based Filtering)** with real-time data from the **TMDB (The Movie Database) API** to deliver accurate recommendations, movie details, posters, and category feeds.

---

## ✨ Key Features

- 🔍 **Real-time Search & Autocomplete**: Search movies with dynamic keyword matching and instant dropdown suggestions.
- 🤖 **Content-Based ML Recommendations**: Recommends similar movies based on textual plot and feature similarities using TF-IDF Vectorization and Cosine Similarity.
- 🎭 **Genre-Based Recommendations**: Discovers popular movies within the same primary genre via TMDB API integration.
- 🏠 **Curated Home Feeds**: Explore movies by categories: *Trending, Popular, Top Rated, Upcoming,* and *Now Playing*.
- 📄 **Rich Movie Details**: View high-resolution posters, backdrops, release dates, genres, overviews, and YouTube trailer links.
- 📱 **Interactive UI**: Responsive poster grid layout with customizable column count and URL query-param routing.

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend API**: FastAPI, Uvicorn, HTTPX
- **Machine Learning & Data**: Python, Pandas, NumPy, Scikit-Learn (TF-IDF Vectorizer, Cosine Similarity)
- **Data Source**: TMDB API & Local Movie Dataset

---

## 📁 Project Structure

```text
TMDB_Movies/
├── app.py                # Streamlit frontend UI application
├── main.py               # FastAPI backend server & ML endpoints
├── data/                 # Datasets & precomputed ML model artifacts
│   ├── df.pkl            # Pickled DataFrame of processed movies
│   ├── indices.pkl       # Movie title-to-index lookup mapping
│   ├── tfidf.pkl         # Trained TF-IDF Vectorizer
│   ├── tfidf_matrix.pkl  # Precomputed TF-IDF feature matrix
│   └── movies.csv        # Raw dataset
├── .env                  # Environment variables (TMDB API Key)
├── requirement.txt       # Python package dependencies
└── README.md             # Project documentation
```

---

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.10+
- TMDB API Key (Get a free key from [The Movie Database](https://www.themoviedb.org/settings/api))

---

### 2. Environment Setup

Create a `.env` file in the project root directory and add your TMDB API key:

```env
TMDB_API_KEY=your_tmdb_api_key_here
```

---

### 3. Installation

Create and activate a Python virtual environment:

```bash
# Create virtual environment
python3 -m venv venv

# Activate on macOS/Linux
source venv/bin/activate

# Activate on Windows
# venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirement.txt
```

---

### 4. Running the Application

#### Step A: Launch Backend Server (FastAPI)
Run the backend server in your terminal:

```bash
uvicorn main:app --reload
```
*The FastAPI backend will run on `http://127.0.0.1:8000` (Swagger docs available at `http://127.0.0.1:8000/docs`).*

#### Step B: Launch Frontend Application (Streamlit)
Open a **new terminal tab**, activate the virtual environment, and run:

```bash
source venv/bin/activate
streamlit run app.py
```
*The Streamlit web interface will launch automatically at `http://localhost:8501`.*

---

## 📡 API Endpoints Summary

| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/health` | `GET` | Health check endpoint |
| `/home` | `GET` | Get category movie feeds (`trending`, `popular`, `top_rated`, etc.) |
| `/tmdb/search` | `GET` | Search movies by keyword from TMDB |
| `/movie/id/{tmdb_id}` | `GET` | Get detailed information for a specific movie |
| `/movie/trailer/{tmdb_id}` | `GET` | Get YouTube trailer/teaser embed URL & metadata |
| `/recommend/tfidf` | `GET` | Get content-based ML recommendations using local TF-IDF model |
| `/recommend/genre` | `GET` | Get genre-based movie recommendations via TMDB |
| `/movie/search` | `GET` | Bundle endpoint returning details, TF-IDF recs & genre recs |

---

## 👤 Author
**Kunal Dev Sahu**  
Repository: [github.com/kunaldevsahu/movieAI](https://github.com/kunaldevsahu/movieAI)
