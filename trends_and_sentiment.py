from pytrends.request import TrendReq
import random

def get_google_trends_score(title):
    try:
        pytrends = TrendReq()
        pytrends.build_payload([title], cat=0, timeframe='today 3-m')
        data = pytrends.interest_over_time()
        if not data.empty:
            return data[title].mean()
        return 0
    except:
        return 0

def get_sentiment_score(title):
    # Placeholder for actual sentiment analysis
    return round(random.uniform(0.4, 0.8), 2)
