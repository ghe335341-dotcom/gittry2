str1='hello'
str2='world'
list1=['aaa','bbb','ccc']
list2=[111,222,333]
tuple1=('ddd','eee','fff')
tuple2=(444,555,666)
dict1={'letter':'aaa','num':'111'}
dict2={'letter':'bbb','num':'222'}
print(str1+str2,list1+list2,tuple1+tuple2)
#+:  str直接并，list,tuple把元素加到后面,dict报错
print(str1*5,list1*3,tuple1*3)
#*:  复制，支持str/list/tuple
print('el' in str1,'aaa' not in str1,111 in list2, 'ddd' not in tuple1)
print('letter' in dict1.keys(),'bbb' not in dict2.values())