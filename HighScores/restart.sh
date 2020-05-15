#!/bin/bash

# dlh
# 2020.05.15
# Overview: start or stop the service

function stop_serv(){
    now_pid=$(ps -ef | grep 8090 | grep usr | awk '{print $2}')
    ps -ef | grep 8090 | grep -q usr
    if [ $? -eq 0 ];then
        echo "重启前的pid:${now_pid}"
        kill -9 ${now_pid}
    else
        echo '服务未启动'
    fi
}

function start_serv(){
    nohup python3 /root/HighScores/manage.py runserver 172.16.0.4:8090 &
    sleep 1 #重启之后,服务没有立马起来,获取不到current_pid,
    current_pid=$(ps -ef | grep 8090 | grep usr | awk '{print $2}')
    ps -ef | grep 8090 | grep -q usr
    if [ $? -eq 0 ];then
        echo "重启后的pid:${current_pid}"
    else
        echo "重启失败"
    fi
}

function main_task(){
    stop_serv
    #start_serv
    
}
main_task


