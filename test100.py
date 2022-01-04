import streamlit as st
import pandas_datareader.data as web
import pandas as pd
import datetime
import dateutil
from dateutil.relativedelta import relativedelta
import calendar
import csv
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image
import plotly.graph_objects as go
import pathlib  # 標準ライブラリ
#import openpyxl # 外部ライブラリ　
#import csv      # 標準ライブラリ
import glob
import pandas as pd
import os
from pathlib import Path
import numpy as np
import math
import pydicom
from PIL import Image
import re
#import cv2



with st.sidebar:
    #image = Image.open('C:\\Users\\koya\\Desktop\\vscord\\image\\rion.png')
    image = Image.open('rion.png')
    st.image(image,width=120)


#st.title('"ライオン戦略"')
with st.sidebar:

    st.title("DAN's WEB Tools")

    st.write('WEBで作ってみるかぁ．金融ライオン戦略．研究MRCT．')
    st.write('')
    sideradio = st.radio('',('Market information','ライオン戦略/資産形成', 'MR', 'CT'))

    st.markdown("")
    st.markdown("## Link")
    st.markdown("[Amazon](https://www.amazon.co.jp/%E4%B8%96%E7%95%8C%E3%81%AE%E3%81%8A%E9%87%91%E6%8C%81%E3%81%A1%E3%81%8C%E5%AE%9F%E8%B7%B5%E3%81%99%E3%82%8B%E3%81%8A%E9%87%91%E3%81%AE%E5%A2%97%E3%82%84%E3%81%97%E6%96%B9/dp/B08VD21WDF/ref=sr_1_1?dchild=1&qid=1635860620&s=books&sr=1-1)")
    st.markdown("[youtube](https://www.youtube.com/channel/UCFXl12dZUPs7MLy_dMkMZYw)")
    st.markdown("[stooq](https://stooq.pl/)")
    st.write("例：日経平均のコードを調べたいとき，stooqサイトの検索ボックスにnikkeiと入力すると，^NKXと出るはず．これを銘柄コードとします")




    today = datetime.datetime.today()
    month = today + relativedelta(months=-1) 
    #print(today)
    #print(month)
    #先月日a，先月日c
    a = today + relativedelta(months=-1, day = 1) 
    A = a.strftime('%Y/%m/%d')
    #print(A)
    b = calendar.monthrange(2019, 1)[1]
    #print(b)
    c = today + relativedelta(months=-1, day = b)
    C = c.strftime('%Y/%m/%d')
    #print(C)

    year = today + relativedelta(years = -1)
    D = year.strftime('%Y/%m/%d')


