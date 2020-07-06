FROM python:3.7
COPY ./requirements.txt /var/requirements.txt
RUN pip install -r /var/requirements.txt
