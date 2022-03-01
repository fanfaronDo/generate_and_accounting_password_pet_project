import tkinter
from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Button, Entry, Label, Checkbutton

from modules.EncryptionPassword import Encryption
from modules.GenerationPass import GenerationPass
from modules.ListDescription import ComboboxSelectionWindow
from modules.FileHandling import HandlingFile
import tkinter.messagebox as ms_bx


class InitialiseComponentGUI(Frame):
    def __init__(self):
        super().__init__()

        # title
        self.master.title("Generate and accounting password")
        self.pack(fill=BOTH, expand=True)

        self.handling_file = HandlingFile()
        # validate arg
        #self.validations = Validations()

        self.encryption_pass = Encryption()

        # initialisation interface elements
        # description elem
        self.label_log = Label(self, text="description: ", width=10)
        self.label_log.grid(row=0, column=0, padx=5, pady=5)
        self.cmbDesc = ComboboxSelectionWindow(self)

        # login elem
        self.label_log = Label(self, text="login: ", width=10)
        self.label_log.grid(row=1, column=0, padx=5, pady=5)
        self.entry_output_login = Entry(self)
        self.entry_output_login.grid(row=1, column=1, padx=0, pady=5, columnspan=3)

        # password elem
        self.label_log = Label(self, text="Password: ", width=10)
        self.label_log.grid(row=2, column=0, padx=5, pady=5)
        self.__entry_output_pass = Entry(self)
        self.__entry_output_pass.grid(row=2, column=1, padx=0, pady=5, columnspan=3)

        # button generation password
        self.butt_gen_pass = Button(self, text='generate',
                                    command=self.gen_pass_button_click)
        self.butt_gen_pass.grid(row=4, column=4, padx=2, pady=5)

        # button find
        self.btn_find = Button(self, text="Find", command=self.find_elem_button_click)
        self.btn_find.grid(row=4, column=0, padx=2, pady=5)

        # button apply
        self.btn_apply = Button(self, text="Add", command=self.__add_elem_button_click)
        self.btn_apply.grid(row=4, column=2, padx=2, pady=5)

        # button delete
        self.btn_delete = Button(self, text="delete", command=self.delete_credentials)
        self.btn_delete.grid(row=4, column=3, padx=2, pady=5)

        # spinbox length password
        self.len_pass = tkinter.Spinbox(self, from_=8, to=18, width=10)
        self.len_pass.grid(row=0, column=4, padx=2, pady=5)

        # checkbox special char in password
        self.spec_char_track = tkinter.IntVar()
        self.spec_char = Checkbutton(self, text="spec char",
                                     variable=self.spec_char_track)
        self.spec_char.grid(row=1, column=4, padx=2, pady=5)

        # checkbox numbers in password
        self.numbers_track = tkinter.IntVar()
        self.numbers = Checkbutton(self, text="numbers",
                                   variable=self.numbers_track)
        self.numbers.grid(row=2, column=4, padx=0, pady=5)

    def gen_pass_button_click(self):
        generate_password = GenerationPass(spec_symbol=self.spec_char_track.get(),
                                           numbers=self.numbers_track.get(),
                                           length=self.len_pass.get())
        self.__entry_output_pass.delete(0, tkinter.END)
        self.__entry_output_pass.insert(0, generate_password.gen_pass)

    def find_elem_button_click(self):
        value = self.cmbDesc.combobox_desc.get()
        try:
            rec = self.handling_file.dict_requisites[value]
            self.entry_output_login.delete(0, tkinter.END)
            self.entry_output_login.insert(0, rec[0])
            self.__entry_output_pass.delete(0, tkinter.END)
            self.__entry_output_pass.insert(0, self.encryption_pass.get_decrypted_word(rec[1]))
        except KeyError:
            self.entry_output_login.delete(0, tkinter.END)
            self.entry_output_login.insert(0, "KeyError")

    def __add_elem_button_click(self):
        description = self.cmbDesc.combobox_desc.get()
        login = self.entry_output_login.get()
        password = self.__entry_output_pass.get()

        # validate data
        self.handling_file.dict_requisites[description] = (login, self.encryption_pass.get_encrypted_word(password))
        self.cmbDesc.update_list_description()

    def delete_credentials(self):
        confirm_deleting = ms_bx.askyesno("delete", "Удалить учетные данные ?")
        desc_for_del = self.cmbDesc.combobox_desc.get()

        if confirm_deleting:
            del self.handling_file.dict_requisites[desc_for_del]
            ms_bx.showinfo("delete", "credentials is delete")
        else:
            ms_bx.showinfo("delete", "credentials is not delete")

        self.cmbDesc.update_list_description()


def mine():
    handling_file = HandlingFile()
    root = Tk()
    root.geometry('340x150')
    root.resizable(False, False)
    handling_file.read()
    app = InitialiseComponentGUI()
    root.mainloop()
    handling_file.write()


if __name__ == '__main__':
    mine()
