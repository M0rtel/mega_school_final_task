QUERY_PROMPT = """
Вопрос: В каком рейтинге (по состоянию на 2021 год) ИТМО впервые вошёл в топ-400 мировых университетов?\n
1. ARWU (Shanghai Ranking)\n
2. Times Higher Education (THE) World University Rankings\n
3. QS World University Rankings\n
4. U.S. News & World Report Best Global Universities Ответ должен содержать только номер правильного ответа. Ответ: 2
Ответь на вопрос опираясь на данную информацию: {context}. Вопрос: {query}. Ответ должен содержать только номер правильного ответа. Ответ:"""

PROMPT = "Ответь на вопрос опираясь на данную информацию: {context}. Вопрос: {query}"

REASONING = "Из информации на сайте"
