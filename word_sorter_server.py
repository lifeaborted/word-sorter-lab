import socket
import threading
from text_processor import TextProcessor

HOST = '127.0.0.1'
PORT = 12345

# Храним глобальный набор слов
all_words = set()
lock = threading.Lock()

def handle_client(conn, addr):
    global all_words
    print(f"Подключён клиент {addr}")
    while True:
        data = conn.recv(4096).decode()
        if not data:
            print(f"Клиент {addr} отключён.")
            break

        if data.strip().lower() == "#clear":
            with lock:
                all_words.clear()
            conn.sendall("Список слов очищен.".encode())
            continue

        new_words = TextProcessor.process(data)

        with lock:
            all_words.update(new_words)
            sorted_all_words = sorted(all_words)

        response = "\n".join(sorted_all_words)
        conn.sendall(response.encode())

    conn.close()

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen()
        print("Сервер сортировщика слов запущен...")

        while True:
            conn, addr = server.accept()
            threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()

if __name__ == "__main__":
    main()
