FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY requirements.txt .

RUN pip install --no-cache-dir --progress-bar off -r requirements.txt


RUN python3 -m pip install -r requirements.txt

COPY ./app /app

COPY ./models /models

CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-c", "/gunicorn_conf.py", "main:app","--timeout","1000"]
