"""
config.py  配置文件
功能:
httpserver  主程序不希望使用中修改
httpserver  中需要用户提供的信息可以写在配置中
"""


# [http server ip]
HOST="0.0.0.0"
PORT=9916
ADDR=(HOST,PORT)

# [debug]
DEBUG=True


# [frame adress]
frame_ip="127.0.0.1"
frame_port=8080