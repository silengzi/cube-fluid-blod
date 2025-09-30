---
title: Cesium 学习笔记（2）—— 坐标系
date: 2025-09-29T11:54:00.000Z
tags: 
  - 前端
  - cesium
  - gis
categories: 
  - 前端
  - 面试
published: true
---


在 Cesium 开发中，**坐标系及其转换**是一个高频且核心的知识点。掌握这些知识不仅是进行 Cesium 开发的基础，也有助于深入理解三维地理信息系统的核心概念。下面我将系统地梳理 Cesium 中的坐标体系、常用类型、转换方法及注意事项。

---

## 一、传统 GIS 概念中的坐标系

首先了解下 GIS（地理信息系统） 中的坐标系。在GIS中，坐标系是用于定义地理要素在地球表面或地图上位置的基础框架。主要可以分为两大类：地理坐标系（Geographic Coordinate System, GCS）和投影坐标系（Projected Coordinate System, PCS）。此外，还有局部坐标系等特殊类型。

### 1. 地理坐标系（Geographic Coordinate System）

地理坐标系使用三维球面来定义地球上的位置，通常用**经度（Longitude）**和**纬度（Latitude）**表示，单位为**度（°）**。它基于一个**大地基准面（Datum）**和一个**参考椭球体（Ellipsoid）**来描述地球的形状。

- **组成要素**：
  - **参考椭球体**：如WGS84、CGCS2000、GRS80等。
  - **大地基准面**：定义椭球体与地球实际表面的关系，如WGS84、北京54、西安80等。
  - **本初子午线**：通常为格林尼治子午线（0°经线）。
  - **角度单位**：通常为度。

- **常见示例**：
  - WGS84（World Geodetic System 1984）：全球通用，GPS系统使用。
  - CGCS2000（中国2000国家大地坐标系）：中国现行国家标准。
  - Beijing 1954、Xian 1980：中国早期使用的坐标系。

### 2. 投影坐标系（Projected Coordinate System）

由于地球是球体，而地图是平面，因此需要通过**地图投影**将地理坐标转换为平面直角坐标。投影坐标系是在地理坐标系基础上，通过数学方法投影到平面上的二维坐标系统，单位通常为**米（m）**或**英尺（ft）**。

- **组成要素**：
  - 基础地理坐标系
  - 投影方法（如高斯-克吕格投影、UTM、墨卡托等）
  - 中央经线、标准纬线、比例尺因子、东偏/北偏等参数

- **常见投影类型**：
  - **高斯-克吕格投影（Gauss-Krüger）**：中国常用，按6°或3°分带。
  - **UTM（Universal Transverse Mercator）**：全球通用，适用于中纬度地区。
  - **墨卡托投影（Mercator）**：常用于Web地图（如Google Maps），保持方向和形状。
  - **兰勃特投影（Lambert）**：适用于中纬度东西延伸区域。

- **坐标单位**：米（m），便于距离、面积计算。

### 3. 局部坐标系（Local Coordinate System）

用于小范围工程测量或特定项目，原点为任意设定点，不与全球或国家坐标系对齐。常用于建筑、矿区、工地等场景。

---

### 对比表：

| 类型 | 维度 | 单位 | 示例 | 用途 |
|------|------|------|------|------|
| 地理坐标系（GCS） | 三维球面 | 度（°） | WGS84, CGCS2000 | 定位、GPS、全球数据 |
| 投影坐标系（PCS） | 二维平面 | 米（m） | Xian80 / 3-degree Gauss | 地图制图、空间分析 |
| 局部坐标系 | 二维或三维 | 米（m）或自定义 | 工程坐标系 | 工程测量、局部建模 |

---

