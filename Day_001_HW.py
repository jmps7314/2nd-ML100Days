#!/usr/bin/env python
# coding: utf-8

# 作業1：
# 
# 請上 Kaggle, 在 Competitions 或 Dataset 中找一組競賽或資料並寫下：
# 
# 1. 你選的這組資料為何重要
# A:我選的是S&P 500 stock data，用以了解未來股市的起伏發展
# 
# 2. 資料從何而來 (tips: 譬如提供者是誰、以什麼方式蒐集)
# A:資料來自於美國500家大型企業，從2013年2月到2018年2月的股價數值
# 
# 3. 蒐集而來的資料型態為何
# A:數字
# 
# 4. 這組資料想解決的問題如何評估
# A:未來股價趨勢
# 
# 
# 作業2：
# 
# 想像你經營一個自由載客車隊，你希望能透過數據分析以提升業績，請你思考並描述你如何規劃整體的分析/解決方案：
# 
# 1. 核心問題為何 (tips：如何定義 「提升業績 & 你的假設」)
# A:哪個時段載客量最多
# 
# 2. 資料從何而來 (tips：哪些資料可能會對你想問的問題產生影響 & 資料如何蒐集)
# A:App叫車資料，價錢、天氣
# 
# 3. 蒐集而來的資料型態為何
# A:excel表格數據
# 
# 4. 你要回答的問題，其如何評估 (tips：你的假設如何驗證)
# A:統計早上、下午、晚上、凌晨各時段的載客量，做檢定測驗結果
# 
# 練習時間
# 請寫一個函式用來計算 Mean Square Error
# $ MSE = \frac{1}{n}\sum_{i=1}^{n}{(Y_i - \hat{Y}_i)^2} $
# 
# Hint: 如何取平方

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


def mean_squared_error(y,yp):
    '''
    計算 MSE
    Args:
         - y: 實際值
         - yp: 預測值
    Return:
         - mse: MSE
    '''
    mse = MSE = sum((y-yp)**2)/len(y)
    return mse


# In[3]:


def mean_absolute_error(y,yp):
    '''
    計算 MAE
    Args:
        - y: 實際值
        - yp: 預測值
    Return:
        - mae: MAE
    '''
    mae = MAE = sum(abs(y - yp)) / len(y)
    return mae


# In[4]:


w = 3
b = 0.5

x_lin = np.linspace(0, 100, 101)

y = (x_lin + np.random.randn(101) * 5) * w + b

plt.plot(x_lin, y, 'b.', label = 'data points')
plt.title("Assume we have data points")
plt.legend(loc = 2)
plt.show()


# In[5]:


y_hat = x_lin * w + b
plt.plot(x_lin, y, 'b.', label = 'data')
plt.plot(x_lin, y_hat, 'r-', label = 'prediction')
plt.title("Assume we have data points (And the prediction)")
plt.legend(loc = 2)
plt.show()


# In[6]:


# 執行 Function, 確認有沒有正常執行
MSE = mean_squared_error(y, y_hat)
MAE = mean_absolute_error(y, y_hat)
print("The Mean squared error is %.3f" % (MSE))
print("The Mean absolute error is %.3f" % (MAE))


# In[ ]:




