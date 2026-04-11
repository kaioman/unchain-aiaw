import os
import uwxpy.configs.app_init as app

# アプリ初期化
app.init_app(
    __file__, 
    "app_config.json", 
    os.environ.get('GCP_CONFIG_FILE_NAME', 'gcp_config-dev.json'),
    os.environ.get('CONFIG_FILE_NAME', 'unchain-aiaw-dev.json.enc')
)

# 環境変数テスト
print(os.environ.get('PROJECT_ROOT', 'root not found'))
print(os.environ.get('CONFIG_FILE_NAME', 'config not found'))
print(os.environ.get('GCP_CONFIG_FILE_NAME', 'gcp config not found'))

# configテスト
print(app.core.config.uwgen.endpoint)
