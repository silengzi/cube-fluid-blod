---
title: Cesium 学习笔记（一）—— 坐标
date: 2025-08-28T15:51:00.000Z
tags: 
  - 前端
  - cesium
  - gis

---

## 前言

想学`Cesium开发`，你如果对一些GIS基础，特别是`坐标系`概念不了解的话，会让你非常难受，今天我们就来聊聊`WebGiser`开发过程中常用到的一些坐标系概念。

## GIS坐标系

要熟悉Cesium中常用到的一些坐标类型以及它们之间是如何进行转换的，到了真正用到的时候可以再返回来细看，加深理解。

### 经纬度坐标（球面坐标）

经纬度坐标通常被称为`地理坐标`或`地球坐标`，它是一种基于地球表面的坐标系统，用于确定地球上任何点的位置。这种坐标系统使用两个主要的数值来表示位置：经度和纬度。

![](images/a6c5dd66235449b2b213732dbbdfcde8~tplv-73owjymdk6-jj-mark-v1_0_0_0_0_5o6Y6YeR5oqA5pyv56S-5Yy6IEAg5pS75Z-O5biI5LiN5rWq_q75.webp)

1.  **经度（Longitude）**：表示从本初子午线（通常通过英国伦敦的格林尼治天文台）向东或向西的角度距离。经度的范围是从 -180° 到 +180°，其中 0° 表示本初子午线。
    
2.  **纬度（Latitude）**：表示从赤道向北或向南的角度距离。纬度的范围是从 -90°（南极点）到 +90°（北极点），其中 0° 表示赤道。
    

经纬度坐标也常常被称为：

-   **球面坐标（Spherical Coordinates）**：因为地球近似为一个球体，经纬度坐标可以看作是在球面上确定点的位置。
    
-   **大地坐标（Geodetic Coordinates）**：在大地测量学中，这种坐标系统用于描述地球表面的点。
    
-   **WGS84坐标**：WGS84（World Geodetic System 1984）是一种广泛使用的全球地理坐标系统，它提供了一个标准化的参考框架，用于地理定位。
    

经纬度坐标广泛应用于地图制作、导航、地理信息系统（GIS）、航空和海洋导航等领域。在数字地图服务和应用程序中，经纬度坐标是最常见的位置表示方式之一。

### 地理坐标（弧度）

在地理信息系统（GIS）中，地理坐标通常指的是地球上某个点的位置，使用经纬度来表示。然而，由于地球是一个近似的椭球体，使用弧度而非角度来表示经纬度坐标可以避免在计算中引入的某些复杂性，尤其是在进行距离和面积的测量时。

![](images/1c690a561350428f8bf246dcf9169077~tplv-73owjymdk6-jj-mark-v1_0_0_0_0_5o6Y6YeR5oqA5pyv56S-5Yy6IEAg5pS75Z-O5biI5LiN5rWq_q75.webp)

弧度是一种角度的度量单位，它基于圆的周长和半径之间的关系。一个完整的圆周被定义为 2π弧度。弧度与角度的转换关系如下：

![](images/ab4b2043c0f247bdb79fa81dc91c12d7~tplv-73owjymdk6-jj-mark-v1_0_0_0_0_5o6Y6YeR5oqA5pyv56S-5Yy6IEAg5pS75Z-O5biI5LiN5rWq_q75.webp)

在GIS中，使用弧度的地理坐标可以简化一些数学运算，尤其是涉及到三角函数和地球曲率的计算。例如，计算两点之间的大圆距离（即地球表面的最短路径）时，使用弧度可以更直接地应用球面三角学公式。

地理坐标（弧度）的应用

1.  **距离计算**：使用球面三角学公式，可以更准确地计算出两点之间的距离。
    
2.  **方向计算**：确定从一个点到另一个点的方向，使用弧度可以简化计算过程。
    
3.  **地图投影**：在某些地图投影中，使用弧度可以更自然地处理地球表面的曲率。
    

### 屏幕坐标系

屏幕坐标系（Screen Coordinate System）是一种二维坐标系统，它用于描述屏幕上的点或区域的位置。屏幕坐标系通常以屏幕的左上角为原点，水平向右为 x 轴正方向，垂直向下为 y 轴正方向。

![](images/14b6eb55200048ecb25ac487aba10431~tplv-73owjymdk6-jj-mark-v1_0_0_0_0_5o6Y6YeR5oqA5pyv56S-5Yy6IEAg5pS75Z-O5biI5LiN5rWq_q75.webp)

