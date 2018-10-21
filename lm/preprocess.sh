#!/usr/bin/bash

# zhwiki abstract

wget https://dumps.wikimedia.org/zhwiki/20181001/zhwiki-20181001-abstract.xml.gz .

cat zhwiki-20181001-abstract.xml|python zhwiki_extract.py --tags "title|abstract" >zhwiki_abstract_pure_20181001.txt
