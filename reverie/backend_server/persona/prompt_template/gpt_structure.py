"""
Author: Joon Sung Park (joonspk@stanford.edu)

File: gpt_structure.py
Description: Wrapper functions for calling OpenAI APIs.
"""
import json
import random

import numpy as np
import openai
import time 
import os
from text2vec import SentenceModel
from transformers import pipeline

from utils import *
openai.api_key = openai_api_key

all_prompt_file_path = '/data/wcc/generative_agent/reverie/backend_server/all_prompt.txt'
wrong_prompt_file_path = '/data/wcc/generative_agent/reverie/backend_server/wrong_prompt.txt'
def save_to_txt(prompt, wrong_prompt_file_path=wrong_prompt_file_path):
  with open(wrong_prompt_file_path, 'a+') as f:
    f.write(prompt+"\n----------------------------------------------------------[PROMPT]----------------------------------------------------------\n")
def Qwen_request(prompt, Qwen_parameter={}):
  os.environ["HTTP_PROXY"] = ""
  os.environ["HTTPS_PROXY"] = ""
  openai.api_base = "http://10.161.39.11:8001/v1"
  openai.api_key = "none"
  response = openai.ChatCompletion.create(
    model="Qwen",
    messages=[
      {"role": "user",
       "content": prompt}
    ],
    stream=False,
    stop=[]
  )
  res = response.choices[0].message.content
  print(f"\nfrom Qwen: \n{res}\n")
  return res


def temp_sleep(seconds=0.1):
  time.sleep(seconds)

def ChatGPT_single_request(prompt):
  temp_sleep()

  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}]
  )
  return completion["choices"][0]["message"]["content"]


# ============================================================================
# #####################[SECTION 1: CHATGPT-3 STRUCTURE] ######################
# ============================================================================

def GPT4_request(prompt):
  """
  Given a prompt and a dictionary of GPT parameters, make a request to OpenAI
  server and returns the response.
  ARGS:
    prompt: a str prompt
    gpt_parameter: a python dictionary with the keys indicating the names of
                   the parameter and the values indicating the parameter
                   values.1
  RETURNS:
    a str of GPT-3's response.
  """
  temp_sleep()

  try:
    completion = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}]
    )
    return completion["choices"][0]["message"]["content"]

  except:
    print ("ChatGPT ERROR")
    return "ChatGPT ERROR"


def ChatGPT_request(prompt):
  """
  Given a prompt and a dictionary of GPT parameters, make a request to OpenAI
  server and returns the response.
  ARGS:
    prompt: a str prompt
    gpt_parameter: a python dictionary with the keys indicating the names of
                   the parameter and the values indicating the parameter
                   values.
  RETURNS:
    a str of GPT-3's response.
  """
  # temp_sleep()
  try:
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}]
    )
    return completion["choices"][0]["message"]["content"]

  except:
    print ("ChatGPT ERROR")
    return "ChatGPT ERROR"


def GPT4_safe_generate_response(prompt,
                                   example_output,
                                   special_instruction,
                                   repeat=3,
                                   fail_safe_response="error",
                                   func_validate=None,
                                   func_clean_up=None,
                                   verbose=False):
  prompt = 'GPT-3 Prompt:\n"""\n' + prompt + '\n"""\n'
  prompt += f"Output the response to the prompt above in json. {special_instruction}\n"
  prompt += "Example output json:\n"
  prompt += '{"output": "' + str(example_output) + '"}'

  if verbose:
    print ("CHAT GPT PROMPT")
    print (prompt)

  for i in range(repeat):

    try:
      curr_gpt_response = GPT4_request(prompt).strip()
      end_index = curr_gpt_response.rfind('}') + 1
      curr_gpt_response = curr_gpt_response[:end_index]
      curr_gpt_response = json.loads(curr_gpt_response)["output"]

      if func_validate(curr_gpt_response, prompt=prompt):
        return func_clean_up(curr_gpt_response, prompt=prompt)

      if verbose:
        print ("---- repeat count: \n", i, curr_gpt_response)
        print (curr_gpt_response)
        print ("~~~~")

    except:
      pass

  return False


