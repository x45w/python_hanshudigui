# 定义一个函数 sum_numbers
# 能够接收一个 num 的整数参数
# 计算 1+2+3...num

def sum_numbers(num):

    # 1.出口
    if num == 1:
        return 1
    # 2.数字的累加 num + (1...num-1)
    # 假设 sum_numbers能够正确处理 1...num-1
    temp = sum_numbers(num -1)

    # 两个数字的相加
    return num + temp


result = sum_numbers(100)
print(result)