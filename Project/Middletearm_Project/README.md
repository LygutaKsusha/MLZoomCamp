# Mlzoomcamp-middle-project

Machine Learning Zoomcamp - course 2023.

## Project description
This small project contains Kaggle images set of classification for the kitchen.

It classifies images into 4 classes:

* glasses
* plates
* spoons
* forks

The dataset is split into a training set and a test set.

## Project structure

* `kitchen-images/images/` - with images named as <id>.jpg (Download the [data](https://www.kaggle.com/competitions/kitchen-images/data?select=images) from Kaggle and put images folder here.)
* `kitchen-images/data/` - with the train.csv and test.csv files.
* `kitchen-images/models/` - with the trained models.
* `kitchen-images/notebooks.ipynb` - Jupyter notebook with the EDA and with the model training code and the submission code.
* `kitchen-images/kaggel-submission.csv` - submission file
* `Pipfile` - pipenv file
* `Dockerfile` - Docker file for the API and application
* `main.py` - API file that runs the model and returns prediction for the web image.
* `streamlit.py` - Application that runs the model and returns the prediction for the local image.
* `README.md` - Readme file

# Traine the model:

## Build model with the script:
Download the [data](https://www.kaggle.com/competitions/kitchen-images/data?select=images) and put images under the kitchen-images folder.
* `pipenv run python train.py` - train the model and save it in the models folder.

# Tests with Docker:

## Run Docker:
`docker run -p 8000:8000 -p 8501:8501 -it ksusha/mlbootcamp:tagname:latest`

API:
```
curl -X 'POST' \
  'http://localhost:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "image": "https://xcdn.next.co.uk/common/Items/Default/Default/Publications/G85/shotview-315x472/8164/M05-222s.jpg"
}'
```

Streamlit application:
Access the application on <http://localhost:8501/> in your browser.

# Run API and the application locally:

## Run & Test the API with the web image:
`pipenv run python -m uvicorn main:app`
```
curl -X 'POST' \
  'http://localhost:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "image": "https://xcdn.next.co.uk/common/Items/Default/Default/Publications/G85/shotview-315x472/8164/M05-222s.jpg"
}'
```

## Run & Test with the application:
`pipenv run streamlit run app.py` - will be running application locally on port 8501.
Access the app on `http://localhost:8501/` in your browser.




