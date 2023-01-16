import pandas as pd
import numpy as np
import os
company_a="alabaster_20160101_tradelist.csv"
#Uses BB_ID
company_b="bernstein_TradeInputList_160101.csv"
#Uses GenericTicker
company_c="trades_comwealth_jan2016.csv"
#Uses RIC$Code
mapping="MappingTable.csv"

def mapping_security(df,df_mapping,identifier):
    df.Date = "2016-01-01"
    ####!!! Need to convert time properly
    mapping=df_mapping.set_index(df_mapping[identifier]).Security
    df['Security'] = df[identifier].map(mapping)
    df=df.set_index(["Security","Date"])
    return df

data_a=pd.read_csv(company_a)
data_b=pd.read_csv(company_b)
data_c=pd.read_csv(company_c)
data_mapping=pd.read_csv(mapping)

df_a=pd.DataFrame(data_a)
df_a=df_a.rename(columns={"Date":"Date","PriceUSD":"Price_alabaster","Qty":"Quantity_alabaster","Beta":"Beta_alabaster"})
df_a=df_a.drop(columns=['PriceEUR', 'MktAdjFactor','AllocationID',"OrderQty","FilledQty","FinancingSpread"])
'''

column_name_list=[[date,price,quan,beta],[date2,price2,quan2,beta],...]
change_list[[0,0,0,1]]
coulum_name_dict={"CompanyA":dict{'date":"Date","price:"price_a...}}
change_dict={"CompanyA":dict{'date':reformate,price:100}}
def rename(df,list)
    df=df.rename(columns={"list[0]":"Date","list[1]":"Price_alabaster","list[2]":"Quantity_alabaster","list[3]":"Beta_alabaster"})

for i in range number of traders:
    rename 

'''
df_b=pd.DataFrame(data_b)
df_b=df_b.rename(columns={"Date":"Date","Price":"Price_bernstein","Quantity":"Quantity_bernstein","Beta":"Beta_bernstein"})
df_b=df_b.drop(columns=["MTMValue","Currency","Financing","SubAccount"])

df_c=pd.DataFrame(data_c)
df_c=df_c.rename(columns={"Trade$Date":"Date","Executed$Price":"Price_comwealth","Executed$Quantity":"Quantity_comwealth","Beta$Hundreds":"Beta_comwealth"})
df_c["Beta_comwealth"]=df_c["Beta_comwealth"]/100

df_mapping=pd.DataFrame(data_mapping)
df_mapping=df_mapping.rename(columns={"GENERIC":"GenericTicker","RIC":"RIC$Code"})


df_a = mapping_security(df_a,df_mapping,"BB_ID")
df_b = mapping_security(df_b,df_mapping,"GenericTicker")
df_c = mapping_security(df_c,df_mapping,"RIC$Code")
df = pd.concat([df_a,df_b,df_c], axis=1)

df = df.drop(columns=['BB_ID','GenericTicker','RIC$Code'])

df = df.drop(index=np.NaN)

df = df[[
    "Price_alabaster", "Price_bernstein", "Price_comwealth",
    "Quantity_alabaster","Quantity_bernstein","Quantity_comwealth",
    "Beta_alabaster","Beta_bernstein","Beta_comwealth"]]

df["No.Non_Nan_Price"] = df[["Price_alabaster", "Price_bernstein", "Price_comwealth"]].count(axis=1)
df["AveragePrice"] = df[["Price_alabaster", "Price_bernstein", "Price_comwealth"]].sum(axis=1,min_count=1)/df["No.Non_Nan_Price"]
df["AveragePrice"] = df.AveragePrice.apply(lambda x: float("{:.2f}".format(x)))
'''
for row in df(iterrate by row):
    [a,b,c]=[row.Price_a,row.Price_b,row_Price_c]
    remove NaN values in the list
    check the rest of the values if they are duplicates:
        - if no of same value as list[0] == len(list)


'''

df["TotalQuantity"] = df[["Quantity_alabaster","Quantity_bernstein","Quantity_comwealth"]].sum(axis=1,min_count=1)
df["MaxBeta"] = df[["Beta_alabaster","Beta_bernstein","Beta_comwealth"]].max(axis=1)

df_trading=df[["AveragePrice","TotalQuantity","MaxBeta"]]
df_operation=df[[
    "Price_alabaster", "Price_bernstein", "Price_comwealth",
    "Quantity_alabaster","Quantity_bernstein","Quantity_comwealth",
    "Beta_alabaster","Beta_bernstein","Beta_comwealth"]]

###!!!Remove when all non_NaN values are the same

os.makedirs('output-trading',exist_ok=True)
os.makedirs('output-operation',exist_ok=True)
    
df_trading.to_csv("output-trading/output.csv",sep='\t')
df_operation.to_csv("output-operation/output.csv",sep="\t")