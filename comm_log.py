#!/usr/bin/env python
# -*- coding: utf8 -*-
# comm_log @ Python
# Functions: 自动创建当日备份目录、日志记录、压缩备份文件
# Created By SoyM on 2018-04-04,Version 0.1

import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='pi.log',
                    filemode='aw')
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)


def get_logging(name):
    return logging.getLogger(name)
