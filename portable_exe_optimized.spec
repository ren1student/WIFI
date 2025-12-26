# -*- mode: python ; coding: utf-8 -*-
import os

datas = []
# 打包图标（如果有）
if os.path.exists('icon.ico'):
    datas.append(('icon.ico', '.'))

# 添加配置文件模板（如果不存在则创建）
config_template = """[Login]
username = 
password = 

[System]
auto_startup = False
version = 2.3.1
login_count = 0
total_logins = 0
"""

if not os.path.exists('login_config.ini'):
    with open('login_config.ini', 'w', encoding='utf-8') as f:
        f.write(config_template)
    datas.append(('login_config.ini', '.'))

a = Analysis(
    ['校园网登录.py'],  # 你的主脚本名
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=['pystray', 'PIL', 'cryptography', 'win32event', 'win32api', 'win32con', 'win32gui', 'winerror', 'pythoncom'],  # 必须的隐藏依赖
    excludes=['tkinter', 'unittest', 'test'],  # 排除无用依赖（保留email，urllib3需要）
    noarchive=False,
)
pyz = PYZ(a.pure)

# 单文件打包核心配置 - 彻底无窗口版本
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    name='校园网自动登录',  # 最终EXE文件名
    debug=False,
    strip=False,
    upx=True,  # 压缩EXE，减小体积
    console=False,  # 关键：彻底关闭控制台
    windowed=True,   # 关键：窗口模式
    icon='icon.ico' if os.path.exists('icon.ico') else None,  # EXE图标
    disable_windowed_traceback=True,  # 禁用窗口化回溯
    argv_emulation=False,
    # 额外参数确保无窗口
    version=None,
    uac_admin=False,
    uac_uiaccess=False,
)