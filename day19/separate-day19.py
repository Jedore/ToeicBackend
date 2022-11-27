"""
    @author: Jedore
    @project: ToeicBackend
    @file: separate-day19.py
    @time: 2022/11/22 23:56
    @desc:
        Separate day19 audios, generate precise time point for every sentence.
"""

import os

import math
from pydub import AudioSegment

lines = []
for file in os.listdir('audio'):
    points = []
    audio = AudioSegment.from_file(f'audio/{file}')
    begin = end = None
    for i, item in enumerate(audio):
        if item.dBFS == -math.inf:
            if i == 0 or audio[i - 1].dBFS != -math.inf:
                begin = i
        elif audio[i - 1].dBFS == -math.inf and i > 0:
            end = i - 1

        if end is not None:
            if end - begin > 2000:
                points.append([begin, end])
            begin = end = None
    line = f'{len(points)}|'

    for index, item in enumerate(points):
        t = (item[1] - item[0]) // 2 + item[0]
        line = f'{line}{t},'
    line = line.strip(', ') + '\r'
    lines.append(line)

with open('time_points.txt', 'w') as fp:
    fp.writelines(lines)
