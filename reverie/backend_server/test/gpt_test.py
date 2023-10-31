import openai
import os
import time
openai_api_key = "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"
openai.api_key = openai_api_key


def gpt_request(prompt, gpt_parameter):
    response = openai.Completion.create(
                model=gpt_parameter["engine"],
                prompt=prompt,
                temperature=gpt_parameter["temperature"],
                max_tokens=gpt_parameter["max_tokens"],
                top_p=gpt_parameter["top_p"],
                frequency_penalty=gpt_parameter["frequency_penalty"],
                presence_penalty=gpt_parameter["presence_penalty"],
                stream=gpt_parameter["stream"],
                stop=gpt_parameter["stop"],)
    return response.choices[0].text




gpt_parameter = {'engine': 'text-davinci-003', 'max_tokens': 1000, 'temperature': 0, 'top_p': 1, 'stream': False, 'frequency_penalty': 0, 'presence_penalty': 0, 'stop': None}
os.environ["HTTP_PROXY"] = "http://127.0.0.1:7890"
os.environ["HTTPS_PROXY"] = "http://127.0.0.1:7890"
with open("content.txt", 'r', encoding='utf-8') as f:
    prompt = f.read()
print(gpt_request(prompt,gpt_parameter))

