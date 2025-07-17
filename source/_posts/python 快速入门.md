---
title: python 快速入门
date: 2025-07-11T16:44:00.000Z
tags: 
  - python
  - 快速入门
index_img: https://silengzi.github.io/cube-fluid-blod/images/6cca11f3b3e8187baf73b04f8ce72ef4.jpeg

---


摘要...


## 简介

Python 是一门由 Guido van Rossum 于 1991 年发布的高级编程语言，以简洁优雅的语法和强大的生态系统著称。它具有跨平台、易上手、开发效率高等特点，广泛应用于数据分析、人工智能、Web 开发、自动化运维等领域。凭借丰富的第三方库和活跃的社区，Python 已成为当前最受欢迎的通用编程语言之一，尤其在 AI 与数据驱动的应用中展现出强大优势。

官方文档：[Python 官网](https://www.python.org/)


## 环境搭建

虽然说我们可以从官网直接下载 python 安装，但时间久了，几乎无可避免的会遇到版本问题，这个项目需要一个版本，另一个项目又需要其他版本的 python ，总不能每次都手动卸载安装吧，这样非常麻烦。

这里我们推荐使用 pyenv 来管理不同版本的 python ，包括不同版本的安装、切换、卸载等。

详细内容可以参考我之前的这篇文章（window版本）：[pyenv-win: Windows上的 Python 版本管理工具](https://silengzi.github.io/cube-fluid-blod/2024/12/27/7452988506778091571/)


## 开发工具

因为我是前端出身，这里我就直接用 vscode/cursor + python插件 来开发了。
如果你习惯用 JetBrains 系列的软件，也可以用 PyCharm ，根据个人习惯来就好。


## 基础语法

Python 是一种解释型、动态类型的语言，语法非常简洁，关键字少，特别适合快速开发。它最大的语法特点是：
- 缩进表示代码块（没有{}）
- 无需变量类型声明，自动推断类型
- 一切皆对象
- 函数也是对象


### 调试

```python
# 普通打印
print("Hello, world")
print(123)
print(True)

# 连续打印
print("Name:", name, "Age:", age)
# 输出：Name: Alice Age: 25

# 打印格式化字符串
name = "Bob"
age = 30
print(f"My name is {name}, and I am {age} years old")
```


### 定义变量

```python
x = 10
name = "Alice"
price = 19.99
is_active = True
b = None
```

python 中定义变量不需要任何关键字，直接定义变量名即可。


### 数据结构

```python
# 列表（数组）
nums = [1, 2, 3]

# 元组（不可变）
point = (3, 4)

# 字典（对象）
user = {"name": "Alice", "age": 25}

# 集合（不重复元素）
tags = {"python", "js", "java"}
```


### 作用域



### 循环

```python
# for 循环
for i in range(5):  # 0 到 4
    print(i)

# 遍历列表：
names = ["Alice", "Bob", "Charlie"]
for name in names:
    print(name)

# while 循环：
i = 0
while i < 5:
    print(i)
    i += 1
```


### 判断

```python
x = 10

if x > 5:
    print("greater than 5")
elif x == 5:
    print("equal to 5")
else:
    print("less than 5")
```

条件后面必须加冒号 :
缩进代表代码块（通常是 4 个空格）

Python 中的布尔值：

```python
# False 的值有：
# False, None, 0, "", [], {}, set()

if not name:
    print("name is empty")
```


### 函数定义及调用

定义函数：
```python
def greet(name):
    print("Hello, " + name)
```

调用函数：
```python
greet("Alice")
```

返回值：
```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)
```


### 列表推导式（强大简洁）

```python
squares = [x * x for x in range(5)]
```

相当于
```python
squares = []
for x in range(5):
    squares.append(x * x)
```


### 三目运算符

```python
result = "yes" if x > 5 else "no"
```


![加油](https://silengzi.github.io/cube-fluid-blod/images/006APoFYly8h5mmvdv4zyg307n07nu10.gif)