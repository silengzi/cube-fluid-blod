---
title: 【2025】Typora免费下载安装永久激活教程图解
date: 2025-10-23T13:53:00.000Z
categories: 
  - 开发工具
  - 教程
tags:
  - Typora
  - 数据库
  - 开发工具
  - 教程
index_img: images/u=2045594280,2556420585&fm=202.png
---

> 使用 [Markdown](https://zhida.zhihu.com/search?content_id=262555905&content_type=Article&match_order=1&q=Markdown&zhida_source=entity) 写文章、做笔记的同学应该都听说过 Typora。  
> Typora 是一款由 [Abner Lee](https://zhida.zhihu.com/search?content_id=262555905&content_type=Article&match_order=1&q=Abner+Lee&zhida_source=entity) 开发的轻量级 Markdown 编辑器，采用所见即所得的编辑方式，适用于 OS X、Windows 和 Linux 三种操作系统

## 第一步：下载软件

下载这一步很关键，一定要下对版本，目前教程只支持 1.9.5 及以前的版本

### 1.安装包及补丁下载:

[https://pan.baidu.com/s/1Uj4C1p45HhaODEmryyNxRg?pwd=c6e8](https://pan.baidu.com/s/1Uj4C1p45HhaODEmryyNxRg?pwd=c6e8)

### 2.安装包下在不含激活补丁

[1.9.5 官网安装包下载链接直达](https://typoraio.cn/releases/all)

点击后选择图中的 1.9.5 的版本，windows64 位

![](https://pic4.zhimg.com/v2-e63732e4e09e66358085f31244ad1715_1440w.jpg)

## 第二步：安装软件

安装软件这一步很简单，除了修改下安装路径（最好不要放在 C 盘），直接一直下一步即可

![](https://pic1.zhimg.com/v2-985a86c4a33836dd4e3f4868d722aad4_1440w.jpg)

安装成功后，打开软件你会看到下面界面

![](https://pic3.zhimg.com/v2-89cc3d95adf2be8523d477e35d0df92e_1440w.jpg)

先不要关闭软件，下面开始我们的激活操作

## 第三步：下载工具

工具已经替大家整理好了，其中也包括下载好的 windows64 位 1.9.5 版本的 exe 应用程序

![](https://pic1.zhimg.com/v2-664445bcb12e6dd62f92cd19bd1993fc_1440w.jpg)

## 第四步：开始激活准备

打开下载后的文件夹，将其中的 [license-gen.exe](https://zhida.zhihu.com/search?content_id=262555905&content_type=Article&match_order=1&q=license-gen.exe&zhida_source=entity) 和 [node\_inject.exe](https://zhida.zhihu.com/search?content_id=262555905&content_type=Article&match_order=1&q=node_inject.exe&zhida_source=entity) 复制到 Typora 安装目录下

比如我的安装目录是“D:\\Programs\\Typora”，复制后如下图

![](https://pic3.zhimg.com/v2-cd7a5b6401c613fb7326e6bc52aa045a_1440w.jpg)

复制完成后，在当前目录下打开命令行，如下图

![](https://pic4.zhimg.com/v2-04c84990d3c6555db729204690cb6079_1440w.jpg)

然后输入“node\_inject.exe”，回车执行，执行成功后，会出现下方的输出信息，出现 done!即代表成功

![](https://pic2.zhimg.com/v2-24f392d7e88b3c3650ce4b885550404b_1440w.jpg)

在当前命令行窗口，再继续输入“license-gen.exe”命令，回车执行，执行成功后，会出现一串序列号，复制下来，这就是我们等会要激活的时候输入的序列号

![](https://pic1.zhimg.com/v2-47da4d14bae7f30f98b0610099a55da6_1440w.jpg)

## 第五步：激活 Typora

先将 Typora 关闭（楼主亲测第一次激活会失败，必须关闭软件重新打开才能激活）

再次打开 Typora，进入激活弹窗界面，输入邮箱（可以随便输，但是要符合邮箱格式，例如：123@123.com 都可以）

然后输入我们刚才生成的序列号

![](https://picx.zhimg.com/v2-0cab586b5e9fd4b626deef3d8572bb7d_1440w.jpg)

**点击激活，成功激活**

![](https://pic2.zhimg.com/v2-91f11b1753b32609950432f0914b6c11_1440w.jpg)

![](https://pic2.zhimg.com/v2-f9ba14f3551002c731204030b969f6f7_1440w.jpg)

## 常见问题，提前为你解答！

### 提示序列号无效

> 安装后，破解完成后，没有关闭软件重新打开，如果第一次提示序列号无效，关闭 Typora 重新打开，重新输入邮箱和序列号即可（注意：不需要重新执行补丁程序）

### cmd 执行出现错误

如果你 cmd 执行 node\_inject.exe 出现以下错误

> nodeinject 结果 thread 『main』 panicked at 『called \`Result::unwrap()\` on an \`Err\` value: IoError(Os { code: 5, kind: PermissionDenied, message: 「拒绝访问。」 })  

说明你不是管理员用户，可以用管理员权限打开 cmd，cd 到 Typora 的安装目录下再执行，或者直接右键选中 node\_inject.exe，以管理员身份运行

### 关闭软件后，重新打开，还是一直报序列号无效

> 确定下自己的 Typora 版本对不对，目前此教程只支持 Typora1.9.5 及以前的版本，1.10.x 之后的版本不支持哈