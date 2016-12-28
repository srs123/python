def strCleaner(fullData):
      text = fullData.replace("'"," ").replace(","," ").replace("\n"," ").replace("\"","")
      return text.encode('utf-8','replace')
def unicodeCleaner(text):
    text_data=unicodedata.normalize('NFKD', text).encode('ascii','ignore')
    return text_data
from TwitterAPI import TwitterAPI
import unicodedata
import datetime
import time
import re
TRACK_TERM = ['bigdata','analytics','hadoop','mapreduce','big data','data science','datascience','IOT','Predictive Modeling','Predictive Analytics',
'Machine Learning','Text Mining','Machine data Analytics',
'Recommendation System','Recommendation engine','Artificial Intelligence ',
'Statistics','business intelligence','Deep Learning','Data Wrangling','Data Munging','Data Preparation','Data Blending',
'Citizen Data Scientist','#CitizenDataScientist','#bigdata',
'#datascience','#PredictiveModeling','#PredictiveAnalytics',
'#MachineLearning','#TextMining','#MachinedataAnalytics','#Recommendationengine',
'#businessintelligence','#DataWrangling','#DataMunging','#DataPreparation','#datablenfing',
'#deeplearning','Algorithm','#Algorithm','Biometrics','#Biometrics',
'Gamification','#Gamification','Internet of Things','#InternetofThings','Natural Language Processing','#NaturalLanguageProcessing',
'NLP','#NLP','behavioral analytics','#behavioralanalytics','brand monitoring','#brandmonitoring',
'clickstream analytics','#clickstreamanalytics',
'#clickstream','complex event processing',
'data analytics','data analyst','data collection','data custodian','decision making','data governance','data profiling','data virtualization',
'pattern recognition']

CONSUMER_KEY = 'rL5I9bWshXlJ5OMFlU9QIg'
CONSUMER_SECRET = '6HuuBPWC75ZqeU1btoJ4dD1sWFwiZkBJetnXYs6Rdpc'
ACCESS_TOKEN_KEY = '46583769-Ddf5BrnZOaQ4kyzUjHRy4276TmjXydytKqYN3Gyd2'
ACCESS_TOKEN_SECRET ='ki0x274dM2xeQgCoOvE9UVKA9FO9KHZGsdkjvpzlY'

api = TwitterAPI(CONSUMER_KEY,
                 CONSUMER_SECRET,
                 ACCESS_TOKEN_KEY,
                 ACCESS_TOKEN_SECRET)
pattern = re.compile(u'<\/?\w+\s*[^>]*?\/?>', re.DOTALL | re.MULTILINE | re.IGNORECASE | re.UNICODE)
r = api.request('statuses/filter', {'track': TRACK_TERM})
twt_id=""
twt_created_at=""
twt_text=""
twt_rt_count=""
twt_source=""
twt_user_id=""
twt_user_location=""
twt_user_following=""
twt_user_screen_name=""
twt_user_friends_count=""
twt_user_statuses_count=""
twt_user_created_at=""
twt_user_lang=""
for item in r:
    try:
        twt_text=strCleaner(unicodeCleaner(item['text'] if 'text' in item else item))
        twt_created_at=item['created_at'] if 'text' in item else item
        twt_id=str(item['id'] if 'text' in item else item)
        twt_rt_count=str(item['retweet_count'] if 'text' in item else item)
        twt_source=strCleaner(unicodeCleaner(item['source'] if 'text' in item else item))
        twt_source = pattern.sub("", twt_source)
        twt_user_id=str(item['user']['id'] if 'text' in item else item)
        twt_user_location=strCleaner(str(unicodeCleaner(item['user']['location'])))
        twt_user_following=str(item['user']['following'])
        twt_user_screen_name=str(item['user']['screen_name'])
        twt_user_friends_count=str(item['user']['friends_count'])
        twt_user_statuses_count=str(item['user']['statuses_count'])
        twt_user_created_at=str(item['user']['created_at'])
        twt_user_lang=str(item['user']['lang'])
        if len(twt_user_location) < 1:
            twt_user_location="N/A"
        else:
            twt_user_location=twt_user_location
        final_data= twt_id+","+strCleaner(twt_created_at)+","+twt_text+","+twt_rt_count+","+twt_source+","+twt_user_id+","+twt_user_location+","+twt_user_following+","+twt_user_screen_name+","+twt_user_friends_count+","+twt_user_statuses_count+","+twt_user_lang+","+time.strftime("%d-%m-%Y")
        print (final_data.decode('ascii','ignore'))
    except Exception:
        pass
