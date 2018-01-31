#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import pysolr
import json


# def search_data():
#     url = 'http://10.9.18.121:8008/solr/talk/select?q=*:*&wt=json&indent=true'
#     r = requests.get(url, verify=False)
#     f = open('/Volumes/sunyf/syf_worker/sensitiveWord.txt', 'r')
#     print r.text
#     r = r.json()['response']['numFound']
#     print str(r)


#pysolr客户端
def search_data():
    url = 'http://172.16.0.157:8008/solr/question/'
    solr = pysolr.Solr(url, timeout=10)
    dict = {'start': 0, 'rows': 1}
    result = solr.search('*:*', **dict)
    f = open('/Volumes/sunyf/syf_worker/question_156.txt', 'w')
    f1 = open('/Volumes/sunyf/syf_worker/sensitiveWord.txt', 'w')
    # result = solr.search('title:视频')
    # print result.raw_response['response']['numFound']
    data = result.raw_response['response']
    #f.write(str(data))
    print data


#
#     # for item in result:
#     #     print 'keyword: %s' % item['keyword']
#     #     print 'title: %s' % item['title']
#     #     print 'source: %s' % item['source']
#     #     print 'link: %s' % item['link']
#     #     print '


search_data()