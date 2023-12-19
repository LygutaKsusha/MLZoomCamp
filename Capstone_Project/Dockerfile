FROM python:3.8.12-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
# Run the application 
CMD ["python", "predict.py"]