屏幕坐标系在Cesium中叫做`二维笛卡尔`平面坐标。

```js
new Cesium.Cartesian2(x, y)
```

屏幕坐标系的特点：

1.  **原点位置**：屏幕坐标系的原点（0,0）位于屏幕的`左上角`。
    
2.  **正方向**：x 轴正方向向右，y 轴正方向向下。
    
3.  **单位**：通常使用像素（px）作为单位。
    
4.  **范围**：坐标值的范围取决于屏幕或窗口的大小。
    

### 空间直角坐标系

在地理信息系统（GIS）中，空间直角坐标系（Spatial Cartesian Coordinate System）是一种三维坐标系统，用于在三维空间中精确地表示点、线、面的位置。这种坐标系通常由三个正交的坐标轴组成：X、Y 和 Z 轴。

![](images/fa171ca043cc4718bad14059871fe5e5~tplv-73owjymdk6-jj-mark-v1_0_0_0_0_5o6Y6YeR5oqA5pyv56S-5Yy6IEAg5pS75Z-O5biI5LiN5rWq_q75.webp)

空间直角坐标系的特点：

1.  **正交性**：X、Y 和 Z 轴相互垂直，形成一个直角坐标系。
    
2.  **三维性**：可以表示三维空间中的任何位置，包括高度或深度信息。
    
3.  **标准化**：通常以地球的质心或某个参考点为原点，建立一个标准化的坐标系统。
    
4.  **应用广泛**：广泛应用于地理测量、城市规划、建筑设计、3D 建模等领域。
    

## Cesium中的坐标系

Cesium中支持两种坐标系：`3D笛卡尔坐标系`和`经纬度坐标系`；

### 3D笛卡尔坐标系

先来了解下笛卡尔空间直角坐标系，它的X、Y、Z三个轴的正方向如下图所示：

![](images/6374bd0a70554076a4611b7372d8060d~tplv-73owjymdk6-jj-mark-v1_0_0_0_0_5o6Y6YeR5oqA5pyv56S-5Yy6IEAg5pS75Z-O5biI5LiN5rWq_q75.webp)

坐标系的原点位于地球的中心。因此，这些坐标通常是负的。单位通常是`米`。

```js
Cesium.Cartesian3(x, y, z)
```

### 地理坐标系

是一种基于经度和纬度的坐标系，它使用度数来表示位置。

在Cesium中，地理坐标可以通过将经度、纬度和高度值传递给Cartographic对象来表示。

其中经度和纬度是以度数表示的，高度值可以是以米或其他单位表示的。

Cesium将地理坐标转换为笛卡尔坐标以在地球表面上进行可视化。

## 坐标系转换

Cesium提供了很多坐标系互相转换的大类。

### 经纬度转空间直角

```js
const cartesian3 = Cesium.Cartesian3.fromDegrees(lng, lat, height);
```

### 经纬度转地理坐标（弧度）

```js
const radians = Cesium.Math.toRadians(degrees) 
```

### 地理坐标（弧度）转经纬度

```js
const degrees = Cesium.Math.toDegrees(radians) 
```

### 空间直角转经纬度

```js
// 先将3D笛卡尔坐标转为地理坐标（弧度） 
const cartographic = Cesium.Cartographic.fromCartesian(cartesian3); 
// 再将地理坐标（弧度）转为经纬度
const lat = Cesium.Math.toDegrees(cartographic.latitude);
const lng = Cesium.Math.toDegrees(cartographic.longitude); 
const height = cartographic.height; 
```

### 屏幕坐标转经纬度

```js
// 监听点击事件，拾取坐标
  const handler = new Cesium.ScreenSpaceEventHandler(viewer.scene.canvas);
  handler.setInputAction((e) => {
    const clickPosition = viewer.scene.camera.pickEllipsoid(e.position);
    const randiansPos = Cesium.Cartographic.fromCartesian(clickPosition);
    console.log(
      "经度：" +
        Cesium.Math.toDegrees(randiansPos.longitude) +
        ", 纬度：" +
        Cesium.Math.toDegrees(randiansPos.latitude)
    );
  }, Cesium.ScreenSpaceEventType.LEFT_CLICK);
```

### 屏幕坐标转空间直角坐标

```js
var cartesian3 = viewer.scene.globe.pick(viewer.camera.getPickRay(windowPostion),    viewer.scene); 
```

### 世界坐标转屏幕坐标

```js
windowPostion = Cesium.SceneTransforms.wgs84ToWindowCoordinates(viewer.scene, cartesian3); 
```
