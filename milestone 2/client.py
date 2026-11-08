"""Legacy Bank mobile app (Client): encrypts a transaction with DES-ECB and sends it."""
import socket, struct
from des import ecb_encrypt

KEY = bytes.fromhex("133457799BBCDFF1")   # must match the server's static key
HOST, PORT = "127.0.0.1", 5000
MESSAGE = "TXN#1001 | FROM:ACC-4821 | TO:ACC-9937 | AMOUNT:$2,500.00"

def main():
    ct = ecb_encrypt(MESSAGE.encode("utf-8"), KEY)
    print(f"[CLIENT] Plaintext : {MESSAGE}")
    print(f"[CLIENT] Ciphertext: {ct.hex().upper()}")
    with socket.create_connection((HOST, PORT)) as s:
        s.sendall(struct.pack("!I", len(ct)) + ct)
    print("[CLIENT] Encrypted transaction sent.")

if __name__ == "__main__":
    main()
