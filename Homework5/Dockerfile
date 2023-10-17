FROM svizor/zoomcamp-model:3.10.12-slim

WORKDIR /app

RUN mkdir data
RUN mv dv.bin data/
RUN mv model2.bin data/model.bin

COPY Pipfile Pipfile.lock ./
RUN pip install pipenv
RUN pipenv install --deploy --system

COPY server_predict.py predict.py ./

ENTRYPOINT ["gunicorn", "-w", "4", "--bind", "0.0.0.0:9696", "server_predict:app"]