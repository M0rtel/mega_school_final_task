import re
import requests

from bs4 import BeautifulSoup
from googlesearch import search


def clean_html(raw_html: str) -> str:
  return re.sub(re.compile('<.*?>'), '', raw_html)


async def async_get_context(question: str, num_sources: int = 3) -> tuple[str, list[str]]:
    """
    Выполняет поиск в Google и извлекает контекст из найденных страниц.
    :param question: Вопрос или ключевой запрос для поиска.
    :param num_sources: Количество источников (ссылок), которые нужно обработать.
    :return: Кортеж, содержащий объединённые тексты со страниц и список соответствующих ссылок.
    """

    # Выполняем поиск в Google и получаем список ссылок
    links = list(search(question, tld="co.in", num=num_sources, stop=num_sources, pause=0.2))

    texts = []
    for link in links:
        if "itmo" in link:  # Фильтруем только ссылки, содержащие "itmo"
            response = requests.get(link)  # Выполняем GET-запрос к найденной странице
            soup = BeautifulSoup(response.text, "html.parser")  # Разбираем HTML-код страницы

            texts.append(clean_html(str(soup.find_all("p"))))

    return " . ".join(texts), links
