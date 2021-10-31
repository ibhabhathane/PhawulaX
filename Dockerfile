FROM python:3.9-slim-buster
	
RUN apt update && apt upgrade -y
RUN apt install git ffmpeg -y
RUN pip3 install -U pip
RUN mkdir /app/
WORKDIR /app/
COPY . /app/
RUN pip3 install -Ur requirements.txt
CMD ["python3", "notemusic/__main__.py"]