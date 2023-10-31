import openai
import os
import time
import requests

def gpt_request(prompt, gpt_parameter={'engine': 'text-davinci-003', 'max_tokens': 1000, 'temperature': 0, 'top_p': 1, 'stream': False, 'frequency_penalty': 0, 'presence_penalty': 0, 'stop': None}):
    openai.api_base = "https://api.openai.com/v1/"
    openai_api_key = "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"
    openai.api_key = openai_api_key
    os.environ["HTTP_PROXY"] = "http://127.0.0.1:7890"
    os.environ["HTTPS_PROXY"] = "http://127.0.0.1:7890"
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

def Qwen_request(prompt, Qwen_parameter={}):
    openai.api_base = "http://10.112.189.233:8000/v1"
    openai.api_key = "none"
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

def baichuan_request(prompt):
    os.environ["HTTP_PROXY"] = ""
    os.environ["HTTPS_PROXY"] = ""
    url = "http://10.112.189.233:5001/baichuan2/chat"
    # time1 = time.time()
    return requests.post(url, data={"content": prompt}).text
    # print(f"baichuan time cost:{time.time() - time2}")

def get_prompt():
    prompt = "你好"
    with open("content.txt", 'r', encoding='utf-8') as f:
        prompt = f.read()
    return prompt

def save_response(title="title", prompt="", GPT_response="", Qwen_response="", Baichuan_response="",note="无备注"):
    with open("record.md", "r+",encoding='utf-8') as f:
        file_contents = f.read()
        f.seek(0)
        # 标题
        f.write(f"# {title}\n")
        # 二级标题 prompt
        f.write("**prompt**\n")
        f.write("```\n")
        f.write(f"{prompt}\n")
        f.write("```\n")
        f.write("**GPT回答**\n")
        f.write("```\n")
        f.write(f"{GPT_response}\n")
        f.write("```\n")
        f.write("**千问回答**\n")
        f.write("```\n")
        f.write(f"{Qwen_response}\n")
        f.write("```\n")
        f.write("**百川回答**\n")
        f.write("```\n")
        f.write(f"{Baichuan_response}\n")
        f.write("```\n")
        f.write("**备注**\n")
        f.write("```\n")
        f.write(f"{note}\n")
        f.write("```\n")

        f.write(file_contents)



# title="测试3"
# prompt = """
# 第一行
# 第二行
# """
# save_response(title, prompt, prompt, prompt, prompt)

# title = input("输入本次测试的说明（prompt标题）")
# note = input("输入备注：")
# command = input("输出save以保存本次结果：")
# print(title,note,type(command))

# print()

opt = 1001

gpt, qwen, baichuan = int(opt%1000/100), int(opt%100/10), int(opt%10)
if __name__ == "__main__":
    prompt = get_prompt()
    start_time = time.time()
    if gpt == 1:
        GPT_response = gpt_request(prompt)
    else:
        GPT_response = "本次不测试"
    gpt_time = time.time()
    print(f"\n-----------------------------response from gpt. cost time:{gpt_time-start_time}-----------------------------\n\n",GPT_response)
    if qwen == 1:
        Qwen_response = Qwen_request(prompt)
    else:
        Qwen_response = "本次不测试"
    qwen_time = time.time()
    print(f"\n-----------------------------response from Qwen. cost time:{qwen_time-gpt_time}-----------------------------\n\n",Qwen_response)
    if baichuan == 1:
        Baichuan_response = baichuan_request(prompt)
    else:
        Baichuan_response = "本次不测试"
    baichuan_time = time.time()
    print(f"\n-----------------------------response from Baichuan. cost time:{baichuan_time-qwen_time}-----------------------------\n\n",Baichuan_response)

    note = ""
    note += f"response from gpt. cost time:{gpt_time-start_time}\n"
    note += f"response from Qwen. cost time:{qwen_time-gpt_time}\n"
    note += f"response from Baichuan. cost time:{baichuan_time-qwen_time}\n"

    title = input("\n输入本次测试的说明（prompt标题）：")
    note_add = input("输入备注：")
    note += note_add
    command = input("输出save保存本次结果：")
    if command == "save":
        save_response(title, prompt, GPT_response, Qwen_response, Baichuan_response, note)
        print("本次结果已保存至recode.md")
    else:
        pass