def ChatGPT_safe_generate_response(prompt,
                                   example_output,
                                   special_instruction,
                                   repeat=3,
                                   fail_safe_response="error",
                                   func_validate=None,
                                   func_clean_up=None,
                                   verbose=False):
  # prompt = 'GPT-3 Prompt:\n"""\n' + prompt + '\n"""\n'
  prompt = '"""\n' + prompt + '\n"""\n'
  prompt += f"Output the response to the prompt above in json. {special_instruction}\n"
  prompt += "Example output json:\n"
  prompt += '{"output": "' + str(example_output) + '"}'

  if verbose:
    print ("~~~ prompt    ----------------------------------------------------")
    print (prompt)

  for i in range(repeat):

    try:
      # curr_gpt_response = ChatGPT_request(prompt).strip()
      curr_gpt_response = Qwen_request(prompt)
      end_index = curr_gpt_response.rfind('}') + 1
      curr_gpt_response = curr_gpt_response[:end_index]
      curr_gpt_response = json.loads(curr_gpt_response)["output"]

      # print ("---ashdfaf")
      # print (curr_gpt_response)
      # print ("000asdfhia")

      if func_validate(curr_gpt_response, prompt=prompt):
        return func_clean_up(curr_gpt_response, prompt=prompt)

      if verbose:
        print ("---- repeat count: \n", i, curr_gpt_response)
        print (curr_gpt_response)
        print ("~~~~")

    except:
      pass

  print("---------------------此处触发安全机制，log已写入wrong_prompt.txt")
  save_to_txt(prompt=prompt)
  return fail_safe_response


def ChatGPT_safe_generate_response_OLD(prompt,
                                   repeat=3,
                                   fail_safe_response="error",
                                   func_validate=None,
                                   func_clean_up=None,
                                   verbose=False):
  if verbose:
    print ("~~~ prompt    ----------------------------------------------------")
    print (prompt)

  for i in range(repeat):
    try:
      curr_gpt_response = Qwen_request(prompt).strip()
      if func_validate(curr_gpt_response, prompt=prompt):
        return func_clean_up(curr_gpt_response, prompt=prompt)
      if verbose:
        print (f"---- repeat count: {i}")
        print (curr_gpt_response)
        print ("~~~~")

    except:
      pass
  print("---------------------此处触发安全机制，log已写入wrong_prompt.txt")
  save_to_txt(prompt=prompt)
  return fail_safe_response


# ============================================================================
# ###################[SECTION 2: ORIGINAL GPT-3 STRUCTURE] ###################
# ============================================================================

def GPT_request(prompt, gpt_parameter):
  """
  Given a prompt and a dictionary of GPT parameters, make a request to OpenAI
  server and returns the response.
  ARGS:
    prompt: a str prompt
    gpt_parameter: a python dictionary with the keys indicating the names of
                   the parameter and the values indicating the parameter
                   values.
  RETURNS:
    a str of GPT-3's response.
  """
  temp_sleep()
  try:
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
  except:
    print ("TOKEN LIMIT EXCEEDED")
    return "TOKEN LIMIT EXCEEDED"


def generate_prompt(curr_input, prompt_lib_file):
  """
  Takes in the current input (e.g. comment that you want to classifiy) and
  the path to a prompt file. The prompt file contains the raw str prompt that
  will be used, which contains the following substr: !<INPUT>! -- this
  function replaces this substr with the actual curr_input to produce the
  final promopt that will be sent to the GPT3 server.
  ARGS:
    curr_input: the input we want to feed in (IF THERE ARE MORE THAN ONE
                INPUT, THIS CAN BE A LIST.)
    prompt_lib_file: the path to the promopt file.
  RETURNS:
    a str prompt that will be sent to OpenAI's GPT server.
  """
  if type(curr_input) == type("string"):
    curr_input = [curr_input]
  curr_input = [str(i) for i in curr_input]

  f = open(prompt_lib_file, "r")
  prompt = f.read()
  f.close()
  for count, i in enumerate(curr_input):
    prompt = prompt.replace(f"!<INPUT {count}>!", i)
  if "<commentblockmarker>###</commentblockmarker>" in prompt:
    prompt = prompt.split("<commentblockmarker>###</commentblockmarker>")[1]
  return prompt.strip()


