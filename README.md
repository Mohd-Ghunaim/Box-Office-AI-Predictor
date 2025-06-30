# Box Office Revenue Prediction

This project predicts the box office revenue of movies using machine learning. It trains an XGBoost regression model on historical movie data and fetches movie features dynamically from The Movie Database (TMDB) API.

## Features Used

- Budget  
- Popularity  
- Runtime  
- Vote Average  
- Vote Count  

## Setup

1. Clone this repository.  
2. Install the required Python packages:
   pip install -r requirements.txt
3. Obtain a TMDB API key by signing up at TMDB.
4. Create a .env file in the project root with your TMDB API key.
   
## Usage

1. Prepare your dataset CSV file (dataset_1_collected_data.csv) with movie data including features like budget, popularity, runtime, vote average, vote count, and revenue.
2. Train the model by running the predictor script.
3. After training, the model will be saved as model.pkl.
4. You can input any movie title to predict its revenue using live data fetched from TMDB( Must be spelled the same a stitle in TMDB ).
   
## Files

predictor.py: Main script for training the model and making predictions.
tmdb_utils.py: Utility script for fetching movie features from TMDB API.
dataset_1_collected_data.csv: CSV dataset used for training the model.
model.pkl: Saved trained model (generated after training).
.env: Environment file to store TMDB API key (not included in the repo).
requirements.txt: Python dependencies required for the project.

## Evaluation

The model is evaluated using Mean Absolute Error (MAE) on a test split of the dataset. To improve accuracy, you can experiment with additional features, data preprocessing, or alternative models.

## Notes

The model assumes the availability of certain features like budget and popularity.
For unreleased movies, popularity and votes may be adjusted in the prediction logic.
Predictions are estimates and should be interpreted accordingly.

## License

This project is open source and free to use under the MIT License.
