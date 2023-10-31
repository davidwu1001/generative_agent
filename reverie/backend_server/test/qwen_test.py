import openai
import os
import time
openai.api_base = "http://10.112.189.233:8000/v1"
openai.api_key = "none"

def Qwen_request(prompt, Qwen_parameter={}):
    os.environ["HTTP_PROXY"] = ""
    os.environ["HTTPS_PROXY"] = ""
    time1 = time.time()
    response = openai.ChatCompletion.create(
        model="Qwen",
        messages=[
            {"role": "user",
             "content": prompt}
        ],
        stream=False,
        stop=[]  # You can add custom stop words here, e.g., stop=["Observation:"] for ReAct prompting.
    )
    return response.choices[0].message.content


with open("content.txt", 'r', encoding='utf-8') as f:
    prompt = f.read()
Qwen_request = Qwen_request(prompt)
print("\nQwen_request:111\n",Qwen_request)


