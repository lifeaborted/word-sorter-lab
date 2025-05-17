import socket

HOST = '127.0.0.1'
PORT = 12345

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            text = input("Введите текст (или пустую строку для выхода): ")
            if not text:
                break
            s.sendall(text.encode())
            data = s.recv(4096).decode()
            print("\nСлова в алфавитном порядке:\n" + data)

if __name__ == "__main__":
    main()
