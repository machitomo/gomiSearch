# gomiSearch
何曜日にゴミが出せてるかを教えてくれる。

### 環境
- Google Cloud Function
- Firestore
- Python 3.7

### 概要
リクエストパラメータに今日、昨日、明日を指定することで、なんのゴミが捨てられるか教えてくれる。  
ex). date = today | tommorow | yesterday  
注　Getできる値はFirestoreの値のため、家庭環境によって変更すること
