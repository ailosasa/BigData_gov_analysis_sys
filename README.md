# BigData_gov_analysis_sys

## 项目人员：何田雨、周震霖、张铁赢、黄皓明

## 使用说明

### 下载
``` bash
# 下载并安装nodejs

# 安装python3，并且安装flask包

# git下载本包

```
### 依赖安装

``` bash
# 数据库的配置
首先安装mysql
我使用的是8.0.18版本
安装过程参考https://www.runoob.com/mysql/mysql-install.html
安装后登录root账户，然后创建数据库govdata
教程https://www.runoob.com/mysql/mysql-create-database.html
随后运行test.py
test.py中有两个函数，
load（）是建立到10.30号为止的数据库
update（）是逐条插入10.30号的数据，用于观察图表实时变化

# 安装vue依赖
进入GovStation目录下面，在命令行使用命令
· npm install

# 安装html依赖
本网站结构下有部分静态网页，需要外部访问
在主目录下，直接使用命令

· npm init

init结束后安装live-server
· npm install live-server --save-dev

在编辑器中打开文件package.json，在script项中添加
"dev": "./node_modules/.bin/live-server --port=8001"
并保存；
```
### 修改
```
需要针对部署计算机具体情况进行修改的部分：

后端连接数据库地址修改：

请将data.py下所有的ip地址修改为你设置的数据库的地址
用户名和密码按照你的数据库的设置修改

静态html部署修改：

在主目录下的node_moduel中搜索live-server文件夹，打开其中的index.js
找到其中的

var serveHost = address.address === "0.0.0.0" ? "127.0.0.1" : address.address;
var openHost = host === "0.0.0.0" ? "127.0.0.1" : host;

将127.0.0.1修改为你的ip地址

```

### 运行使用
```
主目录下：
npm run dev 运行相关静态页面

GovStation目录下：
npm run dev 运行vue

gov_back目录下：
python backstatio.py

此时可以根据vue运行提示访问页面
