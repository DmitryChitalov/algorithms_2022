def summator(n, value=1, done=1):
    value *= -0.5
    done += value
    print(n, value, done)
    if n == 2:
        return done
    return summator(n - 1, value, done)


print(summator(4))
