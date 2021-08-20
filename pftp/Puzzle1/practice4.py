plain = 'BWWWWWBWWWW'
# ans = 1B5W1B4W

def encode(plain):
    encryption = ''
    start = 0
    plain += '0' # 最後の要素を暗号化するために必要
    for i in range(1, len(plain)):
        if (plain[start] != plain[i]):
            encryption += str(i - start) + plain[start]
            start = i
    return encryption

def decode(encryption):
    plain = ''
    for i in range(0,len(encryption),2):
        plain += (int(encryption[i]) * encryption[i+1])
    return plain

# 暗号化
encryption = encode(plain)
print(encryption)

# 復元
plain = decode(encryption)
print(plain)