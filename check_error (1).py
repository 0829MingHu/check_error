import json
import jsonpath
import pandas as pd
import os,sys
import itertools
from collections import Counter

js =json.load(open(r"H:\data-update\0-18443label.json"))
video_path ='./video_path'
clip_path = './clip_path'

def getallpic(path):
    ALLFILEPATH = []
    for x in os.walk('./'):
        res = list(
            filter(lambda x: x.lower().endswith(('.mp4',)), map(lambda y: '/'.join(y), itertools.product(
                *([x[0]], x[-1])))))
        if res != []:
            ALLFILEPATH.extend(res)
    return ALLFILEPATH



video_id_df = list(js.keys())
video_id_vd_path = [x.split('.')[0] for x in getallpic(video_path)]
video_id_clip_path = [x.split('.')[0] for x in getallpic(clip_path)]
video_id_clip_path_unique = {'_'.join(x[::-1].split('_')[1:])[::-1] if len(x.split('_'))!=1 else x.split('.')[0] for x in video_id_clip_path}
video_id_clip_path_count = ['_'.join(x[::-1].split('_')[1:])[::-1]  if len(x.split('_'))!=1 else x.split('.')[0] for x in video_id_clip_path]
video_id_clip_path_count = Counter(video_id_clip_path_count)
count_df = {key:len(js[key]['annotations']) for key in js.keys()}

errorlist=[]
for key in video_id_df:
    try:
        video_id_clip_path_count[key]
    except:
        errorlist.append(key)
        continue
    if count_df[key]!=video_id_clip_path_count[key]:
        errorlist.append(key)



# print('缺少的video-json文件中有但video_path没有的：',set(video_id_df) - set(video_id_vd_path))
# # print('缺少的clip-json文件中有但clip_path没有的：',set(video_id_df) - set(video_id_clip_path_unique))
# print('缺少的clip-json文件中有但clip_path不全的：',errorlist)
#
# print(set(video_id_vd_path))
# print(set(video_id_clip_path_unique))
# pd.DataFrame(video_id_df).to_csv('video_id_df.csv')
# pd.DataFrame(video_id_vd_path).to_csv('video_id_vd_path.csv')
# pd.DataFrame(video_id_clip_path).to_csv('video_id_clip_path.csv')
# pd.DataFrame(video_id_clip_path_unique).to_csv('video_id_clip_path_unique.csv')
# pd.DataFrame(video_id_clip_path_count).to_csv('video_id_clip_path_count.csv')
pd.DataFrame(list(set(video_id_df) - set(video_id_vd_path))).to_csv('1.csv')
pd.DataFrame(errorlist).to_csv('2.csv')
