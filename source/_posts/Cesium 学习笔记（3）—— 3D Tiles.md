---
title: Cesium 学习笔记（3）—— 3D Tiles
date: 2025-09-30T15:25:00.000Z
tags: 
  - 前端
  - cesium
  - gis
categories: 
  - 前端
  - 面试
published: false
---

摘要：

> 本文旨在帮助前端或 GIS 开发者全面掌握 Cesium 中的 3D Tiles 技术，既能熟练使用，也能轻松应对各类面试题。

## 什么是 3d Tiles ？

官网介绍：https://cesium.com/why-cesium/3d-tiles/

### 🧠 概念
3D Tiles 是一种用于 **流式加载和可视化海量异构三维地理空间数据集的开放标准格式/规范**，包括建筑物、树木、点云和矢量数据等，由 Cesium 团队提出并被 OGC 采纳为正式标准。

- 目标：在浏览器中高效展示城市级别三维场景。
- 核心思想：**分块 + 层级 + 按需加载**。

### 🏗 背景
传统 glTF/OBJ 在面对城市级模型时存在显著性能瓶颈。
3D Tiles 提供了一种空间分块与 LOD 管理机制，让海量模型的传输和渲染速度大大提升，从而提升用户体验。

--- 

## 3D Tiles 规范与版本演进（OGC 标准）
- 3D Tiles 1.0: 3D Tiles 规范 1.0 版本已提交至开放地理空间联盟（OGC），并于 2018 年 12 月 14 日被批准为 OGC 社区标准
- 3D Tiles 1.1: 2023年发布
  - 新增功能：
    - 支持可与瓦片集、瓦片、瓦片内容以及瓦片内容组相关联的结构化元数据
    - 直接支持将 glTF 资产作为瓦片内容
    - 支持多个瓦片内容
    - 支持隐式瓦片方案
  - 弃用功能：
    - 原始瓦片格式（b3dm、i3dm、pnts 和 cmpt）已被弃用，推荐使用 glTF 内容
    - tileset.properties 已被弃用，推荐使用更通用的元数据支持

> 详情参阅: [Version History](https://github.com/CesiumGS/3d-tiles?tab=readme-ov-file#version-history)

---

## 3D Tiles 的数据结构（参考官网文章）
  异构？

---

## 与其他格式（glTF / GeoJSON / OBJ）的对比

---

## 3D Tiles 的加载流程

---

## 3D Tiles 的渲染流程

---

## LOD 机制详解（参考官网文章及gpt之前给的分析结果）

---

## 3D Tiles 的使用场景

---

## 3D Tiles 的优缺点

---

## 格式转换（OBJ ⇋ 3D Tiles）

---

## 性能优化思路（代码层 + 模型层）

---

## 模型调优与实践经验

---

## 高频面试题总结

---

## 总结与参考资料