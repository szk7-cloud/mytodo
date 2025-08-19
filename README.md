# Django タスク管理アプリ

## 概要
Django を使って作成した簡易タスク管理アプリです。管理画面からタスクを追加し、トップページで一覧表示されます。

## 使用技術
- Python 3.13.5
- Django 5.2.4
- SQLite（デフォルト）

## 実行方法
```bash
git clone https://github.com/szk7-cloud/mytodo.git
cd mytodo
python manage.py runserver

### 管理画面でのタスク一覧表示

Djangoの管理画面を使って、登録済みのタスクを一覧表示できます。  
以下は、`Task` モデルに登録したタスクの管理画面での表示例です。
<img width="879" height="520" alt="スクリーンショット 2025-08-19 224454" src="https://github.com/user-attachments/assets/fac8d979-c372-4557-8b98-0ed59057f58f" />

### 管理画面でのタスク編集

登録済みのタスクは、Django管理画面から編集できます。  
タイトル、締切日、ステータス、優先度、メモなどを変更し、保存するだけで反映されます。

以下は、既存のタスクを編集する画面の例です。

<img width="867" height="725" alt="スクリーンショット 2025-08-19 224827" src="https://github.com/user-attachments/assets/8bef0408-4c46-47ae-8dd3-a36ee8dda7a0" />


### 管理画面でのタスク追加

新しいタスクは、管理画面から簡単に追加できます。  
必要な項目を入力して「保存」を押すだけで、一覧に反映されます。

以下は、新規タスクを追加する画面の例です。
<img width="876" height="730" alt="スクリーンショット 2025-08-19 224700" src="https://github.com/user-attachments/assets/0183d598-eeea-49cb-958b-b32416df5d55" />



