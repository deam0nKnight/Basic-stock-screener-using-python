
#pre-requisite yfinance api - pip install yfinance
import yfinance as yf

s_info = {}
def get_quote(stock,time='ytd'): #defining a function to get the historical price of a stock
    try:
        str_ticker = yf.Ticker(str(stock))
        s_info[str(stock)] = str_ticker.history(period=str(time))
        for i in s_info:
            globals()[i] = s_info[i]
            globals()[i]['Return'] = globals()[i]['Open'] - globals()[i]['Close']
            #adding a new column called return (it is the daily open -close)
    except:
        print('Ticker not found')
def get_earnings(stock): #defining a function to get the earnings of a stock 
    ticker = yf.Ticker(stock)
    globals()[stock] = ticker.earnings
def info(stock): #defining a function to get the information of a stock     
    str_ticker = yf.Ticker(str(stock))
    globals()[stock] = str_ticker.info
def recommender(s,rating):
    info(s)
    s_rating = globals()[s]['recommendationKey']
    if rating == globals()[s]['recommendationKey']:
        print(s,globals()[s]['recommendationKey']) #prints the stock s and its yahoo rating 

def five_day(stock):
    try:
        get_quote(stock,'5d') #gets price quote for the last 5 days for a stock 
        y_1 = globals()[stock].iloc[4]['Return']
        y_2 = globals()[stock].iloc[3]['Return']
        y_3 = globals()[stock].iloc[2]['Return']
        y_4 = globals()[stock].iloc[1]['Return']
        y_5 = globals()[stock].iloc[0]['Return']
        if y_1>0 and y_2>0 and y_3>0 and y_4>0 and y_5>0:
            print(stock, 'Buy') #buy rating if 5 day positive return trend
        else:
            print(stock, 'Wait') #wait rating if it does not match
    except:
        print(stock,'No Data')
def sector(s,sector): #take s = stock and sector arguments
    info(str(s))
    s_sector = globals()[s]['sector']
    if sector == globals()[s]['sector']:
        print(s,s_sector) #prints the stock ticker and the sector it belongs to 
def rev_earnings(stock):
    try:
        get_earnings(stock)
        y_1 = globals()[stock].iloc[0]['Earnings']
        y_2 = globals()[stock].iloc[1]['Earnings']
        y_3 = globals()[stock].iloc[2]['Earnings']
        y_4 = globals()[stock].iloc[3]['Earnings']
        if y_4>y_3 and y_3>y_2 and y_2>y_1:
            print(stock, 'Buy') #buy rating for 3 positive earning 
        else:
            print(stock, 'Wait') #wait if it does not match 
    except:
        print(stock,'No Data') #if not found


user_input = int(input('Which Screener would you like to use?\n1) Yahoo buy/sell/hold recommendations?\n2)buy rating - 5-day positive stock return?\n3)See tickers by sectors\n4) Buy Rating- 3 year positive earning trend?\n5) Get historical data for ticker by day/month/year\n>>'))
if user_input == 1:
    which_rating = int(input('Which recommendation would you like to see?\n1) Buy\n2)hold\n 3)sell\n>>'))
    if which_rating ==1:
        for s in stocks:
            recommender(s,'buy')
    elif which_rating ==2:
        for s in stocks:
            recommender(s,'hold')
    elif which_rating ==3:
        for s in stocks:
            recommender(s,'sell')
    print('Done')
elif user_input == 2:
        for s in stocks:
            five_day(s)
        print('Done')
elif user_input ==3:
    which_sector = int(input('Which Sector would you like to see?\n1)Technology\n2)Basic Materials\n3)Communication Services\n4)Consumer Cyclical\n5)Consumer Defensive\n6)Energy\n7)Financial Services\n8)Healthcare\n9)Industrials\n10)Utilities\n>>'))
    if which_sector ==1:
        for s in stocks:
            sector(s,'Technology')
    elif which_sector ==2:
        for s in stocks:
            sector(s,'Basic Materials')
    elif which_sector ==3:
        for s in stocks:
            sector(s,'Communication Services')
    elif which_sector ==4:
        for s in stocks:
            sector(s,'Consumer Cyclical')
    elif which_sector ==5:
        for s in stocks:
            sector(s,'Consumer Defensive')
    elif which_sector ==6:
        for s in stocks:
            sector(s,'Energy')
    elif which_sector ==7:
        for s in stocks:
            sector(s,'Financial Services')
    elif which_sector ==8:
        for s in stocks:
            sector(s,'Healthcare')
    elif which_sector ==9:
        for s in stocks:
            sector(s,'Industrials')
    elif which_sector ==10:
        for s in stocks:
            sector(s,'Utilities')
    print('Done')
elif user_input ==4:
    for s in stocks:
        rev_earnings(s)
    print('Done')
elif user_input==5:
    e_input = input('would you like to see all available tickers?(Enter y or n>>')
    if e_input == 'y' or e_input == 'Y':
        print(stocks)
    which_ticker = input('Ticker?>>')
    ticker_cap = which_ticker.upper()
    time_period = input('which time period?(Example 1d,5d, 1mo,6mo,1y,ytd,5y,max)(Enter as in example)')
    str_ticker = yf.Ticker(str(ticker_cap))
    print(str_ticker.history(period=str(time_period)))
    save_csv = input('Would you like to save to csv?(Enter y or n)\n>>')
    if save_csv =='y' or save_csv =='Y': 
        globals()[which_ticker] = str_ticker.history(period=str(time_period))
        globals()[which_ticker].to_csv(which_ticker+'.csv',sep=',') #writes to cwd with the ticker name entered by the user eg aapl - aapl.csv
    print('Done')
