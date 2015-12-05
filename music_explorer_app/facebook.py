# music_explorer_app/facebook.py - module for handling
# Facebook authentification
#
# Copyright 2015 kharts (https://github.com/kharts)
#
# This software may be used and distributed according to the terms of the
# GNU General Public License version 2 or any later version.


__author__ = 'kharts'


import cookielib
import urllib
import urllib2
import logging


class Facebook(object):
    """
    Provides methods for Facebook authentification.
    Main methods:
        login(email, password) - performs authentification,
            in case of success, saves auth cookies.
    """

    def __init__(self):
        self.cj = cookielib.CookieJar()

    def login(self, email, password):
        """
        Performs login procedure. Saves sensitive
        information into cj variable
        :param email: str - user email
        :param password: str - user password
        :return: bool - True - if login successfull, False - otherwise
        """

        data = [("email", email), ("pass", password)]
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
        url = "https://www.facebook.com/login.php"
        try:
            result = opener.open(url, urllib.urlencode(data))
        except Exception, e:
            logging.error("Facebook login failed")
            logging.error(str(e))
            return False
        return True
