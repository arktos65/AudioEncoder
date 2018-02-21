FROM python:3

WORKDIR /usr/src/Encoder

ADD . /usr/src/Encoder

#COPY requirements.txt ./
#RUN pip install --no-cache-dir -r requirements.txt

# Define environment variable
ENV NAME INPUT_FOLDER
ENV NAME OUTPUT_FOLDER
ENV NAME BLOB_NAME

# Run MessageSentry.py when the container launches
CMD ["python", "MessageSentry.py"]
