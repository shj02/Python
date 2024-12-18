# week10_05.py

import os   # 파일/폴더 존재 여부/삭제, 폴더 생성 등등
target_path = "c:\\202444040"
target_file = "sonhyeji02.txt"

if False == os.path.exists(target_path):
    print("폴더 생성"+target_path)
    os.mkdir(target_path)

target_fullfile = target_path + "\\" + target_file

scores = []
if os.path.exists(target_fullfile):
    with open(target_fullfile, 'r') as f:
        lines = f.readlines()
        for line in lines:
            #print(line.strip())
            score = line.strip().split('|')
            #print(score) : ['math, 10', 'kor, 20', 'eng, 30']
            dict_scores = {}
            
            for values in score:
                value = values.split(',')
                #print(value)
                if 2 == len(value):
                    sub = value[0] # 과목
                    s = int(value[1]) # 점수
                    dict_scores[sub] = s
            if dict_scores:
                scores.append(dict_scores)
    print(scores)
else:
    f = open(target_fullfile, 'w')
    f.close()
