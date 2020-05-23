import time
import shutil
from tkinter import *
from tkinter.filedialog import askopenfilename, askdirectory

internal_path_global = ""
external_path_global = ""


def internal_path(mode):
    path = ask_open_file(mode)
    rep = input("Êtes-vous sûr que votre fichier se trouve dans : " + str(path) + " [O/N]?\n=>:")
    make_sure_internal(rep, mode)
    return path


def make_sure_internal(rep, mode):
    if rep == "O":
        external_path()
    elif rep == "N":
        internal_path(mode)
    else:
        print("Vous avez fait une erreur de frappe :=D\n")
        internal_path(mode)


def external_path():
    path = ask_open_directory()
    rep = input("Êtes-vous sûr que votre dispositif se trouve dans : " + str(path) + " [O/N]?\n=>:")
    make_sure_xternal(rep)
    return path


def make_sure_xternal(rep):
    if rep == "N":
        external_path()
    elif rep != "O" and rep != "N" and rep != "o" and rep != "n":
        print("Vous avez fait une erreur de frappe :=D\n")
        external_path()


def choose_time():
    timeout = input("Entrez le temps que vous voulez entre chaque backup en secondes :")
    return timeout


def backup_file(mode):
    timeout = choose_time()
    if mode == "2":
        while True:
            shutil.copy(str(internal_path_global), str(external_path_global))
            copy_time = str(time.localtime().tm_mday) + "/" + str(time.localtime().tm_mon) + "/" + str(
                time.localtime().tm_year) + "/" + "à" + str(time.localtime().tm_hour) + "h" + str(
                time.localtime().tm_min) + "min" + str(time.localtime().tm_sec) + "sec "
            sys.stdout.write("\r dernière copie faite le : " + str(copy_time) + " de : " + str(
                external_path_global) + " vers : " + str(internal_path_global))
            sys.stdout.flush()
            time.sleep(int(timeout))
    elif mode == "1":
        while True:
            attemps = 0
            if attemps > 1:
                shutil.rmtree(external_path_global)
                shutil.copytree(str(internal_path_global), str(external_path_global))
                copy_time = str(time.localtime().tm_mday) + "/" + str(time.localtime().tm_mon) + "/" + str(
                    time.localtime().tm_year) + "/" + "à" + str(time.localtime().tm_hour) + "h" + str(
                    time.localtime().tm_min) + "min" + str(time.localtime().tm_sec) + "sec "
                sys.stdout.write("\r dernière copie faite le : " + str(copy_time) + " de : " + str(
                    external_path_global) + " vers : " + str(internal_path_global))
                sys.stdout.flush()
                time.sleep(int(timeout))
                attemps += 1
            else:
                shutil.copytree(str(internal_path_global), str(external_path_global))
                copy_time = str(time.localtime().tm_mday) + "/" + str(time.localtime().tm_mon) + "/" + str(
                    time.localtime().tm_year) + "/" + "à" + str(time.localtime().tm_hour) + "h" + str(
                    time.localtime().tm_min) + "min" + str(time.localtime().tm_sec) + "sec "
                sys.stdout.write("\r dernière copie faite le : " + str(copy_time) + " de : " + str(
                    external_path_global) + " vers : " + str(internal_path_global))
                sys.stdout.flush()
                time.sleep(int(timeout))
                attemps += 1


def ask_open_file(mode):
    if mode == "2":
        print("Choisissez le chemin vers votre document en cours de modification : ")
        rep = input("Choisir le document dans une fenêtre de l'explorateur[1] écrire le chemin absolu[2]\n=>:")

        if rep == "1":
            path = askopenfilename(parent=fenetre1, initialdir="/", title="Selection d'un document")
        elif rep == "2":
            path = input("Entrez le chemin absolu :")
        else:
            print("Vous avez fait une erreur de frappe :=D\n")
            ask_open_file(mode)
    elif mode == "1":
        print("Choisissez le chemin vers votre répertoire en cours de modification : ")
        rep = input("Choisir le répertoire dans une fenêtre de l'explorateur[1] écrire le chemin absolu[2]\n=>:")
        if rep == "1":
            path = askdirectory(parent=fenetre1, initialdir="/", title="Selection d'un document")
        elif rep == "2":
            path = input("Entrez le chemin absolu :")
        else:
            print("Vous avez fait une erreur de frappe :=D\n")
            ask_open_file(mode)
    return path


def ask_open_directory():
    print("Choisissez le chemin absolu vers votre dossier de sauvegarde : ")
    rep = input("Choisir le dossier dans une fenêtre de l'explorateur[1] écrire le chemin absolu[2]\n=>:")
    if rep == "1":
        path = askdirectory(parent=fenetre1, initialdir="/", title="Selection d'un fichier")
    elif rep == "2":
        path = input("entrez le chemin absolu vers votre dispositif de sauvegarde : \n=>:")
    else:
        print("Vous avez fait une erreur de frappe :=D\n")
        ask_open_directory()
    return path


if __name__ == '__main__':
    mode = input("Vous voulez sauvegarder un répertoire entier [1] ou juste un fichier [2]\n=>:")
    fenetre1 = Tk()
    fenetre1.withdraw()
    internal_path_global = internal_path(mode)
    external_path_global = external_path()
    backup_file(mode)
    fenetre1.mainloop()
