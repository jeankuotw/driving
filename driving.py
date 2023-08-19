#程式:考駕照年齡判斷
driving = input('請問你開過車嗎?(有/沒有)')

#先判斷是是否有回答"有/沒有"
if driving != '有' and driving != '沒有': #如果:沒有回答"有",也沒有回答"沒有"
	print('你只能回答"有/沒有"') #印出警告字
	raise SystemExit #終止程式,不執行下方程式碼

age = input('請問你幾歲?')
age = int(age) #型別轉換

if driving == '有':
	if age >= 18:
		print('你無照駕駛!?請問什麼時候的事情')
	else:
		print('你未成年無照駕駛!!!')
elif driving == '沒有':
	if age >= 18:
		print('很好喔,要不要來嘗試看看考駕照呢')
	else :
		print('那再過幾年你就可以來考考看駕照了')

#此段else刪除,直接在第5行時,先判斷是否有回答"有/沒有"
#else:
#	print('你只能輸入"有/沒有"喔')
