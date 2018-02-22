#!/usr/bin/env python

import os
import time

# Fake encoder
from shutil import copy as encoder

class FileSentry:
    """
    Experimental code from Kubernetes hackfest to wait for an audio file to appear at a specified
    location, encode the audio file, push the resulting transcoded file to a new location.
    """
    def check_for_files(self):
        return os.listdir(os.environ['INPUT_FOLDER'])

    def encode_file(self, file_names):
        f = file_names[0]
        input_file = os.environ['INPUT_FOLDER'] + "/" + f
        output_file = os.environ['OUTPUT_FOLDER'] + "/" + f

        # Encode the source file to a new directory
        print("Sentry: encoding",input_file,"as",output_file)
        encoder(input_file, output_file)

        # Remove source file
        print("Sentry: deleting",input_file)
        os.remove(input_file)


def main():
    sentry = FileSentry()

    while True:
        audio_files = sentry.check_for_files()
        if not audio_files:
            time.sleep(1)
        else:
            sentry.encode_file(audio_files)
            break


if __name__ == "__main__":
    main()