import serial
from time import sleep


class ValveControl:
    def __init__(self, tty_port="/dev/ttyUSB0", baudrate=9600):
        """
        Array with associated photographic information.

        ...

        Attributes
        ----------
        tty_port: string
        System adress 
        """
        self.ser = serial.Serial(port=tty_port, baudrate=baudrate, timeout=10,
                                 bytesize=serial.EIGHTBITS,
                                 stopbits=serial.STOPBITS_ONE,
                                 parity=serial.PARITY_NONE,
                                 xonxoff=False, rtscts=False)
        self.board_adresses = ['0F', '1F']

    def switch_on_off_valve(self, board_no=0, out_no=1, switch_on=True):
        """
        
        """
        if switch_on:
            command = '@' + self.board_adresses[board_no] + '+' + str(out_no)
        else:
            command = '@' + self.board_adresses[board_no] + '-' + str(out_no)
        print(command)
        self.ser.write(str(command).encode())
        sleep(0.2)
        return(self.ser.readline().decode('ascii'))

    def status(self, board_no):
        print('@' + self.board_adresses[board_no] + '??')
        self.ser.write(str('@' + self.board_adresses[board_no] +
                           '??').encode())
        sleep(0.2)
        return(self.ser.readline().decode('ascii'))


if __name__ == '__main__':
    v_control = ValveControl()
    print(v_control.switch_on_off_valve())
    sleep(0.5)
    print(v_control.switch_on_off_valve(0, 3, False))
    sleep(0.5)
    print(v_control.switch_on_off_valve(1, 3))
    sleep(0.5)
    print(v_control.switch_on_off_valve(1, 4))
    sleep(0.5)
    print(v_control.status(1))
    sleep(0.5)
    print(v_control.status(0))
    sleep(0.5)
    print(v_control.status(1))
    sleep(0.5)
    print(v_control.status(0))
