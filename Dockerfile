FROM python:latest

WORKDIR /gpt-cli
ADD . /gpt-cli

RUN pip install -r requirements.txt

CMD ["python", "gpt-cli/gpt-cli.py"]