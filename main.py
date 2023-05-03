import tkinter as tk
import time

class WritingDissistant(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("The Writing Dissistant")
        self.geometry("800x600")

        self.timeout = 5  # Timeout in seconds
        self.last_keypress_time = time.time()

        # Create a frame with padding
        self.frame = tk.Frame(self, padx=20, pady=20)
        self.frame.pack(expand=True, fill=tk.BOTH)

        # Create a label for the prompt
        self.label = tk.Label(self.frame, text="Don't stop typing here...", font=("Helvetica", 12))
        self.label.pack()

        # Create the text widget
        self.text_widget = tk.Text(self.frame, wrap=tk.WORD, padx=10, pady=10, bd=2, relief=tk.GROOVE)
        self.text_widget.pack(expand=True, fill=tk.BOTH)

        self.text_widget.bind("<Key>", self.reset_timer)
        self.check_timer()

    def reset_timer(self, event):
        self.last_keypress_time = time.time()

    def check_timer(self):
        current_time = time.time()
        time_since_last_keypress = current_time - self.last_keypress_time

        if time_since_last_keypress >= self.timeout:
            self.text_widget.delete("1.0", tk.END)

        self.after(100, self.check_timer)


if __name__ == "__main__":
    app = WritingDissistant()
    app.mainloop()

