# 题目：
#
# 你现有管理一个停车场
# 现有一组车位租用情况，结构如下：
#     car_nums = ['A0001','A00X9','A0027']
# 现有新来了一辆车 'A0030', 请把它放在 car_nums 的最后面
# 现有新来了一辆车 'A0000', 请把它放在 car_nums 的最前面
# 'A00X9' 这辆车现在不租你的停车位上，请把它从 car_nums 中删掉
# 现在来了一个车队 ['B0001','B0002','B003'], 请用一行代码把它加到 car_nums 中
if __name__ == '__main__':
    car_nums = ['A0001', 'A00X9', 'A0027']
    car_nums.insert(3, 'A0030')
    print(car_nums)
    car_nums.insert(0, 'A0000')
    print(car_nums)
    del car_nums[1]
    print(car_nums)
    car_nums1 = ['B0001','B0002','B003']
    car_nums2 = car_nums + car_nums1
    print(car_nums2)
