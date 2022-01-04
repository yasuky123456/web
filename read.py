#DICOM画像, streamlitで表示

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
import plotly.graph_objects as go
import pathlib  # 標準ライブラリ
#import openpyxl # 外部ライブラリ　
import csv      # 標準ライブラリ
import glob
import pandas as pd
import os
from pathlib import Path
import numpy as np
import math
import pydicom
from PIL import Image
import re
import cv2

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

files_1 = sorted(glob.glob('C:\\Users\\koya\\Desktop\\SNR_DICOM\\1回目\\*.dcm'), key=natural_keys)
    #順番確認
st.write(files_1)


files_2 = sorted(glob.glob('C:\\Users\\koya\\Desktop\\SNR_DICOM\\2回目\\*.dcm'), key=natural_keys)
    #順番確認
st.write(files_2)

path_img = 'C:\\Users\\koya\\Desktop\\'


for i in files_1 :
    img = pydicom.dcmread(i)
    pixels = img.pixel_array
    cv2.imwrite(path_img + "SNR.jpg", pixels)

#画像表示

image = Image.open('C:\\Users\\koya\\Desktop\\SNR.jpg')
st.image(image, caption='ROI画像',use_column_width=False)