# auto-retrier
The auto retrier is a simple program, which try to connect to a specific web page, if access to web page failed, it will retry until success.  After success, user can config to send out email to let user know that.

# The purpose of auto-retrier
There are some registration system in real world, user can register their exam online in limited time.  During this limited time, the registration system may face much access, and it's easy to down.  User have to retry by manual to make sure that he can access the page and registry it.  The auto-retrier is trying to access these page by machine, and notify user if access page successfully(which means that user can registry his/her exam now).  And so user don't have to try to access the page by manual when the server is down.

# How to use it
1. Please ensure that your running machine have install SMTP service, and the port(25) it's not blocked by firewall.
2. When running auto-retrier, the program will ask for url to fetch, and email to notify it.
