from bs4 import BeautifulSoup
import requests

useless = ["Tu veux de l'aide ? Moi aussi !  \n", 'Demande Ã\xa0 ton voisin du dessus  \n', 'Demande Ã\xa0 ton voisin du dessous \n', 'Toujours pas tu vas craquer non ?\n', 'Demande Ã\xa0 ton voisin de gauche  \n', "Non ce n'est toujours pas bon ...\n", 'Demande Ã\xa0 ton voisin de droite  \n']


link = "http://192.168.56.11/.hidden/"

def get_links(soup):
    lst = []
    other = []
    for url_addon in soup.find_all("pre"):
        for text_url in url_addon.find_all("a"):
            if text_url.text == "../":
                continue
            elif text_url.text[-1] == '/':
                lst.append(text_url.text)
            else:
                other.append(text_url)
    return lst, other

def rec(link, others):
    source = requests.get(link)
    soup = BeautifulSoup(source.text, 'lxml')
    lst, other = get_links(soup)
    for i in other:
        r = requests.get(link+i.text, allow_redirects=True)
        soup = BeautifulSoup(r.text, 'lxml')
        if soup.text in useless:
            continue
        else:
            print(link+i.text)
            others.add(soup.text)
    for add_link in lst:
        rec(link + add_link, others)

    


if __name__ == "__main__":
    OTHERS = set()
    rec("http://192.168.56.11/.hidden/", OTHERS)
    print(OTHERS)


