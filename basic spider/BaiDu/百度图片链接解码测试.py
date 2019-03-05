# -*- coding: utf-8 -*-
# @Author  : Silas9187
# @Email   : silas9187@gmail.com
# @blogsite  :https://blog.csdn.net/acarsar
# @GitHub    :https://github.com/silas9187
a ='ippr_z2C$qAzdH3FAzdH3Ffb_z&e3Bftgwt42_z&e3BvgAzdH3F4omlaAzdH3FaamK8iwuzy0kbFPb4D1d0&mla'
# a = '_z2C$q'
str_table = {
    '_z2C$q': ':',
    '_z&e3B': '.',
    'AzdH3F': '/',
}
"""
char_table = {
    'w': 'a',
    'k': 'b',
    'v': 'c',
    '1': 'd',
    'j': 'e',
    'u': 'f',
    '2': 'g',
    'i': 'h',
    't': 'i',
    '3': 'j',
    'h': 'k',
    's': 'l',
    '4': 'm',
    'g': 'n',
    '5': 'o',
    'r': 'p',
    'q': 'q',
    '6': 'r',
    'f': 's',
    'p': 't',
    '7': 'u',
    'e': 'v',
    'o': 'w',
    '8': '1',
    'd': '2',
    'n': '3',
    '9': '4',
    'c': '5',
    'm': '6',
    '0': '7',
    'b': '8',
    'l': '9',
    'a': '0'
}
"""
# char_table = {ord(key): ord(value) for key, value in char_table.items()}
in_table = '0123456789abcdefghijklmnopqrstuvw'
out_table = '7dgjmoru140852vsnkheb963wtqplifca'
# 将in和out中每个字符转化为各自的ascii码，返回一个字典（dict）
char_table = str.maketrans(in_table, out_table)

print('char_table:',char_table)
# for t in a:
        #解码
if True:
    for key, value in str_table.items():
            a = a.replace(key, value)
            print(a)
    a = a.translate(char_table)
    print(a,end='')


