# 开发时间：2022/10/2  9:18
from cal_similarity import *

if __name__ == '__main__':
    filepath = "./res_dict/dict.txt"
    # 读取字典
    content = read_dict_file(filepath)
    # 获取字典中的键
    texts = content.keys()
    # 输入问题
    question = "今天的天气怎么样？"
    # 计算相似度
    similarities = transform(texts, question)
    # 判断最相似问题的回答 返回相似问题对应的答案
    answer = classify_answer(content, texts, similarities)
    print(f"问题：{question.strip()}\n\n回答：{answer}")