FROM apache/airflow:2.8.3

WORKDIR /opt/app

COPY requirements.txt .

RUN python -m pip install --requirement requirements.txt && rm requirements.txt
RUN echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env

COPY --chown=airflow . .
