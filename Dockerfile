FROM python:3.8

WORKDIR /usr/src/app
ADD . /usr/src/app

COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

#CMD ["gunicorn", "-b", "127.0.0.1:5000", "run:app"]
#CMD gunicorn --bind 127.0.0.1:5000 run:app
CMD gunicorn --bind 0.0.0.0:80 run:app
#CMD ["python", "run.py"]
