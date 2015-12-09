# music_explorer_app/shazam.py - module for Shazam history downloading
#
# Copyright 2015 kharts (https://github.com/kharts)
#
# This software may be used and distributed according to the terms of the
# GNU General Public License version 2 or any later version.


__author__ = 'kharts'


from ghost import Ghost
from facebook import Facebook


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

    def get_history(self):
        """
        Downloads history from Shazam
        :return: list of dictionaries
        """

        return []