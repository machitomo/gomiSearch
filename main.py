import datetime
from datetime  import timedelta
import firebase_admin
from firebase_admin import firestore

# 初期化済みのアプリが存在しないか確認する。
if len(firebase_admin._apps) == 0:
    # アプリを初期化する
    default_app = firebase_admin.initialize_app()
db = firestore.client()

#　定型文
option_word = ["昨日の","今日の","明日の"]
header_word = "ゴミ捨て状況："

# リクエストの取得
def getGomiInfo(request):
    # リクエストパラメータに情報を入れる。
    if request.args and 'date' in request.args:
        # パタメータの分岐
        day = getDay(request.args.get('date'))
        
        # 今月の何週目かを取得する。
        document = getWeek(day[1]) + ' ' + 'week'
        
        # Firestoreからフィールドを取得して辞書化する。
        doc_ref = db.collection(u'gomi').document(document)
        doc_list = doc_ref.get().to_dict()
        
        # 文字列のを送り返す。ex.今日のゴミ捨て状況：何も捨てられません。
        return option_word[day[0]] + header_word + doc_list[getDayOfTheWeek(day[1])]
    else:
        return "使い方が間違っています。"

# 昨日、今日、明日を分割する。
def getDay(day_param):
    print("getDay:{0}".format(day_param))
    
    today = datetime.datetime.today()
    if day_param == "today":
        return 1, today
    elif day_param == "tommorow":
        tommorow = today + timedelta(days=1)
        return 2, tommorow
    elif day_param == "yesterday":
        yesterday = today - timedelta(days=1)
        return 0, yesterday
    else:
        return 1, today
    
# 何週目かを返す
def getWeek(date):
    day = date.day
    weeks = 0
    while day > 0:
        weeks += 1
        day -= 7
    return str(weeks)

# 何曜日かを返す
def getDayOfTheWeek(date):
    wd = ["Mon","Tue","Wed","Thu","Fri","Sat","San"]
    return wd[date.weekday()]
    
        
