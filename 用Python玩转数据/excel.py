import pandas as pd

df = pd.DataFrame()
df = pd.read_excel('excel.xlsx',sheet_name = 'scores')
df['sum'] = df['Python'] + df['Math']
df.to_excel('excel2.xlsx',sheet_name = 'scores')

#import pandas as pd
#stu_df = pd.DataFrame()
#stu_df = pd.read_excel('stu_scores.xlsx', sheet_name = 'scores')
#stu_df['sum'] = stu_df['Python'] + stu_df['Math']
#stu_df.to_excel('stu_scores.xlsx', sheet_name = 'scores')
