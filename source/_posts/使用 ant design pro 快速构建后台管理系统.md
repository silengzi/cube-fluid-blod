---
title: 使用 ant design pro 快速构建后台管理系统
date: 2025-07-10T15:51:00.000Z
tags: 
  - 前端
  - react
  - 效率
index_img: https://silengzi.github.io/cube-fluid-blod/images/pmjt-2025-07-10-155547.png

---


本文介绍了如何基于 Ant Design Pro 快速搭建一个自定义的后台管理系统，包括项目初始化、结构说明、路由与权限配置、全局请求拦截、用户信息与权限管理、以及典型的表格列表页面自定义。通过替换接口、调整类型、配置拦截器和自定义页面逻辑，可以高效地实现符合自身业务需求的中后台系统。希望本文能帮助你快速上手并完成自己的后台管理项目！


## 简介

[Ant Design Pro](https://pro.ant.design/zh-CN) 是由蚂蚁金服开源的一套基于 Ant Design 的企业级中后台前端解决方案，开箱即用，能快速构建现代中后台应用。

官方文档：[Ant Design Pro 官网](https://pro.ant.design/zh-CN)


## 初始化

这里我们选择直接从官方 github 仓库获取源码的方式来初始化。

```bash
git clone https://github.com/ant-design/ant-design-pro.git
```

clone 完成后，安装依赖并运行，查看效果。安装依赖有可能比较慢，耐心等待一会~

```bash
cd ant-design-pro
npm i
npm run 
```

如果依赖安装太慢，可以尝试将 .npmrc 文件内容替换为下面的代码(走国内代理)：

这里我们使用的是 `ant-design-pro` 官方仓库源码的 `master` 分支，属于精简版代码，只有一个 `table-list` 页面。
如果需要其他模板代码（如：分析页、监控页、工作台、高级表单、个人设置页等），可以切到 `all-blocks` 分支，按需使用。

![精简版](https://silengzi.github.io/cube-fluid-blod/images/pmjt-2025-07-11-162057.png)
![完整版](https://silengzi.github.io/cube-fluid-blod/images/pmjt-2025-07-11-161943.png)


```.npmrc
registry=https://registry.npmmirror.com
```

登录默认账号为:
账号: admin / user （二选一）
密码：and.design

![运行效果](https://silengzi.github.io/cube-fluid-blod/images/pmjt-02025-07-11-101326.png)


## 项目结构介绍

```txt
ant-design-pro/
├─ .github/                  
├─ .git/                     
├─ .husky/                   
├─ config/                   # 项目配置
│  ├─ config.ts              # 主配置文件
│  ├─ defaultSettings.ts     # 默认布局与主题设置
│  ├─ oneapi.json
│  ├─ proxy.ts               # 代理配置（如跨域）
│  └─ routes.ts              # 路由配置
├─ dist/                     # 打包产物
├─ mock/                     # mock数据
│  ├─ listTableList.ts       
│  ├─ monitor.mock.ts        
│  ├─ notices.ts             
│  ├─ requestRecord.mock.js  
│  ├─ route.ts               
│  └─ user.ts                
├─ node_modules/
├─ public/                   
│  ├─ CNAME                  
│  ├─ favicon.ico            
│  ├─ icons/                 
│  ├─ logo.svg               
│  ├─ pro_icon.svg           
│  └─ scripts/               
├─ src/                      # 源码目录
│  ├─ .umi/                  
│  ├─ .umi-production/       
│  ├─ components/            # 公共组件
│  │  ├─ Footer/             
│  │  ├─ HeaderDropdown/     
│  │  ├─ index.ts            
│  │  └─ RightContent/       
│  ├─ locales/               # 国际化
│  │  ├─ bn-BD/              
│  │  ├─ en-US/              
│  │  ├─ fa-IR/              
│  │  ├─ id-ID/              
│  │  ├─ ja-JP/              
│  │  ├─ pt-BR/              
│  │  ├─ zh-CN/              
│  │  └─ zh-TW/              
│  ├─ pages/                 # 页面
│  │  ├─ 404.tsx             
│  │  ├─ Admin.tsx           
│  │  ├─ table-list/         
│  │  │  ├─ components/      
│  │  │  │  ├─ CreateForm.tsx    
│  │  │  │  └─ UpdateForm.tsx    
│  │  │  └─ index.tsx        
│  │  ├─ user/               
│  │  │  └─ login/           
│  │  │     ├─ __snapshots__/    
│  │  │     ├─ index.tsx         
│  │  │     └─ login.test.tsx    
│  │  └─ Welcome.tsx         
│  ├─ services/              # 接口服务
│  │  ├─ ant-design-pro/     
│  │  │  ├─ api.ts           
│  │  │  ├─ index.ts         
│  │  │  ├─ login.ts         
│  │  │  └─ typings.d.ts     
│  │  └─ swagger/            
│  │     ├─ index.ts         
│  │     ├─ pet.ts           
│  │     ├─ store.ts         
│  │     ├─ typings.d.ts     
│  │     └─ user.ts          
│  ├─ access.ts              # 权限控制
│  ├─ app.tsx                # 应用入口
│  ├─ global.less            # 全局样式
│  ├─ global.style.ts
│  ├─ global.tsx
│  ├─ loading.tsx
│  ├─ manifest.json
│  ├─ requestErrorConfig.ts
│  ├─ service-worker.js
│  └─ typings.d.ts
├─ tests/
│  └─ setupTests.jsx
├─ types/
│  └─ index.d.ts
├─ .commitlintrc.js
├─ .editorconfig
├─ .gitignore
├─ .lintstagedrc
├─ .npmrc
├─ CODE_OF_CONDUCT.md
├─ LICENSE
├─ README.ar-DZ.md
├─ README.es-ES.md
├─ README.fr-FR.md
├─ README.ja-JP.md
├─ README.md
├─ README.pt-BR.md
├─ README.ru-RU.md
├─ README.tr-TR.md
├─ README.zh-CN.md
├─ biome.json
├─ jest.config.ts
├─ package-lock.json
├─ package.json
└─ tsconfig.json
```


## 各命令的区别

package.json 中有许多 script 命令，乍一看有点懵，这里简单介绍下各脚本的作用。

常用的可能就是 build、dev、openapi、preview 这些，可根据个人需要使用其他命令。

```json
  "scripts": {
    "analyze": "cross-env ANALYZE=1 max build", // 打包并分析产物体积
    "build": "max build", // 项目打包
    "deploy": "npm run build && npm run gh-pages", // 打包并发布到 GitHub Pages
    "dev": "npm run start:dev", // 启动开发环境（等价于 start:dev）
    "gh-pages": "gh-pages -d dist", // 发布 dist 目录到 GitHub Pages
    "i18n-remove": "pro i18n-remove --locale=zh-CN --write", // 移除多余的国际化内容，仅保留中文
    "postinstall": "max setup", // 安装依赖后自动执行 max setup 初始化
    "jest": "jest", // 运行单元测试
    "lint": "npm run biome:lint && npm run tsc", // 代码检查和类型检查
    "lint-staged": "lint-staged", // 针对暂存区文件进行 lint 检查
    "biome:lint": "npx @biomejs/biome lint", // 使用 biome 进行代码风格检查
    "openapi": "max openapi", // 根据 openapi 规范生成接口代码
    "prepare": "husky", // 安装 git 钩子
    "preview": "npm run build && max preview --port 8000", // 打包并本地预览
    "record": "cross-env NODE_ENV=development REACT_APP_ENV=test max record --scene=login", // 录制登录场景的 mock 数据
    "serve": "umi-serve", // 启动 umi 静态服务
    "start": "cross-env UMI_ENV=dev max dev", // 启动开发环境（默认开发配置）
    "start:dev": "cross-env REACT_APP_ENV=dev MOCK=none UMI_ENV=dev max dev", // 启动开发环境（不启用 mock，开发环境变量）
    "start:no-mock": "cross-env MOCK=none UMI_ENV=dev max dev", // 启动开发环境（不启用 mock）
    "start:pre": "cross-env REACT_APP_ENV=pre UMI_ENV=dev max dev", // 启动预发布环境
    "start:test": "cross-env REACT_APP_ENV=test MOCK=none UMI_ENV=dev max dev", // 启动测试环境（不启用 mock）
    "test": "jest", // 运行测试
    "test:coverage": "npm run jest -- --coverage", // 生成测试覆盖率报告
    "test:update": "npm run jest -- -u", // 更新 jest 快照
    "tsc": "tsc --noEmit" // 仅做类型检查，不生成文件
  }
```


## 需自定义的地方

项目初始化后，预览效果使用的实际是 mock 数据，我们需要改成自己的接口，有些配置也需要自定义，下面介绍一些可能需要的自定义的部分。


#### 国际化相关

项目默认使用了国际化，这肯定多少会占用一部分项目体积，如果不需要完全可以移除。

直接使用 package.json 中提供的 i18n-remove 命令，运行，该命令会移除多余的国际化内容，仅保留中文。

有些文件需要手动删除：

1. src/locales 目录
2. 多余的 readme 文件


#### openAPI

在config/config.ts中，修改 openAPI 为如下配置：

```ts
  openAPI: [
    {
      requestLibPath: "import { request } from '@umijs/max'", // 写明你要从哪里引入 request
      schemaPath: 'http://localhost:8123/api/v3/api-docs', // 你的后端接口文档地址
      mock: false, // 是否使用 mock 数据
      projectName: 'api', // 指定生成代码的存放目录 src/services/api
    },
  ],
```


#### 网页元信息

自定义元信息标签，config/config -> 
比如设置防盗链，defineConfig 中新增如下配置：

```ts
  // 自定义网站meta标签
  metas: [
    // 解决图片防盗链问题
    { name: 'referrer', content: 'no-referrer' },
  ],
```


#### 基础配置

config/defaultSettings.ts

如：
  1. title：网站标题
  2. logo：网站 logo

其他基础配置按需选择。


#### proxy 反向代理

config/proxy.ts -> dev 等 或其他环境

```ts
  // 如果需要自定义本地开发服务器  请取消注释按需调整
  dev: {
    // 配置代理
    '/api': {
      target: 'http://127.0.0.1:8123', // 后端服务器地址
      changeOrigin: true, // 允许跨域
    }
  },
```


#### routes 路由

config/routes.ts

路由配置应该都看得懂，需要注意的就是 access 属性，设置这个属性的页面，表示只有管理员才能访问。

```ts
access: 'canAdmin', // 是否必须管理员
```


#### AvatarDropdown组件

src\components\RightContent\AvatarDropdown.tsx

右上角个人头像和昵称的属性需要自定义：

1. AvatarName 的 currentUser?.nickname
```ts
export const AvatarName = () => {
  const { initialState } = useModel('@@initialState');
  const { currentUser } = initialState || {};
  return <span className="anticon">{currentUser?.name}</span>; /* 这里的 name 需要换成自己的字段 */
};
```
2. 自定义退出登录的逻辑（loginOut）
3. 下面这个 name 字段也要改成你自己的字段，不然可能头像那里会一致转圈。
```ts
  if (!currentUser || !currentUser.name) {
    return loading;
  }
```


#### 管理员状态如何获取

src/access.ts

这里需要修改两个地方
1. 自定义 currentUser 的 ts `类型，currentUser?: API.CurrentUser` -> `API.UserInfoResponse`
2. 自定义管理员的判断规则，`canAdmin: currentUser && currentUser.role === 'ADMIN'`

```ts
/**
 * @see https://umijs.org/docs/max/access#access
 * */
export default function access(initialState: { currentUser?: API.UserInfoResponse } | undefined) {
  const { currentUser } = initialState ?? {};
  return {
    canAdmin: currentUser && currentUser.role === 'ADMIN',
  };
}
```


#### 入口文件修改

src/app.tsx

1. 自定义用户详情接口及 currentUser 的 ts 类型
将 `queryCurrentUser` 接口替换为自己的获取用户详情接口，同时将用户的 ts 类型 `API.CurrentUser` 也替换为自己的

2. layout
layout中修改 `avatarProps` 和 `waterMarkProps` 取的字段:

```ts
{
  avatarProps: {
    src: initialState?.currentUser?.avatarUrl,
    title: <AvatarName />,
    render: (_, avatarChildren) => {
      return <AvatarDropdown>{avatarChildren}</AvatarDropdown>;
    },
  },
  waterMarkProps: {
    content: initialState?.currentUser?.nickname,
  },
}
```

3. request全局配置
设置统一前缀、设置拦截器等

```ts
export const request = {
  // ✅ 给所有请求加统一前缀
  prefix: '/api',
  ...errorConfig,
  requestInterceptors: [
    (url: string, options: any) => {
      // 如果请求路径本身已经是 /api 开头就不处理
      const prefix = '/api';
      if (!url.startsWith(prefix)) {
        url = `${prefix}${url}`;
      }

      // ✅ 自动设置请求头携带 token
      const token = localStorage.getItem('token'); // 或 sessionStorage / cookie / Zustand / Redux 等
      const authHeader = token ? { Authorization: `Bearer ${token}` } : {};

      return {
        url,
        options: {
          ...options,
          headers: {
            ...options.headers,
            ...authHeader,
          }
        }
      };
    },
  ],
};
```


#### 自定义 TableList

最常见的后台管理页面，搜索条件、列表、弹窗等，根据个人需要自定义接口和业务逻辑即可。
贴一下我的吧：

tablelist/index.tsx
```ts
// import { addRule, removeRule, rule, updateRule } from '@/services/ant-design-pro/api';
import { getUserListForAdmin, updateUserInfoByIdForAdmin, deleteUserListForAdmin } from '@/services/api/userController';
import type { ActionType, ProColumns, ProDescriptionsItemProps } from '@ant-design/pro-components';
import {
  FooterToolbar,
  PageContainer,
  ProDescriptions,
  ProTable
} from '@ant-design/pro-components';
import { FormattedMessage } from '@umijs/max';
import { Button, Drawer, message, Popconfirm } from 'antd';
import React, { useRef, useState } from 'react';
import UpdateForm from './components/UpdateForm';


/**
 * @en-US Update node
 * @zh-CN 更新节点
 *
 * @param fields
 */
const handleUpdate = async (fields: API.AdminUpdateUserRequest) => {
  const hide = message.loading('正在修改');
  try {
    await updateUserInfoByIdForAdmin({
      id: fields.id,
      role: fields.role,
      nickname: fields.nickname,
      avatarUrl: fields.avatarUrl
    });
    hide();

    message.success('修改成功');
    return true;
  } catch (error) {
    hide();
    message.error('修改失败，请重试');
    return false;
  }
};

/**
 *  Delete node
 * @zh-CN 删除节点
 *
 * @param selectedRows
 */
const handleRemove = async (selectedRows: API.AdminUserInfoResponse[]) => {
  const hide = message.loading('正在删除');
  if (!selectedRows) return true;
  try {
    await deleteUserListForAdmin({
      idList: selectedRows.map((row) => row.id!),
    });
    hide();
    message.success('删除成功');
    return true;
  } catch (error) {
    hide();
    message.error('删除失败，请重试');
    return false;
  }
  return false;
};

const TableList: React.FC = () => {
  /**
   * @en-US The pop-up window of the distribution update window
   * @zh-CN 分布更新窗口的弹窗
   * */
  const [updateModalOpen, handleUpdateModalOpen] = useState<boolean>(false);

  const [showDetail, setShowDetail] = useState<boolean>(false);

  const actionRef = useRef<ActionType | null>(null);
  const [currentRow, setCurrentRow] = useState<API.AdminUserInfoResponse>();
  const [selectedRowsState, setSelectedRows] = useState<API.AdminUserInfoResponse[]>([]);

  const columns: ProColumns<API.AdminUserInfoResponse>[] = [
    {
      title: 'ID',
      dataIndex: 'id',
      hideInSearch: true,
      width: 200,
      align: 'left',
      render: (dom, entity) => {
        return (
          <a
            onClick={() => {
              setCurrentRow(entity);
              console.log(entity);
              setShowDetail(true);
            }}
          >
            {dom}
          </a>
        );
      },
    },
    {
      title: '账号',
      dataIndex: 'username',
    },
    {
      title: '昵称',
      dataIndex: 'nickname',
      sorter: true,
      hideInForm: true,
    },
    {
      title: '角色',
      dataIndex: 'role',
      hideInForm: true,
      valueEnum: {
        'ADMIN': {
          text: '管理员',
        },
        'USER': {
          text: '用户',
        }
      },
    },
    {
      title: '头像',
      dataIndex: 'avatarUrl',
      valueType: 'image',
      hideInSearch: true
    },
    {
      title: '创建时间',
      dataIndex: 'createTime',
      valueType: 'dateTime',
      hideInSearch: true,
      align: 'center',
      width: 250,
    },
    {
      title: '操作',
      dataIndex: 'option',
      valueType: 'option',
      align: 'center',
      width: 150,
      render: (_, record) => [
        <Button type="link" onClick={() => {
          handleUpdateModalOpen(true);
          setCurrentRow(record);
        }}>修改</Button>,
        <Popconfirm title="确定删除吗？" onConfirm={async () => {
          const seccuess = await handleRemove([record]);
          if (seccuess) {
            setShowDetail(false);
            if (actionRef.current) {
              actionRef.current.reload();
            }
          }
        }}>
          <Button type="link">删除</Button>
        </Popconfirm>
      ],
    },
  ];

  return (
    <PageContainer>
      <ProTable<API.AdminUserInfoResponse, API.PageParams>
        headerTitle="用户管理"
        actionRef={actionRef}
        rowKey="id"
        search={{
          labelWidth: 120,
        }}
        request={getUserListForAdmin}
        columns={columns}
        rowSelection={{
          onChange: (_, selectedRows) => {
            setSelectedRows(selectedRows);
          },
        }}
      />
      {selectedRowsState?.length > 0 && (
        <FooterToolbar
          extra={
            <div>
              <FormattedMessage id="pages.searchTable.chosen" defaultMessage="Chosen" />{' '}
              <a style={{ fontWeight: 600 }}>{selectedRowsState.length}</a>{' '}
              <FormattedMessage id="pages.searchTable.item" defaultMessage="项" />
              &nbsp;&nbsp;
              <span>
                <FormattedMessage
                  id="pages.searchTable.totalServiceCalls"
                  defaultMessage="Total number of service calls"
                />{' '}
                {selectedRowsState.reduce((pre, item) => pre + item.callNo!, 0)}{' '}
                <FormattedMessage id="pages.searchTable.tenThousand" defaultMessage="万" />
              </span>
            </div>
          }
        >
          <Button
            onClick={async () => {
              await handleRemove(selectedRowsState);
              setSelectedRows([]);
              actionRef.current?.reloadAndRest?.();
            }}
          >
            <FormattedMessage
              id="pages.searchTable.batchDeletion"
              defaultMessage="Batch deletion"
            />
          </Button>
          <Button type="primary">
            <FormattedMessage
              id="pages.searchTable.batchApproval"
              defaultMessage="Batch approval"
            />
          </Button>
        </FooterToolbar>
      )}

      {/* 修改用户弹窗 */}
      <UpdateForm
        onSubmit={async (value) => {
          const success = await handleUpdate(value);
          if (success) {
            handleUpdateModalOpen(false);
            setCurrentRow(undefined);
            setShowDetail(false);
            if (actionRef.current) {
              actionRef.current.reload();
            }
          }
        }}
        onCancel={() => {
          handleUpdateModalOpen(false);
          if (!showDetail) {
            setCurrentRow(undefined);
          }
        }}
        updateModalOpen={updateModalOpen}
        values={currentRow || {}}
      />

      <Drawer
        width={600}
        open={showDetail}
        onClose={() => {
          setCurrentRow(undefined);
          setShowDetail(false);
        }}
        closable={false}
      >
        {currentRow?.id && (
          <ProDescriptions<API.AdminUserInfoResponse>
            column={2}
            title={currentRow?.username}
            request={async () => ({
              data: currentRow || {},
            })}
            params={{
              id: currentRow?.id,
            }}
            columns={columns as ProDescriptionsItemProps<API.AdminUserInfoResponse>[]}
          />
        )}
      </Drawer>
    </PageContainer>
  );
};

export default TableList;
```

tablelist/components/UpdateForm.tsx
```ts
import {
  ProFormSelect,
  ProFormText
} from '@ant-design/pro-components';
import { Form, Modal } from 'antd';
import React from 'react';
import { useEffect} from 'react'

export type FormValueType = {
  target?: string;
  template?: string;
  type?: string;
  time?: string;
  frequency?: string;
} & Partial<API.RuleListItem>;

export type UpdateFormProps = {
  onCancel: (flag?: boolean, formVals?: FormValueType) => void;
  onSubmit: (values: API.AdminUpdateUserRequest) => Promise<void>;
  updateModalOpen: boolean;
  values: Partial<API.AdminUpdateUserRequest>;
};

const UpdateForm: React.FC<UpdateFormProps> = (props) => {
  // 创建表单实例
  const [form] = Form.useForm();

  // 数据回显
  useEffect(() => {
    if (props.updateModalOpen) {
      form.setFieldsValue(props.values);
    }
  }, [props.values, props.updateModalOpen]);

  return (
    <Modal
      width={640}
      styles={{
        body: {
          padding: '32px 40px 48px',
        },
      }}
      destroyOnHidden
      title={'修改用户'}
      open={props.updateModalOpen}
      // 确定按钮回调
      onOk={() => {
        // 表单验证
        form.validateFields().then((values) => {
          const mergedValues = {
            ...props.values,
            ...values
          }
          props.onSubmit(mergedValues);
        });
      }}
      // 取消按钮回调
      onCancel={() => {
        props.onCancel();
      }}
    >
      <Form form={form}>
        <ProFormText
          name="nickname"
          label={'昵称'}
          width="md"
          rules={[
            {
              required: true,
              message: '请输入昵称',
            },
          ]}
        />
        <ProFormSelect
          name="role"
          width="md"
          label={'角色'}
          valueEnum={{
            ADMIN: '管理员',
            USER: '用户',
            VIP: 'VIP',
          }}
          rules={[
            {
              required: true,
              message: '请选择角色',
            },
          ]}
        />
      </Form>
    </Modal>
  );
};

export default UpdateForm;
```


![加油](https://silengzi.github.io/cube-fluid-blod/images/006APoFYly8h5mmvdv4zyg307n07nu10.gif)