#!/bin/bash

# 全監視対象プロセスを停止する
sudo docker exec -it py311_unchain_aiaw supervisorctl start all
