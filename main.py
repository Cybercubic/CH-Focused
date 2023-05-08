import dataloadKuCoin as dataload
import funcs as funcs
import numpy as np
import pandas as pd

def Candle_Analysis (ticker):
    
    open_list, high_list, low_list, close_list = dataload.Load_HP(ticker)[0], dataload.Load_HP(ticker)[1], dataload.Load_HP(ticker)[2], dataload.Load_HP(ticker)[3]
    
    timeframe1 = 100
    short_list1 = close_list[(260-timeframe1):260]
    end_price, start_price, step = funcs.timeframe_slice(timeframe1)
    print(end_price, start_price, step)
    skeleton1 = funcs.skeleton_founder(short_list1, end_price, start_price, step)
    likelihood_dict1 = funcs.find_nature(skeleton1)[2]
    
    timeframe2 = 20
    short_list2 = close_list[(260-timeframe2):260]
    end_price, start_price, step = funcs.timeframe_slice(timeframe2)
    print(end_price, start_price, step)
    skeleton2 = funcs.skeleton_founder(short_list2, end_price, start_price, step)
    likelihood_dict2 = funcs.find_nature(skeleton2)[2]
    
    my_array = funcs.pl_preprocessing(open_list, high_list, low_list, close_list)
    
    print(my_array)
    
    isto_array = funcs.make_isto(my_array)
    
    emotion_array = funcs.final_isto(isto_array)
    
    #ALL OUTPUT
    
    print('\n\nShort List-1:', short_list1, '\n\nShort List-2:', short_list2)
    print('\n\nSkeleton-1:', skeleton1,'\n\nSkeleton-2:' , skeleton2)
    print('\n\nLikelihood Dict-1:', likelihood_dict1, '\n\nLikelihood Dict-2:', likelihood_dict2)
    
    minmax_list = funcs.minmax(short_list1)
    grained_list = funcs.graining_filter(minmax_list, 20)
    
    #funcs.plot_it(minmax_list)
    #funcs.plot_it(grained_list)
    
    df = funcs.prepare_candles(open_list, high_list, low_list, close_list)
    funcs.plot_candles(df)
    print(funcs.support_levels(close_list))
    
    print(emotion_array)

    funcs.plot_isto(emotion_array)
    
    k1, k2, k3, k = funcs.calculate_k(likelihood_dict1, likelihood_dict2, emotion_array)
    
    print('K1 =', k1)
    print('K2 =', k2)
    print('K3 =', k3)
    print('K =', k)

Candle_Analysis ('VET-USDT')  