import  re

#  正则表达式匹配分组,得到得到内容

#比如我们需要匹配一个html

str = "<h1><body>nihaojdjsdfwf</body></h1>"

match_str = r"<([a-zA-Z0-9]*)><([a-zA-Z0-9]*)>.*</\2></\1>"

res = re.match(match_str,str)

if res:
    print(res.group(1))
else:
    print("meiyou ")