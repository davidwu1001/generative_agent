

"""
对话连贯性：
用语义相似度算法计算相邻回复的语义相似度

主题分析：
主题建模技术，如LDA对对话历史进行主题分析，确保模型能够正确抽取和理解对话的主题
抽取摘要，于千问的摘要做对比

上下文一致性分析：
对比每一轮对话历史中提到的实体、主题或关键信息
实体分析

"""
from text2vec import SentenceModel
from sklearn.metrics.pairwise import cosine_similarity
from data import get_all_generate_data
import os
def set_proxy():
    os.environ["HTTP_PROXY"] = "http://127.0.0.1:7890"
    os.environ["HTTPS_PROXY"] = "http://127.0.0.1:7890"

def get_embedding(text, model="shibing624/text2vec-base-multilingual"):
  text = text.replace("\n", " ")
  if not text:
    text = "this is blank"
  m = SentenceModel(model_name_or_path=model)
  vector = m.encode(text)
  return list(vector)


def context_consistency_evaluation():
    pass

def conversation_coherence_evaluation(conversations):
    """
    对话连贯性评估
    对于n轮对话，计算相邻回复的语义相似度
    Args:
        conversations: [[string]]
    Returns:
        对话连贯性得分
    """
    average_similarity = 0
    for conv in conversations:
        conv_num = len(conv)
        if conv_num > 1:
            conv_vector = [get_embedding(text) for text in conv]
            conv_similarity = cosine_similarity(conv_vector, conv_vector)
            # 求平均相似度
            average_similarity += sum([conv_similarity[i][i + 1] for i in range(conv_num - 1)])/(conv_num - 1)
    return round(average_similarity/len(conversations), 3)

def test():
    conversation = [["How's the weather today?",
    "I recently learned to play the guitar.",
    "Do you like sushi?",
    "I'm planning a trip to the mountains.",
    "Have you ever tried bungee jumping?",
    "What's your favorite book?",
    "I just adopted a pet rabbit.",
    "I'm thinking of starting a podcast."]]
    print(conversation_coherence_evaluation(conversation))
    exit()
def topic_con():
    pass

if __name__ == "__main__":
    set_proxy()

    # test()k'j
    """
    GPT： July1_the_ville_isabella_maria_klaus-step-3-21
    Qwen: 25_February_13_2023_07_46_00
    """
    datas = get_all_generate_data("25_February_13_2023_07_46_00")
    conversations = [data['conversation'] for data in datas if data['conversation']]
    print(conversation_coherence_evaluation(conversations))
