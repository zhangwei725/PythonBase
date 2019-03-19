# 内置方法  三个
cities = ['北京', '上海', '武汉', '深圳']
# 第一种方法  pop
# cities.pop(index)
# 通过下标索引删除元素
# 返回删除的元素
# 注意 修改原来的列表
# city = cities.pop(1)
# print("删除的元素:{}".format(city))
# print(cities)


# 当索引不写时候 默认删除最后一个元素

city = cities.pop()
print(city)
print(cities)
# 通过索引删除元素,索引的大小一定不要超过长度-1
# cities.pop(100)
print(cities)






# 第二种方式  通过元素的值去删除

"""
语法 列表.remove(obj)

"""
cities = ['北京', '上海', '武汉', '深圳']

# cities.remove('北京')
# print(cities)
#
# cities.remove('杭州')
