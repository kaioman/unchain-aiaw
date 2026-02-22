FROM python:3.11.9-slim

# パッケージインストール$
RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get install -y --no-install-recommends \
    python3-dev python3-pip gcc libpq-dev sudo wget vim curl \
    cron supervisor && \
    rm -rf /var/lib/apt/lists/*

# pipのアップグレード
RUN python3 -m pip install --upgrade pip

# タイムゾーンを日本に設定
ENV TZ=Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/${TZ} /etc/localtime && echo ${TZ} > /etc/timezone

# アプリのディレクトリ作成
WORKDIR /var/docker-service/unchain-aiaw

# cron設定ファイル登録
COPY unchain-aiaw.cron /etc/cron.d/unchain-aiaw
RUN chmod 0644 /etc/cron.d/unchain-aiaw && crontab /etc/cron.d/unchain-aiaw

# ログ出力用のファイルを作成
RUN touch /var/log/unchain-aiaw.log

# supervisord設定ファイルを登録
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
