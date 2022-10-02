# 开发时间：2022/10/2  8:46
def num2alp():
    '''将阿拉伯数字映射到字母上'''
    dict_ ={}
    num = 1
    for i in range(65,91):
        dict_[num] = chr(i)
        num+=1

    print(dict_)
    return dict_

if __name__ == '__main__':
    num2alp()