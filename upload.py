from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

import os

# TODO
"""
googleアカウントで資格情報を作成する必要あり
　→　手順書を作成する
初回の一回のみ手動で認証する必要あり

アップロードした画像がぼやけている
"""


def upload_document(document):

    # Googleサービスを認証
    gauth = GoogleAuth()

    # 資格情報ロードするか、存在しない場合は空の資格情報を作成
    gauth.LoadCredentialsFile("mycreds.txt")

    # Googleサービスの資格情報がない場合
    if gauth.credentials is None:
        # ユーザーから認証コードを自動的に受信しローカルWebサーバーを設定
        gauth.LocalWebserverAuth()
    # アクセストークンが存在しないか、期限切れかの場合
    elif gauth.access_token_expired:
        # Googleサービスを認証をリフレッシュする
        gauth.Refresh()
    # どちらにも一致しない場合
    else:
        # Googleサービスを承認する
        gauth.Authorize()
    # 資格情報をtxt形式でファイルに保存する
    gauth.SaveCredentialsFile("mycreds.txt")

    drive = GoogleDrive(gauth)

    path = os.path.abspath(document['path'])

    f = drive.CreateFile({'title': document['name']})
    # ローカルのファイルをセットしてアップロード
    f.SetContentFile(path)
    # Googleドライブにアップロード
    f.Upload()

    f = None
