import tkinter
from tkinter import Tk, BOTH, W, E, RIGHT, LEFT
from tkinter.ttk import Frame, Button, Entry, Label, Combobox
from modules.FileHandling import HandlingFile


class ComboboxSelectionWindow:
    """
    Realized work with combobox
    """
    def __init__(self, root):
        self.__root = root
        self.handle_file = HandlingFile()
        self.__take_list_description()

    def update_list_description(self):
        self.__take_list_description()

    def __take_list_description(self):
        list_description = []
        for desc in self.handle_file.dict_requisites:
            list_description.append(desc)

        self.combobox_desc = Combobox(self.__root, values=list_description, width=18)
        self.combobox_desc.grid(row=0, column=1, padx=0, pady=5, columnspan=3)

    def bind_elem(self):
        self.combobox_desc.bind("<ComboboxSelected>", lambda: print("New element"))




