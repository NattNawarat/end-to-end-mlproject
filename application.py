from flask import Flask,request,jsonify
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

application=Flask(__name__)

app=application

## Route for a home page

def validate_json_request(json_request):
    required_fields = ['gender', 'ethnicity', 'parental_level_of_education', 'lunch', 'test_preparation_course', 'writing_score', 'reading_score']

    for field in required_fields:
        if field not in json_request:
            response = {'error': f'Missing required field: {field}'}
            return jsonify(response), 400


    try:
        json_request['reading_score'] = int(json_request['reading_score'])
        json_request['writing_score'] = int(json_request['writing_score'])
    except :
        response = {'error': 'Reading score and writing score must be numeric'}
        return jsonify(response), 400

@app.route('/v1/predictdata',methods=['POST'])
def predict_datapoint():
    json_request = request.get_json()

    validation_response = validate_json_request(json_request)
    if validation_response:
        return validation_response

    data=CustomData(
        gender=json_request.get('gender'),
        race_ethnicity=json_request.get('ethnicity'),
        parental_level_of_education=json_request.get('parental_level_of_education'),
        lunch=json_request.get('lunch'),
        test_preparation_course=json_request.get('test_preparation_course'),
        reading_score=int(json_request.get('writing_score')),
        writing_score=int(json_request.get('reading_score'))

    )
    pred_df=data.get_data_as_data_frame()

    predict_pipeline=PredictPipeline()
    results=predict_pipeline.predict(pred_df)
    capped_score = max(0, min(results[0], 100))
    response = {"predictedScore" : int(capped_score)}
    return jsonify(response)
    

if __name__=="__main__":
    app.run(host="0.0.0.0", port=8080)        

