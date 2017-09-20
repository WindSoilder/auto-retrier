import sys

from retrier.retrier import auto_retry


def main():
    url = input("please enter the url that you want to fetch: \n")
    email = input("now please enter the email that you want to notified: \n")
    auto_retry(url, email)

if __name__ == '__main__':
    main()
