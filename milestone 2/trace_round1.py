"""Appendix A: prints every intermediate value of DES round 1."""
from des import *
def g(s, n, sep=' '): return sep.join(s[i:i+n] for i in range(0, len(s), n))
key = bytes.fromhex("133457799BBCDFF1"); pt = bytes.fromhex("0123456789ABCDEF")
print("KEY ", g(bits(key),8)); print("PT  ", g(bits(pt),8))
k = permute(bits(key), PC1); c0, d0 = k[:28], k[28:]
print("PC1 ", g(k,7)); print("C0  ", g(c0,7)); print("D0  ", g(d0,7))
c1, d1 = lrot(c0,1), lrot(d0,1); print("C1  ", g(c1,7)); print("D1  ", g(d1,7))
k1 = permute(c1+d1, PC2); print("K1  ", g(k1,6), "=", hex(int(k1,2))); assert k1 == subkeys(key)[0]
s = permute(bits(pt), IP); l0, r0 = s[:32], s[32:]
print("IP  ", g(s,8)); print("L0  ", g(l0,8), hex(int(l0,2))); print("R0  ", g(r0,8), hex(int(r0,2)))
er = permute(r0, E); print("E(R0)", g(er,6))
x = xor(er, k1); print("XOR K1", g(x,6))
out = ''
for i in range(8):
    six = x[6*i:6*i+6]; row, col, v = sbox_lookup(six, i)
    print(f"S{i+1}: in={six} row=({six[0]}{six[5]})={row} col=({six[1:5]})={col} -> {v} = {v:04b}")
    out += f'{v:04b}'
print("S out", g(out,4)); pp = permute(out, P); print("P   ", g(pp,4), hex(int(pp,2)))
r1 = xor(l0, pp); print("R1=L0^f", g(r1,8), hex(int(r1,2)))
print("L1=R0 ", g(r0,8)); 
print("Round1 out L1R1:", hex(int(r0+r1,2)))
