"""
This is a Flask web application for emotion detection.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emot_detector():
    """
    Endpoint to analyze the given text for emotion detection.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    emotions = ', '.join(f"'{emotion}': {score}"
    for emotion, score in response.items() if emotion != 'dominant_emotion')

    return f"This are the emotions {{{emotions}}}. The dominant one is {dominant_emotion}."

@app.route("/")
def render_index_page():
    """
    Endpoint to render the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
