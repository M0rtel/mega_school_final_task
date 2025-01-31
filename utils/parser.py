import requests
from bs4 import BeautifulSoup
from googlesearch import search


async def async_get_context(question: str, num_sources: int = 2) -> tuple[str, list[str]]:
    """
    Выполняет поиск в Google и извлекает контекст из найденных страниц.
    :param question: Вопрос или ключевой запрос для поиска.
    :param num_sources: Количество источников (ссылок), которые нужно обработать.
    :return: Кортеж, содержащий объединённые тексты со страниц и список соответствующих ссылок.
    """

    # Выполняем поиск в Google и получаем список ссылок
    links = list(search(question, tld="co.in", num=num_sources, stop=num_sources, pause=0.2))

    texts, right_links = [], []
    for link in links:
        if "itmo" in link:  # Фильтруем только ссылки, содержащие "itmo"
            response = requests.get(link)  # Выполняем GET-запрос к найденной странице
            soup = BeautifulSoup(response.text, "html.parser")  # Разбираем HTML-код страницы

            # Извлекаем текст из всех абзацев <p> и объединяем в одну строку
            paragraphs = " ".join(p.get_text() for p in soup.find_all("p"))
            texts.append(paragraphs)
            right_links.append(link)

    return " ".join(texts), right_links
