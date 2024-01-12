from dotenv import load_dotenv
from openai import OpenAI
import json





# 環境変数の読み込み
load_dotenv()

#====================================
#データ準備
#===================================

#学習用のデータファイルパス
filepath_train = "training.json"


# ===============================================================================
# OpenAI環境にファイルアップロード
# ===============================================================================

#アップロード
#--------------------------------------------------------

# クライアント作成
client = OpenAI()

# ファイルアップロード(学習)
upload_file_train = client.files.create(
  file=open(filepath_train, "rb"), # トレーニングファイル
  purpose="fine-tune", # ファイルのアップロード目的
)

#出力
# print(upload_file_train)


#ファインチューニング
#--------------------------------------------------------

#アップロードしたファイルのid
file_id_train = upload_file_train.id

#モデル
model = "gpt-3.5-turbo"

#ファインチューニング
# FineTune = client.fine_tuning.jobs.create(
#   training_file = file_id_train,
#   model= model,
# )

# print(FineTune)

list_fine_tuning = client.fine_tuning.jobs.list()
print(list_fine_tuning.data)