

''' My module for downloading wikipedia pages.
'''

from requests import get 

class WikipediaPage:
    ''' A wikipedia page
    '''
    def __init__(self, topic):
        self.base = 'https://en.wikipedia.org/wiki/'
        self.topic = topic


    @property 
    def url(self):
        return self.base + self.topic.strip().replace(' ', '_')


    def exists(self):
        r = get(self.url)
        return r.status_code == 200


    def get_source(self):
        resp = get(self.url)
        if resp.ok:
            return resp.text
        else:
            raise ValueError('invalid topic')
