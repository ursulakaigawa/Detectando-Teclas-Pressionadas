import tkinter as tk

def on_key_press(event):
    # Exibe a tecla pressionada no terminal
    print(f"Tecla pressionada: {event.char}")

def main():
    # Cria a janela principal
    root = tk.Tk()
    root.title("Detector de Teclas")
    root.geometry("300x200")  # Define o tamanho da janela

    # Cria um rótulo para instruções
    label = tk.Label(root, text="Pressione qualquer tecla", font=("Arial", 14))
    label.pack(pady=50)

    # Vincula o evento de pressionar tecla à função on_key_press
    root.bind("<Key>", on_key_press)

    # Inicia o loop principal da interface gráfica
    root.mainloop()

if __name__ == "__main__":
    main()