> 补充：其实还有地心地固坐标系（笛卡尔空间直角坐标系），既不属于地理坐标系，也不属于投影坐标系，只是传统 GIS 教学或应用中常简化为“地理 与 投影”，且用户对这类坐标系的感知也较弱。更完整的坐标系分类可参考如下：
```text
地球空间坐标系
├── 1. 曲面坐标系（Curvilinear）
│   └── 地理坐标系（Lon/Lat/Height）
│
├── 2. 投影平面坐标系（Projected Planar）
│   └── 各种地图投影（UTM, Web Mercator 等）
│
└── 3. 空间直角坐标系（Spatial Cartesian）
    ├── 地心地固坐标系（ECEF, X/Y/Z）
    └── 局部空间直角坐标系（ENU, X/Y/Z）
```

---

<!-- **提示**：在GIS软件（如ArcGIS、QGIS）中，正确设置和转换坐标系至关重要，否则会导致位置偏移、叠加错误等问题。例如，中国常用的CGCS2000_3_Degree_GK_Zone_38就是一个投影坐标系，基于CGCS2000地理坐标系，采用3度高斯投影。 -->

## 二、Cesium 中的四大核心坐标系

了解完 GIS 中的坐标系后，再来看 Cesium 中的几种坐标系。Cesium 使用了多种坐标系来满足不同场景的需求，主要可以分为以下四类：

### 1. **WGS84 地理坐标系（Geographic Coordinate System）**

- **定义**：基于 WGS84 参考椭球体的三维球面坐标系统，使用经度（Longitude）、纬度（Latitude）和高度（Height）表示地球表面的位置。
- **格式**：`[经度, 纬度, 高度]`
  - 经度范围：`-180° ~ +180°`（东经为正）
  - 纬度范围：`-90° ~ +90°`（北纬为正）
  - 高度：相对于 WGS84 椭球面的高度（单位：米），**不是海拔高程**。
- **特点**：
  - 可读性强，适合输入 GPS 坐标或地图标记。
  - Cesium 内部不直接使用角度值，而是以**空间直角坐标`Cartesian3`**存储地理坐标。

#### 📌 核心对象：`Cartographic`

```js
// 创建弧度制地理坐标（注意：参数是弧度）
const cartographic = new Cesium.Cartographic(
  Cesium.Math.toRadians(116.3),  // 经度（弧度）
  Cesium.Math.toRadians(39.9),   // 纬度（弧度）
  1000                           // 高度（米）
);

// 推荐方式：直接用角度创建
const cartographic = Cesium.Cartographic.fromDegrees(116.3, 39.9, 1000);
```

> ⚠️ 注意：`WGS84` 只是用于输入地理坐标，属于应用层面的概念，便于我们输入地理坐标，可根据需要换成其他坐标系。Cesium 底层会将其转换成笛卡尔空间直角坐标，再进行计算。

---

### 2. **地心地固坐标系（ECEF - Earth-Centered, Earth-Fixed）**

- **别名**：笛卡尔空间直角坐标系（`Cartesian3`）
- **定义**：以地球质心为原点的三维笛卡尔坐标系。
- **轴向**：
  - `X` 轴：指向本初子午线与赤道交点（0° 经度，0° 纬度）
  - `Y` 轴：指向东经 90° 与赤道交点
  - `Z` 轴：指向北极（与地球自转轴一致）
- **构成右手坐标系**。
- **用途**：
  - 所有三维空间计算（如距离、平移、旋转、碰撞检测）都在此坐标系下进行。
  - 是 Cesium 内部渲染和计算的核心坐标系。

#### 📌 核心对象：`Cartesian3`

```js
// 创建笛卡尔坐标
const position = new Cesium.Cartesian3(x, y, z);

// 从地理坐标（角度）转换
const cartesian = Cesium.Cartesian3.fromDegrees(116.3, 39.9, 1000);

// 从地理坐标（弧度）转换
const cartesian = Cesium.Cartesian3.fromRadians(
  Cesium.Math.toRadians(116.3),
  Cesium.Math.toRadians(39.9),
  1000
);
```

---

### 3. **东-北-上局部坐标系（ENU - East-North-Up）**

