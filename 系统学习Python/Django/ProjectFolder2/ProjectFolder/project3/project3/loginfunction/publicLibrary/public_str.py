import string
from random import choice, randint, randrange

def selected_chrs(length):
  """
  返回length个随机字符串
  :param length:
  :return:
  """
  # 候选字符集,大小写字母+数字
  chrs = string.ascii_letters + string.digits;
  result = ''.join(choice(chrs) for _ in range(length));
  return result