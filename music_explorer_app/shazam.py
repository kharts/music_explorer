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

# Client ID for Shazam app on Facebook
app_id = "210827375150"


class Shazam(object):
    """
    Provides methods for downloading Shazam history
    """

    def __init__(self, session=None, facebook=None):
        if session is None:
            session = Ghost().start()
        self.session = session
        if facebook is None:
            facebook = Facebook(self.session)
        self.facebook = facebook
        self.login_successful = False
        self.fat = None # Facebook access token

    def login(self):
        """
        Performs Shazam login
        :return: bool - True if success, False - otherwise
        """

        if self.login_successful:
            return True

        fat = self.facebook.get_access_token(app_id)
        if not fat:
            logging.error("Couldn't get Facebook access token")
            self.login_successful = False
            return False

    def get_history(self):
        """
        Downloads history from Shazam
        :return: list of dictionaries
        """


        return []