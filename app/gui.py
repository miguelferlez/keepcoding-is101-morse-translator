from tkinter import *
from app.morse import to_morse, to_string

def click(command:str, get_text:Text, set_text:Text):
    input_text = get_text.get('1.0','end-1c')
    set_text.delete('1.0', END)
    if command == 'to plain':
        set_text.insert('1.0', to_string(input_text))
    elif command == 'to morse':
        set_text.insert('1.0', to_morse(input_text))


def create_plain_frame(container:Frame)->Frame:
    plain_frame = Frame(container, width=250, height=337, padx=10, pady=10)
    plain_frame.place(x=330, y=0)
    plain_frame.pack_propagate(False)

    plain_label = Label(plain_frame, text='PLAIN TEXT')
    plain_label.pack(side='top', anchor='w')

    plain_text_area_container = Frame(plain_frame)
    plain_text_area_container.pack(side='top', expand=True, fill='both')
    plain_text_area_container.pack_propagate(False)
    plain_text_area = Text(plain_text_area_container)
    plain_text_area.pack(side='top')

    return plain_frame, plain_text_area

def create_buttons_frame(container:Frame, morse_text:Text, plain_text:Text)->Frame:
    buttons_frame = Frame(container, width=80, height=337, padx=10, pady=10)
    buttons_frame.place(x=250,y=0)
    buttons_frame.pack_propagate(False)
    buttons_label = Label(buttons_frame, text='')
    buttons_label.pack(side='top')

    morse_to_string_button = Button(buttons_frame, text='>', width=6, command=lambda : click('to plain', morse_text, plain_text))
    morse_to_string_button.pack(side='top', fill='x')
    string_to_morse_button = Button(buttons_frame, text='<', width=6, command=lambda : click('to morse', plain_text, morse_text))
    string_to_morse_button.pack(side='top', fill='x')

    return buttons_frame

def create_morse_frame(container:Frame)->Frame:
    morse_frame = Frame(container, width=250, height=337, padx=10, pady=10)
    morse_frame.place(x=0, y=0)
    morse_frame.pack_propagate(False)

    morse_label = Label(morse_frame, text='MORSE')
    morse_label.pack(side='top', anchor='w')

    morse_text_area_container = Frame(morse_frame)
    morse_text_area_container.pack(side='top', expand=True, fill='both')
    morse_text_area_container.pack_propagate(False)
    morse_text_area = Text(morse_text_area_container)
    morse_text_area.pack(side='top')

    dot_button = Button(morse_frame, text='•', width=6, command=lambda : morse_text_area.insert(END, '.'))
    dot_button.pack(side='left')
    stop_button = Button(morse_frame, text='space', width=6, command=lambda : morse_text_area.insert(END, ' '))
    stop_button.pack(side='right')
    slash_button = Button(morse_frame, text='᠆', width=6, command=lambda : morse_text_area.insert(END, '-'))
    slash_button.pack(side='bottom')

    return morse_frame, morse_text_area

def create_body(container:Frame)->Frame:
    body = Frame(container)
    body.pack(side='top', expand=True, fill='both')

    return body

def create_header(container:Frame)->Frame:
    header = Frame(container)
    header.pack(side='top', fill='x', padx=10, pady=10)

    title = Label(header, text='MORSE TRANSLATOR')
    title.pack(side='top', anchor='w')

    return header

def create_main_window():
    root = Tk()
    root.title('morse translator - tkinter')
    root.geometry('600x400')
    root.config(background='#F0F0F0')

    window = Frame(root)
    window.pack(side='top', expand=True, fill='both', padx=10, pady=10)

    create_header(window)
    body = create_body(window)
    create_morse_frame(body)
    create_plain_frame(body)
    create_buttons_frame(body, create_morse_frame(body)[1], create_plain_frame(body)[1])
      
    root.mainloop()

if __name__ == '__main__':
    create_main_window()
