---
title: C++ 快速入门
date: 2026-03-02 15:59:38
tags: 
  - C++
  - 编程语言
  - 开发环境
  - Visual Studio
  - CMake
categories: 
  - 编程教程
  - 技术分享
keywords: 
  - C++ 入门
  - C++ 教程
  - Visual Studio 配置
  - CMake 构建系统
  - C++ 开发环境
author: silengzi
description: 从零开始学习 C++ 编程语言的完整指南，涵盖环境配置、基础语法、面向对象、智能指针、并发编程等内容，快速掌握 C++ 开发技能。
---

# C++ 快速入门


## 环境配置

### Windows：安装 Visual Studio 2022

推荐 Windows 用户使用 Visual Studio 2022，编译器、调试器、编辑器一体，不需要额外配置。

**1. 下载安装包**

前往 [https://visualstudio.microsoft.com](https://visualstudio.microsoft.com)，选择 **Community 2022**（免费版），下载后运行安装程序。

**2. 选择工作负载**

安装程序会让你选择要安装的组件，勾选 **"使用 C++ 的桌面开发"**，右侧详细列表中确认以下三项已选中：

- MSVC v143（编译器本体）
- Windows SDK（系统头文件和库）
- C++ CMake 工具（可选，后续可能用到）

其余默认即可，点击安装，等待完成（约 5–10 GB）。

**3. 创建第一个项目**

安装完成后打开 Visual Studio：

1. 点击 **"创建新项目"**
2. 搜索并选择 **"控制台应用"**（语言选 C++）
3. 填写项目名称和保存路径，点击 **"创建"**

VS 会自动生成一个包含 `main` 函数的 `.cpp` 文件。

---

### Linux：安装编译器与工具链

**Ubuntu / Debian**

```bash
sudo apt update
sudo apt install build-essential gdb cmake
```

`build-essential` 包含 gcc、g++ 和 make，`gdb` 是调试器，`cmake` 是构建工具。

安装完成后验证：

```bash
g++ --version   # 应输出版本号，≥ 9 即可
cmake --version
```

**编辑器推荐**：安装 [VS Code](https://code.visualstudio.com)，再安装插件 **C/C++**（Microsoft 官方），可以获得语法高亮、跳转定义、调试支持。

---

### 第一个程序

在 VS 自动生成的文件里，或者新建一个 `.cpp` 文件，写入：

```cpp
#include <iostream>

int main()
{
    std::cout << "Hello C++" << std::endl;
    return 0;
}
```

**Windows（Visual Studio）运行方式：**

- 按 `Ctrl + F5` 直接运行（不调试）
- 按 `F5` 以调试模式运行
- 底部输出窗口会显示 `Hello C++`

**Linux 编译运行方式：**

```bash
g++ -g -o hello hello.cpp   # 编译，-g 表示生成调试信息
./hello                      # 运行
```

---

### 调试基本操作

调试能力越早建立越好，读复杂代码时依赖它的频率远超预期。以 Visual Studio 为例：

| 操作 | 快捷键 | 说明 |
|------|--------|------|
| 打 / 取消断点 | F9 | 点击行号左侧也可以 |
| 启动调试 | F5 | 程序运行到断点处暂停 |
| 逐行执行 | F10 | 不进入函数内部 |
| 进入函数 | F11 | 跳入当前行调用的函数 |
| 跳出函数 | Shift+F11 | 执行完当前函数剩余部分，返回调用处 |
| 继续运行 | F5 | 运行到下一个断点 |

程序暂停在断点时，鼠标悬停在变量上可以直接看到它的当前值；左下角的 **"局部变量"** 窗口会列出当前作用域内所有变量。

---

## C++ 最小生存集

### 基础语法

#### 变量与类型

C++ 是强类型语言，变量必须声明类型：

```cpp
int count = 10;
double ratio = 3.14;
bool active = true;
std::string name = "hello";
```

`auto` 可以让编译器自动推断类型，在类型名很长时常用：

```cpp
auto x = 42;          // int
auto y = 3.14;        // double
auto obj = GetSomeObject();  // 编译器推断返回值类型
```

#### 函数

```cpp
// 函数声明：返回类型 函数名(参数列表)
int Add(int a, int b)
{
    return a + b;
}

// 无返回值用 void
void PrintMessage(std::string msg)
{
    std::cout << msg << std::endl;
}
```

#### 条件与循环

```cpp
// if / else
if (count > 0)
{
    // ...
}
else if (count == 0)
{
    // ...
}
else
{
    // ...
}

// for 循环
for (int i = 0; i < 10; ++i)
{
    // ...
}

// 范围 for（遍历容器时常用）
std::vector<int> items = {1, 2, 3};
for (int item : items)
{
    // ...
}

// while
while (active)
{
    // ...
}
```

#### enum class

比起裸 `enum`，`enum class` 有独立的作用域，不会污染外部命名空间，项目里更常见：

```cpp
enum class State
{
    Idle,
    Running,
    Stopped
};

State s = State::Running;

if (s == State::Running)
{
    // ...
}
```

### 指针与引用

```cpp
SomeClass* p;  // 指针：对象可能不存在，可以为 nullptr
SomeClass& r;  // 引用：对象必须存在，不可能为空
```

在实际项目里这两种写法有明确的语义约定：指针传参暗示调用方可能传入空值，函数内需要判空；引用传参暗示对象一定有效，直接使用。读函数签名时先看这一点，能快速判断函数的前提条件。

### const

```cpp
const SomeClass* p;  // 不能通过 p 修改对象内容
SomeClass* const p;  // p 本身不能指向别的地址
```

最常见的形式：

```cpp
SomeClass* GetObject() const;
```

函数签名末尾的 `const` 表示该函数不修改当前对象的任何成员，是一个只读操作。

### 本阶段不需要掌握

- 宏技巧
- 运算符重载
- 多继承的复杂规则

---

## 面向对象与多态

### 类、构造与析构

```cpp
class Foo
{
public:
    Foo();
    ~Foo();
};
```

需要理解两个概念：

- **构造/析构顺序**：派生类构造时先调用基类构造函数，析构顺序相反
- **栈对象 vs 堆对象**：栈对象离开作用域自动析构，堆对象（`new` 出来的）需要显式 `delete`，或者交给智能指针管理

### 继承与虚函数

```cpp
class Base
{
public:
    virtual void Execute() = 0;
    virtual ~Base() = default;
};

class Derived : public Base
{
public:
    void Execute() override;
};
```

**虚析构函数不能省。** 用基类指针 `delete` 派生类对象时，如果基类析构函数不是虚函数，派生类的析构函数不会执行，资源泄漏。

**`override` 不是可选的。** 它让编译器验证父类里确实存在这个虚函数——函数名拼错、或者父类签名变了，编译期就会报错，而不是悄悄变成一个新函数。

**构造/析构里不要调用虚函数。** 基类构造函数执行时，派生类尚未构造完成，此时调用虚函数走的是基类版本，不是预期的派生类版本。

### 多态与调试

遇到 `Base* obj` 调用 `obj->Execute()`，不确定实际执行的是哪个子类实现时，在调用处打断点，F11 单步进入，调试器会跳到真实的派生类方法。

---

## 智能指针与 RAII

### unique_ptr

```cpp
auto obj = std::make_unique<MyClass>();
```

对象的唯一拥有者，离开作用域自动销毁，不需要手动 `delete`。

`unique_ptr` 不能复制，只能转移所有权：

```cpp
void TakeOwnership(std::unique_ptr<MyClass> obj);

TakeOwnership(std::move(myObj));
// std::move 之后 myObj 失效，不能再使用
```

函数参数是 `unique_ptr` 时，意味着调用后所有权转移给了被调函数。

### shared_ptr 与 weak_ptr

```cpp
auto a = std::make_shared<MyClass>();
auto b = a;  // 引用计数为 2，两者共同持有
```

最后一个持有者销毁时，对象才真正释放。

循环引用是共享所有权的常见陷阱——A 持有 B，B 也持有 A，引用计数永远不归零。解决方式是其中一方改用 `weak_ptr`：

```cpp
std::weak_ptr<MyClass> w = a;

if (auto locked = w.lock()) {  // 使用前检查对象是否仍然存活
    locked->DoSomething();
}
```

`weak_ptr` 不增加引用计数，只是一个"不参与所有权"的观察者。

### RAII

C++ 管理资源的核心惯用法：

> 构造函数 = 获取资源  
> 析构函数 = 释放资源

智能指针、`lock_guard`、各种 handle 封装类，本质上都是 RAII。对象生命周期结束，资源跟着释放，适用于所有需要配对操作的场景：内存、锁、文件句柄、回调注册等。

---

## 模板、Lambda 与回调

### 模板

项目里最常见的模板形式：

```cpp
template<typename T>
void Register(T* observer);
```

理解为"该函数适用于任意类型 T"即可。

编译期约束：

```cpp
static_assert(std::is_base_of<BaseClass, T>::value, "T must derive from BaseClass");
```

`static_assert` 在编译期检查类型条件，T 不满足要求时直接报错。这类断言是函数契约的一部分，能帮助理解调用前提。

可变参数模板偶尔会遇到：

```cpp
template<typename... Args>
void Foo(Args&&... args);
```

知道它接受任意数量、任意类型的参数就够了，不需要深入。

### Lambda

```cpp
manager.OnEvent(
    [this](double time, SomeObject* obj) {
        HandleEvent(time, obj);
    }
);
```

方括号是**捕获列表**：

- `[this]`：捕获当前对象指针，可以访问成员变量和成员函数
- `[&]`：按引用捕获所有外部变量
- `[=]`：按值捕获（复制）所有外部变量

**捕获 `this` 的生命周期问题**：如果 lambda 的存活时间超过 `this` 对象，对象析构后 lambda 被触发，程序崩溃。注册回调时需要确保回调生命周期不超过 `this`，或者在对象析构前主动注销。

### std::function

```cpp
std::function<void(double, SomeObject*)> callback;
```

可以包装任何符合该签名的可调用对象：普通函数、lambda、绑定的成员函数。是回调系统常用的存储类型，有一定运行时开销，用于热路径时需要注意。

---

## 并发基础

### mutex 与 lock_guard

```cpp
std::mutex m;

void DoSomething()
{
    std::lock_guard<std::mutex> lock(m);
    // 临界区
}  // lock 析构，自动解锁
```

`lock_guard` 是 RAII 在锁上的应用，不需要手动解锁，异常安全，优先使用它而不是手写 `lock / unlock`。

某些场景下会看到 `recursive_mutex`，用于同一线程可能递归进入同一临界区的情况——普通 `mutex` 在这种情况下会死锁。

### atomic

```cpp
std::atomic<unsigned int> counter;
++counter;  // 线程安全的自增
```

用于简单的计数器场景，比 `mutex` 轻量。

---

## 如何读一个陌生的类

进入实际项目后，对每个陌生的类问自己 5 个问题：

1. **谁创建它？** 找构造函数在哪里被调用
2. **谁持有它？** 看谁持有它的指针或智能指针
3. **生命周期多长？** 析构函数何时执行
4. **是否使用多态？** 虚函数的真实实现在哪个子类
5. **是否涉及线程安全？** 有没有锁，锁保护的范围是什么

---

## 能力检验

- 看到 `unique_ptr` 作为函数参数，清楚所有权在调用后如何转移
- 看到带捕获列表的 lambda，知道它能访问哪些外部变量，以及潜在的生命周期风险
- 看到虚函数调用，能用调试器定位到真正执行的派生类实现
- 看到含模板与回调的头文件，能逐段读下去

---

## CMake：构建系统入门

### 它解决什么问题

写一个文件用 `g++ hello.cpp -o hello` 编译完全够用。但真实项目通常有几十乃至几百个 `.cpp` 文件，还会依赖各种第三方库，不同成员可能分别用 Windows、Linux、macOS 开发。这时候靠手写编译命令已经不现实——**CMake 就是用来描述"这个项目该怎么编译"的工具**。

CMake 本身不是编译器，它读取你写的构建描述文件（`CMakeLists.txt`），然后生成对应平台的构建文件：Windows 上生成 Visual Studio 项目，Linux 上生成 Makefile 或 Ninja 构建文件，再交给编译器去实际编译。

```
CMakeLists.txt
      │
      ▼
    CMake
      │
      ├── Windows → Visual Studio .sln / .vcxproj
      └── Linux   → Makefile / build.ninja
                        │
                        ▼
                    g++ / MSVC（实际编译）
```

读开源项目或接手别人的代码时，项目根目录里有 `CMakeLists.txt` 是常态，看懂它才能知道这个项目是如何组织的。

### CMakeLists.txt 基本结构

一个最简单的单文件项目：

```cmake
cmake_minimum_required(VERSION 3.16)   # 要求的 CMake 最低版本
project(MyApp)                         # 项目名称

set(CMAKE_CXX_STANDARD 17)             # 使用 C++17 标准

add_executable(MyApp main.cpp)         # 生成一个可执行文件，源文件是 main.cpp
```

多个源文件：

```cmake
add_executable(MyApp
    main.cpp
    engine.cpp
    utils.cpp
)
```

引入第三方库（以 CMake 内置的 find_package 为例）：

```cmake
find_package(SomeLib REQUIRED)

target_link_libraries(MyApp PRIVATE SomeLib::SomeLib)
```

### 如何构建项目

CMake 的标准流程分两步：**配置**和**构建**，必须在单独的构建目录里操作（不要在源码目录里直接运行 CMake，会污染源码）。

**Linux / macOS：**

```bash
cmake -S . -B build   # 配置：-S 指定源码目录，-B 指定构建目录
cmake --build build   # 构建：实际编译
```

**Windows（Visual Studio 直接打开）：**

VS 2022 支持直接打开包含 `CMakeLists.txt` 的文件夹（`文件 → 打开 → 文件夹`），会自动识别并配置，不需要手动生成项目文件。这是 Windows 上处理 CMake 项目最省事的方式。

**Windows（命令行）：**

```bash
cmake -S . -B build -G "Visual Studio 17 2022"
cmake --build build --config Debug
```

### Debug 与 Release

```bash
cmake -S . -B build -DCMAKE_BUILD_TYPE=Debug    # 包含调试信息，不优化
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release  # 开启优化，体积更小
```

开发阶段始终用 Debug 构建。如果发现断点无法命中、变量值显示异常，通常是误用了 Release 构建。

### 实战：从零搭一个多文件项目

下面用一个具体的例子把上面的内容串起来。目标是建一个包含两个 `.cpp` 文件的项目，编译后能运行。

**项目结构：**

```
myproject/
├── CMakeLists.txt
├── main.cpp
└── greeter.cpp
└── greeter.h
```

**greeter.h：**

```cpp
#pragma once
#include <string>

std::string Greet(const std::string& name);
```

**greeter.cpp：**

```cpp
#include "greeter.h"

std::string Greet(const std::string& name)
{
    return "Hello, " + name + "!";
}
```

**main.cpp：**

```cpp
#include <iostream>
#include "greeter.h"

int main()
{
    std::cout << Greet("world") << std::endl;
    return 0;
}
```

**CMakeLists.txt：**

```cmake
cmake_minimum_required(VERSION 3.16)
project(MyProject)

set(CMAKE_CXX_STANDARD 17)

add_executable(MyProject
    main.cpp
    greeter.cpp
)
```

**构建并运行（Linux）：**

```bash
cmake -S . -B build -DCMAKE_BUILD_TYPE=Debug
cmake --build build
./build/MyProject
# 输出：Hello, world!
```

**构建并运行（Windows，Visual Studio 打开文件夹）：**

1. `文件 → 打开 → 文件夹`，选择 `myproject/`
2. VS 自动检测到 `CMakeLists.txt` 并完成配置
3. 顶部工具栏选择 `MyProject.exe`，按 `F5` 运行

### 遇到陌生 CMake 项目时的处理流程

1. 看根目录的 `CMakeLists.txt`，找 `project()` 确认项目名，找 `add_executable` 或 `add_library` 确认会生成什么
2. 看有没有 `README`，通常会写构建步骤
3. 按标准流程 `cmake -S . -B build` → `cmake --build build` 尝试构建
4. 构建报错时，优先看第一条错误，后续错误通常是连锁反应
