import warnings
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import date, timedelta
import datetime
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
from datetime import timedelta as td, datetime
from scipy.signal import find_peaks
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
from scipy.interpolate import make_interp_spline, BSpline
from scipy import interpolate
# from configs import *
# mm = MinMaxScaler()
warnings.filterwarnings("ignore")
# data = pd.read_csv('C:/Users/FTECH/OneDrive/Downloads/user.csv')
# data


# for num in range(0, 10):
#     for i in range(2, num):
#         if num % i == 0:
#             j = num/i
#             print(' %d bằng %d*%d ' % (num, i, j))
#             break
#     else:
#         print(num, 'là số nguyên tố')

# n = int(input(' Nhập giá trị n : '))
# s = 0
# for i in range(2,n+1,2):
#     s = s + i
# print('tổng s là: ',s)
# for i in  (range(1,100,2)):
#     print(i) 

n = int(input('Nhập giá trị n :')) 
for i in range(1,11):
    s  = n*i
    print('{:<2}x {:<2}= {:<2}'.format(n, i, n*i))
