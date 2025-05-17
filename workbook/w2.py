# 题目：
#
# 你现在公司的销售经理，要对一些销售数据进行分析
#
# 公司有百亿条销售数据，抽出一些销售额信息让你练手
#
#   sales = [100,200,50,300,20,500,1000,10]
# 请对 sales 进行升序排序，并且打印出来
# 请对 sales 进行降序排序，并且打印出来
# 请用排序+切片的方式，找出 Top3 的销售额
# 请用排序+切片的方式，找出 最低的3个销售额

if __name__ == '__main__':
     sales = [100,200,50,300,20,500,1000,10]
     sales.sort()
     print(sales)
     sales.sort(reverse=True)
     print(sales)
     print(sales[0:3:])

     sales.sort()
     print(sales[0:3:])

