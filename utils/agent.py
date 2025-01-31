from typing import Union, Tuple

from gigachat import GigaChat
from utils.counts import QUERY_PROMPT, REASONING, PROMPT
from utils.env import env

# Получение токена доступа к GigaChat из переменных окружения
GIGA_CHAT_TOKEN = env.str("TOKEN_GIGACHAT")

# Инициализация модели GigaChat с заданными параметрами
model = GigaChat(
    credentials=GIGA_CHAT_TOKEN,
    scope="GIGACHAT_API_CORP",
    verify_ssl_certs=False,  # Отключение проверки SSL-сертификатов
    profanity_check=False,  # Отключение проверки на ненормативную лексику
)


async def async_request_to_gigachat(prompt: str) -> str:
    """
    Отправляет асинхронный запрос к GigaChat и возвращает ответ.
    :param prompt: Текст запроса.
    :return: Ответ модели в виде строки.
    """
    response = await model.achat(prompt)
    return response.choices[0].message.content


async def async_get_answer(query: str, context: str) -> Tuple[Union[int, None], str]:
    """
    Обрабатывает запрос пользователя и получает ответ от GigaChat.
    :param query: Входной запрос от пользователя.
    :param context: Контекст, в котором формируется ответ.
    :return: Кортеж, содержащий числовой ответ (если применимо) и пояснение.
    """
    is_multiline = "\n" in query  # Проверяем, содержит ли запрос несколько строк
    prompt = (QUERY_PROMPT if is_multiline else PROMPT).format(query=query, context=context)

    response = await async_request_to_gigachat(prompt)  # Получаем ответ от GigaChat
    answer = int("".join(filter(str.isdigit, response))) if is_multiline else None  # Извлекаем числовое значение из ответа, если применимо
    reasoning = REASONING if is_multiline else response  # Определяем пояснение

    return answer, reasoning
