import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("\nMasa Lalu - \033[31mZikkWangyy\033[0m", 0.10),
        ("\nBuang jauh masa lalu mu", 0.08),
        ("Dan juga lihat aku karna diriku masa depan mu\n", 0.08),
        ("Now hes gone", 0.07),
        ("U should move on", 0.06),
        ("Here with me", 0.06),
        ("You're not alone\n", 0.05),
        ("Break my heart", 0.05),
        ("But u can't", 0.05),
        ("Cause i'm strong\n", 0.05),
        ("K-K-K-Kau tak pernah katakan apa kurangnya ku untukmu", 0.07),
        ("Namun ku tak sebanding meskipun aku di samping mu", 0.07),
        ("Dan kau masih cinta yang lalu", 0.07),
        ("Dia pergi kau menunggu", 0.07),
        ("Baik kau pergi berhenti bebani diriku\n", 0.07),
        ("Lihatlah aku, ku menunggumu", 0.08),
        ("Namun kau slalu pikir masa lalu", 0.09),
        ("Lihatlah aku, ku menunggumu", 0.08),
        ("Namun kau slalu pikir masa lalu", 0.09)
    ]
    delays = [0.00, 3.00, 5.50, 9.50, 10.00, 11.00, 12.00, 13.00, 13.50, 14.00, 16.00, 20.00, 23.00, 26.00, 27.50, 31.00, 34.00, 38.00, 41.00]

    threads = []

    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()

				for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()