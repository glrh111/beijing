#! coding:utf-8

'''
解析xml：
参考：http://codingpy.com/article/parsing-xml-using-python/
1. 将xml文件的信息读取到内存中，保留节点属性信息
2. 将csv文案的信息读取到内存中，读取为字典，键为英文文案
3. 用xml存储的英文文案信息，匹配字典信息，写入到其他xml文件中

'''

import xml.etree.ElementTree as ET
import csv
import sys
import re
reload(sys)
sys.setdefaultencoding('utf-8')

# 英文 | 葡萄牙语 | 俄语 | 法语
multi_language_wenan = 'data/wenan.csv'

wenan_android_en = 'data/Strings_Android.xml'
wenan_ios_en = 'data/Strings_iOS.txt'

country_list = ['PT', 'RU', 'FR']

def get_xml_data(wenan):
    tree = ET.ElementTree(file=wenan_android_en)
    root = tree.getroot()

    # 新的跟节点

    for top_idx, country in enumerate(country_list):

        exec "new_root_{} = ET.Element('resources')".format(country)

        # root节点信息， root节点没有属性
        # 属性为字典

        for idx, child in enumerate(root, start=1):

            new_text_list = wenan.get(child.text, [''] * 3)
            print idx,new_text_list
            exec "new_element = ET.SubElement(new_root_{}, child.tag)".format(country)
            new_text = new_text_list[top_idx]
            new_element.text = new_text.replace('\n', ' ')
            new_element.attrib = child.attrib

        # 写
        exec "new_tree = ET.ElementTree(new_root_{})".format(country)
        new_tree.write('data/Strings_Android_{}.xml'.format(country), encoding='utf-8')

def get_ios_txt_data(wenan):
    for idx, country in enumerate(country_list):

        print idx, country, '\n\n'

        write_list = []

        pattern = re.compile(r'^".*')
        with open(wenan_ios_en, 'r') as f:
            for row in f:
                # 检测是否以引号开头
                if pattern.match(row):
                    # 如果以引号开头，使用 = 分隔
                    part_list = map(
                        lambda x: x.strip(),
                        row.split('=')
                    )
                    left_part, _ = part_list
                    # 去除左边的引号，并去除里边的空格
                    left_part_no_space = left_part[1:-1].strip()
                    # 找到对应国家的文案
                    special_wenan = wenan.get(left_part_no_space, ['']*3)[idx]
                    write_list.append(left_part + ' = "{}"'.format(special_wenan))
                else:
                    # 原样返回
                    write_list.append(row.strip())

        with open('data/Strings_iOS_{}.txt'.format(country), 'w') as f:
            f.write('\n'.join(write_list))

def read_wenan_from_csv():
    '''将多语言文案读取到字典对象中
    key: 英文文案内容  value: 其他语言的tuple
    :return:
    '''
    return_dict = {}
    with open(multi_language_wenan, 'r') as f:
        csv_reader = csv.reader(f, delimiter='|')
        for row in csv_reader:
            if row:
                return_dict[row[0]] = row[1:]
    return return_dict


def find_diff_for_android():
    '''add in 2016-12-02 by Wang Er
    找出android_diff 中，xml 里有，而android_wenan_find_diff.csv里没有的部分
    :return:
    '''
    # 读取csv
    csv_list = []
    with open('android_diff/android_wenan_find_diff.csv', 'r') as f:
        csv_reader = csv.reader(f, delimiter='|')
        for row in csv_reader:
            if row:
                csv_list.append(row[0].strip())
    # 读取xml
    tree = ET.ElementTree(file='android_diff/strings.xml')
    root = tree.getroot()

    xml_list = []
    for child in root:
        xml_list.append(child.text.strip())

    print 'xml_list length: {}'.format(len(xml_list))
    print 'csv_list length: {}'.format(len(csv_list))

    diff = set(xml_list) - set(csv_list)

    print 'diff length: {}'.format(len(diff))

    for line in diff:
        print line

if __name__ == '__main__':
    # 读取多语言文案
    # wenan = read_wenan_from_csv()
    # # 处理安卓的文案
    # get_xml_data(wenan)
    # 处理iOS的文案
    # get_ios_txt_data(wenan)

    find_diff_for_android()
