# 要求: 顺序并且居中对齐输出以下内容
poem = ["\t\n登鹳雀楼",
        "王之涣",
        "白日依山尽",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"]

for poem_str in poem:

    print("| %s |" % poem_str.strip().center(10,"　"))  #这里第二个参数是中文的空格