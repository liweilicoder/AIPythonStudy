import os

from openai import OpenAI
from dotenv import load_dotenv

# Get the OpenAI API key from the .env file
load_dotenv('.env', override=True)

# Model config mapping
MODEL_CONFIG = {
    'glm': {
        'api_key': 'ARK_API_KEY',
        'base_url': 'ARK_BASE_URL',
        'model': 'GLM_MODEL',
    },
    'doubao': {
        'api_key': 'ARK_API_KEY',
        'base_url': 'ARK_BASE_URL',
        'model': 'DOUBAO_MODEL',
    },
    'minimax': {
        'api_key': 'MINIMAX_API_KEY',
        'base_url': 'MINIMAX_BASE_URL',
        'model': 'MINIMAX_MODEL',
    },
}


def print_llm_response(prompt, model='minimax', thinking_enabled=False):
    llm_response = get_llm_response(prompt, model, thinking_enabled)
    print(llm_response)


def get_llm_response(prompt, model='minimax', thinking_enabled=False):
    """This function takes as input a prompt and a model name,
    and passes it to the specified model. The function then saves
    the response of the model as a string.

    Args:
        prompt: A string enclosed in quotation marks.
        model: One of 'glm', 'doubao', or 'minimax'. Defaults to 'doubao'.
        thinking_enabled: Whether to enable model thinking/reasoning. Defaults to False.
    """
    try:
        if not isinstance(prompt, str):
            raise ValueError("Input must be a string enclosed in quotes.")

        if model not in MODEL_CONFIG:
            raise ValueError(f"Model must be one of: {list(MODEL_CONFIG.keys())}")

        config = MODEL_CONFIG[model]
        api_key = os.getenv(config['api_key'])
        base_url = os.getenv(config['base_url'])
        model_name = os.getenv(config['model'])

        client = OpenAI(api_key=api_key, base_url=base_url)

        extra_body = {}
        if not thinking_enabled:
            extra_body["thinking_enabled"] = False

        completion = client.chat.completions.create(
            model=model_name,
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful but terse AI assistant who gets straight to the point.",
                },
                {"role": "user", "content": prompt.strip()},
            ],
            temperature=0.0,
            extra_body=extra_body if extra_body else None,
        )
        response = completion.choices[0].message.content.strip()

        if not thinking_enabled:
            import re
            # Remove thinking tags like <thinking>...</thinking> or <think>...</think>
            response = re.sub(r'<thinking>.*?</thinking>', '', response, flags=re.DOTALL)
            response = re.sub(r'<think>.*?</think>', '', response, flags=re.DOTALL)
            # Remove blank lines left behind
            response = re.sub(r'\n{3,}', '\n\n', response)
            response = response.strip()

        return response

    except TypeError as e:
        print("Error:", str(e))


# Backward compatibility aliases
def print_llm_response_glm(prompt, thinking_enabled=False):
    print_llm_response(prompt, 'glm', thinking_enabled)


def get_llm_response_glm(prompt, thinking_enabled=False):
    return get_llm_response(prompt, 'glm', thinking_enabled)


def print_llm_response_doubao(prompt, thinking_enabled=False):
    print_llm_response(prompt, 'doubao', thinking_enabled)


def get_llm_response_doubao(prompt, thinking_enabled=False):
    return get_llm_response(prompt, 'doubao', thinking_enabled)


def print_llm_response_minimax(prompt, thinking_enabled=False):
    print_llm_response(prompt, 'minimax', thinking_enabled)


def get_llm_response_minimax(prompt, thinking_enabled=False):
    return get_llm_response(prompt, 'minimax', thinking_enabled)