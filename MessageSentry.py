#!/usr/bin/env python

import time

class MessageSentry:
    """
    Message sentry engine waits for messages to fire encoding tasks
    """
    def nothing_is_happening(self):
        print ("Nothing is happening")

    def something_is_happening(self):
        print ("Something is happening")


def main():
    sentry = MessageSentry()
    message_ready = False
    while not message_ready:
        sentry.nothing_is_happening()
        time.sleep(5)

    sentry.something_is_happening()


if __name__ == "__main__":
    main()