def safe_generate_response(prompt,
                           gpt_parameter,
                           repeat=5,
                           fail_safe_response="error",
                           func_validate=None,
                           func_clean_up=None,
                           verbose=False):
  if verbose:
    print (prompt)

  for i in range(repeat):
    # curr_gpt_response = GPT_request(prompt, gpt_parameter)
    curr_gpt_response = Qwen_request(prompt, gpt_parameter)
    if func_validate(curr_gpt_response, prompt=prompt):
      return func_clean_up(curr_gpt_response, prompt=prompt)
    if verbose:
      print ("---- repeat count: ", i, curr_gpt_response)
      print (curr_gpt_response)
      print ("~~~~")
  print("---------------------此处触发安全机制，log已写入wrong_prompt.txt")
  save_to_txt(prompt=prompt)
  return fail_safe_response

def safe_generate_response_gpt(prompt,
                           gpt_parameter,
                           repeat=5,
                           fail_safe_response="error",
                           func_validate=None,
                           func_clean_up=None,
                           verbose=False):
  if verbose:
    print (prompt)

  for i in range(repeat):
    curr_gpt_response = GPT_request(prompt, gpt_parameter)
    # curr_gpt_response = Qwen_request(prompt, gpt_parameter)
    if func_validate(curr_gpt_response, prompt=prompt):
      return func_clean_up(curr_gpt_response, prompt=prompt)
    if verbose:
      print ("---- repeat count: ", i, curr_gpt_response)
      print (curr_gpt_response)
      print ("~~~~")
  print("---------------------此处触发安全机制，log已写入wrong_prompt.txt")
  save_to_txt(prompt=prompt)
  return fail_safe_response

# def get_embedding(text, model="text-embedding-ada-002"):
#   os.environ["HTTP_PROXY"] = "http://127.0.0.1:7890"
#   os.environ["HTTPS_PROXY"] = "http://127.0.0.1:7890"
#   text = text.replace("\n", " ")
#   if not text:
#     text = "this is blank"
#   vector = openai.Embedding.create(
#           input=[text], model=model)['data'][0]['embedding']
#   return vector

# def get_embedding(text, model="shibing624/text2vec-base-multilingual"):
#   # os.environ["HTTP_PROXY"] = "http://127.0.0.1:7895"
#   # os.environ["HTTPS_PROXY"] = "http://127.0.0.1:7895"
#   text = text.replace("\n", " ")
#   if not text:
#     text = "this is blank"
#   print("待嵌入文本："+text)
#   # todo wcc 为了跑下去 只能扩充至1536维和之前的数据维度保持一致
#   m = SentenceModel(model_name_or_path=model)
#   vector = m.encode(text)
#   expanded_vector = np.zeros(1536)
#   expanded_vector[:len(vector)] = vector
#   return list(expanded_vector)
def get_embedding(text, model="shibing624/text2vec-base-multilingual"):
  # os.environ["HTTP_PROXY"] = "http://127.0.0.1:7895"
  # os.environ["HTTPS_PROXY"] = "http://127.0.0.1:7895"
  text = text.replace("\n", " ")
  if not text:
    text = "this is blank"
  print("待嵌入文本："+text)
  pipe = pipeline("feature-extraction", model="princeton-nlp/sup-simcse-roberta-large")
  return list(np.mean(np.array(pipe(text)[0]), axis=0))  # 1024维



if __name__ == '__main__':
  gpt_parameter = {"engine": "text-davinci-003", "max_tokens": 50,
                   "temperature": 0, "top_p": 1, "stream": False,
                   "frequency_penalty": 0, "presence_penalty": 0,
                   "stop": ['"']}
  curr_input = ["driving to a friend's house"]
  prompt_lib_file = "prompt_template/test_prompt_July5.txt"
  prompt = generate_prompt(curr_input, prompt_lib_file)

  def __func_validate(gpt_response):
    if len(gpt_response.strip()) <= 1:
      return False
    if len(gpt_response.strip().split(" ")) > 1:
      return False
    return True
  def __func_clean_up(gpt_response):
    cleaned_response = gpt_response.strip()
    return cleaned_response

  output = safe_generate_response(prompt,
                                 gpt_parameter,
                                 5,
                                 "rest",
                                 __func_validate,
                                 __func_clean_up,
                                 True)

  print (output)



















