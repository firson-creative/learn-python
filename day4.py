import time
import sys

def lirikna():
    lirik = [
        "我一贯的小心翼翼", 
        "现在却想要告诉你",
        "好喜欢你",
        "像春天的花朵盛开在夏夜里", 
        "像微风吹过雨后泥土的香气",
        "像迷途的旅人到达了目的地",
        "像飞舞蝴蝶被绚烂色彩吸引"
    ]

    d = [2, 2, 2, 1, 1]

    print("Lagu buat ta cinta \n")
    time.sleep(0.3)

    for i, line in enumerate(lirik):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.6)
        print()
        time.sleep(d[i])

if __name__ == '__main__':
    lirikna()