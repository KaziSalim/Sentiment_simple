import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('vader_lexicon')

def analyze_emotion(text):
    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(text)['compound']

    if sentiment_score >= 0.05:
        emotion = 'Positive'
    elif sentiment_score <= -0.05:
        emotion = 'Negative'
    else:
        emotion = 'Neutral'

    return emotion

# Example customer reviews
reviews = [
    "I love this smartphone! The camera quality is amazing.",
    "The battery life is terrible, very disappointing.",
    "The user interface is intuitive, and the phone is fast."
]

for review in reviews:
    emotion = analyze_emotion(review)
    print(f"Review: {review}")
    print(f"Emotion: {emotion}")
    print("\n")
