#!/usr/bin/env python
# coding=utf-8
'''
Author: luantianyu
LastEditors: Luan Tianyu
email: 1558747541@qq.com
github: https://github.com/tianyuluan/
Date: 2022-01-14 21:20:16
LastEditTime: 2022-01-14 21:55:26
motto: Still water run deep
Description: Modify here please
FilePath: /GrabGpu_py/GrabGPU.py
'''
import os
import sys
import time
import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description='CMD code')
    parser.add_argument('scripts', help='...')
    args = parser.parse_args()
    return args
 
def gpu_info():
    gpu_status = os.popen('nvidia-smi | grep %').read().split('|')
    gpu_memory = int(gpu_status[2].split('/')[0].split('M')[0].strip())
    gpu_power = int(gpu_status[1].split('   ')[-1].split('/')[0].split('W')[0].strip())
    return gpu_power, gpu_memory
 
 
def narrow_setup(interval=2, cmd_str=None):
    gpu_power, gpu_memory = gpu_info()
    i = 0
    while gpu_memory > 1000 or gpu_power > 100:  # set waiting condition
        gpu_power, gpu_memory = gpu_info()
        i = i % 5
        symbol = 'monitoring: ' + '>' * i + ' ' * (10 - i - 1) + '|'
        gpu_power_str = 'gpu power:%d W |' % gpu_power
        gpu_memory_str = 'gpu memory:%d MiB |' % gpu_memory
        sys.stdout.write('\r' + gpu_memory_str + ' ' + gpu_power_str + ' ' + symbol)
        sys.stdout.flush()
        time.sleep(interval)
        i += 1
    print('\n' + cmd_str)
    os.system(cmd_str)
 
 
if __name__ == '__main__':
    args = parse_args()
    cmd_str = args.scripts
    narrow_setup(interval=2, cmd_str=cmd_str)