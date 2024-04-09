import tkinter as tk

import socket


def get_keyword_desc():

    message = entry_keyword.get()
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost', 3000)
    print('Connecting to {} port {}'.format(*server_address))
    client_socket.connect(server_address)


    print('Sending:', message)
    client_socket.sendall(message.encode())

    data = client_socket.recv(1024)
    print('Received:', data.decode())

    print('Closing socket')
    client_socket.close()

    text_description.config(state=tk.NORMAL)
    text_description.delete("1.0", tk.END)
    text_description.insert(tk.END, data)
    text_description.config(state=tk.DISABLED)


root = tk.Tk()
root.title("Keyword Description")

root.configure(padx=20, pady=20)


container_frame = tk.Frame(root, width=600, height=1000, padx=20, pady=20, bg="#f9f9f9", bd=3, relief="solid")
container_frame.pack()

label_keyword = tk.Label(container_frame, text="Enter a Keyword:", font=("Arial", 12, "bold"))
label_keyword.grid(row=0, column=0, pady=5, sticky="w")

entry_keyword = tk.Entry(container_frame, width=100)
entry_keyword.grid(row=1, column=0, padx=5, pady=(5, 20))

button_submit = tk.Button(container_frame, text="Submit", width=100, bg="#007bff", fg="white", bd=0, command=get_keyword_desc)
button_submit.grid(row=2, column=0, padx=5, pady=10)

text_description = tk.Text(container_frame, width=100, height=8, wrap=tk.WORD, state=tk.DISABLED)
text_description.grid(row=3, column=0, padx=5, pady=5)

root.mainloop()
