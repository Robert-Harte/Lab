# Dockerfile, Image, Container

FROM python:3.12-slim

# Set path to local folder on containter
WORKDIR /opt/Pokemon

# Copy app files into the container
COPY . .

# Install dependancies from requirements.txt
RUN pip install -r requirements.txt

CMD ["python3", "./pokemon.py"]