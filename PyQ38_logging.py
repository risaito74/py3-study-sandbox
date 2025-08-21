# PyQ模擬試験
# 38. 次のコードを実⾏した結果として表⽰されるものを選択してください（1つ選択）

import logging

# デフォルトで出されるか？

logging.warning("Key not found") # 出力される
logging.critical("Key not found") # 出力される
logging.debug("Key not found")
logging.error("Key not found") # 出力される
logging.info("Key not found")
# 出力：
# WARNING:root:Key not found
# CRITICAL:root:Key not found
# ERROR:root:Key not found

# まとめ：優先度の高い順

# デフォルトで出力されるもの
logging.critical("クリティカルはさすがに鉄板で出力される！！🌰🌰🌰")
logging.error("エラーもまあ普通に出力される")
logging.warning("ワーニングまで出力される！ここがポイント！ワーニングまで出る！🐊🐊🐊ワニ出る！（おい")

# デフォルトで出力されないもの
logging.info("まあ、ただのインフォだし")
logging.debug("優先度最低のデバッグはまあ、鉄板で出力されない")

# 結論：🌰と🐊は出る
