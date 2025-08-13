"""
独立的插件市场API服务
可以部署在服务器上，为MaiBot提供插件市场数据
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import uvicorn
import json
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any

app = FastAPI(
    title="MaiBot Plugin Market API",
    description="MaiBot 插件市场API服务",
    version="1.0.0"
)

# CORS 中间件配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

# 插件数据文件路径
PLUGINS_DATA_FILE = Path(__file__).parent / "plugins_data.json"

def load_plugins_data() -> List[Dict[str, Any]]:
    """加载插件数据"""
    try:
        if PLUGINS_DATA_FILE.exists():
            with open(PLUGINS_DATA_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            # 如果文件不存在，创建默认数据
            default_data = create_default_plugins_data()
            save_plugins_data(default_data)
            return default_data
    except Exception as e:
        print(f"加载插件数据失败: {e}")
        return []

def save_plugins_data(data: List[Dict[str, Any]]):
    """保存插件数据"""
    try:
        with open(PLUGINS_DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"保存插件数据失败: {e}")

def create_default_plugins_data() -> List[Dict[str, Any]]:
    """创建默认插件数据"""
    return [
        {
            "name": "聊天记录分析插件",
            "description": "分析群聊记录，生成统计报告和词云图，帮助了解群聊活跃度和话题趋势",
            "author": "MaiBot Team",
            "github_url": "https://github.com/maibot/chat-analytics-plugin",
            "version": "1.0.0",
            "categories": ["分析", "统计"],
            "keywords": ["聊天记录", "分析", "统计", "词云"],
            "created_at": "2024-01-15T10:00:00Z",
            "updated_at": "2024-01-15T10:00:00Z"
        },
        {
            "name": "音乐点播插件",
            "description": "支持点播网易云音乐、QQ音乐等平台的音乐，可以分享音乐卡片到群聊",
            "author": "Community",
            "github_url": "https://github.com/maibot/music-plugin",
            "version": "2.1.0",
            "categories": ["娱乐", "音乐"],
            "keywords": ["音乐", "点播", "网易云", "QQ音乐"],
            "created_at": "2024-01-10T15:30:00Z",
            "updated_at": "2024-02-01T09:15:00Z"
        },
        {
            "name": "天气查询插件",
            "description": "查询全国各地天气信息，支持实时天气、未来几天预报和空气质量查询",
            "author": "WeatherBot",
            "github_url": "https://github.com/maibot/weather-plugin",
            "version": "1.5.2",
            "categories": ["实用工具", "查询"],
            "keywords": ["天气", "预报", "空气质量", "查询"],
            "created_at": "2024-01-05T08:00:00Z",
            "updated_at": "2024-01-25T14:20:00Z"
        },
        {
            "name": "定时提醒插件",
            "description": "设置定时提醒任务，支持一次性提醒和周期性提醒，可用于会议提醒、生日提醒等",
            "author": "TimeKeeper",
            "github_url": "https://github.com/maibot/reminder-plugin",
            "version": "1.2.1",
            "categories": ["实用工具", "提醒"],
            "keywords": ["定时", "提醒", "任务", "会议"],
            "created_at": "2024-01-12T12:00:00Z",
            "updated_at": "2024-01-30T16:45:00Z"
        },
        {
            "name": "表情包制作插件",
            "description": "快速制作各种表情包，支持文字表情包、GIF表情包制作，内置多种模板",
            "author": "MemeCreator",
            "github_url": "https://github.com/maibot/meme-generator-plugin",
            "version": "3.0.0",
            "categories": ["娱乐", "图片处理"],
            "keywords": ["表情包", "制作", "GIF", "模板"],
            "created_at": "2024-01-08T20:30:00Z",
            "updated_at": "2024-02-05T11:00:00Z"
        },
        {
            "name": "群管理插件",
            "description": "强化群管理功能，包括自动踢人、禁言管理、新人欢迎、群公告管理等",
            "author": "AdminBot",
            "github_url": "https://github.com/maibot/group-admin-plugin",
            "version": "2.3.0",
            "categories": ["管理", "群聊"],
            "keywords": ["群管理", "踢人", "禁言", "欢迎"],
            "created_at": "2024-01-03T09:15:00Z",
            "updated_at": "2024-01-28T13:30:00Z"
        },
        {
            "name": "翻译插件",
            "description": "多语言翻译支持，使用多个翻译API，支持自动检测语言和批量翻译",
            "author": "TranslateBot",
            "github_url": "https://github.com/maibot/translate-plugin",
            "version": "1.4.0",
            "categories": ["实用工具", "翻译"],
            "keywords": ["翻译", "多语言", "自动检测", "批量"],
            "created_at": "2024-01-18T14:20:00Z",
            "updated_at": "2024-02-02T10:10:00Z"
        },
        {
            "name": "游戏插件",
            "description": "群聊小游戏合集，包括猜数字、成语接龙、答题游戏等多种互动游戏",
            "author": "GameMaster",
            "github_url": "https://github.com/maibot/games-plugin",
            "version": "2.0.1",
            "categories": ["娱乐", "游戏"],
            "keywords": ["游戏", "猜数字", "成语接龙", "互动"],
            "created_at": "2024-01-20T16:45:00Z",
            "updated_at": "2024-02-03T08:25:00Z"
        }
    ]

@app.get("/", response_class=HTMLResponse)
async def root():
    """根路径返回API信息页面"""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>MaiBot Plugin Market API</title>
        <meta charset="utf-8">
        <style>
            body { 
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                max-width: 800px; 
                margin: 0 auto; 
                padding: 40px 20px;
                background-color: #f8f9fa;
            }
            .container {
                background: white;
                padding: 30px;
                border-radius: 8px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }
            h1 { color: #333; text-align: center; }
            .api-info { 
                background: #f1f3f4; 
                padding: 15px; 
                border-radius: 6px; 
                margin: 20px 0;
            }
            .endpoint {
                background: #e8f5e8;
                padding: 10px;
                border-radius: 4px;
                margin: 10px 0;
                font-family: monospace;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>MaiBot Plugin Market API</h1>
            <div class="api-info">
                <h3>API 接口</h3>
                <div class="endpoint">GET /plugin_list - 获取插件列表</div>
                <div class="endpoint">GET /docs - API 文档</div>
            </div>
            <p>这是 MaiBot 插件市场的 API 服务，提供插件信息查询功能。</p>
            <p><a href="/docs">查看 API 文档</a></p>
        </div>
    </body>
    </html>
    """

@app.get("/plugin_list")
async def get_plugin_list():
    """获取插件列表"""
    try:
        plugins = load_plugins_data()
        return {
            "success": True,
            "count": len(plugins),
            "plugins": plugins,
            "updated_at": datetime.now().isoformat()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取插件列表失败: {str(e)}")

@app.get("/plugins/{plugin_name}")
async def get_plugin_detail(plugin_name: str):
    """获取特定插件的详细信息"""
    try:
        plugins = load_plugins_data()
        plugin = next((p for p in plugins if p["name"] == plugin_name), None)
        
        if not plugin:
            raise HTTPException(status_code=404, detail="插件不存在")
        
        return {
            "success": True,
            "plugin": plugin
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取插件详情失败: {str(e)}")

@app.get("/health")
async def health_check():
    """健康检查接口"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0"
    }

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8080,
        reload=True,
        log_level="info"
    )