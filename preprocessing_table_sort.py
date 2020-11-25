import pandas as pd
df = pd.read_excel('2018_20.xlsx', sheet_name='20162020')
#df = pd.read_excel('test.xlsx', sheet_name='Sheet1')

result = [['연도', '구', '영업 기간']]
count = 0
print(len(df.columns))
print(len(df[df.columns[0]]))
for i in range(1, len(df.columns)):
    for j in range(len(df[df.columns[0]])):
        count += 1
        print(count, end='\r')
        result.append([df.columns[i], df[df.columns[0]][j], df[df.columns[i]][j]])

#f = open('result.csv', 'w', encoding="utf-8")
#for i in range(len(result)):
#    for j in range(3):
#        f.write(str(result[i][j]))
#        f.write(',')
#    f.write('\n')
#f.close()

result_df = pd.DataFrame(result)
result_df.to_csv('result.csv', index=False, header=False)