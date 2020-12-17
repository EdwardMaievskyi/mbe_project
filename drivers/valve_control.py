import serial
from time import sleep


class ValveControl:
    def __init__(self, tty_port="/dev/ttyUSB0", baudrate=9600):
        """
        Tools used for establishing connection with I/O electronic scheme and
        further controlling of the MBE-setup pneumatic valves.
        ...

        Attributes
        ----------
        tty_port : string
            System address of the USB-UART converter
        baudrate: float
            Number of pulses per second transmitted via serial bus.
        """
        self.ser = serial.Serial(port=tty_port, baudrate=baudrate, timeout=10,
                                 bytesize=serial.EIGHTBITS,
                                 stopbits=serial.STOPBITS_ONE,
                                 parity=serial.PARITY_NONE,
                                 xonxoff=False, rtscts=False)
        self.board_addresses = ['0F', '1F']

    def switch_on_off_valve(self, board_no=0, out_no=1, switch_on=True):
        """
        Switching on and off output channels controlling directly pneumatic
        valves.

        Parameters
        ----------
        board_no : int
            Indexing number of the electronic board where the command will
            be sent. May vary from 0 to N-1, where N is a number of electronic
            boards used for pneumatic valves control in the MBE experimental
            setup.
        out_no : int
            Indexing number of the output on the electronic board. May vary
            from 1 to 8.
        Returns
        -------
        str
            "ok" if a command was accepted for execution

        """
        if switch_on:
            command = '@' + self.board_addresses[board_no] + '+' + str(out_no)
        else:
            command = '@' + self.board_addresses[board_no] + '-' + str(out_no)
        print(command)
        self.ser.write(str(command).encode())
        sleep(0.2)
        return(self.ser.readline().decode('ascii'))

    def status(self, board_no):
        """
        Requesting the status of inputs and outputs of the electronic board.

        Parameters
        ----------
        board_no : int
            Indexing number of the electronic board where the command will
            be sent. May vary from 0 to N-1, where N is a number of electronic
            boards used for pneumatic valves control in the MBE experimental
            setup.
        Returns
        -------
        str
            String where the first three symbols represent the board physical
            address and other symbols present the state (HIGH/LOW == True/False
            == 1/0) of electronic board inputs and outputs.

        """
        print('@' + self.board_addresses[board_no] + '??')
        self.ser.write(str('@' + self.board_addresses[board_no] +
                           '??').encode())
        sleep(0.2)
        return(self.ser.readline().decode('ascii'))


if __name__ == '__main__':
    """
    Some testing script
    """
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