if sideradio == 'Market information':

    st.subheader('トレードの世界へようこそ')

    """
    過去1年分のデータを表示させます.短期/中期戦略に役立ててください．
    """
    
    task = st.selectbox('★お気に入り株価一覧',('','日経平均', 'sp500','上海総合指数', '先進国','あおぞら銀行', 'SPDRｺﾞｰﾙﾄﾞ','20年ｱﾒﾘｶ国債'))
    #task = st.selectbox('★追加用',())


    if task == '日経平均':
    
        #if st.button('入力された銘柄のローソク足を表示する。'):
 
        #  任意の銘柄の株価を取得
            df_Security_code=web.DataReader('^NKX', "stooq",D)
            st.write('株価情報')
            st.dataframe(df_Security_code)
        
            #日足計算
            df_Security_code_ri = df_Security_code.reset_index()
            df_Security_code_ri['SMA005'] = df_Security_code_ri['Close'].rolling(window=5).mean()
            df_Security_code_ri['SMA050'] = df_Security_code_ri['Close'].rolling(window=50).mean()
            df_Security_code_ri['SMA0100'] = df_Security_code_ri['Close'].rolling(window=100).mean()
            fig6 = go.Figure()
            fig6 = go.Figure(data=[go.Candlestick(x=df_Security_code_ri['Date'],
                                          open=df_Security_code_ri['Open'],
                                          high=df_Security_code_ri['High'],
                                          low=df_Security_code_ri['Low'],
                                          close=df_Security_code_ri['Close'],
                                          name='日経平均')])

            fig6.add_traces(go.Scatter(x=df_Security_code_ri['Date'], y=df_Security_code_ri['SMA005'], name='移動平均05日'))
            fig6.add_traces(go.Scatter(x=df_Security_code_ri['Date'], y=df_Security_code_ri['SMA050'], name='移動平均50日'))
            fig6.add_traces(go.Scatter(x=df_Security_code_ri['Date'], y=df_Security_code_ri['SMA0100'], name='移動平均100日'))
            fig6.update_layout(title_text='日足')
            fig6.update_layout(xaxis_rangeslider_visible=True)
            st.plotly_chart(fig6, use_container_width=True)


            #週足計算
            # カラムごとの計算手法を指定
            agg_dict = {
                        "Open": "first", 
                        "High": "max",
                        "Low": "min",
                        "Close": "last",
                        "Volume": "sum"
                        }
 
            # 週足に変換する
            df_week = df_Security_code.resample("W").agg(agg_dict)

            df_week_ri = df_week.reset_index()
            df_week_ri['SMA005'] = df_week_ri['Close'].rolling(window=5).mean()
            df_week_ri['SMA050'] = df_week_ri['Close'].rolling(window=50).mean()
            df_week_ri['SMA0100'] = df_week_ri['Close'].rolling(window=100).mean()
            fig6 = go.Figure()
            fig6 = go.Figure(data=[go.Candlestick(x=df_week_ri['Date'],
                                          open=df_week_ri['Open'],
                                          high=df_week_ri['High'],
                                          low=df_week_ri['Low'],
                                          close=df_week_ri['Close'],
                                          name='日経平均')])

            fig6.add_traces(go.Scatter(x=df_week_ri['Date'], y=df_week_ri['SMA005'], name='移動平均05日'))
            fig6.add_traces(go.Scatter(x=df_week_ri['Date'], y=df_week_ri['SMA050'], name='移動平均50日'))
            fig6.add_traces(go.Scatter(x=df_week_ri['Date'], y=df_week_ri['SMA0100'], name='移動平均100日'))
            fig6.update_layout(title_text='週足')
            fig6.update_layout(xaxis_rangeslider_visible=True)
            st.plotly_chart(fig6, use_container_width=True)


            # 月足に変換する
            df_month = df_Security_code.resample("M").agg(agg_dict)
            
            df_month_ri = df_month.reset_index()
            df_month_ri['SMA005'] = df_month_ri['Close'].rolling(window=5).mean()
            df_month_ri['SMA050'] = df_month_ri['Close'].rolling(window=50).mean()
            df_month_ri['SMA0100'] = df_month_ri['Close'].rolling(window=100).mean()
            fig6 = go.Figure()
            fig6 = go.Figure(data=[go.Candlestick(x=df_month_ri['Date'],
                                          open=df_month_ri['Open'],
                                          high=df_month_ri['High'],
                                          low=df_month_ri['Low'],
                                          close=df_month_ri['Close'],
                                          name='日経平均')])

            fig6.add_traces(go.Scatter(x=df_month_ri['Date'], y=df_month_ri['SMA005'], name='移動平均05日'))
            fig6.add_traces(go.Scatter(x=df_month_ri['Date'], y=df_month_ri['SMA050'], name='移動平均50日'))
            fig6.add_traces(go.Scatter(x=df_month_ri['Date'], y=df_month_ri['SMA0100'], name='移動平均100日'))
            fig6.update_layout(title_text='月足')
            fig6.update_layout(xaxis_rangeslider_visible=True)
            st.plotly_chart(fig6, use_container_width=True)           
            



    if task == 'sp500':
    
        #if st.button('入力された銘柄のローソク足を表示する。'):
            df_Security_code=web.DataReader('1655.JP', "stooq",D)
            st.write('sp500','株価情報')
            st.dataframe(df_Security_code)

            df_Security_code_ri = df_Security_code.reset_index()
            df_Security_code_ri['SMA005'] = df_Security_code_ri['Close'].rolling(window=5).mean()
            df_Security_code_ri['SMA050'] = df_Security_code_ri['Close'].rolling(window=50).mean()
            df_Security_code_ri['SMA0100'] = df_Security_code_ri['Close'].rolling(window=100).mean()
            fig6 = go.Figure()
            fig6 = go.Figure(data=[go.Candlestick(x=df_Security_code_ri['Date'],
                                          open=df_Security_code_ri['Open'],
                                          high=df_Security_code_ri['High'],
                                          low=df_Security_code_ri['Low'],
                                          close=df_Security_code_ri['Close'],
                                          name='sp500')])

            fig6.add_traces(go.Scatter(x=df_Security_code_ri['Date'], y=df_Security_code_ri['SMA005'], name='移動平均05日'))
            fig6.add_traces(go.Scatter(x=df_Security_code_ri['Date'], y=df_Security_code_ri['SMA050'], name='移動平均50日'))
            fig6.add_traces(go.Scatter(x=df_Security_code_ri['Date'], y=df_Security_code_ri['SMA0100'], name='移動平均100日'))
            fig6.update_layout(title_text='sp500')
            fig6.update_layout(xaxis_rangeslider_visible=True)
            st.plotly_chart(fig6, use_container_width=True)



            #週足計算
            # カラムごとの計算手法を指定
            agg_dict = {
                        "Open": "first", 
                        "High": "max",
                        "Low": "min",
                        "Close": "last",
                        "Volume": "sum"
                        }
 
            # 週足に変換する
            df_week = df_Security_code.resample("W").agg(agg_dict)

            df_week_ri = df_week.reset_index()
            df_week_ri['SMA005'] = df_week_ri['Close'].rolling(window=5).mean()
            df_week_ri['SMA050'] = df_week_ri['Close'].rolling(window=50).mean()
            df_week_ri['SMA0100'] = df_week_ri['Close'].rolling(window=100).mean()
            fig6 = go.Figure()
            fig6 = go.Figure(data=[go.Candlestick(x=df_week_ri['Date'],
                                          open=df_week_ri['Open'],
                                          high=df_week_ri['High'],
                                          low=df_week_ri['Low'],
                                          close=df_week_ri['Close'],
                                          name='sp500')])

            fig6.add_traces(go.Scatter(x=df_week_ri['Date'], y=df_week_ri['SMA005'], name='移動平均05日'))
            fig6.add_traces(go.Scatter(x=df_week_ri['Date'], y=df_week_ri['SMA050'], name='移動平均50日'))
            fig6.add_traces(go.Scatter(x=df_week_ri['Date'], y=df_week_ri['SMA0100'], name='移動平均100日'))
            fig6.update_layout(title_text='週足')
            fig6.update_layout(xaxis_rangeslider_visible=True)
            st.plotly_chart(fig6, use_container_width=True)


            # 月足に変換する
            df_month = df_Security_code.resample("M").agg(agg_dict)
            
            df_month_ri = df_month.reset_index()
            df_month_ri['SMA005'] = df_month_ri['Close'].rolling(window=5).mean()
            df_month_ri['SMA050'] = df_month_ri['Close'].rolling(window=50).mean()
            df_month_ri['SMA0100'] = df_month_ri['Close'].rolling(window=100).mean()
            fig6 = go.Figure()
            fig6 = go.Figure(data=[go.Candlestick(x=df_month_ri['Date'],
                                          open=df_month_ri['Open'],
                                          high=df_month_ri['High'],
                                          low=df_month_ri['Low'],
                                          close=df_month_ri['Close'],
                                          name='sp500')])

            fig6.add_traces(go.Scatter(x=df_month_ri['Date'], y=df_month_ri['SMA005'], name='移動平均05日'))
            fig6.add_traces(go.Scatter(x=df_month_ri['Date'], y=df_month_ri['SMA050'], name='移動平均50日'))
            fig6.add_traces(go.Scatter(x=df_month_ri['Date'], y=df_month_ri['SMA0100'], name='移動平均100日'))
            fig6.update_layout(title_text='月足')
            fig6.update_layout(xaxis_rangeslider_visible=True)
            st.plotly_chart(fig6, use_container_width=True)           






    if task == '上海総合指数':
    
        #if st.button('入力された銘柄のローソク足を表示する。'):
            df_Security_code=web.DataReader('^SHC', "stooq",D)
            st.write('上海総合指数','株価情報')
            st.dataframe(df_Security_code)

            df_Security_code_ri = df_Security_code.reset_index()
            df_Security_code_ri['SMA005'] = df_Security_code_ri['Close'].rolling(window=5).mean()
            df_Security_code_ri['SMA050'] = df_Security_code_ri['Close'].rolling(window=50).mean()
            df_Security_code_ri['SMA0100'] = df_Security_code_ri['Close'].rolling(window=100).mean()
            fig6 = go.Figure()
            fig6 = go.Figure(data=[go.Candlestick(x=df_Security_code_ri['Date'],
                                          open=df_Security_code_ri['Open'],
                                          high=df_Security_code_ri['High'],
                                          low=df_Security_code_ri['Low'],
                                          close=df_Security_code_ri['Close'],
                                          name='上海総合指数')])

            fig6.add_traces(go.Scatter(x=df_Security_code_ri['Date'], y=df_Security_code_ri['SMA005'], name='移動平均05日'))
            fig6.add_traces(go.Scatter(x=df_Security_code_ri['Date'], y=df_Security_code_ri['SMA050'], name='移動平均50日'))
            fig6.add_traces(go.Scatter(x=df_Security_code_ri['Date'], y=df_Security_code_ri['SMA0100'], name='移動平均100日'))
            fig6.update_layout(title_text='上海総合指数')
            fig6.update_layout(xaxis_rangeslider_visible=True)
            st.plotly_chart(fig6, use_container_width=True)

            #週足計算
            # カラムごとの計算手法を指定
            agg_dict = {
                        "Open": "first", 
                        "High": "max",
                        "Low": "min",
                        "Close": "last",
                        "Volume": "sum"
                        }
 
            # 週足に変換する
            df_week = df_Security_code.resample("W").agg(agg_dict)

            df_week_ri = df_week.reset_index()
            df_week_ri['SMA005'] = df_week_ri['Close'].rolling(window=5).mean()
            df_week_ri['SMA050'] = df_week_ri['Close'].rolling(window=50).mean()
            df_week_ri['SMA0100'] = df_week_ri['Close'].rolling(window=100).mean()
            fig6 = go.Figure()
            fig6 = go.Figure(data=[go.Candlestick(x=df_week_ri['Date'],
                                          open=df_week_ri['Open'],
                                          high=df_week_ri['High'],
                                          low=df_week_ri['Low'],
                                          close=df_week_ri['Close'],
                                          name='上海総合指数')])

            fig6.add_traces(go.Scatter(x=df_week_ri['Date'], y=df_week_ri['SMA005'], name='移動平均05日'))
            fig6.add_traces(go.Scatter(x=df_week_ri['Date'], y=df_week_ri['SMA050'], name='移動平均50日'))
            fig6.add_traces(go.Scatter(x=df_week_ri['Date'], y=df_week_ri['SMA0100'], name='移動平均100日'))
            fig6.update_layout(title_text='週足')
            fig6.update_layout(xaxis_rangeslider_visible=True)
            st.plotly_chart(fig6, use_container_width=True)


            # 月足に変換する
            df_month = df_Security_code.resample("M").agg(agg_dict)
            
            df_month_ri = df_month.reset_index()
            df_month_ri['SMA005'] = df_month_ri['Close'].rolling(window=5).mean()
            df_month_ri['SMA050'] = df_month_ri['Close'].rolling(window=50).mean()
            df_month_ri['SMA0100'] = df_month_ri['Close'].rolling(window=100).mean()
            fig6 = go.Figure()
            fig6 = go.Figure(data=[go.Candlestick(x=df_month_ri['Date'],
                                          open=df_month_ri['Open'],
                                          high=df_month_ri['High'],
                                          low=df_month_ri['Low'],
                                          close=df_month_ri['Close'],
                                          name='上海総合指数')])

            fig6.add_traces(go.Scatter(x=df_month_ri['Date'], y=df_month_ri['SMA005'], name='移動平均05日'))
            fig6.add_traces(go.Scatter(x=df_month_ri['Date'], y=df_month_ri['SMA050'], name='移動平均50日'))
            fig6.add_traces(go.Scatter(x=df_month_ri['Date'], y=df_month_ri['SMA0100'], name='移動平均100日'))
            fig6.update_layout(title_text='月足')
            fig6.update_layout(xaxis_rangeslider_visible=True)
            st.plotly_chart(fig6, use_container_width=True)           







    if task == '先進国':
    
        #if st.button('入力された銘柄のローソク足を表示する。'):
            df_Security_code=web.DataReader('1657.JP', "stooq",D)
            st.write('先進国','株価情報')
            st.dataframe(df_Security_code)

            df_Security_code_ri = df_Security_code.reset_index()
            df_Security_code_ri['SMA005'] = df_Security_code_ri['Close'].rolling(window=5).mean()
            df_Security_code_ri['SMA050'] = df_Security_code_ri['Close'].rolling(window=50).mean()
            df_Security_code_ri['SMA0100'] = df_Security_code_ri['Close'].rolling(window=100).mean()
            fig6 = go.Figure()
            fig6 = go.Figure(data=[go.Candlestick(x=df_Security_code_ri['Date'],
                                          open=df_Security_code_ri['Open'],
                                          high=df_Security_code_ri['High'],
                                          low=df_Security_code_ri['Low'],
                                          close=df_Security_code_ri['Close'],
                                          name='先進国')])

            fig6.add_traces(go.Scatter(x=df_Security_code_ri['Date'], y=df_Security_code_ri['SMA005'], name='移動平均05日'))
            fig6.add_traces(go.Scatter(x=df_Security_code_ri['Date'], y=df_Security_code_ri['SMA050'], name='移動平均50日'))
            fig6.add_traces(go.Scatter(x=df_Security_code_ri['Date'], y=df_Security_code_ri['SMA0100'], name='移動平均100日'))
            fig6.update_layout(title_text='先進国')
            fig6.update_layout(xaxis_rangeslider_visible=True)
            st.plotly_chart(fig6, use_container_width=True)


            #週足計算
            # カラムごとの計算手法を指定
            agg_dict = {
                        "Open": "first", 
                        "High": "max",
                        "Low": "min",
                        "Close": "last",
                        "Volume": "sum"
                        }
 
            # 週足に変換する
            df_week = df_Security_code.resample("W").agg(agg_dict)

            df_week_ri = df_week.reset_index()
            df_week_ri['SMA005'] = df_week_ri['Close'].rolling(window=5).mean()
            df_week_ri['SMA050'] = df_week_ri['Close'].rolling(window=50).mean()
            df_week_ri['SMA0100'] = df_week_ri['Close'].rolling(window=100).mean()
            fig6 = go.Figure()
            fig6 = go.Figure(data=[go.Candlestick(x=df_week_ri['Date'],
                                          open=df_week_ri['Open'],
                                          high=df_week_ri['High'],
                                          low=df_week_ri['Low'],
                                          close=df_week_ri['Close'],
                                          name='先進国')])

            fig6.add_traces(go.Scatter(x=df_week_ri['Date'], y=df_week_ri['SMA005'], name='移動平均05日'))
            fig6.add_traces(go.Scatter(x=df_week_ri['Date'], y=df_week_ri['SMA050'], name='移動平均50日'))
            fig6.add_traces(go.Scatter(x=df_week_ri['Date'], y=df_week_ri['SMA0100'], name='移動平均100日'))
            fig6.update_layout(title_text='週足')
            fig6.update_layout(xaxis_rangeslider_visible=True)
            st.plotly_chart(fig6, use_container_width=True)


            # 月足に変換する
            df_month = df_Security_code.resample("M").agg(agg_dict)
            
            df_month_ri = df_month.reset_index()
            df_month_ri['SMA005'] = df_month_ri['Close'].rolling(window=5).mean()
            df_month_ri['SMA050'] = df_month_ri['Close'].rolling(window=50).mean()
            df_month_ri['SMA0100'] = df_month_ri['Close'].rolling(window=100).mean()
            fig6 = go.Figure()
            fig6 = go.Figure(data=[go.Candlestick(x=df_month_ri['Date'],
                                          open=df_month_ri['Open'],
                                          high=df_month_ri['High'],
                                          low=df_month_ri['Low'],
                                          close=df_month_ri['Close'],
                                          name='先進国')])

            fig6.add_traces(go.Scatter(x=df_month_ri['Date'], y=df_month_ri['SMA005'], name='移動平均05日'))
            fig6.add_traces(go.Scatter(x=df_month_ri['Date'], y=df_month_ri['SMA050'], name='移動平均50日'))
            fig6.add_traces(go.Scatter(x=df_month_ri['Date'], y=df_month_ri['SMA0100'], name='移動平均100日'))
            fig6.update_layout(title_text='月足')
            fig6.update_layout(xaxis_rangeslider_visible=True)
            st.plotly_chart(fig6, use_container_width=True)           







    if task == 'あおぞら銀行':
    
        #if st.button('入力された銘柄のローソク足を表示する。'):
            df_Security_code=web.DataReader('8304.JP', "stooq",D)
            st.write('あおぞら銀行','株価情報')
            st.dataframe(df_Security_code)

            df_Security_code_ri = df_Security_code.reset_index()
            df_Security_code_ri['SMA005'] = df_Security_code_ri['Close'].rolling(window=5).mean()
            df_Security_code_ri['SMA050'] = df_Security_code_ri['Close'].rolling(window=50).mean()
            df_Security_code_ri['SMA0100'] = df_Security_code_ri['Close'].rolling(window=100).mean()
            fig6 = go.Figure()
            fig6 = go.Figure(data=[go.Candlestick(x=df_Security_code_ri['Date'],
                                          open=df_Security_code_ri['Open'],
                                          high=df_Security_code_ri['High'],
                                          low=df_Security_code_ri['Low'],
                                          close=df_Security_code_ri['Close'],
                                          name='あおぞら銀行')])

            fig6.add_traces(go.Scatter(x=df_Security_code_ri['Date'], y=df_Security_code_ri['SMA005'], name='移動平均05日'))
            fig6.add_traces(go.Scatter(x=df_Security_code_ri['Date'], y=df_Security_code_ri['SMA050'], name='移動平均50日'))
            fig6.add_traces(go.Scatter(x=df_Security_code_ri['Date'], y=df_Security_code_ri['SMA0100'], name='移動平均100日'))
            fig6.update_layout(title_text='あおぞら銀行')
            fig6.update_layout(xaxis_rangeslider_visible=True)
            st.plotly_chart(fig6, use_container_width=True)


            #週足計算
            # カラムごとの計算手法を指定
            agg_dict = {
                        "Open": "first", 
                        "High": "max",
                        "Low": "min",
                        "Close": "last",
                        "Volume": "sum"
                        }
 
            # 週足に変換する
            df_week = df_Security_code.resample("W").agg(agg_dict)

            df_week_ri = df_week.reset_index()
            df_week_ri['SMA005'] = df_week_ri['Close'].rolling(window=5).mean()
            df_week_ri['SMA050'] = df_week_ri['Close'].rolling(window=50).mean()
            df_week_ri['SMA0100'] = df_week_ri['Close'].rolling(window=100).mean()
            fig6 = go.Figure()
            fig6 = go.Figure(data=[go.Candlestick(x=df_week_ri['Date'],
                                          open=df_week_ri['Open'],
                                          high=df_week_ri['High'],
                                          low=df_week_ri['Low'],
                                          close=df_week_ri['Close'],
                                          name='あおぞら銀行')])

            fig6.add_traces(go.Scatter(x=df_week_ri['Date'], y=df_week_ri['SMA005'], name='移動平均05日'))
            fig6.add_traces(go.Scatter(x=df_week_ri['Date'], y=df_week_ri['SMA050'], name='移動平均50日'))
            fig6.add_traces(go.Scatter(x=df_week_ri['Date'], y=df_week_ri['SMA0100'], name='移動平均100日'))
            fig6.update_layout(title_text='週足')
            fig6.update_layout(xaxis_rangeslider_visible=True)
            st.plotly_chart(fig6, use_container_width=True)


            # 月足に変換する
            df_month = df_Security_code.resample("M").agg(agg_dict)
            
            df_month_ri = df_month.reset_index()
            df_month_ri['SMA005'] = df_month_ri['Close'].rolling(window=5).mean()
            df_month_ri['SMA050'] = df_month_ri['Close'].rolling(window=50).mean()
            df_month_ri['SMA0100'] = df_month_ri['Close'].rolling(window=100).mean()
            fig6 = go.Figure()
            fig6 = go.Figure(data=[go.Candlestick(x=df_month_ri['Date'],
                                          open=df_month_ri['Open'],
                                          high=df_month_ri['High'],
                                          low=df_month_ri['Low'],
                                          close=df_month_ri['Close'],
                                          name='あおぞら銀行')])

            fig6.add_traces(go.Scatter(x=df_month_ri['Date'], y=df_month_ri['SMA005'], name='移動平均05日'))
            fig6.add_traces(go.Scatter(x=df_month_ri['Date'], y=df_month_ri['SMA050'], name='移動平均50日'))
            fig6.add_traces(go.Scatter(x=df_month_ri['Date'], y=df_month_ri['SMA0100'], name='移動平均100日'))
            fig6.update_layout(title_text='月足')
            fig6.update_layout(xaxis_rangeslider_visible=True)
            st.plotly_chart(fig6, use_container_width=True)           





    if task == 'SPDRｺﾞｰﾙﾄﾞ':
    
        #if st.button('入力された銘柄のローソク足を表示する。'):
            df_Security_code=web.DataReader('1326.JP', "stooq",D)
            st.write('SPDRｺﾞｰﾙﾄﾞ','株価情報')
            st.dataframe(df_Security_code)

            df_Security_code_ri = df_Security_code.reset_index()
            df_Security_code_ri['SMA005'] = df_Security_code_ri['Close'].rolling(window=5).mean()
            df_Security_code_ri['SMA050'] = df_Security_code_ri['Close'].rolling(window=50).mean()
            df_Security_code_ri['SMA0100'] = df_Security_code_ri['Close'].rolling(window=100).mean()
            fig6 = go.Figure()
            fig6 = go.Figure(data=[go.Candlestick(x=df_Security_code_ri['Date'],
                                          open=df_Security_code_ri['Open'],
                                          high=df_Security_code_ri['High'],
                                          low=df_Security_code_ri['Low'],
                                          close=df_Security_code_ri['Close'],
                                          name='SPDRｺﾞｰﾙﾄﾞ')])

            fig6.add_traces(go.Scatter(x=df_Security_code_ri['Date'], y=df_Security_code_ri['SMA005'], name='移動平均05日'))
            fig6.add_traces(go.Scatter(x=df_Security_code_ri['Date'], y=df_Security_code_ri['SMA050'], name='移動平均50日'))
            fig6.add_traces(go.Scatter(x=df_Security_code_ri['Date'], y=df_Security_code_ri['SMA0100'], name='移動平均100日'))
            fig6.update_layout(title_text='SPDRｺﾞｰﾙﾄﾞ')
            fig6.update_layout(xaxis_rangeslider_visible=True)
            st.plotly_chart(fig6, use_container_width=True)


            #週足計算
            # カラムごとの計算手法を指定
            agg_dict = {
                        "Open": "first", 
                        "High": "max",
                        "Low": "min",
                        "Close": "last",
                        "Volume": "sum"
                        }
 
            # 週足に変換する
            df_week = df_Security_code.resample("W").agg(agg_dict)

            df_week_ri = df_week.reset_index()
            df_week_ri['SMA005'] = df_week_ri['Close'].rolling(window=5).mean()
            df_week_ri['SMA050'] = df_week_ri['Close'].rolling(window=50).mean()
            df_week_ri['SMA0100'] = df_week_ri['Close'].rolling(window=100).mean()
            fig6 = go.Figure()
            fig6 = go.Figure(data=[go.Candlestick(x=df_week_ri['Date'],
                                          open=df_week_ri['Open'],
                                          high=df_week_ri['High'],
                                          low=df_week_ri['Low'],
                                          close=df_week_ri['Close'],
                                          name='SPDRゴールド')])

            fig6.add_traces(go.Scatter(x=df_week_ri['Date'], y=df_week_ri['SMA005'], name='移動平均05日'))
            fig6.add_traces(go.Scatter(x=df_week_ri['Date'], y=df_week_ri['SMA050'], name='移動平均50日'))
            fig6.add_traces(go.Scatter(x=df_week_ri['Date'], y=df_week_ri['SMA0100'], name='移動平均100日'))
            fig6.update_layout(title_text='週足')
            fig6.update_layout(xaxis_rangeslider_visible=True)
            st.plotly_chart(fig6, use_container_width=True)


            # 月足に変換する
            df_month = df_Security_code.resample("M").agg(agg_dict)
            
            df_month_ri = df_month.reset_index()
            df_month_ri['SMA005'] = df_month_ri['Close'].rolling(window=5).mean()
            df_month_ri['SMA050'] = df_month_ri['Close'].rolling(window=50).mean()
            df_month_ri['SMA0100'] = df_month_ri['Close'].rolling(window=100).mean()
            fig6 = go.Figure()
            fig6 = go.Figure(data=[go.Candlestick(x=df_month_ri['Date'],
                                          open=df_month_ri['Open'],
                                          high=df_month_ri['High'],
                                          low=df_month_ri['Low'],
                                          close=df_month_ri['Close'],
                                          name='SPDRゴールド')])

            fig6.add_traces(go.Scatter(x=df_month_ri['Date'], y=df_month_ri['SMA005'], name='移動平均05日'))
            fig6.add_traces(go.Scatter(x=df_month_ri['Date'], y=df_month_ri['SMA050'], name='移動平均50日'))
            fig6.add_traces(go.Scatter(x=df_month_ri['Date'], y=df_month_ri['SMA0100'], name='移動平均100日'))
            fig6.update_layout(title_text='月足')
            fig6.update_layout(xaxis_rangeslider_visible=True)
            st.plotly_chart(fig6, use_container_width=True)           









    if task == '20年ｱﾒﾘｶ国債':
    
        #if st.button('入力された銘柄のローソク足を表示する。'):
            df_Security_code=web.DataReader('2621.JP', "stooq",D)
            st.write('20年ｱﾒﾘｶ国債','株価情報')
            st.dataframe(df_Security_code)

            df_Security_code_ri = df_Security_code.reset_index()
            df_Security_code_ri['SMA005'] = df_Security_code_ri['Close'].rolling(window=5).mean()
            df_Security_code_ri['SMA050'] = df_Security_code_ri['Close'].rolling(window=50).mean()
            df_Security_code_ri['SMA0100'] = df_Security_code_ri['Close'].rolling(window=100).mean()
            fig6 = go.Figure()
            fig6 = go.Figure(data=[go.Candlestick(x=df_Security_code_ri['Date'],
                                          open=df_Security_code_ri['Open'],
                                          high=df_Security_code_ri['High'],
                                          low=df_Security_code_ri['Low'],
                                          close=df_Security_code_ri['Close'],
                                          name='20年ｱﾒﾘｶ国債')])

            fig6.add_traces(go.Scatter(x=df_Security_code_ri['Date'], y=df_Security_code_ri['SMA005'], name='移動平均05日'))
            fig6.add_traces(go.Scatter(x=df_Security_code_ri['Date'], y=df_Security_code_ri['SMA050'], name='移動平均50日'))
            fig6.add_traces(go.Scatter(x=df_Security_code_ri['Date'], y=df_Security_code_ri['SMA0100'], name='移動平均100日'))
            fig6.update_layout(title_text='20年ｱﾒﾘｶ国債')
            fig6.update_layout(xaxis_rangeslider_visible=True)
            st.plotly_chart(fig6, use_container_width=True)


            #週足計算
            # カラムごとの計算手法を指定
            agg_dict = {
                        "Open": "first", 
                        "High": "max",
                        "Low": "min",
                        "Close": "last",
                        "Volume": "sum"
                        }
 
            # 週足に変換する
            df_week = df_Security_code.resample("W").agg(agg_dict)

            df_week_ri = df_week.reset_index()
            df_week_ri['SMA005'] = df_week_ri['Close'].rolling(window=5).mean()
            df_week_ri['SMA050'] = df_week_ri['Close'].rolling(window=50).mean()
            df_week_ri['SMA0100'] = df_week_ri['Close'].rolling(window=100).mean()
            fig6 = go.Figure()
            fig6 = go.Figure(data=[go.Candlestick(x=df_week_ri['Date'],
                                          open=df_week_ri['Open'],
                                          high=df_week_ri['High'],
                                          low=df_week_ri['Low'],
                                          close=df_week_ri['Close'],
                                          name='20年アメリカ国債')])

            fig6.add_traces(go.Scatter(x=df_week_ri['Date'], y=df_week_ri['SMA005'], name='移動平均05日'))
            fig6.add_traces(go.Scatter(x=df_week_ri['Date'], y=df_week_ri['SMA050'], name='移動平均50日'))
            fig6.add_traces(go.Scatter(x=df_week_ri['Date'], y=df_week_ri['SMA0100'], name='移動平均100日'))
            fig6.update_layout(title_text='週足')
            fig6.update_layout(xaxis_rangeslider_visible=True)
            st.plotly_chart(fig6, use_container_width=True)


            # 月足に変換する
            df_month = df_Security_code.resample("M").agg(agg_dict)
            
            df_month_ri = df_month.reset_index()
            df_month_ri['SMA005'] = df_month_ri['Close'].rolling(window=5).mean()
            df_month_ri['SMA050'] = df_month_ri['Close'].rolling(window=50).mean()
            df_month_ri['SMA0100'] = df_month_ri['Close'].rolling(window=100).mean()
            fig6 = go.Figure()
            fig6 = go.Figure(data=[go.Candlestick(x=df_month_ri['Date'],
                                          open=df_month_ri['Open'],
                                          high=df_month_ri['High'],
                                          low=df_month_ri['Low'],
                                          close=df_month_ri['Close'],
                                          name='20年アメリカ国債')])

            fig6.add_traces(go.Scatter(x=df_month_ri['Date'], y=df_month_ri['SMA005'], name='移動平均05日'))
            fig6.add_traces(go.Scatter(x=df_month_ri['Date'], y=df_month_ri['SMA050'], name='移動平均50日'))
            fig6.add_traces(go.Scatter(x=df_month_ri['Date'], y=df_month_ri['SMA0100'], name='移動平均100日'))
            fig6.update_layout(title_text='月足')
            fig6.update_layout(xaxis_rangeslider_visible=True)
            st.plotly_chart(fig6, use_container_width=True)           


