from gigachat import GigaChat
from utils.counts import QUERY_PROMPT, REASONING, PROMPT
from utils.env import env

GIGA_CHAT_TOKEN = env.str("TOKEN_GIGACHAT")

model = GigaChat(
    credentials=GIGA_CHAT_TOKEN,
    scope="GIGACHAT_API_CORP",
    verify_ssl_certs=False,
    profanity_check=False,
)


async def async_request_to_gigachat(prompt: str) -> str:
    response = await model.achat(prompt)
    return response.choices[0].message.content


async def async_get_answer(query: str, context: str) -> tuple[str, str]:
    is_multiline = "\n" in query
    prompt_template = QUERY_PROMPT if is_multiline else PROMPT
    prompt = prompt_template.format(query=query, context=context)

    response = await async_request_to_gigachat(prompt)
    if is_multiline:
        answer = "".join(filter(str.isdigit, response))
        reasoning = REASONING
    else:
        answer, reasoning = None, response

    print(f"Answer: {answer}")
    print(f"reasoning: {reasoning}")
    return answer, reasoning
