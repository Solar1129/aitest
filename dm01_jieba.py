import jieba
import jieba.posseg as pseg

def dm01_jieba_base():

    content = "传智教育是一家上市公司，旗下有黑马程序员品牌。我是在黑马这里学习人工智能"
    # 1 精确模式：按照词法句法句意，精确的把词给分开 # 默认方式
    # def cut(self, sentence, cut_all=False, HMM=True, use_paddle=False):
    myobj1 = jieba.cut(sentence=content, cut_all=False)
    print('myobj1-->', myobj1)

    mydata1 = jieba.lcut(sentence=content, cut_all=False)
    print('mydata1-->', mydata1)

    # 2 全词模式：把句子中所有的可以成词的词语都扫描出来, 速度非常快，但是不能消除歧义
    myobj2 = jieba.cut(sentence=content, cut_all=True)
    print('myobj2-->', myobj2)

    mydata2 = jieba.lcut(sentence=content, cut_all=True)
    print('mydata2-->', mydata2)

    # 3 搜索引擎模式分词: 在精确模式的基础之上，对长词再切分 适合做搜索
    myobj3 = jieba.cut_for_search(sentence=content)
    print('myobj3-->', myobj3)

    mydata3 = jieba.lcut_for_search(sentence=content)
    print('mydata3-->', mydata3)
    pass


def  dm02_jieba_base():
    content = "煩惱即是菩提，我暫且不提"
    mydata = jieba.lcut(content)  #   精确模式
    print('mydata-->', mydata)
    pass


def  dm03_test_load_userdict():
    # 1 不用
    content = "传智教育是一家上市公司，旗下有黑马程序员品牌。我是在黑马这里学习人工智能"
    # content = "上市"
    # 1 精确模式：按照词法句法句意，精确的把词给分开 # 默认方式
    mydata1 = jieba.lcut(sentence=content, cut_all=False)
    print('mydata1-->', mydata1)

    # 2 使用
    jieba.load_userdict('./userdict.txt')
    mydata2 = jieba.lcut(sentence=content, cut_all=False)
    print('mydata2--->', mydata2)
    pass


def dm04_test_pseg():
    mydata = pseg.lcut("我爱北京天安门")
    print('mydata-->', mydata)
    pass


if __name__ == '__main__':
    # dm01_jieba_base()
    # dm02_jieba_base()
    dm03_test_load_userdict()
    # dm04_test_pseg()
    print('结巴分词 End')