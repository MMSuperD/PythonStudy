
from pymysql import connect

def main():
    """主要函数"""
    # 1.创建connect 链接
    con = connect(host='localhost', port='3306', database='Goods', user='root', password='mysql',charset='utf8')

    # 2.得的游标对象
    cs1 = con.cursor()

    # 3.执行select 语句
    content = cs1.execute("select * from good_table")

    for temp in range(content):

        # 获取查询结果
        result = cs1.fetchone()

        # 输出数据
        print("查询的数据:" % result)


    # 4.关闭游标对象
    cs1.close()

    # 5.关闭连接
    con.close()

if __name__ == '__main__':
    main()
