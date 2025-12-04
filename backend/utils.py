import math

# Pricing constants (USD)
WHISPER_PRICE_PER_MIN = 0.006

# GPT-4o pricing (approximate, verify current rates)
# Input: $5.00 / 1M tokens
# Output: $15.00 / 1M tokens
GPT4_INPUT_PRICE_PER_1K = 0.005  # $5/1M = $0.005/1k
GPT4_OUTPUT_PRICE_PER_1K = 0.015 # $15/1M = $0.015/1k

# Gemini 1.5 Flash pricing
# Input: $0.075 / 1M tokens
# Output: $0.30 / 1M tokens
GEMINI_INPUT_PRICE_PER_1K = 0.000075
GEMINI_OUTPUT_PRICE_PER_1K = 0.0003

def calculate_whisper_cost(duration_seconds: float) -> float:
    duration_min = duration_seconds / 60.0
    # Whisper is billed per minute, usually rounded up to nearest second or minute? 
    # OpenAI API usually bills by second but let's just use raw duration for now.
    return duration_min * WHISPER_PRICE_PER_MIN

def calculate_gpt4_cost(input_tokens: int, output_tokens: int) -> float:
    input_cost = (input_tokens / 1000.0) * GPT4_INPUT_PRICE_PER_1K
    output_cost = (output_tokens / 1000.0) * GPT4_OUTPUT_PRICE_PER_1K
    return input_cost + output_cost

def calculate_gemini_cost(input_tokens: int, output_tokens: int) -> float:
    input_cost = (input_tokens / 1000.0) * GEMINI_INPUT_PRICE_PER_1K
    output_cost = (output_tokens / 1000.0) * GEMINI_OUTPUT_PRICE_PER_1K
    return input_cost + output_cost
