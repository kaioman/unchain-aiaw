# unchain-aiaw

## .env

- .envは開発環境と本番環境で.env.devと.env.prodにそれぞれ分ける。各環境ではdocker-composeの読み込みの為
  .envという名前でシンボリックリンクを作成する。手順は以下の通り

### 開発環境

管理者権限でPowerShellを起動し、.env.devがあるディレクトリに移動する

```powershell
$New-Item -ItemType SymbolicLink -Path ".env" -Target ".env.dev"
```

### 本番環境

```powershell
$ln -s .env.prod .env
```
