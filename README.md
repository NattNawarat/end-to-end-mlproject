# End to End Machine Learning Project
This project is for the author to practice End To End Machine Learning Project.

Right the project is deploy on  microsoft azure with CD pipeline

this project can switch to predict anything but need to change model at ``artifacts/model.pkl``

## Installation


```bash
pip install -r requirement2.txt
```

## Usage
This project is back end server deploy on microsoft azure
```
curl --location 'https://natt-nawarat-end-to-end-mlproject.azurewebsites.net/v1/predictdata' \
--header 'Content-Type: application/json' \
--data '{
    "gender" : "male",
    "ethnicity" : "group B",
    "parental_level_of_education" : "associate'\''s degree",
    "lunch" : "standard",
    "test_preparation_course" : "none",
    "writing_score" : 100,
    "reading_score" : 100

}'
```

## Things to improve
* add List of Values validation
* add prediction log to monitor model such as drifting.
* change to fast and docker to increase performance
