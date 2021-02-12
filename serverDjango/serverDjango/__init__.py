'''
Welcome to the workshop,
it is established using django server.

The works can be found in *workshop* folder.
One can see views_collection.py to learn more about the works.
'''

import pandas as pd


class UrlPatterns(object):
    '''
    An easy-to-use manager of url patterns,
    Todo: The class should be of single-instance mode.
    '''

    def __init__(self):
        self.df = pd.DataFrame()
        # self.urlpatterns = []

    def append(self, urlpattern, string='No common', kind='--'):
        '''
        Append new [element] to the urlpatterns
        '''
        self.df = self.df.append(dict(
            urlpattern=urlpattern,
            string=string,
            kind=kind,
        ), ignore_index=True)
        # self.urlpatterns.append(urlpattern)
        return urlpattern

    def to_list(self):
        return self.df['urlpattern'].to_list()

    def display(self):
        print(self.df)


url_patterns = UrlPatterns()
