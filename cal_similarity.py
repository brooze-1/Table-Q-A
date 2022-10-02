# 开发时间：2022/8/6  13:24
# [Python+gensim-文本相似度分析（小白进）](https://blog.csdn.net/Yellow_python/article/details/81021142)
from gensim.similarities import SparseMatrixSimilarity
from gensim.corpora import Dictionary
from gensim.models import TfidfModel
from jieba import lcut
import jieba

jieba.setLogLevel(jieba.logging.INFO)

def read_dict_file(filepath):
    '''读取字典文件，并以字典的数据格式返回'''
    f = open(filepath,"r+",encoding="utf-8")
    content = eval(f.read())
    f.close()
    return content

def transform(texts,keyword):
    '''对文本进行转换并且计算keyword与texts的相似度'''
    # 1、将【文本集】生成【分词列表】
    texts = [lcut(text) for text in texts]
    # 2、基于文本集建立【词典】，并获得词典特征数
    dictionary = Dictionary(texts)
    num_features = len(dictionary.token2id)
    # 3.1、基于词典，将【分词列表集】转换成【稀疏向量集】，称作【语料库】
    corpus = [dictionary.doc2bow(text) for text in texts]
    # 3.2、同理，用【词典】把【搜索词】也转换为【稀疏向量】
    kw_vector = dictionary.doc2bow(lcut(keyword))
    # 4、创建【TF-IDF模型】，传入【语料库】来训练
    tfidf = TfidfModel(corpus)
    # 5、用训练好的【TF-IDF模型】处理【被检索文本】和【搜索词】
    tf_texts = tfidf[corpus]  # 此处将【语料库】用作【被检索文本】
    tf_kw = tfidf[kw_vector]
    # 6、相似度计算
    sparse_matrix = SparseMatrixSimilarity(tf_texts, num_features)
    similarities = sparse_matrix.get_similarities(tf_kw)
    # for e, s in enumerate(similarities):
        # print('kw 与 text%d 相似度为：%.2f' % (e, s))

    return similarities

def classify_answer(content,texts,similarities):
    '''根据相似度 选择合适的答案'''
    # temp列表用于存储所有的相似度
    temp = []
    for e, s in enumerate(similarities):
        temp.append(s)

    # 取出最大的相似度
    max_rate = max(temp)
    # 获得最大相似度再temp中的索引
    index = temp.index(max_rate)

    # 将texts转换为列表
    texts = list(texts)
    # 根据index索引出键
    key = texts[index]
    # print("key:",key)
    # 通过键值对获取answer
    answer = content[key]
    # print("value:",answer)
    return answer



if __name__=="__main__":
    filepath = "./res_dict/dict.txt"
    # 读取字典
    content = read_dict_file(filepath)
    # 获取字典中的键
    texts = content.keys()
    # 输入问题
    question = "张三的语文成绩？"
    # 计算相似度
    similarities = transform(texts, question)
    # 判断最相似问题的回答 返回相似问题对应的答案
    answer = classify_answer(content, texts, similarities)
    print(f"问题：{question.strip()}\n\n回答：{answer}")

    # while True:
    #     question = input("客户：")
    #     # 计算相似度
    #     similarities = transform(texts, question)
    #     answer = classify_answer(content, texts, similarities)
    #     print(f"客服：{answer}\n")

