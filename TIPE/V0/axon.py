import serial
import serial.tools.list_ports
import threading
import time
from typing import Tuple

def serial_innit(baud: int = 9600) -> serial.Serial:
    """
    Initializes the serial connection by selecting a port from available ports, opening and returning it.

    Parameters
    ----------
    baud : int, optional
        The baud rate for the serial connection, by default 9600.

    Returns
    -------
    serial.Serial
        The initialized and opened serial connection.

    Raises
    ------
    Exception
        If no serial ports are available or if the user fails to select a valid port.
    """
    ports = serial.tools.list_ports.comports()
    portsList = []
    for i, p in enumerate(ports):
        portsList.append(str(p).split()[0])
        print(f"{i} - {p}")
    if not portsList:
        raise Exception("No ports available")
    
    serialInst = serial.Serial()
    serialInst.baudrate = baud
    serialInst.port = portsList[int(input("Select port n° : "))]
    serialInst.open()
    return serialInst


def test_serial(baud: int = 9600) -> Tuple[serial.Serial, int]:
    """
    Sets up a pseudoterminal-based serial connection for testing purposes.

    This function creates a pseudoterminal pair using the 'openpty' function from the pty module and initializes
    a serial connection on the slave device with the specified baud rate. It opens and returns the serial connection along with
    the master file descriptor of the pseudoterminal, which can be used to simulate serial communication during tests.

    Parameters
    ----------
    baud : int, optional
        The baud rate for the serial connection, by default 9600.

    Returns
    -------
    tuple
        A tuple containing:
            - serial.Serial: The initialized and opened serial connection using the pseudoterminal.
            - int: The master file descriptor of the pseudoterminal.
    """
    from os import ttyname
    from pty import openpty

    master, slave = openpty()  # open the pseudoterminal
    serialInst = serial.Serial()
    serialInst.baudrate = baud
    serialInst.port = ttyname(slave)  # set port to the pseudoterminal slave device
    serialInst.open()
    return serialInst, master



def serial_read(serialInst: serial.Serial, timeout: float = 0.1) -> str | None:
    """
    Reads a line of data from the serial port.

    Parameters
    ----------
    serialInst : serial.Serial
        The serial connection to read data from.
    timeout : float, optional
        The timeout in seconds for the blocking read, by default 0.01.

    Returns
    -------
    str | None
        The decoded string received from the serial port, or None if no data is received
        within the timeout or an error occurs.
    """
    try:
        serialInst.timeout = timeout  # Set timeout for blocking read
        return serialInst.readline().decode('utf-8').strip()
    except Exception as e:
        print(f"Error reading from serial: {e}")
        return None


def serial_write(serialInst: serial.Serial, data: str) -> None:
    """
    Sends a string of data to the serial port.

    Parameters
    ----------
    serialInst : serial.Serial
        The serial connection to write data to.
    data : str
        The data to send to the serial port.
    """
    try:
        serialInst.write(data.encode('utf-8'))
    except Exception as e:
        print(f"Error writing to serial: {e}")


def serial_write_and_await(serialInst: serial.Serial, data: str, timeout: float = 10) -> str | None:
    """
    Sends a string of data to the serial port and waits for a response, returning the
    received data or None if the response is not received within the timeout.

    Parameters
    ----------
    serialInst : serial.Serial
        The serial connection to write and await a response from.
    data : str
        The data to send to the serial port.
    timeout : float, optional
        The timeout in seconds for waiting for a response, by default 1.0.

    Returns
    -------
    str | None
        The decoded string response from the serial port, or None if no response is received
        within the timeout.
    """
    try:
        serialInst.write(data.encode('utf-8'))
        start_time = time.time()
        while time.time() - start_time < timeout:
            incoming_data = serial_read(serialInst)
            if incoming_data:
                return incoming_data
        print(f"No response received within {timeout} seconds")
        return None  # Return None if no response within the timeout
    except Exception as e:
        print(f"Error in write and wait: {e}")
        return None


def serial_monitor(serialInst: serial.Serial) -> None:
    """
    Starts a basic serial monitor that continuously reads from the serial port and allows the user
    to send input to the serial port. The program runs indefinitely until the user enters 'exit'.

    Parameters
    ----------
    serialInst : serial.Serial
        The serial connection to monitor and interact with.
    """
    exit_flag = False

    def serial_read_thread(serialInst: serial.Serial):
        while not exit_flag:
            incoming_data = serial_read(serialInst)
            if incoming_data:
                print(f"\r| {incoming_data}", end="\n> ", flush=True)

    def user_input_thread(serialInst: serial.Serial):
        nonlocal exit_flag
        while not exit_flag:
            user_input = input("> ")
            if user_input.lower() == 'exit':
                print("\nExiting serial monitor...")
                exit_flag = True
            serialInst.write(user_input.encode('utf-8'))

    serial_thread = threading.Thread(target=serial_read_thread, args=(serialInst,))
    user_thread = threading.Thread(target=user_input_thread, args=(serialInst,))

    serial_thread.start()
    user_thread.start()

    serial_thread.join()
    user_thread.join()


def main():
    ser = serial_innit()
    serial_monitor(ser)


if __name__ == "__main__":
    main()

"""
Comands for attaching to WSL2
-----------------------------
usbipd list
usbipd bind --busid 1-2
usbipd attach --wsl --busid 1-2
lsusb
usbipd detach --busid 1-2
wsl --shutdown
"""

