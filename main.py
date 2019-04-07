from modules import external

def start():
    print("Temperature (C): ", external.get_temp())
    print("Altitude (m): ", external.get_altitude())
    print("Pressure (kPa):", external.get_pressure())


if __name__ == "__main__":
    start()