###
    if task == '':
        
        Security_code = st.text_input('★銘柄コード入力(stooqサイトでのコードで！link参照')


    #'入力された銘柄名:', Security_code
        if st.button('入力された銘柄のローソク足を表示する。'):
    
        #  任意の銘柄の株価を取得
            df_Security_code=web.DataReader(Security_code, "stooq",D)
        #df_Security_code=web.DataReader(Security_code, "stooq",D)
            st.write(Security_code)
            st.dataframe(df_Security_code)

        # 日付がインデックスだとplotlyで描画されないようなので、インデックスから外す
            df_Security_code_ri = df_Security_code.reset_index()
        # st.print(df7203_reset_index)
        #st.write('Date をインデックスから外した')
        #st.dataframe(df_Security_code_ri)

        # 終値（Close）の移動平均線　5日、10日、25日を算出してデータフレームに追加します
            df_Security_code_ri['SMA005'] = df_Security_code_ri['Close'].rolling(window=5).mean()
        #df_Security_code_ri['SMA010'] = df_Security_code_ri['Close'].rolling(window=10).mean()
        #df_Security_code_ri['SMA025'] = df_Security_code_ri['Close'].rolling(window=25).mean()
            df_Security_code_ri['SMA050'] = df_Security_code_ri['Close'].rolling(window=50).mean()
            df_Security_code_ri['SMA0100'] = df_Security_code_ri['Close'].rolling(window=100).mean()
        #st.write('移動平均を算出')
        #st.dataframe(df_Security_code_ri)
        # 初期化
            fig6 = go.Figure()
 
        #st.write('ローソク足に移動平均線を追加')
 
            fig6 = go.Figure(data=[go.Candlestick(x=df_Security_code_ri['Date'],
                                          open=df_Security_code_ri['Open'],
                                          high=df_Security_code_ri['High'],
                                          low=df_Security_code_ri['Low'],
                                          close=df_Security_code_ri['Close'],
                                          name=Security_code)])
        # 移動平均線を追加
            fig6.add_traces(go.Scatter(x=df_Security_code_ri['Date'], y=df_Security_code_ri['SMA005'], name='移動平均05日'))
        #fig6.add_traces(go.Scatter(x=df_Security_code_ri['Date'], y=df_Security_code_ri['SMA010'], name='移動平均10日'))
        #fig6.add_traces(go.Scatter(x=df_Security_code_ri['Date'], y=df_Security_code_ri['SMA025'], name='移動平均25日'))
            fig6.add_traces(go.Scatter(x=df_Security_code_ri['Date'], y=df_Security_code_ri['SMA050'], name='移動平均50日'))
            fig6.add_traces(go.Scatter(x=df_Security_code_ri['Date'], y=df_Security_code_ri['SMA0100'], name='移動平均100日'))
        # チャートのタイトルを表示
            fig6.update_layout(title_text=Security_code)
 
        #スライドバー表示
            fig6.update_layout(xaxis_rangeslider_visible=True)
 
        # fig.show()
            st.plotly_chart(fig6, use_container_width=True)


            #週足計算
            # カラムごとの計算手法を指定
            agg_dict = {
                        "Open": "first", 
                        "High": "max",
                        "Low": "min",
                        "Close": "last",
                        "Volume": "sum"
                        }
 
            # 週足に変換する
            df_week = df_Security_code.resample("W").agg(agg_dict)

            df_week_ri = df_week.reset_index()
            df_week_ri['SMA005'] = df_week_ri['Close'].rolling(window=5).mean()
            df_week_ri['SMA050'] = df_week_ri['Close'].rolling(window=50).mean()
            df_week_ri['SMA0100'] = df_week_ri['Close'].rolling(window=100).mean()
            fig6 = go.Figure()
            fig6 = go.Figure(data=[go.Candlestick(x=df_week_ri['Date'],
                                          open=df_week_ri['Open'],
                                          high=df_week_ri['High'],
                                          low=df_week_ri['Low'],
                                          close=df_week_ri['Close'],
                                          name='銘柄コード')])

            fig6.add_traces(go.Scatter(x=df_week_ri['Date'], y=df_week_ri['SMA005'], name='移動平均05日'))
            fig6.add_traces(go.Scatter(x=df_week_ri['Date'], y=df_week_ri['SMA050'], name='移動平均50日'))
            fig6.add_traces(go.Scatter(x=df_week_ri['Date'], y=df_week_ri['SMA0100'], name='移動平均100日'))
            fig6.update_layout(title_text='週足')
            fig6.update_layout(xaxis_rangeslider_visible=True)
            st.plotly_chart(fig6, use_container_width=True)


            # 月足に変換する
            df_month = df_Security_code.resample("M").agg(agg_dict)
            
            df_month_ri = df_month.reset_index()
            df_month_ri['SMA005'] = df_month_ri['Close'].rolling(window=5).mean()
            df_month_ri['SMA050'] = df_month_ri['Close'].rolling(window=50).mean()
            df_month_ri['SMA0100'] = df_month_ri['Close'].rolling(window=100).mean()
            fig6 = go.Figure()
            fig6 = go.Figure(data=[go.Candlestick(x=df_month_ri['Date'],
                                          open=df_month_ri['Open'],
                                          high=df_month_ri['High'],
                                          low=df_month_ri['Low'],
                                          close=df_month_ri['Close'],
                                          name='銘柄コード')])

            fig6.add_traces(go.Scatter(x=df_month_ri['Date'], y=df_month_ri['SMA005'], name='移動平均05日'))
            fig6.add_traces(go.Scatter(x=df_month_ri['Date'], y=df_month_ri['SMA050'], name='移動平均50日'))
            fig6.add_traces(go.Scatter(x=df_month_ri['Date'], y=df_month_ri['SMA0100'], name='移動平均100日'))
            fig6.update_layout(title_text='月足')
            fig6.update_layout(xaxis_rangeslider_visible=True)
            st.plotly_chart(fig6, use_container_width=True)           






