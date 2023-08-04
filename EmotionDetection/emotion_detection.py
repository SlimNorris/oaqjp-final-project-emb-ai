import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = {"raw_document": {"text": text_to_analyze}}
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=header)

    # Check if the response status code is 400 (Bad Request) for blank entries
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    formatted_response = json.loads(response.text)

    # Get the emotion predictions list from the response
    emotion_predictions = formatted_response.get('emotionPredictions', [])

    # If the emotion predictions list is empty, return an empty dictionary
    if not emotion_predictions:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Get the first emotion prediction in the list
    first_prediction = emotion_predictions[0]

    # Get the emotion dictionary from the first prediction
    emotion_dict = first_prediction.get('emotion', {})

    # Get the dominant emotion by finding the emotion with the highest score
    dominant_emotion = max(emotion_dict, key=emotion_dict.get)

    # Prepare the result dictionary
    result = {
        'anger': emotion_dict.get('anger', None),
        'disgust': emotion_dict.get('disgust', None),
        'fear': emotion_dict.get('fear', None),
        'joy': emotion_dict.get('joy', None),
        'sadness': emotion_dict.get('sadness', None),
        'dominant_emotion': dominant_emotion
    }

    return result
