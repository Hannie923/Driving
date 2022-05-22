driving = input('請問你有開過車嗎？')
if driving != '有' and driving != '沒有' :
	print ('只能輸入 有/沒有')
	exit ()
age = input ('請輸入你的年齡')
age = int (age)
if driving == '有' :
	if age >= 18 :
		print ('你可以開車囉！')
	else :
		print ('你是違法開車哦！')
if driving == '沒有' :
	if age >= 18 :
		print ('你已經可以考駕照了，為什麼不去考')
	else :
		print ('在等你滿18歲就可以考駕照囉！')	


		
