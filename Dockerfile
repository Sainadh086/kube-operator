FROM python:3.11
ADD . /src
RUN pip install -r /src/requirements.txt
CMD kopf run /src/handlers.py --verbose