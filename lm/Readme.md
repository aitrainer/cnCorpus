# 文本语料整理，用于训练LM模型

## 1. zhwiki语料

### 1.1 zhwiki abstract
```
wget https://dumps.wikimedia.org/zhwiki/20181001/zhwiki-20181001-abstract.xml.gz .

cat zhwiki-20181001-abstract.xml|python zhwiki_extract.py --tags "title|abstract" >zhwiki_abstract_pure_20181001.txt
```
### 1.2 zhwiki page


1) 下载Wiki Dump
```
wget http://download.wikipedia.com/zhwiki/latest/zhwiki-latest-pages-articles.xml.bz2
```

2) [WikiExtractor](https://github.com/attardi/wikiextractor)

这是一个抽取wiki内容的工具，是意大利人用 Python 写的一个维基百科抽取器，使用非常方便。直接使用这条命令即可完成抽取
```
bzcat zhwiki-latest-pages-articles.xml.bz2 | python WikiExtractor.py -b1000M -o extracted >output.txt
```

其中参数 -b1000M 表示以 1000M 为单位切分文件，默认是 500K。


