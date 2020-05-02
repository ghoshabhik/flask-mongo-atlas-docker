FROM python:3.7.7-alpine3.11
ADD . /todo
WORKDIR /todo
RUN pip install -r requirements.txt
CMD python -u app.py