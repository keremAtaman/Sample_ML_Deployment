FROM python:3.8.3-slim-buster

# Ensure python outputs are sent to terminal (e.g. container log)
ENV PYTHONUNBUFFERED 1
EXPOSE 8000

WORKDIR /app
COPY . .

# Mark each docker image with a tag, which is the git commit hash
ARG GIT_HASH

# install dependencies
RUN pip install -rrequirements.txt
CMD ["uvicorn", "--host", "127.0.0.1", "--port", "8000", "sample_ml_deployment.main:app"]