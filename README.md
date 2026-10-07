# Token Carbon Counter

A Python CLI tool that analyzes a prompt and reports:
- Token count
- Estimated API cost
- Estimated CO₂ equivalent
- Potentially wasteful prompt patterns

## Features

The program uses `tiktoken` to tokenize the user's prompt and checks for potentially wasteful patterns, including:
- Prompts over 500 tokens
- Consecutive repeated words
- Characters repeated three or more times

## Model and Pricing

Model: OpenAI GPT-5.6 Luna

Input price: $0.20 per 1,000,000 tokens

Date consulted: October 6, 2026

Source: [OpenAI API Pricing](https://developers.openai.com/api/docs/pricing)

Estimated cost is calculated using:

`(input tokens / 1,000,000) × input price`

## CO₂ Estimate

The program uses an estimated carbon intensity of:

`0.5 mg CO₂ per token`

Estimated emissions are calculated using:

`number of tokens × 0.5 mg CO₂`

Source: [The Real Carbon Cost of an AI Token](https://ditchcarbon.com/blog/llm-carbon-emissions)

This is an estimate. Actual emissions can vary depending on the model, hardware, data center, and electricity source.

## Installation

Install the required dependency:

```bash
pip install -r requirements.txt
```

## Run
python3 token_counter.py

##Examples 
(screenshots/regular.png)
(screenshots/char.png)
(screenshots/repeat.png)