###
if sideradio == 'ライオン戦略/資産形成':
    
    st.subheader('ライオン戦略とは')

    """
    Link参照. 
    """
    """
    購入商品の前月の騰落率が計算されます．アセットアロケーション，ポートフォリオにどうぞ．
    """

    task = st.selectbox('★購入商品',('','日経平均', 'sp500','上海総合指数', '先進国','あおぞら銀行', 'SPDRｺﾞｰﾙﾄﾞ','20年ｱﾒﾘｶ国債'))
    #task = st.selectbox('★追加用',())

    ##値上がり率，騰落率計算
    def my_sum(x,y):
        z = (y - x) / x * 100
        return z

    

    if task == '日経平均':
        #日経平均のデータ取得，前月始めと終日
        dn = web.DataReader('^NKX' , "stooq",A,C)  
        pre_firstday_NKX = dn.tail(1)
        pre_Allday_NKX = dn.head(1)
        X = pre_firstday_NKX.iloc[0, 3]
        Y = pre_Allday_NKX.iloc[0, 3]
        
        st.write('前月始め',X)
        st.write('前月終日',Y)

        if __name__ == '__main__':
            pre_NKX = my_sum(X, Y)
            st.write('値上がり率:','{:.2f}'.format(pre_NKX),'%')
        
        dn


        #グラフ
        st.write(
            px.line(dn, y='Close' ,title="日経")
                )
    

    if task == 'sp500':
        #sp500のデータ
        ds = web.DataReader('1655.JP' , "stooq",A ,C )
        pre_firstday_sp500 = ds.tail(1)
        pre_Allday_sp500 = ds.head(1)
        XX = pre_firstday_sp500.iloc[0, 3]
        YY = pre_Allday_sp500.iloc[0, 3]
        
        st.write('前月始め',XX)
        st.write('前月終日',YY)

        if __name__ == '__main__':
            pre_sp500 = my_sum(XX, YY)
            st.write('値上がり率:','{:.2f}'.format(pre_sp500),'%')

        ds

        #グラフ
        st.write(
            px.line(ds, y='Close' ,title="sp500")
            )
    
    if task == '上海総合指数':
        #上海総合指数のデータ
        dc = web.DataReader('^SHC' , "stooq",A ,C )
        pre_firstday_SHC = dc.tail(1)
        pre_Allday_SHC = dc.head(1)
        XXX = pre_firstday_SHC.iloc[0, 3]
        YYY = pre_Allday_SHC.iloc[0, 3]
        
        st.write('前月始め',XXX)
        st.write('前月終日',YYY)


        if __name__ == '__main__':
            pre_SHC = my_sum(XXX, YYY)
            st.write('値上がり率:','{:.2f}'.format(pre_SHC),'%')

        dc

        #グラフ
        st.write(
            px.line(dc, y='Close' ,title="上海総合指数")
            )

    if task == '先進国':
        #先進国のデータ
        dfi = web.DataReader('1657.JP' , "stooq",A ,C) 
        pre_firstday_1657 = dfi.tail(1)
        pre_Allday_1657 = dfi.head(1)
        XXXX = pre_firstday_1657.iloc[0, 3]
        YYYY = pre_Allday_1657.iloc[0, 3]
        
        st.write('前月始め',XXXX)
        st.write('前月終日',YYYY)

        if __name__ == '__main__':
            pre_1657 = my_sum(XXXX, YYYY)
            st.write('値上がり率:','{:.2f}'.format(pre_1657),'%')

        dfi

        #グラフ
        st.write(
            px.line(dfi, y='Close' ,title="先進国")
            )

    if task == 'あおぞら銀行':
        #あおぞら銀行のデータ
        dmy = web.DataReader('8304.JP' , "stooq",A,C) 
        pre_firstday_8304 = dmy.tail(1)
        pre_Allday_8304 = dmy.head(1)
        XXXXX = pre_firstday_8304.iloc[0, 3]
        YYYYY = pre_Allday_8304.iloc[0, 3]
        
        st.write('前月始め',XXXXX)
        st.write('前月終日',YYYYY)

        if __name__ == '__main__':
            pre_8304 = my_sum(XXXXX, YYYYY)
            st.write('値上がり率:','{:.2f}'.format(pre_8304),'%')

        dmy

        #グラフ
        st.write(
            px.line(dmy, y='Close' ,title="あおぞら銀行")
            )

    if task == 'SPDRｺﾞｰﾙﾄﾞ':
        #金のデータ
        dgo = web.DataReader('1326.JP' , "stooq",A,C)
        pre_firstday_1326 = dgo.tail(1)
        pre_Allday_1326 = dgo.head(1)
        XXXXXX = pre_firstday_1326.iloc[0, 3]
        YYYYYY = pre_Allday_1326.iloc[0, 3]
        
        st.write('前月始め',XXXXXX)
        st.write('前月終日',YYYYYY)


        if __name__ == '__main__':
            pre_1326 = my_sum(XXXXXX, YYYYYY)
            st.write('値上がり率:','{:.2f}'.format(pre_1326),'%')

        dgo

        #グラフ
        st.write(
            px.line(dgo, y='Close' ,title="SPDRｺﾞｰﾙﾄﾞ")
            )
    
    if task == '20年ｱﾒﾘｶ国債':
        #20年ｱﾒﾘｶ国債のデータ
        dsai = web.DataReader('2621.JP', "stooq",A,C)
        pre_firstday_2621 = dsai.tail(1)
        pre_Allday_2621 = dsai.head(1)
        XXXXXXX = pre_firstday_2621.iloc[0, 3]
        YYYYYYY = pre_Allday_2621.iloc[0, 3]
        
        st.write('前月始め',XXXXXXX)
        st.write('前月終日',YYYYYYY)

        if __name__ == '__main__':
            pre_2621 = my_sum(XXXXXXX, YYYYYYY)
            st.write('値上がり率:','{:.2f}'.format(pre_2621),'%')

        dsai

        #グラフ
        st.write(
            px.line(dsai, y='Close' ,title="20年ｱﾒﾘｶ国債")
            )


    if task == '':
        my_code = st.text_input('★銘柄コード入力(stooqサイトでのコードで！link参照)')
        if st.button('入力された銘柄のローソク足を表示する。'):
        #  任意の銘柄の株価を取得
            my_code=web.DataReader(my_code, "stooq",A,C)

            pre_firstday_my = my_code.tail(1)
            pre_Allday_my = my_code.head(1)
            XXXXXXXX = pre_firstday_my.iloc[0, 3]
            YYYYYYYY = pre_Allday_my.iloc[0, 3]
            st.write('前月始め',XXXXXXXX)
            st.write('前月終日',YYYYYYYY)

            if __name__ == '__main__':
                pre_my = my_sum(XXXXXXXX, YYYYYYYY)
                st.write('値上がり率:','{:.2f}'.format(pre_my),'%')
            
            my_code

            #グラフ
            st.write(
                px.line(my_code, y='Close' ,title= None)
                )






    st.subheader('資産形成')

    agree = st.checkbox('さぁ，自分だけのライオンを作るんだ！')

    if agree == True :
        def my_sum(x,y):
            z = (y - x) / x * 100
            return z

        #日経平均
        dn = web.DataReader('^NKX' , "stooq",A,C)  
        pre_firstday_NKX = dn.tail(1)
        pre_Allday_NKX = dn.head(1)
        X = pre_firstday_NKX.iloc[0, 3]
        Y = pre_Allday_NKX.iloc[0, 3]
        pre_NKX = my_sum(X, Y)
        #sp500
        ds = web.DataReader('1655.JP' , "stooq",A ,C )
        pre_firstday_sp500 = ds.tail(1)
        pre_Allday_sp500 = ds.head(1)
        XX = pre_firstday_sp500.iloc[0, 3]
        YY = pre_Allday_sp500.iloc[0, 3]
        pre_sp500 = my_sum(XX, YY)


        #先進国
        dfi = web.DataReader('1657.JP' , "stooq",A ,C) 
        pre_firstday_1657 = dfi.tail(1)
        pre_Allday_1657 = dfi.head(1)
        XXXX = pre_firstday_1657.iloc[0, 3]
        YYYY = pre_Allday_1657.iloc[0, 3]
        pre_1657 = my_sum(XXXX, YYYY)

         #VTIのデータ
        dmy = web.DataReader('VTI.US' , "stooq",A,C) 
        pre_firstday_vti = dmy.tail(1)
        pre_Allday_vti = dmy.head(1)
        XXXXX = pre_firstday_vti.iloc[0, 3]
        YYYYY = pre_Allday_vti.iloc[0, 3]
        pre_vti = my_sum(XXXXX, YYYYY)

        #金のデータ
        dgo = web.DataReader('1326.JP' , "stooq",A,C)
        pre_firstday_1326 = dgo.tail(1)
        pre_Allday_1326 = dgo.head(1)
        XXXXXX = pre_firstday_1326.iloc[0, 3]
        YYYYYY = pre_Allday_1326.iloc[0, 3]
        pre_1326 = my_sum(XXXXXX, YYYYYY)

        #20年アメリカ国債
        dsai = web.DataReader('2621.JP', "stooq",A,C)
        pre_firstday_2621 = dsai.tail(1)
        pre_Allday_2621 = dsai.head(1)
        XXXXXXX = pre_firstday_2621.iloc[0, 3]
        YYYYYYY = pre_Allday_2621.iloc[0, 3]
        pre_2621 = my_sum(XXXXXXX, YYYYYYY)


        df = pd.DataFrame(data={'銘柄コード': ['先進国', 'VTI','SPDRｺﾞｰﾙﾄﾞ','20年ｱﾒﾘｶ国債','日経平均','sp500'],
                            '値上がり率(%)':[pre_1657, pre_vti, pre_1326, pre_2621,pre_NKX,pre_sp500]
                            })
        df_list = df['銘柄コード'].unique()
        options = st.multiselect('最強ポートフォリオ．若松監修',df_list,['先進国', 'VTI','SPDRｺﾞｰﾙﾄﾞ','20年ｱﾒﾘｶ国債'])
        DF = df[(df['銘柄コード'].isin(options))]
        st.table(DF)


        my_code = st.text_input('★追加したい銘柄コード')
        
        if st.button('入力された銘柄を追加する。'):
        #  任意の銘柄の株価を取得
            my_code=web.DataReader(my_code, "stooq",A,C)
            pre_firstday_my = my_code.tail(1)
            pre_Allday_my = my_code.head(1)
            XXXXXXXX = pre_firstday_my.iloc[0, 3]
            YYYYYYYY = pre_Allday_my.iloc[0, 3]
            pre_my = my_sum(XXXXXXXX, YYYYYYYY)    
            df1 = pd.DataFrame(data={'銘柄コード': ['入力した銘柄'],'値上がり率(%)':[pre_my]})
            df2 = df.append(df1)
            st.table(df2)



