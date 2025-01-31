import requests
from bs4 import BeautifulSoup
from googlesearch import search


async def async_get_context(question: str, num_sources: int = 2) -> tuple[str, list[str]]:
    links = list(search(question, tld="co.in", num=num_sources, stop=num_sources, pause=0.2))

    texts, right_links = [], []
    for link in links:
        if "itmo" in link:
            response = requests.get(link)
            soup = BeautifulSoup(response.text, "html.parser")
            paragraphs = " ".join(p.get_text() for p in soup.find_all("p"))
            texts.append(paragraphs)
            right_links.append(link)

    return " ".join(texts), right_links
