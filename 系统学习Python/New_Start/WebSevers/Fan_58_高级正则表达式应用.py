import re


def sub_fun():
    """找到和替代"""
    search_str = "hh=999  mm=34 dsfsd"

    search_re = re.sub(r"\d+", "88", search_str)

    print(search_re)


def serach_fun():
    """查找到第一个就结束了"""
    search_str = "hh=999  mm=34"

    search_re = re.search(r"\d+", search_str)

    print(search_re.group())


def filAll_fun():
    """找到所有的"""
    search_str = "hh=999  mm=34"

    search_re = re.findall(r"\d+", search_str)

    print(search_re)


def splite_fun():
    search_str = "hh=999  mm=34"

    search_re = re.split(r" +", search_str)

    print(search_re)

def group_fun():
    """组的使用"""
    search_str = "<h1><body>hello world</body></h1>"

    search_re = re.match(r"<(?P<p1>\w*)><(?P<p2>\w*)>.*</(?P=p2)></(?P=p1)>", search_str)

    print(search_re)

def main():
    #serach_fun()
    #filAll_fun()
    #sub_fun()
    #splite_fun()
    group_fun()



if __name__ == '__main__':
    main()