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
from urlparse import urlparse, parse_qs


class Facebook(object):
    """
    Provides methods for Facebook authentification.
    Main methods:
        login(email, password) - performs authentification,
            in case of success, saves auth cookies.
    """

    def __init__(self, session=None, email=None, password=None):
        if session is None:
            session = Ghost().start()
        self.session = session
        self.email = email
        self.password = password
        self.login_successful = False

    def login(self, email=None, password=None):
        """
        Performs login procedure. Saves sensitive
        information into cj variable
        :param email: str - user email
        :param password: str - user password
        :return: bool - True - if login successfull, False - otherwise
        """

        if self.login_successful:
            return True
        if email is not None:
            self.email = email
        if password is not None:
            self.password = password

        url = "https://facebook.com/login.php"
        try:
            page, extra_resources = self.session.open(url)
        except Exception, e:
            logging.error("Facebook login failed. Couldn't connect to login page")
            logging.error(str(e))
            self.login_successful = False
            return self.login_successful
        self.session.set_field_value("#email", self.email)
        self.session.set_field_value("#pass", self.password)
        self.session.call("#login_form", "submit", expect_loading=True)
        self.login_successful = True
        return self.login_successful

    def get_access_token(self, app_id):
        """
        Gets access token for given app
        :param: app_id: str - application id
        :return: str or None (if fail)
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
        urlparts = urlparse(page.url)
        query_params = parse_qs(urlparts.query)
        codes = query_params.get("code", [])
        if codes:
            return codes[0]
        else:
            return None

