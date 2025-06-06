# 笛子供应链原型项目

## 项目简介
本项目演示如何通过 AI 辅助生成供应链管理系统的原型图，前端采用 Flutter 技术，适用于 Chrome 浏览器和 iPad。主要功能包括多角色登录、AI对话区、供应商信息查询与详情展示等。

---

## 交互演示动图

> 下方为本项目主要原型交互流程动图（GitHub 可直接预览）：

![交互演示动图](prototype/demo-record.gif)

---

## 关键插件
- Chrome录屏插件：[Loom](https://chrome.google.com/webstore/detail/loom-screen-recorder/liecbddmkiiihnedobmlmillhodjkdmb)
- VSCode原型预览插件：[Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer)

---

## 目录结构说明
- `prototype/`：所有原型页面（index.html、login.html、chat-home.html、setting.html等）
- `README.md`：项目说明与演示入口
- `功能介绍.md`：详细功能需求与原型设计说明

---

## 如何本地运行
1. 克隆本仓库到本地
2. 用 VSCode 打开项目，右键 `prototype/index.html`，选择"Open with Live Server"
3. 浏览器中即可完整体验所有原型交互

---

如需进一步定制或有疑问，欢迎 issue 交流！

### 本项目主要介绍如何通过Cursor 生成一个原型图
关键步骤:
0) 设置curosr 为  Agent模式,  claude-3.7-sonnet
1) 先总结好本次工作和需求--> " 功能介绍.md "
2) 根据 功能介绍.md  然后让AI 生成 可以使用 "Live Server"插件打开的原型图
----- 重复 1),2) 步骤, 直到生成你需要的
4) 生成的原型图, 放在Flutter的项目的同级目录中, 让AI根据原型图写代码

### 关键的cursor 的设置
设置curosr 为  Agent模式,  claude-3.7-sonnet

### 关键提示词

```markdown
1.  这个是一个Flutter 项目为前端的AI项目, 将会运行在Chrome 或者IPad
2.  这个是笛子供应链供应链管理的项目,但是我们本次只需要完成简单的功能:
    - 应用登录有多个角色,每个角色有不同的权限, 角色有: 采购总经理, 资源开发, 供应商。所以有一个简易的登录界面,可以选择不同的登录角色
    - 登录完成后,进入工作页面 "Chat-Home 界面"--其中左边是对话区,右边为详情区。大体是一个对话界面,类似CherryStudio那样,然后不同角色,根据自然语言对话, 就能够不同采购功能;
3.  完成第一个功能: 供应商信息查询
    - 采购总经理,资源开发拥有的权利: 可以查看每一个供应商的基础信息
    - 采购总经理和资源开发可以通过对话形式, 对话框中,查询基础信息。同时,带有一个链接, 跳转到"详细的供应商信息概要"界面,界面处于"Chat-Home 界面"的右边详情区
```

@功能介绍.md 中是我本次项目的关键信息,请cursor 帮我总结一下:

@功能介绍.md 工具这个功能介绍生成原型图,记得我后续需要再LiveServer 插件一次容易地查看原型图,你先帮我将这个提示词拓展好

自动补充到"功能介绍.md"中
------------------
新增一个prototype 文件中吧, 我希望你按功能区分不同的html, 同时有一个index.html 统一查看所有的功能界面. 我都是桌面端. 需要假数据颜色流程
--------------
<使用iframe>标签在 chat-home 右边默认插入 供应商信息概要的界面

----------------------------------

### 后续提示词

```markdown
1. @功能介绍.md 中是我本次项目的关键信息, 请 cursor 帮我总结一下。
2. @功能介绍.md 工具这个功能介绍生成原型图, 记得我后续需要再 LiveServer 插件一次容易地查看原型图, 你先帮我将这个提示词拓展好。
3. 自动补充到 "功能介绍.md" 中。
4. 新增一个 prototype 文件中吧, 我希望你按功能区分不同的 html, 同时有一个 index.html 统一查看所有的功能界面。我都是桌面端。需要假数据颜色流程。
5. <使用iframe> 标签在 chat-home 右边默认插入供应商信息概要的界面。
```

----------------------------------




