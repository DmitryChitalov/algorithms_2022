def left_piece(n, done=1, count=1):
    print(n, done)
    if (n * (n + 1)) / 2 == done:  # если они равны
        print("Done!")
        return n, done
    else:
        done += count
        return left_piece(n, done + 1, count + 1)


print(left_piece(6))
