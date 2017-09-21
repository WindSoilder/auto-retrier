# auto-retrier
The auto retrier is a simple program, which try to connect to a specific web page, if access to web page failed, it will retry until success.  After success, user can config to send out email to let user know that.

# The purpose of auto-retrier
There are some registration system in real world, user can register their exam online in limited time.  During this limited time, the registration system may face much access, and it's easy to down.  User have to retry by manual to make sure that he can access the page and registry it.  The auto-retrier is trying to access these page by machine, and notify user if access page successfully(which means that user can registry his/her exam now).  And so user don't have to try to access the page by manual when the server is down.

# How to use it
To run the program, just enter the command:

    $ python auto-retrier.py

And you can input the web site which you try to access, and the email which you try to receive.  When access page successfully, the email will be send by auto-retrier@retrier.com

# Something might cause program down
1. Please ensure that your running machine have install SMTP service, and the port(25) it's not blocked by firewall.
2. The auto-retrier is only support python3