- **定义**：以某一点为原点的局部笛卡尔坐标系，用于描述相对于该点的方向。
- **轴向**：
  - `X` 轴：指向**东（East）**
  - `Y` 轴：指向**北（North）**
  - `Z` 轴：指向**上（Up）**，垂直于椭球面
- **用途**：
  - 控制模型姿态（如飞机朝向）
  - 局部移动、偏移计算（如“向东移动 100 米”）

#### 📌 转换方法：通过 `Transforms.eastNorthUpToFixedFrame`

```js
// 定义原点（地理坐标）
const origin = Cesium.Cartesian3.fromDegrees(116.3, 39.9);

// 获取 ENU 到 ECEF 的变换矩阵
const enuToEcef = Cesium.Transforms.eastNorthUpToFixedFrame(origin);

// 应用变换（例如：向东 100m，向北 50m）
const localOffset = new Cesium.Cartesian3(100, 50, 0); // ENU 偏移
const globalPosition = new Cesium.Cartesian3();
Cesium.Matrix4.multiplyByPoint(enuToEcef, localOffset, globalPosition);
```

---

### 4. **屏幕坐标系（Screen Coordinate System）**

- **定义**：二维坐标系，用于表示屏幕上的像素位置。
- **原点**：Canvas 左上角 `(0, 0)`
- **方向**：
  - `X` 向右为正
  - `Y` 向下为正
- **单位**：像素（px）
- **用途**：
  - 处理鼠标事件（点击、拖拽）
  - 添加 HUD 元素、标签定位

#### 📌 核心对象：`Cartesian2`

```js
// 获取鼠标点击的屏幕坐标
const handler = new Cesium.ScreenSpaceEventHandler(viewer.scene.canvas);
handler.setInputAction(function(click) {
  const windowPosition = click.position; // Cartesian2 类型
  console.log(`屏幕坐标: (${windowPosition.x}, ${windowPosition.y})`);
}, Cesium.ScreenSpaceEventType.LEFT_CLICK);
```

---

## 三、常见问题与回答

### ❓ Q1: Cesium 中有哪些坐标系？它们的区别是什么？

> **答**：主要有四种：
>
> 1. **WGS84 地理坐标系**：用经纬度表示位置，适合人类阅读；
> 2. **地心地固坐标系（ECEF/Cartesian3）**：以地心为原点的三维直角坐标，用于所有空间计算；
> 3. **东-北-上局部坐标系（ENU）**：以某点为原点的局部坐标，用于模型姿态控制；
> 4. **屏幕坐标系（Cartesian2）**：表示屏幕像素位置，用于交互和 UI 定位。

---

### ❓ Q2: 如何将经纬度转为 Cartesian3？

> **答**：使用 `Cesium.Cartesian3.fromDegrees(longitude, latitude, height)` 方法，它会自动将角度转为弧度并计算出对应的 ECEF 坐标。

---

### ❓ Q3: Cartesian3 能否直接转为经纬度？如何转？

> **答**：不能直接得到角度经纬度。需要先用 `Cesium.Cartographic.fromCartesian(cartesian3)` 得到弧度制的地理坐标，再用 `Cesium.Math.toDegrees()` 转为角度。

---

### ❓ Q4: 如何实现“在某个点向东移动 100 米”？

> **答**：使用 ENU 局部坐标系：
>
> 1. 获取该点的 ENU 到 ECEF 的变换矩阵；
> 2. 在 ENU 坐标中设置偏移 `(100, 0, 0)`；
> 3. 使用矩阵变换得到新的 ECEF 坐标。

---

## 总结

| 坐标系 | 对象 | 用途 | 是否用于计算 |
|-------|------|------|-------------|
| WGS84 地理坐标 | `Cartographic` | 人类输入/输出 | ❌ |
| 地心地固坐标 | `Cartesian3` | 空间计算、渲染 | ✅（核心） |
| 局部坐标（ENU） | 矩阵变换 | 模型姿态、局部移动 | ✅ |
| 屏幕坐标 | `Cartesian2` | 鼠标交互、UI | ✅ |
