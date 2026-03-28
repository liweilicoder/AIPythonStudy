# import gradio as gr
import os

from openai import OpenAI
from dotenv import load_dotenv

import random

# Get the OpenAI API key from the .env file
load_dotenv('.env', override=True)
openai_api_key = os.getenv('ARK_API_KEY')
base_url = os.getenv('ARK_BASE_URL')

#model
doubao_model = os.getenv('ARK_MODEL')
glm_model = os.getenv('GLM_MODEL')

# Set up the OpenAI client
client = OpenAI(api_key=openai_api_key, base_url=base_url)


def print_llm_response_glm(prompt):
    llm_response = get_llm_response_glm(prompt)
    print(llm_response)

def get_llm_response_glm(prompt):
    """This function takes as input a prompt, which must be a string enclosed in quotation marks,
    and passes it to GLM model. The function then saves the response of the model as
    a string.
    """
    try:
        if not isinstance(prompt, str):
            raise ValueError("Input must be a string enclosed in quotes.")

        completion = client.chat.completions.create(
            model=glm_model,
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful but terse AI assistant who gets straight to the point.",
                },
                {"role": "user", "content": prompt.strip()},
            ],
            temperature=0.0,
            # GLM web_search 工具需通过 tools 参数传递（可选）
            tools=[{
                "type": "function",
                "function": {
                    "name": "web_search",
                    "parameters": {"max_keyword": 2}
                }
            }] if "glm" in glm_model.lower() else None
        )

        # 提取响应文本（核心修复：获取真正的回复内容）
        response_text = completion.choices[0].message.content.strip()
        return response_text

    except TypeError as e:
        print("Error:", str(e))





def print_llm_response_doubao(prompt):
    """This function takes as input a prompt, which must be a string enclosed in quotation marks,
    and passes it to OpenAI's GPT3.5 model. The function then prints the response of the model.
    """
    llm_response = get_llm_response_doubao(prompt)
    print(llm_response)


def get_llm_response_doubao(prompt):
    """This function takes as input a prompt, which must be a string enclosed in quotation marks,
    and passes it to OpenAI's GPT3.5 model. The function then saves the response of the model as
    a string.
    """
    try:
        if not isinstance(prompt, str):
            raise ValueError("Input must be a string enclosed in quotes.")
        completion = client.chat.completions.create(
            model=doubao_model,
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful but terse AI assistant who gets straight to the point.",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=0.0,
        )
        response = completion.choices[0].message.content
        return response
    except TypeError as e:
        print("Error:", str(e))


def get_chat_completion(prompt, history):
    history_string = "\n\n".join(["\n".join(turn) for turn in history])
    prompt_with_history = f"{history_string}\n\n{prompt}"
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful but terse AI assistant who gets straight to the point.",
            },
            {"role": "user", "content": prompt_with_history},
        ],
        temperature=0.0,
    )
    response = completion.choices[0].message.content
    return response
