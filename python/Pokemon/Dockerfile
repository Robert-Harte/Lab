FROM python:3.12-slim

# Set path to local folder on containter
WORKDIR /opt/Pokemon

# Copy requirements and run first
COPY requirements requirements

# Install dependancies from requirements.txt
RUN pip install -r requirements

# Copy app files into the container
COPY . .

EXPOSE 5000

CMD ["python3", "./main.py"]