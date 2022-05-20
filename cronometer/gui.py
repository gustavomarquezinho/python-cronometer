from tests import get_interval
import sv_ttk as sun_valley


from tkinter.ttk import (
    Frame,
    Label,
    Button
)

from tkinter import Tk, PhotoImage


class Cronometer(Tk):
    def __init__(self, title: str):
        super().__init__()

        self.center_window(400, 332)
        self.resizable(0, 0)

        self.title(title)
        self.milliseconds = 0

        self.iconphoto(False, PhotoImage(file='./cronometer/assets/icon_small.png'))
        sun_valley.set_theme('dark')

        self.create_label()
        self.create_button()


    def center_window(self, size_x: int, size_y: int):
        pos_x = (self.winfo_screenwidth() / 2) - (size_x / 2) 
        pos_y = (self.winfo_screenheight() / 2) - (size_y / 2)

        self.geometry('{}x{}+{}+{}' .format(size_x, size_y, int(pos_x), int(pos_y)))


    def create_label(self):
        frame_label = Frame().pack()

        self.label = Label(
            frame_label,
            text='00:00:00',
            font=('Odibee Sans', 56, 'bold')
        )
        
        self.label.pack(pady=(56, 0), side='top')


    def create_button(self):
        frame_button = Frame().pack()

        self.button = Button(
            frame_button,
            text='Iniciar',
            width=12,
            command=lambda: self.update_cronometer(pressed=True)
        )
        self.button.pack(padx=(84, 8), ipady=12, side='left')

        button = Button(
            frame_button,
            text='Resetar',
            width=12,
            command=self.reset_cronometer
        )
        button.pack(padx=(8, 0), ipady=12, side='left')

    
    def update_cronometer(self, pressed: bool = False):
        self.label['text'] = self.format_cronometer(self.milliseconds)

        if pressed:
            get_interval(self.label['text'], self.milliseconds, self.button['text'] == 'Iniciar')

            if not self.verify_button_state():
                return

        self.after_id = self.after(1, self.update_cronometer)
        self.milliseconds += 1

    
    def reset_cronometer(self):
        if self.button['text'] == 'Pausar':
            self.verify_button_state()
        
        self.label['text'] = '00:00:00'
        self.milliseconds = 0


    def verify_button_state(self) -> bool:
        if self.button['text'] == 'Iniciar':
            self.button['text'] = 'Pausar'
            return True
    
        self.button['text'] = 'Iniciar'
        self.after_cancel(self.after_id)
        return False


    def format_cronometer(self, milliseconds: int) -> str:
        seconds = int(milliseconds / 1000)
        milliseconds -= seconds * 1000

        hours = int(seconds / 3600)
        seconds -= hours * 3600

        minutes = int(seconds / 60)
        seconds -= minutes * 60

        return '{:02}:{:02}:{:02}' .format(hours, minutes, seconds)
