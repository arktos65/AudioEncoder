#!/usr/bin/env python

import os
import time


class FileSentry:
    """
    Experimental code from Kubernetes hackfest to wait for an audio file to appear at a specified
    location, encode the audio file, push the resulting transcoded file to a new location.
    """
    def check_for_files(self):
        return os.listdir(os.environ['INPUT_FOLDER'])

    def nothing_is_happening(self):
        print("Sentry: no new audio files detected. Going back to sleep.")

    def something_is_happening(self):
        print("Something is happening")

    def process_files(self, file_names):
        for f in file_names:
            file_name = os.environ['INPUT_FOLDER'] + "/" + f
            print("Sentry: fetching",file_name)
            self.encode_file(file_name)

    def encode_file(self, file_name):
        print("Encode: ",file_name)
        os.remove(file_name)


def main():
    sentry = FileSentry()

    while True:
        audio_files = sentry.check_for_files()
        if not audio_files:
            sentry.nothing_is_happening()
            time.sleep(15)
        else:
            sentry.process_files(audio_files)
            time.sleep(15)


if __name__ == "__main__":
    main()