# -*- coding: utf-8 -*-
import re
pat_season = re.compile(r'하스스톤 등급전 (.+)년 (.+)월 시즌 (.+)')
pat_expansion = re.compile(r'(.+) 출시되었습니다!')
def check_season(title):
    match = pat_season.match(title)
    if match:
        return [ match.group(i) for i in range(1,4)]
    else:
        return False

def check_expansion(title):
    match = pat_expansion.match(title)
    if match:
        return match.group(1)
    else:
        return False

from os.path import isfile
from os import remove, listdir
import json

save_folder = 'data/'
save_format = '.md'
data_folder = '../crawler/data/'
data_format = '.json'

def save(season, expansion):
    file = save_folder + 'content' + save_format
    if isfile(file): remove(file)
    with open(file, 'a') as f:
        f.write('\n# Seasons\n')
        for s in season:
            f.write('- ' + "{} / {}년 {}월\n".format(s[2][2:],s[0],s[1]))
        f.write('\n# Expansion\n')
        for e in expansion:
            f.write('- ' + "{} 출시!\n".format(e))

def load():
    data = []
    for n in listdir(data_folder):
        with open(data_folder + n, 'r') as f:
            try:
                d = json.load(f)
            except:
                d = {'title': '', 'text': '', 'href': ''}
        data.append(d)
    return data

def parse(data):
    season = []
    expansion = []
    for d in data:
        title = d['title'].replace('\n', '')
        check = check_season(title)
        if check: 
            season.append(check)
        check = check_expansion(title)
        if check: 
            expansion.append(check)
    save(season, expansion)

if __name__ == '__main__':
    data = load()
    parse(data)
