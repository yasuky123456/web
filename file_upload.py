#DICOM読み込み
#https://biotech-lab.org/articles/2391#DICOM-4


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
from io import StringIO


#DICOM_single 入出力
"""
uploaded_file = st.file_uploader("Choose DICOM")
if uploaded_file is not None:
    img_1 = pydicom.dcmread(uploaded_file)
    pixels_1 = img_1.pixel_array
    #st.write(type(img_1))
    #st.write(type(pixels_1))
    #st.image(pixels_1,caption = 'サムネイル画像',use_column_width = True)
    #st.pyplot(pixels_1)
    fig, ax = plt.subplots(figsize=(1,1))
    ax.imshow(pixels_1,cmap='gray')
    ax.set_axis_off()
    st.pyplot(fig)
"""

"""
uploaded_file = st.file_uploader("Choose DICOM")
if uploaded_file is not None:
    img_1 = pydicom.dcmread(uploaded_file)
    pixels_1 = img_1.pixel_array
    #st.write(img_1)

"""





#DICOM_マルチ 入出力
"""
uploaded_files = st.file_uploader("Choose a DICOM file", accept_multiple_files=True)
datas_1 = []
for uploaded_file in uploaded_files:
    img_1 = pydicom.dcmread(uploaded_file)
    pixels_1 = img_1.pixel_array
    data_df_1 = pd.DataFrame(pixels_1)
    datas_1.append(data_df_1)
df_1 = pd.concat(datas_1,axis=0)
df_1 = df_1.astype("float64")
#st.write(datas_1)
st.write(df_1)
"""