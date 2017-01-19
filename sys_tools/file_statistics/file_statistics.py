#! /usr/bin/env python
# coding: utf-8

'''
文件夹及文件计数

folder_count 有多少文件夹
file_count 有多少文件

line_count 有多少行
character_count 有多少字符
'''

import click
import os


class FileStatisticser(object):

    def __init__(self, filename, black_list=None):
        self.filename = os.path.abspath(filename)
        self.folder_count = 0
        self.file_count = 0
        self.line_count = 0
        self.character_count = 0
        self.black_list = black_list if black_list else []
        self.main(self.filename)

    def open_folder(self, filename):
        '''打开一个文件夹，返回里边的文件列表
        文件列表中的文件，需要用全名
        :return:
        '''
        filename = os.path.abspath(filename)
        file_list = os.listdir(filename)
        return map(lambda x: os.path.join(filename, x), file_list)

    def statistics_for_file(self, filename):
        '''统计文件内的字符数量
        :param filename:
        :return:
        '''
        try:
            with open(filename, 'r') as f:
                for line in f:
                    self.line_count += 1
                    self.character_count += len(line)
        except Exception, e:
            click.secho(e.message, bg='red', fg='white')

    def is_satistied(self, filename):
        '''根据扩展名过滤
        扩展名带有 .， 所以需要截取
        :param ext_name:
        :return:
        '''
        _, ext_name = os.path.splitext(filename)
        if len(ext_name) > 1:
            ext_name = str(ext_name[1:])
            return ext_name not in self.black_list
        return True

    def main(self, filename):
        '''
        :return:
        '''
        if not os.path.exists(filename):
            return
        file_list = self.open_folder(filename)
        for sub_file in file_list:
            if os.path.isfile(sub_file) and self.is_satistied(sub_file):
                self.file_count += 1
                # 统计字符
                self.statistics_for_file(sub_file)
            elif os.path.isdir(sub_file):
                self.folder_count += 1
                # 打开文件，统计相关字符
                self.main(sub_file)
            else:
                print 'Skip ...', sub_file

    def __str__(self):
        for sub_type in ['filename', 'folder_count', 'file_count', 'line_count', 'character_count']:
            click.secho('{:>15}: <{:>5}>'.format(sub_type, getattr(self, sub_type)), fg='white', bg='green')
        return ''


@click.command()
@click.argument('filename', type=click.Path(exists=True))
def main(filename):
    '''
    :return:
    '''
    handler = FileStatisticser(filename, black_list=['pyc'])
    print handler



if __name__ == '__main__':
    main()