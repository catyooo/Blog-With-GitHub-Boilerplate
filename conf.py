# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Kepler",
    "type": "git",
    "url": "https://github.com/AlanDecode/Maverick-Theme-Kepler.git",
    "branch": "latest"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "catyooo/Blog-With-GitHub-Boilerplate@gh-pages"
}

# 站点设置
site_name = "猫鼬CAT-WIKI"
site_logo = "https://cdn.jsdelivr.net/gh/catyooo/catyo-resources/img/cyapper/images.png"
site_build_date = "2019-12-18T16:51+08:00"
author = "Catyo"
email = "1548589898@qq.com"
author_homepage = "https://www.imalan.cn"
description = "只坚持一种正义。我的正义。"
key_words = ['Maverick', '熊猫小A', 'Galileo', 'blog']
language = 'zh-CN'
external_links = [
    {
        "name": "Maverick",
        "url": "https://github.com/AlanDecode/Maverick",
        "brief": "🏄‍ Go My Own Way."
    },
    {
        "name": "猫鼬 NAVI",
        "url": "https://www.catyo.cn",
        "brief": "猫鼬的星球计划主页。"
    },
    {
        "name": "猫鼬 API",
        "url": "https://api.catyo.cn",
        "brief": "猫鼬的API主页。"
    },
    {
        "name": "猫鼬 PRISM",
        "url": "https://prism.catyo.cn",
        "brief": "猫鼬的PRISM主页。"
    },
    {
        "name": "LBTSTO.",
        "url": "https://www.libertystore.one",
       
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Twitter",
        "url": "https://twitter.com/",
        "icon": "gi gi-twitter"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/catyooo",
        "icon": "gi gi-github"
    },
    {
        "name": "Weibo",
        "url": "https://weibo.com/zhangccmmp",
        "icon": "gi gi-weibo"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="icon" type="image/x-icon" href="https://upyun.catyo.cn/phvo/catyo-resources/img/cyapper/catyo32x32.ico" />
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
