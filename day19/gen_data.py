from model.day19 import Lrc


def gen_lrc():
    data = {}
    with open('lrc.txt', 'r', encoding='utf8') as fp:
        record = []
        day = ''
        for line in fp:
            if line == '\n':
                continue
            line = line.strip('\n')
            if line.startswith('##'):
                day = line[3:]
            elif line.startswith('-'):
                line = line[2:]
                # index = line.index('.')
                # st, en = int(line[:index]), line[index + 1:].strip()
                record.append(line)
            else:
                zh = line.strip()
                record.append(zh)
                value = data.setdefault(day, [])
                value.append(tuple(record))
                record.clear()
    print(data)


if __name__ == '__main__':
    gen_lrc()
