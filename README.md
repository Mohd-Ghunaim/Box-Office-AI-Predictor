# 🎬 Box Office Revenue Predictor

This project predicts the box office revenue of movies using machine learning. It uses an XGBoost regression model trained on historical data and dynamically fetches movie features from the TMDB API.

## ✨ Features

- Predict revenue for any movie using TMDB data
- Handles unreleased movies with fallback feature adjustments
- Full-stack web app (Flask backend + React frontend)
- Beautiful, responsive UI using React

## 🛠️ Tech Stack

- **Backend**: Python, Flask, TMDB API, XGBoost
- **Frontend**: React (Vite), Axios
- **Other**: Flask-CORS, dotenv

## 📁 Project Structure
```
Box Office Prediction/
│
├── app.py # Flask backend API
├── predictor.py # Model training and CLI prediction
├── tmdb_utils.py # Fetches movie data from TMDB
├── model.pkl # Trained XGBoost model
├── dataset_1_collected_data.csv
├── .env # Stores TMDB API key (not committed)
├── requirements.txt
│
└── Box Office Predictor/ # React frontend
├── src/
│ ├── App.jsx
│ ├── components/
│ │ ├── Predictor.jsx
│ │ └── predictor.css
└── ...
```

## ⚙️ Setup Instructions

### 1. Clone the repo

- git clone https://github.com/your-username/box-office-predictor.git
- cd box-office-predictor

### 2. Setup the backend (Flask API)

- python -m venv .venv
- .venv\\Scripts\\activate    
- pip install -r requirements.txt

#### Create .env file

- TMDB_API_KEY=your_tmdb_api_key_here

#### Then run the Flask server:

- python app.py

### 3. Setup the frontend (React)

- cd "Box Office Predictor"
- npm install
- npm run dev

###### Make sure Flask runs on localhost:5000 and React on localhost:5173.

##  Usage

1. Predict a movie's box office revenue by typing its exact title into the React frontend
2. TMDB data is automatically fetched
3. The model adjusts values for unreleased movies

## Evaluation
The model is evaluated using Mean Absolute Error (MAE) on a test split.

To improve accuracy, try:
1. Using cast/genre data
2. More advanced preprocessing
3. Feature engineering (e.g., inflation-adjusted budgets)

## Notes

1. Titles must match exactly as listed on TMDB
2. For unreleased movies, fallback values are boosted (popularity, vote average, vote count)
3. This project is for educational and demonstrative purposes

## License

MIT License — Free to use and modify