from easygui import *
import random

balance = 100000
week = 1

STOCKS = ['BABA.gif',
          'AMZN.gif',
          'HD.gif',
          'INTC.gif',
          'SBUX.gif',
          'AAPL.gif',
          'MSFT.gif',
          'GOOG.gif',
          'WMT.gif',
          'V.gif',
          'NKE.gif',
          'TSLA.gif',
          'EA.gif',
          'PYPL.gif',
          'NFLX.gif',
          'MCD.gif',
          'RL.gif',
          'IBM.gif',
          'CMG.gif',
          'KO.gif',
          'PEP.gif']

babaprice = 149
amznprice = 1592
hdprice = 172
intcprice = 48
sbuxprice = 65
aaplprice = 165
msftprice = 106
googprice = 1042
wmtprice = 92
vprice = 135
nkeprice = 73
tslaprice = 366
eaprice = 80
pyplprice = 86
nflxprice = 267
mcdprice = 183
rlprice = 102
ibmprice = 120
cmgprice = 458
koprice = 49
pepprice = 114

your_stocks = []

stocks_bought = 0

babastocks_bought = 0
amznstocks_bought = 0
hdstocks_bought = 0
intcstocks_bought = 0
sbuxstocks_bought = 0
aaplstocks_bought = 0
msftstocks_bought = 0
googstocks_bought = 0
wmtstocks_bought = 0
vstocks_bought = 0
nkestocks_bought = 0
tslastocks_bought = 0
eastocks_bought = 0
pyplstocks_bought = 0
nflxstocks_bought = 0
mcdstocks_bought = 0
rlstocks_bought = 0
ibmstocks_bought = 0
cmgstocks_bought = 0
kostocks_bought = 0
pepstocks_bought = 0

def main_menu(balance,week):
    msg = 'Balance: $'+ str(balance) + '\nWeek: ' + str(week) + '\n\nPlease choose an action...'
    title = 'Stock Market Simulator'
    choices = ['Exchange Stocks','My Stocks','Simulate','Quit Simulator']
    
    main = buttonbox(msg,title,choices = choices)
    return main

def stock_menu(balance,STOCKS):
    msg = 'Balance: $'+ str(balance) + '\n\nChoose a stock that you would like to view...'
    title = 'Stock Market Simulator'
    choices = STOCKS
    
    stockpick = buttonbox(msg,title,choices)

    if choices == 'BABA.gif':
        stockpick = 'BABA'

    elif choices == 'AMZN.gif':
        stockpick = 'AMZN'

    elif choices == 'HD.gif':
        stockpick = 'HD'

    elif choices == 'INTC.gif':
        stockpick = 'INTC'

    elif choices == 'SBUX.gif':
        stockpick = 'SBUX'

    elif choices == 'AAPL.gif':
        stockpick = 'AAPL'

    elif choices == 'MSFT.gif':
        stockpick = 'MSFT'
        
    elif choices == 'HD.gif':
        stockpick = 'HD'

    return stockpick

