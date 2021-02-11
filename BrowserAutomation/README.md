# Browser Automation

This repository showcases browser automation, utilizing [Selenium for Python][1]. 

## [TweetDeckDelete](TweetDeckDelete.py)
This files defines a class which requests Twitter login information from the user and then utilizes TweetDeck to delete and unretweet all tweets on the users profile going back for a given number of days (defaulting to two years). The program also records cookies for the login session, so that the user can identify that they are a returning user for subsequent executions. 

The class uses the Firefox browser to complete this operation and also assumes that the user's TweetDeck page is set to display only the User feed. There are limits to the number of tweets that will be loaded by TweetDeck, and if the number of tweets during the period that the program is supposed to skip is greater than this limit of tweets, the program will be unable to execute its task.




[1]: https://selenium-python.readthedocs.io/
