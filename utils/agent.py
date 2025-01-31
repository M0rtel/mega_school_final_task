from gigachat import GigaChat
from utils.env import env

GIGA_CHAT_TOKEN = env.str('TOKEN_GIGACHAT')

model = GigaChat(
    credentials=GIGA_CHAT_TOKEN,
    scope="GIGACHAT_API_CORP",
    verify_ssl_certs=False,
    profanity_check=False,
)


def request_to_gigachat(prompt: str) -> str:
    response = model.chat(prompt)
    return response.choices[0].message.content


def get_answer(query: str, context: str) -> tuple[str]:
    if "\n" in query:
        prompt = f"Ответь на вопрос опираясь на данную информацию: {context}. Вопрос: {query}. Ответ должен содержать только номер правильного ответа"
        answer = "".join([symbol for symbol in request_to_gigachat(prompt) if symbol.isdigit()])
        reasoning = "Из информации на сайте"

    else:
        prompt = f"Ответь на вопрос опираясь на данную информацию: {context}. Вопрос: {query}"
        answer = None
        reasoning = request_to_gigachat(prompt)

    return answer, reasoning