def xstock(balance,price,stocks_bought,stockname,your_stocks,babastocks_bought,amznstocks_bought,hdstocks_bought,intcstocks_bought,sbuxstocks_bought,aaplstocks_bought,msftstocks_bought,googstocks_bought,wmtstocks_bought,vstocks_bought,nkestocks_bought,tslastocks_bought,eastocks_bought,pyplstocks_bought,nflxstocks_bought,mcdstocks_bought,rlstocks_bought,ibmstocks_bought,cmgstocks_bought,kostocks_bought,pepstocks_bought):
    msg = 'Balance: $'+ str(balance) + '\nBuy or Sell ' + str(stockname) +' stocks.' + '\n\nCurrent Value: '+ str(price) + '\nChange from last Week: ' 
    title = 'Stock Market Simulator'
    choices = ['Buy','Sell','Cancel']

    option = buttonbox(msg,title,choices)
    if option == 'Buy':
        intmsg = 'Type the quantity you wish to buy'
        amount = integerbox(intmsg,lowerbound = 1, upperbound = balance//price)
        cost = price * amount
        stocks_bought = stocks_bought + amount
        msgnumber = 'Here is the cost of your purchase. \nTotal Cost: $' + str(cost) + '\nCurrent Balance: $' + str(balance) + '\nBalance after Purchase: $' + str(balance - cost) 
        choices = ['Confirm Transaction','Back']
        buychoices = buttonbox(msgnumber,title,choices)

        if buychoices == 'Confirm Transaction':
                balance = balance - cost

        if stockname == 'Alibaba':
            babastocks_bought = stocks_bought
            stocks_bought = 0

        elif stockname == 'Amazon':
            amznstocks_bought = stocks_bought
            stocks_bought = 0
            
        elif stockname == 'Home Depot':
            hdstocks_bought = stocks_bought
            stocks_bought = 0
            
        elif stockname == 'Intel':
            intcstocks_bought = stocks_bought
            stocks_bought = 0
            
        elif stockname == 'Starbucks':
            sbuxstocks_bought = stocks_bought
            stocks_bought = 0
            
        elif stockname == 'Apple':
            aaplstocks_bought = stocks_bought
            stocks_bought = 0
            
        elif stockname == 'Microsoft':
            msftstocks_bought = stocks_bought
            stocks_bought = 0
            
        elif stockname == 'Google':
            googstocks_bought = stocks_bought
            stocks_bought = 0
            
        elif stockname == 'Walmart':
            wmtstocks_bought = stocks_bought
            stocks_bought = 0
            
        elif stockname == 'Visa':
            vstocks_bought = stocks_bought
            stocks_bought = 0
            
        elif stockname == 'Nike':
            nkestocks_bought = stocks_bought
            stocks_bought = 0
            
        elif stockname == 'Tesla':
            tslastocks_bought = stocks_bought
            stocks_bought = 0
            
        elif stockname == 'Electronic Arts':
            eastocks_bought = stocks_bought
            stocks_bought = 0
            
        elif stockname == 'Paypal':
            pyplstocks_bought = stocks_bought
            stocks_bought = 0
            
        elif stockname == 'Netflix':
            nflxstocks_bought = stocks_bought
            stocks_bought = 0
            
        elif stockname == 'McDonalds':
            mcdstocks_bought = stocks_bought
            stocks_bought = 0
            
        elif stockname == 'Ralph Lauren':
            rlstocks_bought = stocks_bought
            stocks_bought = 0
            
        elif stockname == 'IBM':
            ibmstocks_bought = stocks_bought
            stocks_bought = 0
            
        elif stockname == 'Chipotle Mexican Grill':
            cmgstocks_bought = stocks_bought
            stocks_bought = 0
            
        elif stockname == 'Coca Cola':
            kostocks_bought = stocks_bought
            stocks_bought = 0
            
        elif stockname == 'Pepsi':
            pepstocks_bought = stocks_bought
            stocks_bought = 0 

    if option == 'Sell':

        if stockname == 'Alibaba':
            stocks_bought = babastocks_bought

        elif stockname == 'Amazon':
            stocks_bought = amznstocks_bought

        elif stockname == 'Home Depot':
            stocks_bought = hdstocks_bought
            
        elif stockname == 'Intel':
            stocks_bought = intcstocks_bought
            
        elif stockname == 'Starbucks':
            stocks_bought = sbuxstocks_bought
            
        elif stockname == 'Apple':
            stocks_bought = aaplstocks_bought
            
        elif stockname == 'Microsoft':
            stocks_bought = msftstocks_bought
            
        elif stockname == 'Google':
            stocks_bought = googstocks_bought
            
        elif stockname == 'Walmart':
            stocks_bought = wmtstocks_bought
            
        elif stockname == 'Visa':
            stocks_bought = vstocks_bought
            
        elif stockname == 'Nike':
            stocks_bought = nkestocks_bought
            
        elif stockname == 'Tesla':
            stocks_bought = tslastocks_bought
            
        elif stockname == 'Electronic Arts':
            stocks_bought = eastocks_bought
            
        elif stockname == 'Paypal':
            stocks_bought = pyplstocks_bought
            
        elif stockname == 'Netflix':
            stocks_bought = nflxstocks_bought
            
        elif stockname == 'McDonalds':
            stocks_bought = mcdstocks_bought
            
        elif stockname == 'Ralph Lauren':
            stocks_bought = rlstocks_bought
            
        elif stockname == 'IBM':
            stocks_bought = ibmstocks_bought
            
        elif stockname == 'Chipotle Mexican Grill':
            stocks_bought = cmgstocks_bought
            
        elif stockname == 'Coca Cola':
            stocks_bought = kostocks_bought
            
        elif stockname == 'Pepsi':
            stocks_bought = pepstocks_bought

        intmsg = 'Type the amount of stocks you wish to sell'
        amount = integerbox(intmsg,lowerbound = 1, upperbound = stocks_bought)
        moneyback = amount * price
        msgnumber = 'Here is the amount of money you will receive back: ' + str(moneyback) + '\nCurrent Balance: ' + str(balance) + '\nUpdated Balance: ' + str(balance + moneyback)
        choices = ['Confirm Transaction','Back']
        sellchoices = buttonbox(msgnumber,title,choices)
        cost = 0
        if sellchoices == 'Confirm Transaction':
            balance = balance + moneyback      
            stocks_bought = stocks_bought - amount

        if stockname == 'Alibaba':
            babastocks_bought = stocks_bought
            stocks_bought = 0

        elif stockname == 'Amazon':
            amznstocks_bought = stocks_bought
            stocks_bought = 0
            
        elif stockname == 'Home Depot':
            hdstocks_bought = stocks_bought
            stocks_bought = 0
            
        elif stockname == 'Intel':
            intcstocks_bought = stocks_bought
            stocks_bought = 0
            
        elif stockname == 'Starbucks':
            sbuxstocks_bought = stocks_bought
            stocks_bought = 0
            
        elif stockname == 'Apple':
            aaplstocks_bought = stocks_bought
            stocks_bought = 0
            
        elif stockname == 'Microsoft':
            msftstocks_bought = stocks_bought
            stocks_bought = 0
            
        elif stockname == 'Google':
            googstocks_bought = stocks_bought
            stocks_bought = 0
            
        elif stockname == 'Walmart':
            wmtstocks_bought = stocks_bought
            stocks_bought = 0
            
        elif stockname == 'Visa':
            vstocks_bought = stocks_bought
            stocks_bought = 0
            
        elif stockname == 'Nike':
            nkestocks_bought = stocks_bought
            stocks_bought = 0
            
        elif stockname == 'Tesla':
            tslastocks_bought = stocks_bought
            stocks_bought = 0
            
        elif stockname == 'Electronic Arts':
            eastocks_bought = stocks_bought
            stocks_bought = 0
            
        elif stockname == 'Paypal':
            pyplstocks_bought = stocks_bought
            stocks_bought = 0
            
        elif stockname == 'Netflix':
            nflxstocks_bought = stocks_bought
            stocks_bought = 0
            
        elif stockname == 'McDonalds':
            mcdstocks_bought = stocks_bought
            stocks_bought = 0
            
        elif stockname == 'Ralph Lauren':
            rlstocks_bought = stocks_bought
            stocks_bought = 0
            
        elif stockname == 'IBM':
            ibmstocks_bought = stocks_bought
            stocks_bought = 0
            
        elif stockname == 'Chipotle Mexican Grill':
            cmgstocks_bought = stocks_bought
            stocks_bought = 0
            
        elif stockname == 'Coca Cola':
            kostocks_bought = stocks_bought
            stocks_bought = 0
            
        elif stockname == 'Pepsi':
            pepstocks_bought = stocks_bought
            stocks_bought = 0 
    if stocks_bought > 0:
        your_stocks.append(stockname)

    return balance,stocks_bought,cost,your_stocks,babastocks_bought,amznstocks_bought,hdstocks_bought,intcstocks_bought,sbuxstocks_bought,aaplstocks_bought,msftstocks_bought,googstocks_bought,wmtstocks_bought,vstocks_bought,nkestocks_bought,tslastocks_bought,eastocks_bought,pyplstocks_bought,nflxstocks_bought,mcdstocks_bought,rlstocks_bought,ibmstocks_bought,cmgstocks_bought,kostocks_bought,pepstocks_bought

def your_stockpick(your_stocks):
    msgyourstock = 'These are your current stocks...'
    title = 'Stock Market Simulator'
    your_stockpick = choicebox(msgyourstock,title,choices = your_stocks,callback = None,run = True)
    return your_stockpick

def stock_info(stockpick,stocks_bought):
    if stockpick == 'BABA':
        stockname = 'Alibaba'
        price = babaprice
        if stocks_bought > 0:
            babastocks_bought = stocks_bought
    elif stockpick == 'AMZN':
        stockname = 'Amazon'
        price = amznprice
        if stocks_bought > 0:
            amznstocks_bought = stocks_bought
    elif stockpick == 'HD':
        stockname = 'Home Depot'
        price = hdprice
        if stocks_bought > 0:
            hdstocks_bought = stocks_bought
    elif stockpick == 'INTC':
        stockname = 'Intel'
        price = intcprice
        if stocks_bought > 0:
            intcstocks_bought = stocks_bought
    elif stockpick == 'SBUX':
        stockname = 'Starbucks'
        price = sbuxprice
        if stocks_bought > 0:
            sbuxstocks_bought = stocks_bought
    elif stockpick == 'AAPL':
        stockname = 'Apple'
        price = aaplprice
        if stocks_bought > 0:
            aaplstocks_bought = stocks_bought
    elif stockpick == 'MSFT':
        stockname = 'Microsoft'
        price = msftprice
        if stocks_bought > 0:
            msftstocks_bought = stocks_bought
    elif stockpick == 'GOOG':
        stockname = 'Google'
        price = googprice
        if stocks_bought > 0:
            googstocks_bought = stocks_bought
    elif stockpick == 'WMT':
        stockname = 'Walmart'
        price = wmtprice
        if stocks_bought > 0:
            wmtstocks_bought = stocks_bought
    elif stockpick == 'V':
        stockname = 'Visa'
        price = vprice
        if stocks_bought > 0:
            vstocks_bought = stocks_bought
    elif stockpick == 'NKE':
        stockname = 'Nike'
        price = nkeprice
        if stocks_bought > 0:
            nkestocks_bought = stocks_bought
    elif stockpick == 'TSLA':
        stockname = 'Tesla'
        price = tslaprice
        if stocks_bought > 0:
            tslastocks_bought = stocks_bought
    elif stockpick == 'EA':
        stockname = 'Electronic Arts'
        price = eaprice
        if stocks_bought > 0:
            eastocks_bought = stocks_bought
    elif stockpick == 'PYPL':
        stockname = 'Paypal'
        price = pyplprice
        if stocks_bought > 0:
            pyplstocks_bought = stocks_bought
    elif stockpick == 'NFLX':
        stockname = 'Netflix'
        price = nflxprice
        if stocks_bought > 0:
            nflxstocks_bought = stocks_bought
    elif stockpick == 'MCD':
        stockname = 'McDonalds'
        price = mcdprice
        if stocks_bought > 0:
            mcdstocks_bought = stocks_bought
    elif stockpick == 'RL':
        stockname = 'Ralph Lauren'
        price = rlprice
        if stocks_bought > 0:
            rlstocks_bought = stocks_bought
    elif stockpick == 'IBM':
        stockname = 'IBM'
        price = ibmprice
        if stocks_bought > 0:
            ibmstocks_bought = stocks_bought
    elif stockpick == 'CMG':
        stockname = 'Chipotle Mexican Grill'
        price = cmgprice
        if stocks_bought > 0:
            cmgstocks_bought = stocks_bought
    elif stockpick == 'KO':
        stockname = 'Coca Cola'
        price = koprice
        if stocks_bought > 0:
            kostocks_bought = stocks_bought
    elif stockpick == 'PEP':
        stockname = 'Pepsi'
        price = pepprice
        if stocks_bought > 0:
            pepstocks_bought = stocks_bought

    return stockname, price, stocks_bought

#############################STOCK FLUCTUATIONS###############################

def babasim(baba):
    flux = random.randint(3,9)
    if baba >= 50:
        change = random.randint(1,2)
        if change == 1:
            baba = baba + flux
            flux = flux * 1
        elif change == 2:
            baba = baba - flux
            flux = flux * -1
    else:
        baba = baba + flux
        flux = flux * 1 

    if flux > 0:
        flux = '+' + str(flux)
    elif flux < 0:
        flux = str(flux)
    elif flux == 0:
        flux = 'no change'
    
    return baba,flux

def amznsim(amzn):
    flux = random.randint(50,105)
    if amzn >= 1000:
        change = random.randint(1,3)
        if change == 1:
            amzn = amzn + flux
            flux = flux * 1
        elif change == 2:
            amzn = amzn - flux
            flux = flux * -1
    else:
        amzn = amzn + flux

    if flux > 0:
        flux = '+' + str(flux)
    elif flux < 0:
        flux = str(flux)
    elif flux == 0:
        flux = 'no change'

    return amzn,flux

def hdsim(hd):
    flux = random.randint(2,8)
    if hd >= 100:
        change = random.randint(1,2)
        if change == 1:
            hd = hd + flux
        elif change == 2:
            hd = hd - flux
    else:
        hd = hd + flux

    if flux > 0:
        flux = '+' + str(flux)
    elif flux < 0:
        flux = str(flux)
    elif flux == 0:
        flux = 'no change'
        
    return hd,flux

def intcsim(intc):
    flux = random.randint(1,4)
    if intc >= 20:
        change = random.randint(1,2)
        if change == 1:
            intc = intc + flux
        elif change == 2:
            intc = intc - flux
    else:
        intc = intc + flux

    if flux > 0:
        flux = '+' + str(flux)
    elif flux < 0:
        flux = str(flux)
    elif flux == 0:
        flux = 'no change'
        
    return intc,flux

def sbuxsim(sbux):
    flux = random.randint(0,3)
    if sbux >= 25:
        change = random.randint(1,2)
        if change == 1:
            sbux = sbux + flux
        elif change == 2:
            sbux = sbux - flux
    else:
        sbux = sbux + flux

    if flux > 0:
        flux = '+' + str(flux)
    elif flux < 0:
        flux = str(flux)
    elif flux == 0:
        flux = 'no change'
        
    return sbux,flux

def aaplsim(aapl):
    flux = random.randint(2,8)
    if aapl >= 100:
        change = random.randint(1,2)
        if change == 1:
            aapl = aapl + flux
        elif change == 2:
            aapl = aapl - flux
    else:
        aapl = aapl + flux

    if flux > 0:
        flux = '+' + str(flux)
    elif flux < 0:
        flux = str(flux)
    elif flux == 0:
        flux = 'no change'
    
    return aapl,flux

def msftsim(msft):
    flux = random.randint(2,8)
    if msft >= 50:
        change = random.randint(1,2)
        if change == 1:
            msft = msft + flux
        elif change == 2:
            msft = msft - flux
    else:
        msft = msft + flux
    
    return msft

def googsim(goog):
    flux = random.randint(10,50)
    if goog >= 700:
        change = random.randint(1,2)
        if change == 1:
            goog = goog + flux
        elif change == 2:
            goog = goog - flux
    else:
        goog = goog + flux
    
    return goog

def wmtsim(wmt):
    flux = random.randint(0,4)
    if wmt >= 50:
        change = random.randint(1,2)
        if change == 1:
            wmt = wmt + flux
        elif change == 2:
            wmt = wmt - flux
    else:
        wmt = wmt + flux
    
    return wmt

def vsim(v):
    flux = random.randint(0,7)
    if v >= 90:
        change = random.randint(1,2)
        if change == 1:
            v = v + flux
        elif change == 2:
            v = v - flux
    else:
        v = v + flux
    
    return v

def nkesim(x):
    flux = random.randint(1,5)
    if x >= 40:
        change = random.randint(1,2)
        if change == 1:
            x = x + flux
        elif change == 2:
            x = x - flux
    else:
        x = x + flux
    
    return x

def tslasim(x):
    flux = random.randint(5,21)
    if x >= 250:
        change = random.randint(1,2)
        if change == 1:
            x = x + flux
        elif change == 2:
            x = x - flux
    else:
        x = x + flux
    
    return x

def easim(x):
    flux = random.randint(1,6)
    if x >= 40:
        change = random.randint(1,2)
        if change == 1:
            x = x + flux
        elif change == 2:
            x = x - flux
    else:
        x = x + flux
    
    return x

def pyplsim(x):
    flux = random.randint(1,6)
    if x >= 40:
        change = random.randint(1,2)
        if change == 1:
            x = x + flux
        elif change == 2:
            x = x - flux
    else:
        x = x + flux
    
    return x

def nflxsim(x):
    flux = random.randint(5,17)
    if x >= 150:
        change = random.randint(1,2)
        if change == 1:
            x = x + flux
        elif change == 2:
            x = x - flux
    else:
        x = x + flux
    
    return x

def mcdsim(x):
    flux = random.randint(1,7)
    if x >= 90:
        change = random.randint(1,2)
        if change == 1:
            x = x + flux
        elif change == 2:
            x = x - flux
    else:
        x = x + flux
    
    return x

def rlsim(x):
    flux = random.randint(4,10)
    if x >= 40:
        change = random.randint(1,2)
        if change == 1:
            x = x + flux
        elif change == 2:
            x = x - flux
    else:
        x = x + flux
    
    return x

def ibmsim(x):
    flux = random.randint(2,7)
    if x >= 50:
        change = random.randint(1,2)
        if change == 1:
            x = x + flux
        elif change == 2:
            x = x - flux
    else:
        x = x + flux
    
    return x

def cmgsim(x):
    flux = random.randint(10,24)
    if x >= 300:
        change = random.randint(1,2)
        if change == 1:
            x = x + flux
        elif change == 2:
            x = x - flux
    else:
        x = x + flux
    
    return x

def kosim(x):
    flux = random.randint(0,3)
    if x >= 15:
        change = random.randint(1,2)
        if change == 1:
            x = x + flux
        elif change == 2:
            x = x - flux
    else:
        x = x + flux
    
    return x

def pepsim(x):
    flux = random.randint(1,6)
    if x >= 50:
        change = random.randint(1,2)
        if change == 1:
            x = x + flux
        elif change == 2:
            x = x - flux
    else:
        x = x + flux
    
    return x

def changes(baba,amzn,hd,intc,sbux,aapl):
    msg = 'Stock Updates\n\nBABA: ' + baba +'\nAMZN: '+ amzn + '\nHD: ' + hd + '\nINTC: ' + intc + '\nSBUX: ' + sbux + '\nAAPL: ' + aapl
    msgbox(msg = msg,title = 'Stock Market Simulator')
    



menu_choice = main_menu(balance,week)

while menu_choice != 'Quit Simulator':

    if menu_choice == 'Exchange Stocks':
        stockpick = stock_menu(balance,STOCKS)
        stockname,price,stocks_bought = stock_info(stockpick,stocks_bought)
        balance,stocks_bought,cost,your_stocks,babastocks_bought,amznstocks_bought,hdstocks_bought,intcstocks_bought,sbuxstocks_bought,aaplstocks_bought,msftstocks_bought,googstocks_bought,wmtstocks_bought,vstocks_bought,nkestocks_bought,tslastocks_bought,eastocks_bought,pyplstocks_bought,nflxstocks_bought,mcdstocks_bought,rlstocks_bought,ibmstocks_bought,cmgstocks_bought,kostocks_bought,pepstocks_bought = xstock(balance,price,stocks_bought,stockname,your_stocks,babastocks_bought,amznstocks_bought,hdstocks_bought,intcstocks_bought,sbuxstocks_bought,aaplstocks_bought,msftstocks_bought,googstocks_bought,wmtstocks_bought,vstocks_bought,nkestocks_bought,tslastocks_bought,eastocks_bought,pyplstocks_bought,nflxstocks_bought,mcdstocks_bought,rlstocks_bought,ibmstocks_bought,cmgstocks_bought,kostocks_bought,pepstocks_bought)
        stock_info(stockpick,stocks_bought)

    elif menu_choice == 'My Stocks':
        stockpick = your_stockpick(your_stocks)

    elif menu_choice == 'Simulate':
        week = week + 1
        babaprice,babaflux = babasim(babaprice)
        amznprice,amznflux = amznsim(amznprice)
        hdprice,hdflux = hdsim(hdprice)
        intcprice,intcflux = intcsim(intcprice)
        sbuxprice,sbuxflux = sbuxsim(sbuxprice)
        aaplprice,aaplflux = aaplsim(aaplprice)
        msftprice = msftsim(msftprice)
        googprice = googsim(googprice)
        wmtprice = wmtsim(wmtprice)
        vprice = vsim(vprice)
        nkeprice = nkesim(nkeprice)
        tslaprice = tslasim(tslaprice)
        eaprice = easim(eaprice)
        pyplprice = pyplsim(pyplprice)
        nflxprice = nflxsim(nflxprice)
        mcdprice = mcdsim(mcdprice)
        rlprice = rlsim(rlprice)
        ibmprice = ibmsim(ibmprice)
        cmgprice = cmgsim(cmgprice)
        koprice = kosim(koprice)
        pepprice = pepsim(pepprice)

        changes(babaflux,amznflux,hdflux,intcflux,sbuxflux,aaplflux)


                
    menu_choice = main_menu(balance,week)





 









