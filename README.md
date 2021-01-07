# 2021_userstudy

## 概要
ウェブ検索ユーザの行動ログを調べるための実験システム．
</br>ユーザが情報検索タスク行っている間，その検索行動ログ（ex.クリック数，ページ閲覧時間など）を取得する仕組みになっている．

## ユーザ実験の流れ
1. アカウント登録をする (accounts/signup)
2. 事前アンケートに回答(userstudy/pre-qustionaire)
3. 事前アンケートの内容に応じて群を振り分け，群に応じて異なる情報を与える(userstudy/task_introduction_{1,2,3,4})
4. 情報検索タスクを行ってもらう (userstudy/search)
5. 事後アンケートを回答する (userstudy/post-questionaire,userstudy/exit-questionaire


## 使用技術
Python/Django/JavaScript/html/css/MySQL/

## データベースについて
データベースは以下のような構成になっている．
- Task：それぞれの群に与えるIDとしての役割
- Search_result：アーカイブしたhtmlを表示する
- Description：それぞれの群に与える詳細な情報
- Answer：情報検索タスクの回答
- User：アカウント登録したユーザ
- Pre_questionaire：事前アンケート
- Post_qustionaire：事後アンケート
- Behavior：行動ログ（クリック数や時間などが格納される）


![database](https://user-images.githubusercontent.com/34092320/103791656-0b476480-5086-11eb-878b-33c163bfbdec.png)


