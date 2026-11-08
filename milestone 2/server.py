"""Legacy Bank mainframe (Server): receives DES-ECB ciphertext, decrypts, prints."""
import socket, struct
from des import ecb_decrypt

KEY = bytes.fromhex("133457799BBCDFF1")   # static hard-coded 64-bit key (Milestone 2 requirement)
HOST, PORT = "127.0.0.1", 5000

def recv_exact(conn, n):
    buf = b""
    while len(buf) < n:
        chunk = conn.recv(n - len(buf))
        if not chunk:
            raise ConnectionError("connection closed early")
        buf += chunk
    return buf

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as srv:
        srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        srv.bind((HOST, PORT))
        srv.listen(1)
        print(f"[SERVER] Listening on {HOST}:{PORT}")
        conn, addr = srv.accept()
        with conn:
            print(f"[SERVER] Connection from {addr}")
            (length,) = struct.unpack("!I", recv_exact(conn, 4))   # 4-byte length prefix
            ct = recv_exact(conn, length)
            print(f"[SERVER] Ciphertext received ({length} bytes): {ct.hex().upper()}")
            pt = ecb_decrypt(ct, KEY)
            print(f"[SERVER] Decrypted transaction: {pt.decode('utf-8')}")

if __name__ == "__main__":
    main()
