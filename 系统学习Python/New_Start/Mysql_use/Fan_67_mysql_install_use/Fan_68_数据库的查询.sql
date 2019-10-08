

-- 常用查询
    -- 去重查询 消除重复行
    -- select distinct 字段名字 from 表名
    select distinct gender from student;

-- 条件查询 都是where 后面的运算
    -- 条件运算符 < > != <= >=
    -- 逻辑运算符 or,and not
    -- 括号优先级()

    -- 模糊查询
        -- like
        -- % 替换 0 个 1个 或者多个
        -- _ 替换一个

        -- 查询姓名中 以 小 开头的记录
        select * from student where name like "小%";

        -- 查询姓名中包含 小 的记录
        select * from student where name like "%小%";

        -- 查询姓名中 以 小 结尾的 记录
        select  * from student where name like "%小";

        -- 查询姓名中 只有两个字的 记录
        select * from student where name like "__";

        -- 查询姓名在两个字以上的记录
        select * from student where name like "__%";

        -- rlike
        -- rlike 正则表达式
        -- 查询姓名中以 "王" 开头的 "反" 结尾的 记录
        select * from student where name rlike "^王.*反$";

    -- 范围查询
        -- in (1,3,5) 表示一个非连续的返回值
        -- 查询年龄 是 18 和 88 岁的记录
        select * from student where age=18 or age=88;
        select * from student where age in (18,88);

        -- not in (1,3,5)表示不再这个非连续范围的返回值
        -- 查询年龄不是 18 和 88岁的记录
        select * from student where age not in (18,88);

        -- between ... and ... 表示连续的包含两头的值
        -- 查询年龄在 18 到 22之间的记录
        select * from student where age between 18 and 22 ;

        -- not between ... and ... 表示不包含两者之间的值
        -- 查询年龄不在 18 到 22之间的记录
        select * from student where age not between 18 and 22 ;

    -- 空判断
        -- is null
        -- 查询身高信息是否为空
        select * from student where height is null;

        -- is not null
        -- 查询身高信息不为空的
        select * from student where height is not null;


-- 数据记录排序 order by
    -- order by asc 从小到大排序
    -- order by desc 从大到小排序

    -- 例子 这个是多个字段联合排序,如果没有多个字段,就写一个就好了
    -- 查询 身高大于180 的男性 按照身高 从小到大排序,如果相同 按照id 从大到小排序
    select * from student where age>180 order by height asc, id desc ;