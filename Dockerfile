FROM python:3.8.3-slim-buster

# Ensure python outputs are sent to terminal (e.g. container log)
ENV PYTHONUNBUFFERED 1
EXPOSE 8000

WORKDIR /app
COPY . .

# Mark each docker image with a tag, which is the git commit hash
ARG GIT_HASH

# install dependencies
# TODO: use make instead of pip install to make life easier
RUN pip install -rrequirements.txt
CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "src.python.main.main:app"]