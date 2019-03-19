# . 模拟超市付款： 商品单价   商品数量
#    	键盘上输入商品单价，以及商品数量，
#    	   然后计算应付总额
#    	   计算总额  float
#    	提示用户可以有4种付款方式
#    	   不同的付款方式有不同的折扣: 先展示四种付款方式
#    	   	现金没有折扣
#          		微信 0.95折
#    	   	支付宝 鼓励金付款金额的10%   鼓励金可以直接折算到付款金额中
#    	   	刷卡 满100-20

price = float(input('请输入商品的单价:\n'))
count = int(input('请输入商品的数量'))
# 总价
sum_price = price * count
pay_method = int(input('请选择支付方式'))
if pay_method == 1:
    print('现金支付 没有优惠 {}'.format(sum_price))
elif pay_method == 2:
    print('现金支付 没有优惠 {}'.format(sum_price * 0.95))
elif pay_method == 3:
    print('现金支付 没有优惠 {}'.format(sum_price * 0.9))
elif pay_method == 3:
    print('现金支付 没有优惠 {}'.format(sum_price - sum_price//100 * 20))
