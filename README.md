# Mail_command Integration Pack

メールを受信すると、本文に記載されているコマンド列を、
サーバ上で実行し、実行結果の出力をメールで返信する

## Configuration

- smtp_account: emailパッケージのsmtp_acountを指定する
- sender_email_address: メール送信時の送信者アドレス

## Sensors


## Actions

- mail_command: コマンドを実行して、結果をメールする。
