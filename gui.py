import tkinter as tk
from core.manager import ARISManager

class ARISGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("ARIS - AI Voice Assistant")
        self.manager = ARISManager()
        self.create_widgets()

    def create_widgets(self):
        self.text_area = tk.Text(self.root, height=20, width=60, state='disabled', wrap='word')
        self.text_area.pack(pady=10)

        self.entry = tk.Entry(self.root, width=50)
        self.entry.pack(side=tk.LEFT, padx=10)
        self.entry.bind("<Return>", self.send_command)

        self.send_button = tk.Button(self.root, text="Send", command=self.send_command)
        self.send_button.pack(side=tk.LEFT)

        self.status_label = tk.Label(self.root, text="Status: Idle")
        self.status_label.pack(pady=5)

    def send_command(self, event=None):
        user_input = self.entry.get()
        if user_input:
            self.append_text(f"You: {user_input}")
            intent, entities = self.manager.nlu.parse(user_input)
            response = self.manager.route(intent, entities, user_input)
            self.append_text(f"ARIS: {response}")
            self.entry.delete(0, tk.END)

    def append_text(self, text):
        self.text_area.config(state='normal')
        self.text_area.insert(tk.END, text + "\n")
        self.text_area.config(state='disabled')
        self.text_area.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    gui = ARISGUI(root)
    root.mainloop()