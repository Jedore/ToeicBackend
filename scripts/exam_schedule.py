import pickle

import httpx
from bs4 import BeautifulSoup


def parse_schedule(url: str):
    rsp = httpx.get(url)
    if not httpx.codes.is_success(rsp.status_code):
        return

    soup = BeautifulSoup(rsp.text)
    tbody = soup.table.tbody
    schedules = []
    title = ''
    for index, tr in enumerate(tbody.find_all('tr')):
        if 0 == index:
            title = tr.text.split()[0]
        if index <= 1:
            continue

        line = []
        # 考试日期
        td = tr.find('td')
        line.append(''.join(td.text.split()))
        # 开考城市数量
        td = td.find_next_sibling('td')
        line.append(td.text.split()[0])
        # 开考城市
        td = td.find_next_sibling('td')
        line.append(''.join(td.text.split()))
        # 常规报名缴费起止日期
        td = td.find_next_sibling('td')
        line.append(td.text.split())
        # 加急报名截止日期
        td = td.find_next_sibling('td')
        line.append(''.join(td.text.split()))

        schedules.append(line)
    return title, schedules


if __name__ == '__main__':
    listen_read = parse_schedule('https://www.test-toeic.cn/aboutExam.aspx?id=29')
    speak_write = parse_schedule('https://www.test-toeic.cn/aboutExam.aspx?id=125')

    with open('schedules_lr.txt', 'br') as fp:
        lr = pickle.load(fp)
    with open('schedules_sw.txt', 'br') as fp:
        sw = pickle.load(fp)

    if lr != listen_read or sw != speak_write:
        print('Schedule changed!!!')
        exit(-1)

    with open('schedules_lr.txt', 'bw') as fp:
        pickle.dump(listen_read, fp)
    with open('schedules_sw.txt', 'bw') as fp:
        pickle.dump(speak_write, fp)
