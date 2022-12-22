import httpx
from bs4 import BeautifulSoup


def parse_schedule(url: str):
    rsp = httpx.get(url)
    if not httpx.codes.is_success(rsp.status_code):
        return

    soup = BeautifulSoup(rsp.text)
    tbody = soup.table.tbody
    for index, item in enumerate(tbody.find_all('tr')):
        if index <= 1:
            continue

        for td in item.find_all('td'):
            # todo
            ...


if __name__ == '__main__':
    parse_schedule('https://www.test-toeic.cn/aboutExam.aspx?id=29')
