---
title: vue 面试题
date: 2025-09-28T18:19:00.000Z
categories: 
  - 前端
  - 面试
tags:
  - 前端
  - 面试
  - Vue
index_img: images/1749179465178.png
published: false
---

# Vue 面试题

## 前言

Vue.js 是目前最流行的前端框架之一，在前端面试中经常被问到。本文整理了一些常见的 Vue 面试题，帮助大家更好地准备面试。

## 基础篇

### 1. 什么是 Vue.js？

Vue.js 是一套用于构建用户界面的渐进式 JavaScript 框架。与其它大型框架不同的是，Vue 被设计为可以自底向上逐层应用。Vue 的核心库只关注视图层，不仅易于上手，还便于与第三方库或既有项目整合。

### 2. Vue 的核心特性有哪些？

- **数据驱动视图**：通过简单的 API 实现数据绑定
- **组件化开发**：可复用的组件让代码更易维护
- **虚拟 DOM**：提升渲染性能
- **指令系统**：提供常用的指令如 v-if、v-for、v-bind、v-on 等
- **轻量级**：体积小，易于集成

### 3. Vue 实例的生命周期

Vue 实例从创建到销毁的过程称为生命周期，主要分为以下几个阶段：

1. **创建前/后**：beforeCreate / created
2. **挂载前/后**：beforeMount / mounted
3. **更新前/后**：beforeUpdate / updated
4. **销毁前/后**：beforeDestroy / destroyed

### 4. computed 和 watch 的区别

- **computed**：计算属性，依赖其他属性计算得出，有缓存机制，只有依赖改变时才会重新计算
- **watch**：监听属性，监听某个属性的变化，执行相应的回调函数，适用于异步操作或开销较大的操作

## 进阶篇

### 1. Vue 组件间通信方式有哪些？

- **props / $emit**：父子组件通信
- **$parent / $children**：访问父/子实例
- **ref**：访问组件实例
- **EventBus**：中央事件总线
- **provide / inject**：跨层级组件通信
- **Vuex**：状态管理

### 2. Vue 的响应式原理

Vue 2.x 使用 Object.defineProperty() 劫持各个属性的 setter/getter，在数据变动时发布消息给订阅者，触发相应的监听回调。Vue 3.x 使用 Proxy 代替 Object.defineProperty()，性能更好，支持监听数组索引等。

### 3. Virtual DOM 是什么？

Virtual DOM 是一个 JavaScript 对象，用来描述真实的 DOM 结构。通过对比新旧 Virtual DOM 树的差异，最小化地更新真实 DOM，从而提升性能。

## Vuex 状态管理

### 1. 什么是 Vuex？

Vuex 是 Vue.js 应用程序开发的状态管理模式。它采用集中式存储管理应用的所有组件的状态，并以相应的规则保证状态以一种可预测的方式发生变化。

### 2. Vuex 的核心概念

- **State**：存储应用状态
- **Getter**：从 state 中派生出一些状态
- **Mutation**：更改 Vuex 中的 state 的唯一方法
- **Action**：提交 mutation，可以包含任意异步操作
- **Module**：将 store 分割成模块

## Vue Router

### 1. Vue Router 的两种模式

- **hash 模式**：通过 URL 的 hash 变化进行路由，不会向服务器发送请求
- **history 模式**：利用 history.pushState() API 完成 URL 跳转，需要服务器配置支持

### 2. 导航守卫有哪些？

- **全局前置守卫**：router.beforeEach
- **全局解析守卫**：router.beforeResolve
- **全局后置钩子**：router.afterEach
- **路由独享守卫**：beforeEnter
- **组件内守卫**：beforeRouteEnter、beforeRouteUpdate、beforeRouteLeave

## 实战篇

### 1. 如何优化 Vue 应用的性能？

- 合理使用 v-show 和 v-if
- 为 v-for 添加 key
- 路由懒加载
- 第三方插件按需引入
- 合理使用 keep-alive 缓存组件
- 使用 Object.freeze 冻结不需要响应的数据

### 2. Vue 项目如何进行 SEO 优化？

- 使用服务端渲染（SSR）方案如 Nuxt.js
- 预渲染（Prerendering）
- 合理设置 meta 标签
- 使用 SSR 友好的 meta 信息管理库

## 总结

以上是一些常见的 Vue 面试题，涵盖了基础概念、核心原理、状态管理和路由等方面。掌握这些知识点，能够帮助你在面试中更好地展示自己的 Vue 技能。

> 持续更新中...