# 11章：標準ライブラリめぐり Part2
# loggingモジュール

import logging

# ログの出力設定（デフォルトレベルは WARNING 以上）
# basicConfig()はログを出力する前に1回のみ有効、ログ出力後や複数回使っても効果が出ない
logging.basicConfig(level=logging.DEBUG)

# ログメッセージの優先度：DUBUG < INFO < WARNING < ERROR < CRITICAL
# デフォルトでは DUBUG, INFO は表示されない
logging.debug("デバッグ用メッセージ")
logging.info("情報メッセージ")

logging.warning("警告メッセージ")
logging.error("エラーメッセージ")
logging.critical("致命的エラー")

# 途中でbasicConfig()でログの出力設定を変更することはできない
logging.basicConfig(level=logging.ERROR)

logging.debug("デバッグ用メッセージ2") # 表示される
logging.info("情報メッセージ2") # 表示される
