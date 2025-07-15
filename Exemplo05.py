import tkinter as tk 

class MinhaAPP:
    def _init_(self, parent):
        self.myParent = parent
        self.buttons_frame = tk.Frame(parent,background="lightgray") 
        self.buttons_frame.pack(padx=10, fill=tk.BOTH,expand=TRUE) 

        self.botao1 =tk.Button(self.buttons_frame, text="Botao 1" ,background="greenn") 
        self.botao1.pack(side=tk.LEFT, padx=5, padx=5) 

        self.botao2 = tk.Button(self.buttons_frame, text="Botao 2",background="yellon") 
        self.botao2.pack(side=tk.LEFT, padx=5, pady=5) 

        self.botao3 = tk.Button(self.buttons_frame, text="BOTÂO 3",background="red") 
        self.botao3.pack(side=tk.LEFT, padx=5, pady=5) 

root = tk.TK() 
root.title("Exemplo com Pack") 
root.geometry("400x300") 
app = MinnhaApp(root) 
root.mainloop()

                               

        
