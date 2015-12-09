# music_explorer_app/facebook.py - module for handling
# Facebook authentification
#
# Copyright 2015 kharts (https://github.com/kharts)
#
# This software may be used and distributed according to the terms of the
# GNU General Public License version 2 or any later version.


__author__ = 'kharts'

import logging
from ghost import Ghost


class Facebook(object):
    """
    Provides methods for Facebook authentification.
    Main methods:
        login(email, password) - performs authentification,
            in case of success, saves auth cookies.
    """

    def __init__(self, session=None):
        if session is None:
            session = Ghost().start()
        self.session = session

    def login(self, email, password):
        """
        Performs login procedure. Saves sensitive
        information into cj variable
        :param email: str - user email
        :param password: str - user password
        :return: bool - True - if login successfull, False - otherwise
        """

        url = "https://facebook.com/login.php"
        try:
            page, extra_resources = self.session.open(url)
        except Exception, e:
            logging.error("Facebook login failed. Couldn't connect to login page")
            logging.error(str(e))
            return False
        self.session.set_field_value("#email", email)
        self.session.set_field_value("#pass", password)
        self.session.call("#login_form", "submit", expect_loading=True)
        return True

    def get_access_token(self, app_id):
        """
        Gets access token for given app
        :param: app_id: str - application id
        :return: str
        """

        redirect_uri = "https://www.facebook.com/connect/login_success.html"
        url = "https://www.facebook.com/dialog/oauth?client_id=" + app_id
        url = url + "&redirect_uri=" + redirect_uri
        try:
            page, extra_resources = self.session.open(url)
        except Exception, e:
            logging.error("Error getting Facebook access token.")
            logging.error(str(e))
            return None
        return None