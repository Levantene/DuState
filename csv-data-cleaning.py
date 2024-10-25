import pandas as pd
import datetime
pd.options.mode.chained_assignment = None

df = pd.read_csv('C:/Users/tenielev/1_IT/3_Pet_Projects/3_dxbstates/data/Transactions.csv')

CONDITION_1 = df['property_usage_en'] == 'Residential'
CONDITION_2 = (
    (df['rooms_en'] != 'Office') &
    (df['rooms_en'] != 'Shop') &
    (df['rooms_en'] != 'Single Room') &
    (df['rooms_en'].notnull())
    )
CONDITION_3 = (
    df['project_name_en'].notnull()
)
CONDITION_4 = (
    df['master_project_en'].notnull()
)

# Clean Data
res_df = df[
    (CONDITION_1) &
    (CONDITION_2) &
    (CONDITION_3) &
    (CONDITION_4)]

res_df['instance_date'] = pd.to_datetime(res_df['instance_date'], format='%d-%m-%Y')

CONDITION_5 = (
    res_df['instance_date'].dt.date.astype(str) >= '2022-01-01'
)

res_df = res_df[CONDITION_5]
res_df['instance_date'] = res_df['instance_date'].dt.date.astype(str)

res_df.to_csv('C:/Users/tenielev/1_IT/3_Pet_Projects/3_dxbstates/data/transactions-clean.csv')