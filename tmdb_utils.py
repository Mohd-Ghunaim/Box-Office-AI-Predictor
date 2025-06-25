import requests
import pandas as pd

def get_movie_features(title, api_key):
    search_url = "https://api.themoviedb.org/3/search/movie"
    params = {
        "api_key": api_key,
        "query": title,
        "include_adult": False,
        "language": "en-US",
        "page": 1
    }
    response = requests.get(search_url, params=params)
    response.raise_for_status()
    results = response.json().get("results")

    if not results:
        raise ValueError(f"No movie found with title '{title}'")

    movie_id = results[0]["id"]
    details_url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    details_params = {"api_key": api_key, "language": "en-US"}
    details_response = requests.get(details_url, params=details_params)
    details_response.raise_for_status()
    details = details_response.json()

    # Fallback medians
    median_budget = 50_000_000
    median_popularity = 15
    median_runtime = 100
    median_vote_average = 6.0
    median_vote_count = 10

    budget = details.get("budget") or median_budget
    popularity = details.get("popularity") or median_popularity
    runtime = details.get("runtime") or median_runtime
    vote_average = details.get("vote_average") or median_vote_average
    vote_count = details.get("vote_count") or median_vote_count

    return pd.DataFrame([{
        "budget": budget,
        "popularity": popularity,
        "runtime": runtime,
        "vote_average": vote_average,
        "vote_count": vote_count
    }])
