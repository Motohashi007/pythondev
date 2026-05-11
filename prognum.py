def fibo(input_num):

    if input_num > 2:
        return fibo(input_num-1) + fibo(input_num-2)

    else:
        return 1
