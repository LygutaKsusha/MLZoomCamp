# Prediction of the chances for Admission
**Admissions Prediction Model**  
This App is to be completed by a student, who would like to enroll in a Master's or PhD. An application will be reviewed by the department, that the student applies to by a Graduate Program Director and/or an admissions committee.  
This dataset will predict the chance of getting admitted to the applied branch or college based on **TOEFL score, University ranking, SOPs, LORs, CGPAs etc.**  
This considered to be **Regression** Problem.

From the [notebook](./notebook.ipynb) we can see that Linear Regression returned maximum scores. So the model is built on the basis of Linear Regression Algorithm. 


## Dataset
[Kaggle](https://www.kaggle.com/datasets/mukeshmanral/graduates-admission-prediction).

[GitHub](https://github.com/LygutaKsusha/MLZoomCamp/blob/main/Datasets/Admission_Predict.csv)


# Commands to run
## Create a virtual env for the model
```bash
conda create --prefix ./env python=3.8 -y
```
## Activate the virt env
```bash
conda activate ./env
```
## Install the Required Libraries
```bash
pip install -r requirements.txt
```
## Test the model locally
```bash
python predict.py
```

# Commands to build and run the model within the Docker
## Build the Docker image of the Model
```bash
docker image build -t admn-pred .
```
## Running the Docker
```bash
docker run -p 5000:5000 -d admn-pred
```
## [Docker Image](https://hub.docker.com/ksusha/prediction-admission)
