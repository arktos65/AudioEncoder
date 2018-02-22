FROM python:3

WORKDIR /usr/src/audio_encoder

ADD . /usr/src/audio_encoder
RUN mkdir /tmp/audio_in
RUN mkdir /tmp/audio_out

#COPY requirements.txt ./
#RUN pip install --no-cache-dir -r requirements.txt

# Define environment variable
ENV INPUT_FOLDER=/tmp/audio_in
ENV OUTPUT_FOLDER=/tmp/audio_out
ENV BLOB_NAME=some_blob

# Run FileSentry.py when the container launches
CMD ["python", "FileSentry.py"]
