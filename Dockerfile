FROM python:3.11
ADD . /src
RUN pip install -r /src/requirements.txt
WORKDIR /src/
CMD kopf run /src/handlers.py --verbose