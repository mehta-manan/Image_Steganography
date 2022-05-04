from modules import *
import steganography


class Stego:

    def OpenEncodeDialog(self):
        self.encode_dialog = tkinter.Toplevel(self.root)
        self.encode_dialog.resizable(True, False)
        self.encode_dialog.title('Image Steganographer - Encode')
        self.encode_dialog.configure(bg='#393E46')
        self.encode_dialog.geometry('400x400')
        self.encode_dialog.minsize(400, 400)

        self.img_path_label = tkinter.Label(self.encode_dialog, text='Image Path', font=(
            'Inter', 12, 'bold'), fg='#F7F7F7', bg='#393E46').place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

        self.img_path_entry = tkinter.Entry(
            self.encode_dialog, width=30, bg='#F7F7F7')
        self.img_path_entry.place(
            relx=0.5, rely=0.21, anchor=tkinter.CENTER)

        self.message_label = tkinter.Label(self.encode_dialog, text='Secret Message', font=(
            'Inter', 12, 'bold'), fg='#F7F7F7', bg='#393E46').place(relx=0.5, rely=0.30, anchor=tkinter.CENTER)

        self.message_entry = tkinter.Entry(
            self.encode_dialog, width=30, bg='#F7F7F7')
        self.message_entry.place(
            relx=0.5, rely=0.36, anchor=tkinter.CENTER)

        self.out_path_label = tkinter.Label(self.encode_dialog, text='Encoded File Name (Path)', font=(
            'Inter', 12, 'bold'), fg='#F7F7F7', bg='#393E46').place(relx=0.5, rely=0.46, anchor=tkinter.CENTER)

        self.out_path_entry = tkinter.Entry(
            self.encode_dialog, width=30, bg='#F7F7F7')
        self.out_path_entry.place(
            relx=0.5, rely=0.52, anchor=tkinter.CENTER)

        self.encode_button = tkinter.Button(self.encode_dialog, text='ENCODE', bg='#EEEEEE', height=1, width=10, font=('Inter', 13, 'bold'), bd=0, command=lambda: steganography.Encode(self.img_path_entry.get(), self.message_entry.get(), self.out_path_entry.get(),self)).place(
            relx=0.5, rely=0.63, anchor=tkinter.CENTER)

        self.abort_button = tkinter.Button(self.encode_dialog, text='Abort', bg='#EEEEEE', width=10, font=('Inter', 10), bd=0, command=self.encode_dialog.destroy).place(
            relx=0.5, rely=0.9, anchor=tkinter.CENTER)

    def OpenDecodeDialog(self):

        self.decode_dialog = tkinter.Toplevel(self.root)
        self.decode_dialog.resizable(True, False)
        self.decode_dialog.title('Image Steganographer - Decode')
        self.decode_dialog.configure(bg='#393E46')
        self.decode_dialog.geometry('400x400')
        self.decode_dialog.minsize(400, 400)

        self.img_path_label = tkinter.Label(self.decode_dialog, text='Encoded Image Path', font=(
            'Inter', 12, 'bold'), fg='#F7F7F7', bg='#393E46').place(relx=0.5, rely=0.17, anchor=tkinter.CENTER)

        self.img_path_entry = tkinter.Entry(
            self.decode_dialog, width=30, bg='#F7F7F7')
        self.img_path_entry.place(
            relx=0.5, rely=0.23, anchor=tkinter.CENTER)

        self.message_label = tkinter.Label(self.decode_dialog, text='Decoded Message', font=(
            'Inter', 12, 'bold'), fg='#F7F7F7', bg='#393E46').place(relx=0.5, rely=0.56, anchor=tkinter.CENTER)

        self.text_ = tkinter.Text(self.decode_dialog, height=5, width=30)

        self.text_.place(relx=0.5, rely=0.70, anchor=tkinter.CENTER)

        self.text_.config(state='normal')

        self.decode_button = tkinter.Button(self.decode_dialog, text='DECODE', bg='#EEEEEE', height=1, width=10, font=('Inter', 13, 'bold'), bd=0, command=lambda: steganography.Decode(self.img_path_entry.get(), self)).place(
            relx=0.5, rely=0.32, anchor=tkinter.CENTER)

        self.text_.delete(1.0, "end")
        self.text_.insert("end", self.decoded_message)

        self.abort_button = tkinter.Button(self.decode_dialog, text='Abort', bg='#EEEEEE', width=10, font=('Inter', 10), bd=0, command=self.decode_dialog.destroy).place(
            relx=0.5, rely=0.9, anchor=tkinter.CENTER)

    def OpenSuccessDialog(self):
        self.success_dialog = tkinter.Toplevel(self.encode_dialog)
        self.success_dialog.resizable(True, False)
        self.success_dialog.title('Image Steganographer - Success')
        self.success_dialog.configure(bg='#44AC33')
        self.success_dialog.geometry('500x100')
        self.success_dialog.minsize(500, 100)
        self.success_label = tkinter.Label(self.success_dialog, text='SUCCESS: Image Encoded Successfully!', font=(
            'Inter', 15, 'bold'), fg='#F7F7F7', bg='#44AC33').place(relx=0.5, rely=0.33, anchor=tkinter.CENTER)
        self.ok_button = tkinter.Button(self.success_dialog, text='Ok', bg='#EEEEEE', width=10, font=('Inter', 10), bd=0, command=self.success_dialog.destroy).place(
            relx=0.5, rely=0.7, anchor=tkinter.CENTER)

    def NoHiddenMessageDialog(self):
        self.nhm_dialog = tkinter.Toplevel(self.decode_dialog)
        self.nhm_dialog.resizable(True, False)
        self.nhm_dialog.title('Image Steganographer - ERROR#1')
        self.nhm_dialog.configure(bg='#D0342C')
        self.nhm_dialog.geometry('600x100')
        self.nhm_dialog.minsize(600, 100)
        self.nhm_label = tkinter.Label(self.nhm_dialog, text='ERROR: No Hidden Message Found', font=(
            'Inter', 15, 'bold'), fg='#F7F7F7', bg='#D0342C').place(relx=0.5, rely=0.33, anchor=tkinter.CENTER)
        self.abort_button = tkinter.Button(self.nhm_dialog, text='Abort', bg='#EEEEEE', width=10, font=('Inter', 10), bd=0, command=self.nhm_dialog.destroy).place(
            relx=0.5, rely=0.7, anchor=tkinter.CENTER)

    def GreaterSizeRequired(self):
        self.gs_dialog = tkinter.Toplevel(self.encode_dialog)
        self.gs_dialog.resizable(True, False)
        self.gs_dialog.title('Image Steganographer - ERROR#1')
        self.gs_dialog.configure(bg='#D0342C')
        self.gs_dialog.geometry('500x100')
        self.gs_dialog.minsize(500, 100)
        self.succes_label = tkinter.Label(self.gs_dialog, text='ERROR: Greater size image required', font=(
            'Inter', 15, 'bold'), fg='#F7F7F7', bg='#D0342C').place(relx=0.5, rely=0.33, anchor=tkinter.CENTER)
        self.abort_button = tkinter.Button(self.gs_dialog, text='Abort', bg='#EEEEEE', width=10, font=('Inter', 10), bd=0, command=self.gs_dialog.destroy).place(
            relx=0.5, rely=0.7, anchor=tkinter.CENTER)

    def __init__(self):
        self.decoded_message = ''

        self.root = tkinter.Tk()

        self.root.resizable(True, False)
        self.root.title('Image Steganographer')
        self.root.configure(bg='#393E46')
        self.root.geometry('500x500')
        self.root.minsize(500, 500)

        self.heading_label_1 = tkinter.Label(self.root, text='WELCOME TO', font=(
            'Inter', 15), fg='#F7F7F7', bg='#393E46').place(relx=0.5, rely=0.33, anchor=tkinter.CENTER)

        self.heading_label_2 = tkinter.Label(self.root, text='IMAGE STEGANOGRAPHER', font=(
            'Inter', 20, 'bold'), fg='#F7F7F7', bg='#393E46').place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

        self.encode_button = tkinter.Button(self.root, text='ENCODE', bg='#EEEEEE', height=1, width=10, font=('Inter', 13, 'bold'), bd=0, command=self.OpenEncodeDialog).place(
            relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.decode_button = tkinter.Button(self.root, text='DECODE', bg='#EEEEEE', height=1, width=10, font=('Inter', 13, 'bold'), bd=0, command=self.OpenDecodeDialog).place(
            relx=0.5, rely=0.58, anchor=tkinter.CENTER)

        self.quit_button = tkinter.Button(self.root, text='Quit', bg='#EEEEEE', width=10, font=('Inter', 10), bd=0, command=self.root.destroy).place(
            relx=0.5, rely=0.8, anchor=tkinter.CENTER)

        self.prj_info = tkinter.Label(self.root, text='Minor Project - 2022 - Image Steganography - 141', font=(
            'Inter', 8), fg='#F7F7F7', bg='#393E46').place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

        self.root.mainloop()


stg = Stego()
