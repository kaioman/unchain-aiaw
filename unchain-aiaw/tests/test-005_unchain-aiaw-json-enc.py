import os
import uwxpy.configs.app_init as app
import libcore_hng.utils.crypto as crypto

if not os.environ.get('PROJECT_ROOT'):
    os.environ["PROJECT_ROOT"] = "E:\\Dev\\034 unchain-aiaw\\unchain-aiaw\\unchain-aiaw"

# アプリ初期化
app.init_app(__file__, "app_config.json", os.environ.get('CONFIG_FILE_NAME', 'unchain-aiaw.json'))

# 設定ファイルを暗号化して新規ファイルとして作成
key = crypto.create_encryption_file_from_secret_manager("unchain-aiaw/configs/unchain-aiaw.json", "DECRYPTION_KEY")

# 生成された鍵を表示
print("以下の鍵を GCP Secret Manager (または環境変数 APP_SECRET_KEY) に登録してください:")
print(key.decode("utf-8"))