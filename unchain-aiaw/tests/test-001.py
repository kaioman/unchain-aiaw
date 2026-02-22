import os
import uwxpy.configs.app_init as app

if not os.environ.get('PROJECT_ROOT'):
    os.environ["PROJECT_ROOT"] = "E:\\Dev\\034 unchain-aiaw\\unchain-aiaw\\unchain-aiaw"

# アプリ初期化
app.init_app(__file__, "logger.json", "unchain-aiaw.json")

# 設定確認
print(app.core.config.uwgen.api_key)
print(app.core.config.uwgen.endpoint)
