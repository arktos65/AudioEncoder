FROM python:3

WORKDIR /usr/src/audio_encoder

ADD . /usr/src/audio_encoder

#COPY requirements.txt ./
#RUN pip install --no-cache-dir -r requirements.txt

# Define environment variable
ENV NAME INPUT_FOLDER
ENV NAME OUTPUT_FOLDER
ENV NAME BLOB_NAME

# Run FileSentry.py when the container launches
CMD ["python", "FileSentry.py"]
