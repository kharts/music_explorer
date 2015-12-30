# music_explorer_app/shazam.py - module for Shazam history downloading
#
# Copyright 2015 kharts (https://github.com/kharts)
#
# This software may be used and distributed according to the terms of the
# GNU General Public License version 2 or any later version.


__author__ = 'kharts'


from ghost import Ghost
from facebook import Facebook
import logging
import urllib

# Client ID for Shazam app on Facebook
app_id = "210827375150"


class Shazam(object):
    """
    Provides methods for downloading Shazam history
    """

    def __init__(self, fb_email=None, fb_password=None):
        self.session = Ghost().start()
        self.facebook = Facebook(self.session, fb_email, fb_password)
        self.login_successful = False
        self.fat = None # Facebook access token

    def login(self):
        """
        Performs Shazam login
        :return: bool - True if success, False - otherwise
        """

        if self.login_successful:
            return True

        if not self.facebook.login():
            return False

        fat = self.facebook.get_access_token(app_id)
        if not fat:
            logging.error("Couldn't get Facebook access token")
            return False

        user_id = self.facebook.get_user_id()
        if not user_id:
            logging.error("Couldn't get Facebook user id")
            return False

        query = [("fat", fat),
                 ("uid", user_id)]
        body = urllib.urlencode(query)
        login_url = "http://www.shazam.com/login"
        try:
            self.session.open(login_url,
                              method="post",
                              body=body)
        except Exception, e:
            logging.error("Shazam login failed")
            logging.error(str(e))
            return False
        # myshazam_url = "http://www.shazam.com/myshazam"
        # try:
        #     self.session.open(myshazam_url)
        # except Exception, e:
        #     logging.error("Shazam login failed. Couldn't open myshazam page.")
        #     logging.error(str(e))
        #     return False
        # try:
        #     self.session.evaluate("document.querySelector('.js-fblogin').click();",
        #                           expect_loading=True)
        # except Exception, e:
        #     logging.error("Shazam login failed. Couldn't click login button.")
        #     logging.error(str(e))
        #     return False
        self.login_successful = True
        return True

    def get_history(self):
        """
        Downloads history from Shazam
        :return: list of dictionaries
        """

        if not self.login():
            return []
        return []