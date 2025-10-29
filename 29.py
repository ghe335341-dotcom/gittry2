s1={10,20,30,40,50} #没有顺序
s2={10,20,30,40,10,20,30} #省略超过1次出现的数据(去重)
print(s1,s2,type(s1)) #类型集合set
s3=set() #空集创建（不能{}（字典））
s4=set('abcdefg')
print(s3,s4)
s1.add(100)
print(s1,end=' ')
s1.add(20) #已有数据，什么都不发生
print(s1)
s1.update([40,50,60,70])
print(s1)
s1.remove(10) #没有就报错
s1.discard(20) #没有不报错
a=s1.pop() #随机删除（我质疑） 并返回值
print(a,s1)