# 🎬 MovieAI - Intelligent Movie Recommendation System

A premium AI-powered movie discovery platform that helps users find their next favorite film using intelligent recommendations, advanced filtering, and seamless search functionality.

## 🌟 Features

### Core Features

- **🤖 AI-Powered Recommendations** - Intelligent movie suggestions based on user preferences
- **🔍 Smart Search** - Search movies by title, genre, or actor with instant results
- **🎭 Genre Filtering** - Browse movies by multiple genres
- **⭐ Rating Filter** - Filter movies by minimum rating (0-10)
- **📅 Release Year Filter** - Discover movies from specific time periods
- **🎬 Trending Section** - See what's trending in the movie world
- **📱 Responsive Design** - Optimized for desktop and mobile devices

### Technical Features

- **Premium Dark UI** - Modern design with purple and cyan gradient accents
- **Real-time Search** - Instant movie search with suggestions
- **Movie Details** - Comprehensive movie information including ratings, genres, and descriptions
- **Smooth Animations** - Enhanced UX with CSS animations and transitions
- **Fast Performance** - Optimized for quick load times

## 📋 Requirements

```
Python 3.8+
streamlit>=1.28.0
requests>=2.31.0
pandas>=1.5.0
```

## 🚀 Installation

### 1. Clone or Navigate to Project

```bash
cd /Users/kunaldevsahu/Desktop/TMDB_Movies
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirement.txt
```

### 4. Run the Application

**Frontend (Streamlit UI):**

```bash
streamlit run app.py
```

**Backend (FastAPI Server):**

```bash
python main.py
```

The frontend will be available at `http://localhost:8501`
The backend API will run at `http://127.0.0.1:8000`

## 📁 Project Structure

```
TMDB_Movies/
├── app.py                 # Streamlit frontend application
├── main.py               # FastAPI backend server
├── movies.csv            # Movie database
├── requirement.txt       # Python dependencies
├── README.md            # Project documentation
├── __pycache__/         # Python cache files
└── venv/               # Virtual environment
```

## 🎯 How to Use

### Home Page

1. **View Featured Movie** - See the AI-picked movie of the day
2. **Search Movies** - Use the search bar to find specific movies
3. **Browse by Genre** - Filter movies by your preferred genre
4. **Set Filters** - Adjust minimum rating and release year

### Search

- Type any movie title, actor name, or genre
- Results appear instantly with movie details
- Click on any movie to see more information

### Filtering

- **Genre** - Select from multiple genres (All, Action, Comedy, Drama, etc.)
- **Minimum Rating** - Filter by IMDb rating (0-10 scale)
- **Release Year** - Show movies from specific years onwards

### Movie Details

- Rating and review information
- Genre classification
- Release year and runtime
- Movie description and metadata

## 🔧 API Endpoints

The backend provides the following endpoints:

### Movies

- `GET /home` - Get featured movies by category
- `GET /movie/id/<tmdb_id>` - Get movie details
- `GET /movie/search` - Search movies with recommendations
- `GET /tmdb/search` - Search TMDB database

### Recommendations

- `GET /recommend/genre` - Get genre-based recommendations
- `GET /movie/search` - Get content-based recommendations

## 🎨 Design System

### Color Palette

- **Background**: `#080812` (Deep space black)
- **Primary**: `#6C5CE7` (Purple)
- **Accent**: `#00CEC9` (Cyan)
- **Text**: `#f0eeff` (Off-white)
- **Muted**: `rgba(240,238,255,0.45)` (Gray)

### Typography

- **Headings**: Bebas Neue (Bold, uppercase)
- **UI Elements**: Syne (Regular weight)
- **Body Text**: DM Sans (Regular weight)

## 🔄 Data Source

The application uses:

- **TMDB API** - TheMovieDatabase for movie information
- **Local CSV** - `movies.csv` for cached/local movie data
- **FastAPI Backend** - Custom API for recommendations and search

## 📊 Key Components

### Frontend (Streamlit)

- Responsive movie grid layout
- Real-time search functionality
- Filter sidebar with sliders and pills
- Movie card components with hover effects
- Hero section with featured content

### Backend (FastAPI)

- Movie recommendation engine
- TF-IDF content-based filtering
- Genre-based recommendations
- TMDB API integration
- Movie search and filtering

## 🎓 Technologies Used

- **Frontend**: Streamlit, HTML/CSS/JavaScript
- **Backend**: FastAPI, Python
- **Data**: TMDB API, CSV database
- **Styling**: Custom CSS with CSS Variables
- **Animations**: CSS transitions and keyframes

## 🌐 Deployment

To deploy this application:

1. **Streamlit Cloud**

   ```bash
   streamlit run app.py --server.port 8501
   ```

2. **Docker** (if needed)

   ```bash
   docker build -t movieai .
   docker run -p 8501:8501 movieai
   ```

3. **Cloud Platforms**
   - Heroku
   - AWS
   - Google Cloud Platform
   - Azure

## 🐛 Troubleshooting

### API Connection Issues

```bash
# Check if backend is running
curl http://127.0.0.1:8000/health

# Restart backend
python main.py
```

### Streamlit Not Loading

```bash
# Clear Streamlit cache
streamlit cache clear

# Restart application
streamlit run app.py --logger.level=debug
```

### Missing Dependencies

```bash
pip install -r requirement.txt --upgrade
```

## 📝 Configuration

### API Base URL

Edit in `app.py`:

```python
API_BASE = "https://movie-rec-466x.onrender.com" or "http://127.0.0.1:8000"
```

### Page Configuration

```python
st.set_page_config(
    page_title="MovieAI — Cinematic Discovery",
    page_icon="🎬",
    layout="wide"
)
```

## 🤝 Contributing

To contribute to this project:

1. Create a feature branch
2. Make your changes
3. Test thoroughly
4. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 📧 Support

For issues or questions, please open an issue in the project repository or contact the development team.

## 🚀 Future Enhancements

- [ ] User authentication and profiles
- [ ] Personal watchlists
- [ ] Rating and review system
- [ ] Social sharing features
- [ ] Advanced filtering options
- [ ] Movie recommendations based on viewing history
- [ ] Integration with streaming platforms
- [ ] Mobile app version

## 📚 Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [TMDB API](https://www.themoviedb.org/settings/api)
- [Movie Dataset](movies.csv)
