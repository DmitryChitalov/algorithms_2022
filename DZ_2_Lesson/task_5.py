# 32 - 127
def decoder(qwe, q):
    if qwe == 127:
        return "\nEND"

    if q == 0:
        print("\n")
        q = 10
    print(f"{qwe} - " + chr(qwe), end=" ")

    return decoder(qwe + 1, q - 1)

print(decoder(32, 10))