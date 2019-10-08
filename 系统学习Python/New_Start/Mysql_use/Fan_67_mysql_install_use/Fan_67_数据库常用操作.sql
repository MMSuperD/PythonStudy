

-- 数据库常用操作

    -- 链接数据库
    mysql -uroot -pmysql
    mysql -uroot -p

    -- 退出数据库
    exit/quit/control + d

    -- sql 语句都需要有分号(;)结尾

    -- 显示数据库版本
    select version();

    -- 显示时间
    select now();

    -- 查看所有的数据库
    show databases;

    -- 创建数据库
    -- create database 数据库名字 charset=utf8;
    create database mmddatabase charset=utf8;
    create database mmdnewdatabase;


    -- 查看当前使用的数据库
    select database();

    -- 使用数据库
    -- use 数据库名字;
    use mmddatabase;


    -- 查看创建数据库语句
    -- show create database 数据库名字
    show create database mmddatabase;


    -- 删除数据库
    -- drop database 数据库名字
    drop database mmddatabase;


    -- 查看数据库中所有的表
    show tables;

    -- 创建表
    -- auto_increment 表示自动增长
    -- not null 表示不能为空
    -- primary key 表示主键
    -- default 默认值
    -- create table 表的名字(字段,类型,约束[,字段,类型,约束]);
    -- 创建一个学生表
    create table student(
        id int unsigned not null primary key auto_increment,
        name varchar(30) not null ,
        age tinyint unsigned default 0,
        height decimal(5,2),
        gender enum("男", "女", "中性", "保密") default "保密",
        cls_id int unsigned
    );

    -- 创建一个classes 表
    create table classes(
        id int unsigned not null primary key auto_increment,
        name varchar(30) not null
    );

    -- 查看数据表的结构
    -- desc 数据表的名字
    desc student;

    -- 插入数据
    -- insert into 表的名字 values(顺序各个字段的值)
    insert into student value(0, "老王", 23, 188.23, "男", 0 );

    -- 查看数据
    -- select * from 表的名字;
    select * from student;


    -- 查看表的创建语句
    show create table 表的名字;

    -- 修改表 -添加字段
    -- alter table 表的名字 add 字段名字 类型和约束
    alter table student add birth datetime;

    -- 修改表 -自改字段类型 和 约束(不修改字段名字)
    -- alter table 表的名字 modify 字段名字 新的类型 和 约束
    alter table student modify birth data;

    -- 修改表 -修改表的字段名字
    -- alter table 表的名字 change 原名 新的名字 类型和约束
    alter table student change birth birthday data default "2019/10/08";

    -- 修改表 -删除字段
    -- alter table 表的名字  drop 字段的名字
    alter table student drop birthday;

    -- 删除表
    -- drop table 表的名字;
    drop table student;


    -- 插入数据 - 向学生表中插入一条数据
    -- insert into 表的名字 values();
    --  mysql> desc student;
# +--------+-------------------------------------+------+-----+---------+----------------+
# | Field  | Type                                | Null | Key | Default | Extra          |
# +--------+-------------------------------------+------+-----+---------+----------------+
# | id     | int(10) unsigned                    | NO   | PRI | NULL    | auto_increment |
# | name   | varchar(30)                         | NO   |     | NULL    |                |
# | age    | tinyint(3) unsigned                 | YES  |     | 0       |                |
# | height | decimal(5,2)                        | YES  |     | NULL    |                |
# | gender | enum('男','女','中性','保密')       | YES  |     | 保密    |                |
# | cls_id | int(10) unsigned                    | YES  |     | NULL    |                |
# +--------+-------------------------------------+------+-----+---------+----------------+
    -- 向student 表中插入一条学生信息,自动增长的主键 可以是 0,default,null
    insert into student values(0, "王五", 12, 232.23, "男", 0);
    insert into student values(default, "王五", 12, 232.23, "男", 0);
    insert into student values(null, "王五", 12, 232.23, "男", 0);

    -- 失败
    insert into student values(0, "王五", 12, 232.23, "男二号", 0);
    -- 成功 枚举中的值 下标从1 开始
    insert into student values(0, "王五", 12, 232.23, 1, 0);
    insert into student values(0, "王五", 12, 232.23, 2, 0);

    -- 部分插入数据
    -- insert into student 字段列表(字段1,字段2) values (字段1的值,字段2的值);
    insert into student (name, gender) values ("李四", 1);
    insert into student (name, gender) values ("李四", 2);

    -- 多行插入数据
    -- insert into student 字段列表(字段1,字段2) values (字段1的值,字段2的值), (字段1的值,字段2的值).......;
    insert into student (name, gender) values ("李四", 1),("哥哥", 2);
    insert into student values (null, "王五", 12, 232.23, "男", 0), (null, "宝宝", 12, 232.23, "男", 0);

    -- 修改表中的数据
    -- update 表的名字 set 字段名1=值2,字段名2=值2 where ....;
    update student set name="王五", gender=1;
    update student set name="王五", gender=1 where id=2;
    update student set name="王五", gender=1 where name="宝宝";


    -- 查询数据
        -- 查询所有的列
        -- select * from 表的名字;
        select * from student;

        -- 查询某一列,或者几列 并给 列取一个别名
        -- select 字段1, 字段2 from student;
        -- select 字段1[ as 别名], 字段二[ as 序号] from student;
        select name from student;
        select name,gender from student;
        select name as "姓名" ,gender as "性别" from student;

        -- 根据某一个条件查询数据
        select name,id from student where id<7;

        -- 给表 取别名
        select s.name as "姓名" from student as s;

    -- 删除数据
        -- 物理删除
        -- delete from 表名 where 条件;
        -- 清空表数据 delete from student
        -- 条件清空数据 delete from student where id>5;

        -- 逻辑删除
        -- 用一个字段来表示,这条信息是否能够被使用
        -- 给student 表添加一个is_delete 字段 bit 类型
        alter table student add is_delete bit default 0;

        -- update student set is_delete=1 where id=2;





