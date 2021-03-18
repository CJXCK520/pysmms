def _help():
    """
    显示帮助信息
    """

    return (
        "pysmms {arg}\n\n"
        "   profile              查看用户资料（需要配置 Authorization）\n"
        "   ip_history           基于 IP 的临时上传历史记录\n"
        "   history              获取用户上传记录（需要配置 Authorization）\n"
        "   gh /path/to/picture  使用 GitHub 作为图床上传\n"
        "   /path/to/picture     上传图片\n\n"
        "上传图片不强制配置 Authorization，但不保证图片的使用时效。\n"
        "支持格式：.jpeg, .jpg, .png, .gif, .bmp\n"
        "配置 Authorization 需要在用户根目录创建 .pysmms 文件，文件写入以下内容：\n\n"
        "    [sm.ms]\n"
        "    auth=['4a44b5aab53e9b51e317b6f375f9aca7ff4a16f0']\n\n"
        "注意：auth 以列表存放，支持多个 auth 随机上传。\n"
        "===============================================================\n"
        "GitHub 配置如下：\n\n"
        "    [github]\n"
        "    user=CJXCK520"
        "    repo=blog-img"
        "    branch=main"
        "    token=4a44b5aab53e9b51e317b6f375f9aca7ff4a16f0"
    )
