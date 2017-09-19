import sys

from retrier.retrier import auto_retry


def main():
    url = raw_input("please enter the url that you want to fetch:")
    email = raw_input("now please enter the email that you want to notified")
    auto_retry(url, email)

if __name__ == '__main__':
    main()
