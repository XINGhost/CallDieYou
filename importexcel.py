import pymysql
import pandas as pd
from sqlalchemy import create_engine

file = r'd:\Desktop\my1.xlsx'
df = pd.read_excel(file)

print(type(df))

engine = create_engine("mysql+pymysql://root:@localhost:3306/test?charset=utf8")
df.to_sql('testexcel1',con=engine,if_exists='replace',index=False)