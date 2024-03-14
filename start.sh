# 检查操作系统
if [ $(uname) == "Darwin" ]; then
    # 在 MacOS 上运行
    pip install -r requirements.txt
    cd ./web
    npm install
    npm run dev
elif [ $(uname) == "Linux" ]; then
    # 在 Linux 上运行
    pip install -r requirements.txt
    cd ./web
    npm install
    npm run dev
elif [ $(uname) == "Windows" ]; then
    # 在 Windows 上运行
    pip install -r requirements.txt
    cd ./web
    npm install
    npm run dev
else
    # 其他操作系统
    echo "不支持的操作系统"
    exit 1
fi

# 运行 Django 服务器
python manage.py runserver

# 检查服务器是否正在运行
if ps aux | grep "python manage.py runserver" > /dev/null; then
    # 服务正在运行，重启服务
    killall python
    echo "服务已重启"
else
    # 服务未运行
    echo "服务未运行"
fi