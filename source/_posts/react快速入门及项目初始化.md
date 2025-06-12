---
title: react快速入门及项目初始化
date: 2025-06-11T10:26:46.000Z
tags: 
  - 前端
  - react
  - 工程化
index_img: ![查看访问地址](https://silengzi.github.io/cube-fluid-blod/images/06801c81bb61b9e4010e4d53e2f489b.png)
---

## 简介

react 是由 facebook 团队内部开发并维护的前端框架，属于当前前端三大主流框架之一。
相比于我们常用的 vue 来说，vue 更适合开发一些中小型项目尤其是小项目（配置简单），学习成本更低，且在国内中小型企业中流行度非常高，而 react 则更偏向于做中大型项目，在国内大厂和国外流行度更高。

官方文档：[Homepage](https://react.docschina.org/)

## 基本语法

先来简单了解下 react 中几个比较重要的概念和用法。

#### JSX语法

一句话解释 JSX，其实就是 JavaScript 的语法扩展，使得在 js 中也可以编写 html。

例如，在以前写原生的前端可能就是 .html 文件 + .js 文件，在 .vue 模板中，也是通过 template 和 script 标签来区分 js 和 html 代码的，但在 .jsx 文件中我们可以这样写：

```jsx
const element = <h1>Hello, world!</h1>;

const list = [1, 2, 3];
const items = (
  <ul>
    {list.map(item => <li key={item}>{item}</li>)}
  </ul>
);
```

遇到 <></> 这样的标签符号，它就知道你写的是一个html，而遇到 {} 时，则又能知道你开始写 js 表达式 了。比如上面在 ul 标签中写的 {list.map...} 就是用 js 的 map 方法，遍历返回了 3 个 li 标签，最终渲染结果应该是：

```html
<ul>
  <li key="1">1</li>
  <li key="2">2</li>
  <li key="3">3</li>
</ul>
```

#### 函数式组件

react 中定义组件的方式非常简单，在 jsx 文件中像如下方式导出一个函数就可以了。

```jsx
export default function MyApp() {
  return (
    <div>
      <h1>Welcome to my app</h1>
      <MyButton />
    </div>
  );
}
```

要注意该函数要满足以下几个特点：

1. 函数名必须大写（组件名一般都是大写，跟 html 原生标签做区分）
2. 只能有一个根标签，如上面例子中的跟标签为 div 。

因为 jsx 就是 js 的增强，本质上跟 js 差不多，所以编写函数式组件就跟写 js 一样很舒服，你可以在任何位置编写 js 逻辑，最终导出一个返回 dom 元素的方法即可。

#### 绑定类名

react 中绑定类名要使用 className 而不能用 class，因为在 react 里 class 用作保留字了，这个可以不用深究，记住绑定类名时用 className 就可以了。

```jsx
<img className="avatar" />
```

#### 条件渲染

react 中没有 v-if 这种语法，假如我们需要根据不同的条件来渲染不同的组件，可以这样写：

```jsx
export default function MyApp() {
  let button;
  if (isLoggedIn) {
    button = <LoginButton />;
  } else {
    button = <RegisterButton />;
  }
  return (
    <div>
      <h1>Welcome to my app</h1>
      { button }
    </div>
  );
}
```

是不是跟写一般的 js 一样简单。

#### 列表渲染

列表渲染也同理，没有 v-for，而是跟写 js 一样：

```jsx
export default function MyApp() {
  const products = [
    { title: 'Cabbage', id: 1 },
    { title: 'Garlic', id: 2 },
    { title: 'Apple', id: 3 },
  ];

  const listItems = products.map(product => {
    return <li key={product.id}>
      {product.title}
    </li>
  });

  return (
    <div>
      <h1>Welcome to my app</h1>
      <ul>
        {listItems}
      </ul>
    </div>
  );
}
```

listItems 其实就是数组的 .map 方法返回的一个新的数组，其中每一个元素都是一个 li 标签。

#### 数据驱动

像 vue 中的 v-model 这种，当你修改数据时，页面上对应的引用也会发生变化。

在 react 中则是用 useState 实现的，示例如下：

```jsx
import { useState } from 'react';

function MyButton() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return (
    <button onClick={handleClick}>
      Clicked {count} times
    </button>
  );
}
```

关键部分就是 const [count, setCount] = useState(0);

这实际上就是一个 es6 的数组解构语法，左侧固定为两个变量（命名随意，可以叫任何名字，都是变量名而已），右侧 useState 括号中的值其实就是默认赋值。

简单点说，count 就是你要用的变量，值为 0 ，setCount 则是修改 count 的方法。

第一个（count）就是需要在页面中引用的变量，而第二个变量（setCount）则是专门用来修改 count 的方法，也就是说如果我们需要实现更新数据后页面自动更新这种效果，就要用 setCount 方法来修改数据。

当然如果是一般的变量，不需要在页面上自动更新，那也就不需要使用 useState 来定义了，用原生 js 的方式即可。

#### 事件绑定

绑定点击事件（onClick属性），这个很简单，就直接看示例吧：

```jsx
import { useState } from 'react';

function MyButton() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return (
    <button onClick={handleClick}>
      Clicked {count} times
    </button>
  );
}
```

其他事件同理，如：onMouseEnte、onKeyDown、onDoubleClick 等。

## 环境准备
## 开始
## 项目结构
#### 布局
#### 路由
#### 请求
#### 通用代码
#### 引入**依赖
#### 测试文件
#### 等等......
## 配置
#### 代理
#### 等等......
## 总结



`Homepage` 是一个现代优雅的个人主页项目，具有流体动画背景、响应式设计和流畅的页面过渡效果，让我们可以轻松搭建出炫酷的个人主页。

官方文档：[Homepage](https://github.com/SimonAKing/HomePage)

[在线预览](http://simonaking.com)

效果图
--

![预览效果](https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExMncyb3oyc21zc3czejU3cGk4M2tiNTdkaTM0N3FodGVpZmU5azNxaCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/fhXFCZEogq39rOpKUi/giphy.gif)

是不是很酷炫，打开的一瞬间，让人眼前一亮。下面我们就来看一下是怎么搭建的。

## 安装

```bash
# 克隆项目
git clone https://github.com/SimonAKing/HomePage.git
cd HomePage

# 安装依赖
npm install

# 启动项目
npm run dev
```

## 项目结构

先来看一下项目结构，一共分为两大类：
1. `intro` 首屏，就是刚打开后显示的页面
2. `main` 副屏，下拉显示的页面

相应的配置也是根据此标准来组织的。

## 基本配置

直接修改配置文件 `config.json` 就好，配置也不多，其中的每一个键名，都是其字面意思，见名知意。例如：

```json
{
  "head": {
    "title": "SimonAKing",
    "description": "Category:Personal Blog",
    "favicon": "favicon.ico"
  }
}
```

这就是配置页面 head 信息，就是这里：

![head](https://silengzi.github.io/cube-fluid-blod/images/image-20250605160304200.png)

## 高级配置

主屏的背景效果如需关闭，可以设置 `intro.background: false`。

配置中默认开启了 `supportAuthor` 选项，即支持作者。

开启支持作者时：
1. 会在首页右上角显示项目作者的 github 链接
2. 控制台会打印作者的站点信息

如需关闭，可以设置 `intro.supportAuthor: false`。

## 项目部署

这里我直接部署到Github Pages了，非常方便，在项目根目录下创建如下的目录和文件，`static.yml` 内容在后面。

```bash
.github/
└── workflows/
    └── static.yml
```

```static.yml
# Simple workflow for deploying static content to GitHub Pages
name: Deploy static content to Pages

on:
  # Runs on pushes targeting the default branch
  push:
    branches: ["main"]

  # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:

# Sets permissions of the GITHUB_TOKEN to allow deployment to GitHub Pages
permissions:
  contents: read
  pages: write
  id-token: write

# Allow only one concurrent deployment, skipping runs queued between the run in-progress and latest queued.
# However, do NOT cancel in-progress runs as we want to allow these production deployments to complete.
concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  # Single deploy job since we're just deploying
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - name: Setup Pages
        uses: actions/configure-pages@v5
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          # Upload entire repository
          path: 'dist'
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

有了这个工作流配置文件，就能自动部署喽~

稍等一会后，可以在这里查看访问地址：

![查看访问地址](https://silengzi.github.io/cube-fluid-blod/images/023550cf64cb48b5ec17354a8b7f1fd.png)

![真是辛苦我了](https://silengzi.github.io/cube-fluid-blod/images/006APoFYly8h3e81seuavg30k00k0jxz.gif)

## 最后

最后放一下我自己搭建的个人主页吧。

[四棱子](https://silengzi.github.io/HomePage/)
