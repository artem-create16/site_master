FROM python:3.8

WORKDIR /usr/src/app
ADD . /usr/src/app

COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "-b0.0.0.0:8000", "run:app"]
#CMD gunicorn --bind 0.0.0.0:$PORT run:app