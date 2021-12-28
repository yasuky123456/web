#範囲変数作成
num = 256
for i in range(50):
    code = 'row{} = {}'.format(i, i * num) 
    exec(code)
x = row1 + 256 