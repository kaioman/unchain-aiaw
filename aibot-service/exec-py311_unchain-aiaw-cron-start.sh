#!/bin/bash

# 全監視対象プロセスを開始する
sudo docker exec -it py311_unchain_aiaw supervisorctl start all
