# fool bot

傻瓜机器龟-树莓派控制代码

## 用法

* 安装依赖库
```bash
pip install -r requirements.txt
```

* 将舵机控制板pca9685与树莓派GPIO口（SDA1,SCL1）连接

* 命令行运行
```bash
python main.py
```

## 文件功能描述

* main.py 主文件

* actions 控制模块
    * servo.py 舵机控制类
    * motion.py 机器动作控制类
    * pca9685.py 16路舵机控制板pca9685
    * I2C.py I2c(Inter－Integrated Circuit)库
    * smbus.py SMBus(System Management Bus,系统管理总线)库
    
* communications 数据传输模块
    * mqttController.py mqtt即时通讯协议库

* vision 视觉模块

* comm_log.py 日志记录

## 资料
[PCA9685 datasheet](https://cdn-shop.adafruit.com/datasheets/PCA9685.pdf)

RaspberryPi-GPIO

![RaspberryPi-GPIO](doc/Pi-GPIO-pins.png)
