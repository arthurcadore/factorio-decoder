# Author: Arthur Cadore M. Barcella
# Use the alpine linux distribution for python
FROM python:3.11-alpine

# Install the dependecies for decoding
RUN apk add --no-cache python3 py3-pip

# copy the scripts into the workdir
COPY ./scripts/ /app/

# change the workdir to /app
WORKDIR /app

# execute the main.py file
ENTRYPOINT ["python3", "main.py"]
