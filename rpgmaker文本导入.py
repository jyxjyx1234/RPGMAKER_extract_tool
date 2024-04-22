#第一步，将翻译后的文件的内容导入到提取文本.json中，与dir相对应
#第二步，将内容按照dir写入脚本
import json
import os

yiwenpath='译文.json'
wenbenpath='提取文本.json'

yiwen=open(yiwenpath,'r',encoding='utf8')
wenben=open(wenbenpath,'r',encoding='utf8')
yiwen=json.load(yiwen)
wenben=json.load(wenben)

'''
译文文件格式
[
    {
        "index": 2,
        "name": "",
        "pre_jp": "打撃/物理",
        "post_jp": "打撃/物理",
        "pre_zh": "打击/物理",
        "proofread_zh": "",
        "trans_by": "sakura-010",
        "proofread_by": "",
        "post_zh_preview": "打击/物理"
    }
]
转化为{原文:文本}
'''
yw={}
for dic in yiwen:
    yw[dic["pre_jp"]]=dic["post_zh_preview"]



def xieru(dic):
    dir=dic['dir']
    msg=dic['message']
    dir=dir.split('.')
    res=''
    for i in dir:
        if i=='':
            continue
        elif i[0]=='{':
            res=res+'["'+i[1:]+'"]'
        elif i[0]=='[':
            res=res+'['+i[1:]+']'
        elif i[0]=='(':
            f=i[1:]
    exec(f+res+'=msg')

filenames=os.listdir('.\www\data')

for filename in filenames:
    file=open('.\www\data_back\\'+filename,'r',encoding='utf8')
    exec(filename[:-5]+'=json.load(file)')

for dic in wenben:
    if dic["message"] in yw:
        dic["message"]=yw[dic["message"]]
    xieru(dic)

for filename in filenames:
    with open('.\www\data\\'+filename,'w',encoding='utf8') as file:
        json.dump(eval(filename[:-5]),file,ensure_ascii=False,indent=4)