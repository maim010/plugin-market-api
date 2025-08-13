# MaiBot Plugin Market API

独立的插件市场API服务，可以部署在服务器上为MaiBot提供插件市场数据。

## 功能特性

- 提供插件列表查询API
- 支持插件详情查询
- 可自定义插件数据
- 简单的健康检查接口
- 支持CORS跨域访问

## API接口

### 获取插件列表
```
GET /plugin_list
```

返回所有可用的插件列表。

### 获取插件详情
```
GET /plugins/{plugin_name}
```

获取特定插件的详细信息。

### 健康检查
```
GET /health
```

检查API服务运行状态。

## 部署方式

### 本地运行
```bash
# 安装依赖
pip install -r requirements.txt

# 启动服务
python main.py
```

服务将在 `http://localhost:8080` 启动。

### Docker部署
```bash
# 构建镜像
docker build -t maibot-plugin-market .

# 运行容器
docker run -d -p 8080:8080 maibot-plugin-market
```

### 云服务器部署
1. 上传文件到服务器
2. 安装Python依赖
3. 使用PM2或systemd管理进程
4. 配置Nginx反向代理（可选）

## 配置说明

插件数据存储在 `plugins_data.json` 文件中，可以直接编辑此文件来添加、修改或删除插件信息。

### 插件数据格式
```json
{
  "name": "插件名称",
  "description": "插件描述",
  "author": "作者名称",
  "github_url": "GitHub仓库地址",
  "version": "版本号",
  "categories": ["分类1", "分类2"],
  "keywords": ["关键词1", "关键词2"],
  "created_at": "创建时间",
  "updated_at": "更新时间"
}
```

## 使用示例

在MaiPanel的后端配置中，将插件市场API地址设置为部署的服务地址：
```python
PLUGIN_MARKET_URL = "https://your-domain.com/plugin_list"
```

## 注意事项

- 确保服务器防火墙开放8080端口
- 生产环境建议使用HTTPS
- 定期备份插件数据文件