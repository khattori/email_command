# Mail_command Integration Pack

メールを受信すると、本文に記載されているコマンド列を、
サーバ上で実行し、実行結果の出力をメールで返信する

## Configuration

- smtp_account: emailパッケージのsmtp_acountを指定する
- sender_email_address: メール送信時の送信者アドレス

ノードの情報はあらかじめkey-valueストアに登録しておく必要がある。

```yaml:nodes.yaml
---
- name: config.nodes.hattori-server
  value:
    hostname: 10.20.0.108
    username: hattori
    password: secret
- name: config.nodes.kompira-server
  value:
    hostname: kompira.fixpoint.co.jp
    username: root
    password: secret
```

```sh:
$ st2 key load nodes.yaml
```

キー名の形式は config.nodes.<サーバ名> とする。


## 送信メールの形式

件名: コマンド実行@<サーバ名>
本文: <実行するコマンドを1行ずつ記述>

## Sensors


## Actions

- mail_command: コマンドを実行して、結果をメールする。
