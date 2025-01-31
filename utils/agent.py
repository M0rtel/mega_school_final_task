from gigachat import GigaChat

from utils.counts import QUERY_PROMPT, REASONING, PROMPT
from utils.env import env

GIGA_CHAT_TOKEN = env.str('TOKEN_GIGACHAT')

model = GigaChat(
    credentials=GIGA_CHAT_TOKEN,
    scope="GIGACHAT_API_CORP",
    verify_ssl_certs=False,
    profanity_check=False,
)


async def async_request_to_gigachat(prompt: str) -> str:
    response = await model.achat(prompt)
    return response.choices[0].message.content


async def async_get_answer(query: str, context: str) -> tuple[str]:
    if "\n" in query:
        prompt = QUERY_PROMPT.format(query=query, context=context)
        answer = await async_request_to_gigachat(prompt)
        answer = "".join([symbol for symbol in answer if symbol.isdigit()])
        reasoning = REASONING

    else:
        prompt = PROMPT.format(query=query, context=context)
        answer = None
        reasoning = await async_request_to_gigachat(prompt)

    return answer, reasoning
