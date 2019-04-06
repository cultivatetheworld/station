from modules import external

def start():
    print("TEST")
    external.get_temp()
    external.get_hum()


if __name__ == "__main__":
    start()
