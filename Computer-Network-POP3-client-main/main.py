import tkinter as tk
from tkinter import messagebox
import sys
import io

from actions.list import list
from actions.top import top
from actions.quit import quit
from actions.dele import delete
from actions.stat import stat
from actions.retr_full import retrieve_full_message
from actions.NOOP import noop
from actions.rset import rset
from actions.welcome import welcome
from actions.msg_content import get_msg_content
import poplib

# Configuration for the email account
POP3_SERVER = 'pop.gmail.com'
POP3_PORT = 995
EMAIL = 'lyminhhung5694@gmail.com'
PASSWORD = 'yybn plrr vqgj euye'

class TextRedirector(io.StringIO):
    def __init__(self, text_box):
        super().__init__()
        self.text_box = text_box

    def write(self, string):
        self.text_box.insert(tk.END, string)
        self.text_box.see(tk.END)  # Scroll to the end of the text box

def rset(server):
    print('Resetting the session')
    response = server.rset()
    print(response.decode())

class EmailClientGUI:
    def __init__(self, master):
        self.master = master
        master.title("POP3 Client")

        self.server = poplib.POP3_SSL(POP3_SERVER, POP3_PORT)
        self.server.user(EMAIL)
        self.server.pass_(PASSWORD)
    
        self.label = tk.Label(master, text="Select an action:")
        self.label.pack()

        self.action_var = tk.StringVar()
        self.action_var.set("list")  # Default action

        self.action_dropdown = tk.OptionMenu(master, self.action_var, "list", "top", "retrieve_full", "get_msg_content", "stat", "noop", "delete", "rset", "quit")
        self.action_dropdown.pack()

        self.message_number_label = tk.Label(master, text="Enter message number:")
        self.message_number_label.pack()

        self.message_number_entry = tk.Entry(master)
        self.message_number_entry.pack()

        self.lines_label = tk.Label(master, text="Enter number of lines (for top action):")
        self.lines_label.pack()

        self.lines_entry = tk.Entry(master)
        self.lines_entry.pack()

        self.execute_button = tk.Button(master, text="Execute", command=self.execute_action)
        self.execute_button.pack()

        self.output_text = tk.Text(master, height=20, width=50)
        self.output_text.pack()

    def execute_action(self):
        action = self.action_var.get()
        message_number = self.message_number_entry.get()
        num_lines = self.lines_entry.get()

        try:
            message_number = int(message_number)
        except ValueError:
            messagebox.showerror("Error", "Invalid message number")
            return

        try:
            num_lines = int(num_lines)
        except ValueError:
            num_lines = 0

        redirector = TextRedirector(self.output_text)
        sys.stdout = redirector

        if action == "list":
            list(self.server)
        elif action == "top":
            top(self.server, message_number, num_lines)
        elif action == "retrieve_full":
            retrieve_full_message(self.server, message_number)
        elif action == "get_msg_content":
            get_msg_content(self.server, message_number)
        elif action == "stat":
            stat(self.server)
        elif action == "noop":
            noop(self.server)
        elif action == "delete":
            delete(self.server, message_number)
        elif action == "rset":
            rset(self.server)   
        elif action == "quit":
            quit(self.server)
            self.master.quit()
        

        # Reset stdout to its original state
        sys.stdout = sys.__stdout__

root = tk.Tk()
email_client_gui = EmailClientGUI(root)
root.mainloop()