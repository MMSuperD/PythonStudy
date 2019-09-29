import urllib.request
import gevent
from gevent import monkey

monkey.patch_all()


def download(image_name, image_url):
    """图片下载"""
    re = urllib.request.urlopen(image_url)
    image_contents = re.read()

    with open(image_name, "wb") as f:
        f.write(image_contents)


def main():

    gevent.joinall({
        gevent.spawn(download, "1.jpg", "http://pic25.nipic.com/20121112/9252150_150552938000_2.jpg"),
        gevent.spawn(download, "2.jpg", "http://pic41.nipic.com/20140524/9643307_104442624152_2.jpg")
    })


if __name__ == '__main__':
    main()