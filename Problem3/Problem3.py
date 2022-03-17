import pandas as pd
import datetime
from pytz import timezone, utc
import pytz


def jmeter_log(filepath):
    # Read jtl file
    df = pd.read_csv(filepath)

    for i, j in df.iterrows():
        if j['responseCode'] > 200:
            your_dt = datetime.datetime.fromtimestamp(j['timeStamp'] / 1000)

            now_pacific = your_dt.astimezone(timezone('US/Pacific'))
            now_pacific = now_pacific.strftime("%Y-%m-%d %H:%M:%S %Z")

            print(j['label'], j['responseCode'], j['responseMessage'], j['failureMessage'], now_pacific)
