#import streamlit as st
import pandas_datareader.data as web
import pandas as pd
import datetime
import dateutil
from dateutil.relativedelta import relativedelta
import calendar
import csv
#import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image
import plotly.graph_objects as go
import qrcode


#QRコード化したい文字列を指定
QR_STR = 'https://share.streamlit.io/yasuky123456/web/main/WEB.py'
 
#QRコード画像ファイル名
#QR_FILE_NAME = 'QR.png'
 
#QRコード化したい文字列を設定
img = qrcode.make(QR_STR)
 
#画像ファイルを保存
img.save('C:\\Users\\koya\\Desktop\\QR.png')