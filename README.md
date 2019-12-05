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
### 运行使用
```
主目录下：
npm run dev 运行相关静态页面

GovStation目录下：
npm run dev 运行vue

gov_back目录下：
python backstatio.py

此时可以根据vue运行提示访问页面
