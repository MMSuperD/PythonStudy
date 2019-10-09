

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

-- 聚合函数
    -- 总数
    -- count
    -- 查询一共有多少条记录
    select count(*) from student;
    -- 查询一共有多少条男性
    select count(*) from student where gender=1;
    -- 查询男性有多少人
    select count(*) as 男性人数 from student where gender=1;

    -- 最大值
    -- max
    -- 查询女性中最大的年龄
    select max(age) as 女性最大年龄 from student where gender=2;
    -- 查询女性中最大的升高
    select max(height) as 女性中最高的身高 from student where gender=2;

    -- 最小值
    -- min
    -- 查询女性中最小的年龄
    select min(age) as 女性最大年龄 from student where gender=2;
    -- 查询女性中最小的身高
    select min(height) as 女性中最高的身高 from student where gender=2;

    -- 求和
    -- sum
    -- 查询所有女性年龄总和
    select sum(age) as 女性最大年龄 from student where gender=2;
    -- 查询所有女性身高总和
    select sum(height) as 女性身高总和 from student where gender=2;

    -- 平均数
    -- avg
    -- 查询所有男性年龄的平均值
    select avg(age) as 女性年龄平均值 from student where gender=2;
    select sum(age)/count(*) as 女性年龄平均值 from student where gender=2;

    -- 四舍五入
    -- round(123.33,1) 1表示保留一位小数
    -- 计算所有学生平均年龄 保留两位小数
    select round(avg(age), 2) as 所有学生平均年龄 from student;


-- 分组
    -- group by
    -- 按照性别分组,查询所有的性别
    select gender as 性别 from student group by gender;

    -- 计算每组性别中的人数
    select gender as 性别, count(*) as 人数 from student group by gender;

    -- 计算男性的人数
    select gender as 性别, count(*) as 人数 from student where gender=1 group by gender;

    -- group_concat(字段1,字段2,"字符串1",...)
    -- 查询同一种性别,及其姓名列表  还有 人数 升序排列
    select gender as 性别, group_concat(name," ") as 姓名列表, count(*) as 人数 from student group by gender order by count(*) asc ;


-- 分页
    -- limit start, count ; start 表示开始位置(必须是具体的数字,不能是表达式) count 表示每一页的页数
    -- 查询所有的女性记录 每一页显示 3条数据
    select * from student where gender=1 limit 0, 3;

    -- 查询所有的女性记录 按照身高由高到低排序 每一页显示 3条数据(有一个记录点,limit 使用一定要在最后)
    select * from student where gender=1 order by height desc limit 0, 3;
