import math

# Pricing constants (USD)
WHISPER_PRICE_PER_MIN = 0.006

# GPT-5 (Standard) pricing
# Input: $1.25 / 1M tokens
# Output: $10.00 / 1M tokens
GPT5_INPUT_PRICE_PER_1K = 0.00125
GPT5_OUTPUT_PRICE_PER_1K = 0.01

# Gemini 2.5 Flash pricing
# Input: $0.30 / 1M tokens
# Output: $2.50 / 1M tokens
GEMINI_INPUT_PRICE_PER_1K = 0.0003
GEMINI_OUTPUT_PRICE_PER_1K = 0.0025

def calculate_whisper_cost(duration_seconds: float) -> float:
    duration_min = duration_seconds / 60.0
    # Whisper is billed per minute, usually rounded up to nearest second or minute? 
    # OpenAI API usually bills by second but let's just use raw duration for now.
    return duration_min * WHISPER_PRICE_PER_MIN

def calculate_gpt5_cost(input_tokens: int, output_tokens: int) -> float:
    # Using GPT-5 pricing as requested
    input_cost = (input_tokens / 1000.0) * GPT5_INPUT_PRICE_PER_1K
    output_cost = (output_tokens / 1000.0) * GPT5_OUTPUT_PRICE_PER_1K
    return input_cost + output_cost

def calculate_gemini_cost(input_tokens: int, output_tokens: int) -> float:
    # Using Gemini 2.5 Flash pricing
    input_cost = (input_tokens / 1000.0) * GEMINI_INPUT_PRICE_PER_1K
    output_cost = (output_tokens / 1000.0) * GEMINI_OUTPUT_PRICE_PER_1K
    return input_cost + output_cost
