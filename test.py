    
# 字面量  
# 注释
# 变量
# 数据类型
# 数据类型转换
# 标识符
# 运算符
# 字符串的三种定义方式
# 字符串的拼接
# 字符串格式化 %s %d %f  (,)
# 字符串格式化的精度控制 m.n形式 
# 表达式快速格式化     f"内容{占位}"

# 数据输入 input
# 布尔类型和比较运算符
# if语句的基本格式  if : else:    if elif else 
# while 循环  where 条件 :
# for循环     for x in name :
# range语法  range(num1,num2,step)

# 函数 len()  def  djh():  return None

# global关键字  函数内变量声明全局变量


#数据容器 ： list []  tuple元组 str set dict字典
# 列表 list     常用方法.index()   .append() .extend() .insert()

#元组 t1=(1,"A",True)  不能修改元组内容  元组内容有list 可以修改

# main 变量   all变量 from   import *  


# pip install

# pyexcharts模块  Line  Map  Bar  Timeline


# josn.dumps json.load
print(type("122"))

strin_type = type("122")
print(strin_type)


num_str = str(11)
print(type(num_str),num_str)
if 1>2:
    print("AAA")

for i  in range(1,10):
    for j in  range(1,i+1):
        print(f"{j}*{i}={j*i}\t",end='')
    print()


def  djh(mo):
    asq = 100



def add(x,y):
    """添加

    Args:
        x (_type_): 参数1
        y (_type_): 参数1

    Returns:
        _type_: 结果
    """
    result =x +y
    return result
    