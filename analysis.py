import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def run_smc_analysis():
    prompt = """
Ты — профессиональный трейдер по Smart Money Concepts. 
Проанализируй BTCUSDT на D1, H1, M15. 
Определи направление тренда, BOS/CHOCH, ликвидность, имбалансы, order blocks.
Дай торговый план: Entry, SL, TP.
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["choices"][0]["message"]["content"]
