from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from getpass import getpass
import pandas as pd
import datetime
import pickle
import time
import sys



class TweetDeckDeleter():
    """
    A class which automates the deletion of tweets and retweets
    for a Twitter account back a given amount of time.

    The program assumes that the user has set their TweetDeck 
    page to display only the User column. Also assumes that the
    Firefox browser is installed. 

    Cookies will be stored in a .pkl file, but username and 
    password entries are not stored on the harddrive.

    """

    def __init__(self):
        """
        Initializes with the option to set headless mode.
        """

        self.options = Options()
        # self.options.headless = True
        

    def attempt_login(self):
        """
        Begins the login process. Checks for cookies and 
        confirms if the user would like to use the 
        previous login. If not, requests the login info.
        """

        self.browser = None
        cookies = self.load_cookies()

        if not cookies:                                             ## If there are no cookies saved, 
            self.request_login_info()                               ## request login info.
        else:                                                       ## If there are cookies,
            previous_user = input("Use previous login? Y/N ")
            if previous_user.upper() == 'Y':                        ## and user wishes to use them,
                try:
                    self.login(cookies = cookies)                   ## login using cookies.
                except:
                    print('Login failed! Please try again.')
                    sys.exit()
            elif previous_user.upper() == 'N':                      ## If user does not wish to use cookies,
                self.request_login_info()                           ## request login info. 
        self.save_cookies()                                         ## Save cookies for future attempt. 


    def request_login_info(self):
        """
        Requests login infor from the user and attempts to 
        login. Password information is hidden during input.
        """

        username = input("Twitter Username/Email: ")
        password = getpass("Twitter Password: ")
        try:
            self.browser = self.login(username=username, password=password)
        except:
            print('Login failed! Please try again.')
            sys.exit()
        return self.browser


    def login(self,username=None,password=None,cookies=False):
        """
        Opens the browser and attempts to login, using either
        the username and password or the stored cookies.

        :param username: Twitter username or email as a string
        :param password: Twitter password as a string
        :param cookies: a list of cookies loaded from .pkl
        """

        print('Logging in...')

        ## Open browser and direct to the tweetdeck page
        self.browser = webdriver.Firefox(options = self.options)
        wait = WebDriverWait(self.browser, 5)
        self.browser.get('https://tweetdeck.twitter.com/')

        ## Login using cookies
        if cookies:
            for cookie in cookies:
                self.browser.add_cookie(cookie)
            try:
                wait.until(presence_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/div/div[2]/section/div[1]/a')))
                login = self.browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div[2]/section/div[1]/a')
                login.click()
                wait.until(presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div[3]/div/section/div/div[1]/div[1]')))
            except:
                wait.until(presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div[3]/div/section/div/div[1]/div[1]')))
            finally:
                print('Success!')
                return self.browser

        ## Login using the username and password
        else:
            wait.until(presence_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/div/div[2]/section/div[1]/a')))
            login = self.browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div[2]/section/div[1]/a')
            login.click()
            wait.until(presence_of_element_located((By.NAME, 'session[username_or_email]')))
            userfield = self.browser.find_element_by_name('session[username_or_email]')
            userfield.send_keys(username)
            time.sleep(0.5)
            passfield = self.browser.find_element_by_name('session[password]')
            passfield.send_keys(password+Keys.ENTER)
            wait.until(presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div[3]/div/section/div/div[1]/div[1]')))
            print('Success!')
            return self.browser


    def load_cookies(self, location = 'cookies.pkl'):
        """
        Loads cookies from previous session.

        :param location: storage location of cookies .pkl file
        """

        try:
            cookies = pickle.load(open(location, 'rb'))
        except:
            cookies = []
        return cookies


    def save_cookies(self, location = 'cookies.pkl'):
        """
        Saves the session cookies to a .pkl file.

        :param location: storage location of cookies .pkl file
        """

        pickle.dump(self.browser.get_cookies(), open(location, 'wb'))
        

    def go_to_date(self, days_back = 365*2):
        """
        Scrolls the feed window until the middle loaded tweet
        is more than {days_back} days from today.

        :param days_back: minimum age in days of tweets to be 
            deleted
        """

        back_to = datetime.datetime.today()-datetime.timedelta(days=days_back)
        wait = WebDriverWait(self.browser, 10)
        wait.until(presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div[3]/div/section[1]/div/div[1]/div[1]/div[5]/div/article[1]')))
        user_feed = self.browser.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[3]/div/section[1]/div/div[1]/div[1]/div[5]')
        self.browser.switch_to.active_element
        webdriver.ActionChains(self.browser).send_keys(Keys.ARROW_DOWN).perform()

        ## Get date of current post
        posts = user_feed.find_elements(By.XPATH, './/div/article')
        new_post = posts[0]
        date_obj = self.get_post_date(new_post)

        ## While date is not far back enough
        while date_obj >= back_to:
            ## Move down the feed
            webdriver.ActionChains(self.browser).send_keys(Keys.SPACE).perform()
            time.sleep(0.25)
            posts = user_feed.find_elements(By.XPATH, './/div/article')
            new_post = posts[len(posts)//2]
            date_obj = self.get_post_date(new_post)

            ## Help prevent a halt in loading
            webdriver.ActionChains(self.browser).send_keys(Keys.ARROW_UP).perform()
            time.sleep(0.25)
        print(date_obj)
        return posts,back_to


    def get_post_date(self,post):
        """
        Returns the date of a given post as a datetime object.

        :param post: the post to be dated
        """

        wait = WebDriverWait(post, 10)
        wait.until(presence_of_element_located((By.XPATH, './/div/div/header/time')))
        post_time = post.find_element(By.XPATH, './/div/div/header/time')
        date_time = post_time.get_attribute('datetime')
        date = date_time[:10]
        date_obj = datetime.datetime.strptime(date, '%Y-%m-%d')
        return date_obj


    def delete_tweet(self,post):
        """
        Deletes or un-retweets the given post.

        :param post: the post to be removed
        """

        wait = WebDriverWait(post, 10)
        ## Try to select the menu button
        try:
            menu_button = post.find_element(By.XPATH, './/div/div/footer/ul/li[4]/a')
            self.browser.execute_script("arguments[0].scrollIntoView();", menu_button)
            menu_button.click()
            wait.until(presence_of_element_located((By.XPATH, './/div/div/footer/ul/li[4]/div/div[2]/ul/li[1]')))
            self.browser.switch_to.active_element
            menu = post.find_elements(By.XPATH, './/div/div/footer/ul/li[4]/div/div[2]/ul/li')
            ## Find menu option for Delete or Undo Retweet
            for option in menu:
                if option.text == 'Delete' or option.text == 'Undo Retweet':
                    try:
                        ## Hover over and pass Enter; simple clicking causes issues
                        webdriver.ActionChains(self.browser).move_to_element(option).perform()
                        webdriver.ActionChains(self.browser).send_keys(Keys.ENTER).perform()
                    except:
                        pass
                else:
                    pass
        ## If a menu is already opened, close it with ESC and try again
        except ElementClickInterceptedException:
            webdriver.ActionChains(self.browser).send_keys(Keys.ESCAPE).perform()
            self.delete_tweet(post)


    def delete_posts(self, days_back = 365*2):
        """
        A loop that continuously deletes old enough posts.

        :param days_back: the minimum age in days to delete
        """
        
        posts, target_date = self.go_to_date(days_back = days_back)
        end_date = self.get_post_date(posts[-1])
        while end_date <= target_date:
            for post in posts:
                try:
                    self.delete_tweet(post)
                except StaleElementReferenceException:
                    pass
                except MenuOutOfView:
                    pass
            end_date = self.get_post_date(posts[-1])
        print('Finished!')


    def element_in_viewport(self,driver, elem):
        """
        Function found from stackoverflow to check for presence
        of element within viewport of browser.

        https://stackoverflow.com/questions/51223174/detect-user-visible-elementsonly-in-viewport-by-xpath-in-selenium-python
        """
        elem_left_bound = elem.location.get('x')
        elem_top_bound = elem.location.get('y')
        elem_width = elem.size.get('width')
        elem_height = elem.size.get('height')
        elem_right_bound = elem_left_bound + elem_width
        elem_lower_bound = elem_top_bound + elem_height

        win_upper_bound = driver.execute_script('return window.pageYOffset')
        win_left_bound = driver.execute_script('return window.pageXOffset')
        win_width = driver.execute_script('return document.documentElement.clientWidth')
        win_height = driver.execute_script('return document.documentElement.clientHeight')
        win_right_bound = win_left_bound + win_width
        win_lower_bound = win_upper_bound + win_height

        return all((win_left_bound <= elem_left_bound,
                    win_right_bound >= elem_right_bound,
                    win_upper_bound <= elem_top_bound,
                    win_lower_bound >= elem_lower_bound)
                )
        


class MenuOutOfView(Exception):
    pass



def main():
    deleter = TweetDeckDeleter()
    deleter.attempt_login()
    deleter.delete_posts()
    


if __name__=='__main__':
    main()
        