"""Appendix B: ECB reveals patterns - identical plaintext blocks -> identical ciphertext blocks."""
from des import ecb_encrypt, des_block
KEY = bytes.fromhex("133457799BBCDFF1")
pt = b"PAY $100" * 2 + b"PAY $999"      # 3 blocks of 8 bytes: A, A, B
ct = ecb_encrypt(pt, KEY)
print(f"Key       : {KEY.hex().upper()}")
print(f"Plaintext : {pt.decode()}")
for i in range(0, len(ct), 8):
    p = pt[i:i+8] if i < len(pt) else b"(PKCS5 pad 0808080808080808)"
    label = p.decode() if i < len(pt) else "<padding>"
    print(f"Block {i//8+1}: {label:10s} -> {ct[i:i+8].hex().upper()}")
print("Block 1 == Block 2 ?", ct[0:8] == ct[8:16])
print("Block 1 == Block 3 ?", ct[0:8] == ct[16:24])
