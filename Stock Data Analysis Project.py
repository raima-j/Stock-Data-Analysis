
# Importing required libraries.
import yfinance as yf 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 
from datetime import date,timedelta

today=date.today()
tickers_list=['AMZN','GOOG','MSFT','AAPL'] 
#For Amazon, Google, Microsoft and Apple stocks.

## To get the format of dates.
date1=today.strftime("%Y-%m-%d")
date2=today-timedelta(days=365)  #Taking 1 Year's data as the sample.
start_date=date2
end_date=date1

## To read and save the data to analyse directly.
data_amzn=yf.download('AMZN',start=start_date,end=end_date,progress=False)
data_goog=yf.download('GOOG',start=start_date,end=end_date,progress=False)
data_msft=yf.download('MSFT',start=start_date,end=end_date,progress=False)
data_aapl=yf.download('AAPL',start=start_date,end=end_date,progress=False)
df_list=[]

## Dataframe for Amazon
print ('\n%--This prediction analysis takes stocks data for the past 1 Year--%\n')
data_amzn["Date"] = data_amzn.index
data_amzn = data_amzn[["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]]
data_amzn.reset_index(drop=True, inplace=True)
amzn_df=pd.DataFrame(data_amzn)
print('\nSample data for first 5 days for Amazon:\n',data_amzn.head())
df_list.append(amzn_df)

## Dataframe for Google
data_goog["Date"] = data_goog.index
data_goog = data_goog[["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]]
data_goog.reset_index(drop=True, inplace=True)
goog_df=pd.DataFrame(data_goog)
print('\nSample data for first 5 days for Google:\n',data_goog.head())
df_list.append(goog_df)

## Dataframe for Microsoft
data_msft["Date"] = data_msft.index
data_msft = data_msft[["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]]
data_msft.reset_index(drop=True, inplace=True)
msft_df=pd.DataFrame(data_msft)
print('\nSample data for first 5 days for Microsoft:\n',data_msft.head())
df_list.append(msft_df)

## Dataframe for Apple
data_aapl["Date"] = data_aapl.index
data_aapl = data_aapl[["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]]
data_aapl.reset_index(drop=True, inplace=True)
aapl_df=pd.DataFrame(data_aapl)
print('\nSample data for first 5 days for Apple:\n',data_aapl.head())
df_list.append(aapl_df)

## Checking and Cleaning data from each stock's dataframe.
print ('\nAbout the dataframes:')
amzn_df.info() #All dataframes have the same information.
print ('\nTotal null values in the AMZN dataframe:\n',amzn_df.isna().sum())
print ('\nTotal null values in the GOOG dataframe:\n',goog_df.isna().sum())
print ('\nTotal null values in the MSFT dataframe:\n',msft_df.isna().sum())
print ('\nTotal null values in the AAPL dataframe:\n',aapl_df.isna().sum())

print ('\nTotal duplicate values in the AMZN dataframe:\n',amzn_df.duplicated().sum())
print ('Total duplicate values in the GOOG dataframe:\n',goog_df.duplicated().sum())
print ('Total duplicate values in the MSFT dataframe:\n',msft_df.duplicated().sum())
print ('Total duplicate values in the AAPL dataframe:\n',aapl_df.duplicated().sum())

print ('\nMean values in the AMZN dataframe:\n',amzn_df.describe().round(2))
print ('\nMean values in the GOOG dataframe:\n',goog_df.describe().round(2))
print ('\nMean values in the MSFT dataframe:\n',msft_df.describe().round(2))
print ('\nMean values in the AAPL dataframe:\n',aapl_df.describe().round(2))
#If these values return all 0, the data is cleaned and ready for analysis.


## Daily return for each stock.
for df in df_list:
    df['Daily Ret']=(df['Close']-df['Open'])/df['Open']*100

## Percentage change for each stock.
for df in df_list:
    df['Chg%']=df['Close'].pct_change()*100

print ("\nDaily return average for AMZN stocks:\n",data_amzn['Daily Ret'].mean())
print ("Daily return average for GOOG stocks:\n",data_goog['Daily Ret'].mean())
print ("Daily return average for MSFT stocks:\n",data_msft['Daily Ret'].mean())
print ("Daily return average for AAPL stocks:\n",data_aapl['Daily Ret'].mean())

## Change in the prices of each stock over a period of 1 Year.
sns.set_style('dark')
sns.set_palette('deep')
sns.lineplot(data=amzn_df,x=amzn_df['Date'],y=amzn_df['Close'],label='AMZN')
sns.lineplot(data=goog_df,x=goog_df['Date'],y=goog_df['Close'],label='GOOG')
sns.lineplot(data=msft_df,x=msft_df['Date'],y=msft_df['Close'],label='MSFT')
sns.lineplot(data=aapl_df,x=aapl_df['Date'],y=aapl_df['Close'],label='AAPL')
plt.title("Change in Close Prices for each Stocks")
plt.xticks(rotation=25)
plt.show()

## Change in the volume of each stock traded over a period of 1 Year.
fig,axs=plt.subplots(2,2)
axs[0,0].plot(amzn_df['Date'],amzn_df['Volume'],color='pink')
axs[0,0].set_title('AMZN Volumes Traded')
axs[1,0].plot(goog_df['Date'],goog_df['Volume'],color='hotpink')
axs[1,0].set_title('GOOG Volumes Traded')
axs[0,1].plot(msft_df['Date'],msft_df['Volume'],color='purple')
axs[0,1].set_title('MSFT Volumes Traded')
axs[1,1].plot(aapl_df['Date'],aapl_df['Volume'],color='lightblue')
axs[1,1].set_title('AAPL Volumes Traded')
fig.tight_layout()
plt.show()

## Moving average for each stock.
for df in df_list:
    df['Moving Avg']=df['Close'].rolling(7).mean()

plt.style.use('seaborn-pastel')
fig,axs=plt.subplots(2,2)
axs[0,0].plot(amzn_df['Date'],amzn_df[['Close','Moving Avg']])
axs[0,0].set_title('AMZN Moving Average')
axs[1,0].plot(goog_df['Date'],goog_df[['Close','Moving Avg']])
axs[1,0].set_title('GOOG Moving Average')
axs[0,1].plot(msft_df['Date'],msft_df[['Close','Moving Avg']])
axs[0,1].set_title('MSFT Moving Average')
axs[1,1].plot(aapl_df['Date'],aapl_df[['Close','Moving Avg']])
axs[1,1].set_title('AAPL Moving Average')
fig.tight_layout()
plt.show()

## Plotting each moving average in one plot.
sns.set_style('dark')
sns.set_palette('muted')
sns.lineplot(data=amzn_df,x=amzn_df['Date'],y=amzn_df['Moving Avg'],label='AMZN')
sns.lineplot(data=goog_df,x=goog_df['Date'],y=goog_df['Moving Avg'],label='GOOG')
sns.lineplot(data=msft_df,x=msft_df['Date'],y=msft_df['Moving Avg'],label='MSFT')
sns.lineplot(data=aapl_df,x=aapl_df['Date'],y=aapl_df['Moving Avg'],label='AAPL')
plt.title("Moving Average for each Stocks")
plt.xticks(rotation=25)
plt.show()

## Trend for each stock's daily return.

def trend_frequency(df):
    trend_frequency = {
        'Uptrend': 0,
        'Downtrend': 0,
        'Sideways': 0
    }

    for return_value in df['Daily Ret']:
        if return_value > 1:
            trend_frequency['Uptrend'] += 1
            df['Trend']='Uptrend'
        elif return_value < -1:
            trend_frequency['Downtrend'] += 1
            df['Trend']='Downtrend'
        else:
            trend_frequency['Sideways'] += 1
            df['Trend']='Sideways'

    #Frequency percentages
    total_data_points = len(df['Daily Ret'])
    for trend, count in trend_frequency.items():
        trend_frequency[trend] = (count / total_data_points) * 100
    return (trend_frequency)


plt.style.use('seaborn-pastel')
fig,axs=plt.subplots(2,2)
axs[0,0].pie(trend_frequency(amzn_df).values(),labels=trend_frequency(amzn_df).keys(),autopct='%0.2f')
axs[0,0].set_title('AMZN Trend Frequency')
axs[1,0].pie(trend_frequency(goog_df).values(),labels=trend_frequency(goog_df).keys(),autopct='%0.2f')
axs[1,0].set_title('GOOG Trend Frequency')
axs[0,1].pie(trend_frequency(msft_df).values(),labels=trend_frequency(msft_df).keys(),autopct='%0.2f')
axs[0,1].set_title('MSFT Trend Frequency')
axs[1,1].pie(trend_frequency(aapl_df).values(),labels=trend_frequency(aapl_df).keys(),autopct='%0.2f')
axs[1,1].set_title('AAPL Trend Frequency')
fig.tight_layout()
plt.show()

## Correlation between Daily returns.
corr_data=pd.DataFrame({'AMZN':amzn_df['Daily Ret'],'GOOG':goog_df['Daily Ret'],'MSFT':msft_df['Daily Ret'],'AAPL':aapl_df['Daily Ret']})
corr_matrix=corr_data.corr()
print ('\nThe correlation between the daily returns of each stock is as follows:\n',corr_matrix)

## Conclusion.
print ('\nUsing the trend details and the moving average, it becomes easier to analyse stock predictions.\n\n')

##---End of Code for Final Project (Internship, Edureka) Raima Joseph---##
