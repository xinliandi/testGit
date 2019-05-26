#!/usr/bin/env python
# -*-coding:utf-8-*-
# author:weijh time:2018/9/29
import os
import csv
import codecs
import re


def get_dir(num,path):
    try:
        path_dict=os.listdir(path)
    except FileNotFoundError:
        print(num,"not exist")
        path_dict=0
    return path_dict


if __name__ == "__main__":
    target_dir1_1 = '/root/weijiahao/weijiahao/weijiahao/assert/'
    target_dir1_2 ='commons-lang-master'
    target_dir1=target_dir1_1+target_dir1_2
    # target_dir1 = '/Volumes/weijiahao/commons-math/jodatimeassert2/joda-time-master'
    target_dir2 = '/commons-lang-master/target/pit-reports'
    res_lists = []
    res_lists.append(tuple(["size","cov1","cov2"]))
    for num in range(500,16000,500):
        res_list = []
        path = target_dir1 + str(num)+target_dir2
        print(path)
        # print(path)
        path_isexist=get_dir(num,path)
        if(path_isexist!=0):
            path = path + '/' + path_isexist[0]

        filename = path + '/index.html'
        # num_str = r'/pit-reports([\s\S]*)/2018'
        # num = re.findall(num_str, filename)[0]
        # print(num)
        res_list.append(num)
        flag = 1
        # if os.path.exists(filename):
        #     print(num)

        try:
            with open(filename, 'r') as f:

                for row in f:
                    if "class=\"coverage_legend\">" in row and flag != 3:
                        flag = flag + 1
                        regex = r'class="coverage_legend">([\s\S]*)</div></div></td>'
                        match = re.findall(regex, row)
                        li = match[0].split("/")
                        res_list.append('%.2f%%' % (int(li[0]) / int(li[1]) * 100))
            # print (res_list)
            res_list = tuple(res_list)
            res_lists.append(res_list)
        except FileNotFoundError:
            res_list.append("0")
            res_list.append("0")
            res_list = tuple(res_list)
            res_lists.append(res_list)
    de_path=target_dir1_1+'/'+target_dir1_2+'.csv'
    # print(de_path)
    file_csv = codecs.open(de_path, 'w+', 'utf-8')  # 追加
    writer = csv.writer(file_csv, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    # print (res_lists)
    for data in res_lists:
        print(data)
        writer.writerow(data)
    print("保存文件成功，处理结束")
    
