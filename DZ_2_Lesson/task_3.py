done_num = ''
def reverser(num):
    global done_num
    done_num = done_num + str(num % 10)
    now_num = num // 10
    if now_num == 0:
        return done_num
    return reverser(now_num)


print(reverser(19235))