if sideradio == 'MR':

    st.title('SNR(差分法)だしてみた')

    st.subheader('SNRを手計算でしている方必見!')

    
    uploaded_files_1 = st.file_uploader("★DATA_1を選択してね！", accept_multiple_files=True)
    datas_1 = []
    for uploaded_file_1 in uploaded_files_1:
        img_1 = pydicom.dcmread(uploaded_file_1)
        pixels_1 = img_1.pixel_array
        data_df_1 = pd.DataFrame(pixels_1)
        datas_1.append(data_df_1)
    ##必要な時に書く
    #df_1 = pd.concat(datas_1,axis=0)
    #df_1 = df_1.astype("float64")
    #st.write(datas_1)
    #st.write(df_1)

    uploaded_files_2 = st.file_uploader("★DATA_2を選択してね！", accept_multiple_files=True)
    datas_2 = []
    for uploaded_file_2 in uploaded_files_2:
        img_2 = pydicom.dcmread(uploaded_file_2)
        pixels_2 = img_2.pixel_array
        data_df_2 = pd.DataFrame(pixels_2)
        datas_2.append(data_df_2)

    #必要な時に書く
    #df_2 = pd.concat(datas_2,axis=0)
    #df_2 = df_2.astype("float64")


    #rogin_name = st.text_input('★ROIのピクセル数を入力．imageJ等で調査','例.5000')
    z = int(st.number_input('★ROIのピクセル数を入力．imageJ等で調査'))
    #'入力された銘柄名:', Security_code
    if st.button('ROI設定とSNR結果一覧'):
        st.write('ROI画像')
        fig, ax = plt.subplots(figsize=(1,1))
        ax.imshow(pixels_1,cmap='gray')
        ax.set_axis_off()
        st.pyplot(fig)



     

    



    


 


