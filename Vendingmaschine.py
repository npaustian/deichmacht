import tkinter as tk
from functools import partial


class Potable(object):

    def __init__(self, name, available):
        self.name = name
        self.available = available


class VendingMachine(object):

    def __init__(self, potables):
        self.potables = potables

    def emit(self, index):
        potable = self.potables[index]
        if potable.available:
            print(potable.name, 'wird ausgegeben')
        else:
            print(
                potable.name,
                'steht zur Zeit nicht zur Verfügung. Bitte auffüllen.'
            )


def main():
    vending_machine = VendingMachine(
        [
            Potable('Cola', True),
            Potable('Fanta', True),
            Potable('Mezzo Mix', False),
            Potable('Cola Light', True),
        ]
    )

    root = tk.Tk()
    root.title('Wählen Sie Ihr Getränk')
    root.geometry('500x500')

    for i, potable in enumerate(vending_machine.potables):
        tk.Button(
            root, text=potable.name, command=partial(vending_machine.emit, i)
        ).pack(expand=True, fill=tk.BOTH)

    root.mainloop()


if __name__ == '__main__':
    main()
