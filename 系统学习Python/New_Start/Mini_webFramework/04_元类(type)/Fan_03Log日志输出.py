import logging  #这个是日志输出的头文件

def 简单的屏幕输出日志():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s) - %(filename)s[Line:%(lineno)d] - %(levelname)s:')

    logging.debug("这个是debug 日志")
    logging.info("这个是info 日志")
    logging.warning("这个是warning日志")
    logging.error("这个是error 日志")
    logging.critical("这个是critical日志 致命日志")


def 简单的文件日志输出():
    logging.basicConfig(level=logging.WARNING,
                        filename="./log.txt",
                        filemode="w",
                        format='%(asctime)s) - %(filename)s[Line:%(lineno)d] - %(levelname)s:')

    logging.debug("这个是debug 日志")
    logging.info("这个是info 日志")
    logging.warning("这个是warning日志")
    logging.error("这个是error 日志")
    logging.critical("这个是critical日志 致命日志")

def 复杂的屏幕和文件日志一起输出():

    # 1. 第一步 创建log
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)  # 这个是log 等级的总开关

    # 2.第二步 创建一个handler 用于写入日志文件
    log_file = "./log_file.txt"
    file_handler = logging.FileHandler(log_file,mode='a') # open 打开模式 这里可以参考
    file_handler.setLevel(level=logging.DEBUG)  # 输出到 file  log 的等级开关

    # 3.第三部 创建一个handler 用些输出到屏幕
    screen_handler = logging.StreamHandler()
    screen_handler.setLevel(level=logging.WARNING)  # 输出到 屏幕 log 的等级开关

    # 4.第四部 定义输出格式
    format_str = logging.Formatter('%(asctime)s) - %(filename)s[Line:%(lineno)d] - %(levelname)s:')
    file_handler.setFormatter(format_str)
    screen_handler.setFormatter(format_str)

    # 5.第五步 将logger 添加到handler 里面
    logging._addHandlerRef(file_handler)
    logging._addHandlerRef(screen_handler)

    # 6.第六步 设置日志输出
    logging.debug("这个是debug 日志")
    logging.info("这个是info 日志")
    logging.warning("这个是warning日志")
    logging.error("这个是error 日志")
    logging.critical("这个是critical日志 致命日志")


# 简单的屏幕输出日志()

# 简单的文件日志输出()

复杂的屏幕和文件日志一起输出()

