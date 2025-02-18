---
title: "olcs插件实现二三维地图切换"
date: 2025-02-18T10:42:46.000Z
tags: 
  - 前端
  - 地图
  - openlayers
  - cesium
---


`ol-cesium（olcs）` 是一个结合了 `OpenLayers` 和 `Cesium` 的 js 库，用于在 Web 应用中提供高质量的地图可视化。这个库允许开发者在 `OpenLayers` 中无缝集成 `Cesium` 的三维地图功能，只需要一套代码就能在二维和三维地图之间切换，极大地增强了地图交互性和展示效果。

官方文档：[ol-cesium](https://openlayers.org/ol-cesium/)


背景
--

OpenLayers 是一个广泛使用的开源 JavaScript 地图库，提供了强大的地图渲染功能，支持多种地图投影、图层、标注、地图事件等。而 Cesium 则是一个用于创建和查看三维地球和地图的开源库，特别适用于处理大规模地理数据并生成高效的三维场景。

虽然 OpenLayers 和 Cesium 都是非常强大的地图可视化工具，但它们在功能上有所不同。OpenLayers 主要专注于二维地图和图层管理，而 Cesium 提供了完整的三维地球场景和强大的空间分析功能。`olcs` 库的出现，弥补了两者之间的差距，允许用户轻松地在同一应用中**同时使用 OpenLayers 和 Cesium 的功能**。


效果图
--

![二维效果](https://silengzi.github.io/cube-fluid-blod/images/olcs_ol_demo.png)

![三维效果](https://silengzi.github.io/cube-fluid-blod/images/olcs_cs_demo.png)


## 引入 OLCS

为了使用 OLCS，你需要先安装并引入相关的依赖。可以通过 npm 或直接在 HTML 中引入库文件，这里我们使用npm的方式。同时还需要手动引入 Cesium。

### 1. 使用 npm 安装

安装 `ol`、`cesium` 和 `olcs` 依赖：

```bash
npm install ol cesium olcs
```

### 2. 引入 Cesium

在 HTML 文件中引入 `Cesium` (线上链接，也可以替换成你本地的)：

```html
<script src="https://cesium.com/downloads/cesiumjs/releases/1.113/Build/Cesium/Cesium.js"></script>
```

> **Tip：** 如果只引入 `ol cesium olcs`，使用时会报错 `Cesium` 找不到，需要引入一个全局 `Cesium` 变量，因此在html中又引入一次。这可能是 `olcs` 的历史问题，不过多探讨。

## 使用

olcs 基本用法

```js
// 创建一个OpenLayers地图
import Map from 'ol/Map.js';
const ol2dMap = new Map({
    ...
});
ol2dMap.addLayer(....)

// 创建一个 OLCesium 实例，并将 OpenLayers 地图传递给它。
// OL-Cesium 将会从你的图层和数据中创建并同步一个三维的 CesiumJs 地球。
import OLCesium from 'olcs';
const ol3d = new OLCesium({map: ol2dMap});
```

## 完整代码

```vue
<template>
  <div class="map-container">
    <div class="map" ref="map"></div>
    <button class="toggle-btn" @click="toggle3D">{{ is3D ? "切换到2D" : "切换到3D" }}</button>
  </div>
</template>

<script>
import Map from "ol/Map";
import View from "ol/View";
import TileLayer from "ol/layer/Tile";
import OSM from "ol/source/OSM";
import { fromLonLat } from "ol/proj";
import VectorLayer from "ol/layer/Vector";
import VectorSource from "ol/source/Vector";
import Feature from "ol/Feature";
import Point from "ol/geom/Point";
import LineString from "ol/geom/LineString";
import Polygon from "ol/geom/Polygon";
import { Circle as CircleStyle, Fill, Stroke, Style } from "ol/style";
import OLCesium from 'olcs';

export default {
  data() {
    return {
      ol2dMap: null,
      ol3D: null,
      is3D: false,
    };
  },
  mounted() {
    this.initMap();
  },
  methods: {
    initMap() {
      // 创建 OSM 用作底图
      const rasterLayer = new TileLayer({
        source: new OSM(),
      });

      // 创建点线面图形
      const pointGeometry = new Point(fromLonLat([100, 37]));
      const lineStringGeometry = new LineString([
        fromLonLat([107, 33]),
        fromLonLat([114, 41.5]),
      ]);
      const polygonGeometry = new Polygon([
        [
          fromLonLat([117, 33]),
          fromLonLat([117, 41.5]),
          fromLonLat([127.5, 41.5]),
          fromLonLat([127.5, 33]),
        ],
      ]);

      // 创建矢量数据源，并将点线面图形作为地理要素添加到矢量数据源中
      const vectorSource = new VectorSource({
        features: [
          new Feature({
            geometry: pointGeometry
          }),
          new Feature({
            geometry: lineStringGeometry
          }),
          new Feature({
            geometry: polygonGeometry
          }),
        ],
      });

      // 创建矢量图层，并将矢量数据源添加到矢量图层中，同时通过 style 设置样式
      // 具体样式可以根据需求进行自定义，这里仅设置了填充颜色、边框颜色和边框宽度等样式。
      const vectorLayer = new VectorLayer({
        source: vectorSource,
        style: new Style({
          fill: new Fill({ color: "rgba(255, 0, 0, 0.6)" }),
          stroke: new Stroke({ color: "#ff0000", width: 5 }),
          image: new CircleStyle({
            radius: 7,
            fill: new Fill({ color: "#ff0000" }),
          }),
        }),
      });

      // 创建地图，并将 OSM 底图和矢量图层添加到地图中
      this.ol2dMap = new Map({
        target: this.$refs.map,
        layers: [rasterLayer, vectorLayer],
        view: new View({
          center: fromLonLat([117, 37]),
          zoom: 4,
          // 设置地图的投影为 EPSG:4326，即 WGS84 地球坐标系
          // 该投影可直接用于表示 WGS84 坐标系下的经纬度坐标，如 [117, 37] 表示中国上海。
          // 但在高纬度的情况下，可能会出现一些问题，不太好看，如：
          //  1. 地球表面被截断，无法完整地显示；
          //  2. 地球表面被拉伸，无法完整地显示；
          //  3. 地球表面被扭曲，无法完整地显示。
          // 因此，这里使用默认的 EPSG:3857，即 Web Mercator 地球坐标系，该投影可以表示 WGS84 坐标系下的经纬度坐标，需要使用 fromLonLat 方法将经纬度坐标转换为 Web Mercator 坐标系下的坐标。
          // 但不会出现上述问题，可以完整地显示地球表面。
          // projection: "EPSG:4326",
        }),
      });

      // 创建 OLCesium，并将二维地图作为参数传入
      this.ol3D = new OLCesium({ map: this.ol2dMap });
    },
    /**
     * 切换3D视图状态
     * 此方法用于在当前视图状态与3D视图状态之间进行切换通过反转当前的is3D属性来改变视图状态
     * 并调用ol3D对象的setEnabled方法，将新的is3D值作为参数传递进去，以启用或禁用3D视图功能
     */
    toggle3D() {
      // 反转当前的is3D属性，以切换视图状态
      this.is3D = !this.is3D;
      // 调用ol3D对象的setEnabled方法，根据当前的is3D属性值来启用或禁用3D视图功能
      // true 表示启用3D视图功能，false 表示禁用3D视图功能(也就是设置为2D模式)
      this.ol3D.setEnabled(this.is3D);
    },
  },
};
</script>

<style scoped>
.map-container {
  position: relative;
  width: 100%;
  height: 100vh;
}

/* 必须给 .map 宽高，否则地图不会显示 */
.map {
  width: 100%;
  height: 100%;
}

.toggle-btn {
  position: absolute;
  top: 10px;
  right: 10px;
  padding: 10px 15px;
  background-color: #007bff;
  color: white;
  border: none;
  cursor: pointer;
  font-size: 14px;
  border-radius: 5px;
}

.toggle-btn:hover {
  background-color: #0056b3;
}
</style>

```
