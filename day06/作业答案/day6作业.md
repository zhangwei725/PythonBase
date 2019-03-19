第一部分

课堂代码敲一遍

第二部分 

1. 定义一个函数，通过参数，接收三角形边长，打印三角形

```
*
**
***
****
*****
******
*******
********
```

```
def print_triangle(n):
	for i in range(1,n+1):
		for j in range(1,i+1):
        	print('*' ,end='')
        print()	
```



2. 定义一个函数，通过参数，接收3个边长，求三角形的面积

   ```python
   def get_area(x, y, z):
   	if x + y > z and x + z > y and y + z > x:
   		p = (x + y +z) /2
   		s = (p *  (p -x) * (p - y) * (p - z)) ** 0.5
   		return s
       else:
           return 0
   
       
   def   get_area(x,y,z):
       s = ((x + y +z) / 2 * ((x + y +z) / 2-x) * ((x + y +z) / 2 - y) * ((x + y +z) / 2 - z)) ** 0.5 if x + y > z and x + z > y and y + z > x else 0
       return s
       
   ```

3. 定义一个函数，求一个数的绝对值

   ```python
   def abs1(x): 
      x =  x if x > 0 else -x
      retrun x
   ```

4. 定义一个函数，求1-n的范围内，偶数的和

   ```python
   def  sum(n):
       count = 0
   	for i in range(1,n+1):
   		count = count+i if i % 2 ==0 else count
       return  count   
   ```

5. 定义一个函数，返回两个数中的最大值

   ```
   def get_max(a, b):
       max_num = a if a >= b else b
       retrun max_num
   ```

6. 求3个数的总和，

   ```
   def get_sum(*args):
       sum = 0
       for i in args:
           sum += i
       return sum
   
   
   value = get_sum(2, 6, 9)
   print(value)
   ```

7. 求3个数的平均值

   ```
   def get_average(*args):
       average = 0
       count = 0
       for i in args:
           count += 1
           average += i
       average /= count
       return average
   
   
   value = get_average(8, 6, 4)
   print(value)
   ```



