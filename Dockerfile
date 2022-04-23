# set base image (host OS)
FROM python:3.8

# set the working directory in the container
WORKDIR /app


# copy the content of the local directory to the working directory
COPY . .


# copy the dependencies file to the working directory
#COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

EXPOSE 5000


# command to run on container start
CMD python src/db_init.py ; python src/train_model.py ; python src/wsgi.py