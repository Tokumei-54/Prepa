import serial.tools.list_ports
def serial_innit():
    ports = serial.tools.list_ports.comports()
    serialInst = serial.Serial()
    portsList = []
    for i,p in enumerate(ports):
        portsList.append(str(p).split()[0])
        print(f"{i} - {p}")
    serialInst.baudrate = 9600
    serialInst.port = portsList[int(input("Select port n° : "))]
    serialInst.open()
    return serialInst


def main():
    ser = serial_innit()

if __name__ == "__main__":
    main()