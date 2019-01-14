import urllib.request
import gevent
from gevent import monkey
import ssl


#这句话的作用是使用 gevent 的时候,框架会帮我们把 系统的延迟函数修改成框架中的延迟函数
monkey.patch_all()


def downloader(image_name,urlstr):

    #当我们使用的是https 下载图片的时候,我们需要做一个不需要验证的context
    context = ssl._create_unverified_context()

    req = urllib.request.urlopen(urlstr,context=context)

    img_content = req.read()

    with open(image_name,"wb") as f:
        f.write(img_content)



def main():
    gevent.joinall([
        gevent.spawn(downloader,"1.jpg","https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1547278500296&di=7694484c9100f9aa52d8cd2c3632eec7&imgtype=0&src=http%3A%2F%2Ftu.simei8.com%3A7788%2Fpic170%2F17048-1.jpg"),
        gevent.spawn(downloader,"2.jpg","https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1547278500296&di=f928fca8fc4adb020d767dd73257c98a&imgtype=0&src=http%3A%2F%2Fimg.7160.com%2Fuploads%2Fallimg%2F181224%2F1-1Q224130350.jpg")
    ])
if __name__ == '__main__':
    main()
