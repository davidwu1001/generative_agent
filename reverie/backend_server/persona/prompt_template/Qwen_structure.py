import openai
import os

def Qwen_request(prompt, Qwen_parameter={}):
    os.environ["HTTP_PROXY"] = ""
    os.environ["HTTPS_PROXY"] = ""
    openai.api_base = "http://10.112.189.233:8000/v1"
    openai.api_key = "none"
    response = openai.ChatCompletion.create(
        model="Qwen",
        messages=[
            {"role": "user",
             "content": prompt}
        ],
        stream=False,
        stop=[]  # You can add custom stop words here, e.g., stop=["Observation:"] for ReAct prompting.
    )
    res = response.choices[0].message.content
    print("\nfrom Qwen\n")
    return res

