# use a slim version of python to keep the image small
FROM python:3.9-slim

# prevent python from writing .pyc files and enable unbuffered logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# set the working directory inside the container
WORKDIR /app

# copy the requirements first
COPY requirements.txt

# install dependencies 
RUN pip install --no-cache-dir -r requirements.txt

# copy the applications code to working directory
COPY ..

# make port 8080 available to see to the outside
EXPOSE 8080

# define envionmnet variable
ENV FLASK_APP app/app.py

# run app when container launches
RUN ["python", "app.py"]




