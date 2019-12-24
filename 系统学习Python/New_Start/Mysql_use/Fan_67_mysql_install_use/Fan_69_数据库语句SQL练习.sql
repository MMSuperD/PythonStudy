
-- 1.创建数据库
create database Goods charset=utf8;

-- 2.查看数据库是否创建成功
select database();

-- 3.使用 数据库
use Goods;

-- 4.创建good_table;
create table good_table(
    id int unsigned not null auto_increment primary key ,
    good_name varchar(20) not null default '我是Fan',
    brand_name varchar(20) not null default '联想',
    kind_name varchar(20) not null default '电脑',
    price decimal(10,3) not null default '0.000'
);

-- 5.插入数据到 good_table 表中
insert into good_table values
    (0,'联想电脑1','联想','电脑',3000.000),
    (0,'联想电脑2','联想','电脑',4000.000),
    (0,'联想电脑3','联想','电脑',5000.000),
    (0,'联想电脑4','联想','电脑',6000.000),
    (0,'联想电脑5','联想','电脑',7000.000),
    (0,'华硕电脑1','华硕','电脑',7000.000),
    (0,'华硕电脑2','华硕','电脑',9000.000),
    (0,'联想数据线1','联想','数据线',3000.000),
    (0,'联想数据线2','联想','数据线',4000.000),
    (0,'联想数据线3','联想','数据线',5000.000),
    (0,'联想数据线4','联想','数据线',6000.000),
    (0,'联想数据线5','联想','数据线',7000.000),
    (0,'华硕数据线1','华硕','数据线',7000.000),
    (0,'华硕数据线2','华硕','数据线',9000.000),
     (0,'联想USB1','联想','USB',30.000),
    (0,'联想USB2','联想','USB',40.000),
    (0,'联想USB3','联想','USB',50.000),
    (0,'联想USB4','联想','USB',600.000),
    (0,'联想USB5','联想','USB',70.000),
    (0,'华硕USB1','华硕','USB',7.000),
    (0,'华硕USB2','华硕','USB',90.000);

-- 6.查询价格最高的电脑
select max(price) as price from good_table where kind_name='电脑';
select * from good_table where price=(select max(price) as price from good_table where kind_name='电脑') and kind_name='电脑';


-- 7.创建笔记表
    -- 7.1 创建表
    create table IF NOT EXISTS note_table (
        note_id int unsigned not null auto_increment primary key,
        title varchar(20) not null ,
        content text not null ,
        create_time datetime not null ,
        update_time datetime not null ,
        isNow bit not null default 1,
        isDelete bit not null default 0,
        sign_text varchar(20) not null
    );
    -- 7.2 插入数据
    insert into note_table values (0, 'title', 'content', 'create_time', 'update_time', default, default,'sign_text');

    -- 7.3 显示数据
    select * from note_table where isDelete=0 and isNow=1  limit 0,10;

    -- 7.4 更新数据
    update note_table set isNow=0 where note_id=22;

    -- 7.5 删除数据
    update note_table set isDelete=1 where note_id=22;


