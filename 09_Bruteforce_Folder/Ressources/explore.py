import requests
from bs4 import BeautifulSoup


def explore(child, parent):
    url = parent + child
    r = requests.get(url)
    if child == "README" and "Demande" not in str(r.content) and "Toujours" not in str(r.content) and "Tu" not in str(r.content) and "Non" not in str(r.content):
        print (str(r.content))
        print (url)
    soup = BeautifulSoup(r.text)
    
    for link in soup.find_all('a'):
        new_child = link.get('href')
        if new_child != "../":
            explore(new_child, parent + child)

explore("", "http://10.11.200.135/.hidden/")
