import os
import uuid

path=input('请输入文件路径（结尾加上/）：')

#获取该目录下所有文件，存入列表中
f = os.listdir(path)


n=0
for i in f:
	#设置旧文件名（路径+文件名）
	oldNmae = path + f[n]

	suffix = os.path.splitext(oldNmae)[-1]

	#设置新名
	uid = uuid.uuid1()
	newName = path +str(uid).split('-')[0] + suffix

	#用os的rename方法对文件改名
	os.rename(oldNmae,newName)
	print(oldNmae,'=========>',newName)

	n+=1	