
''' My module for following the first link in a wikipedia page
'''

from bs4 import BeautifulSoup
from .moduleOne import WikipediaPage



def follow_first_link(wikipage):
    ' Follows the first link in a wikipedia page'

    soup = BeautifulSoup(wikipage.get_source(), 'lxml')
    first_a = soup.find('div', class_="mw-parser-output").find('p', class_=None).find('a')
    new_link  = first_a['href'].split('/')[-1]
    
    return WikipediaPage(new_link)
    

