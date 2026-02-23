import manager
import secrets
import string

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(chars) for _ in range(length))


def main():

    print(" PASSWORD MANAGER ")
    master = input("Inserisci la master password ")
    if not manager.check_master(master):
        print("Master password sbagliata")
        return

    while True:
        print("\nMenu:")
        print("1. Aggiungi nuova entry")
        print("2. Genera password casuale")
        print("3. Cerca sito")
        print("4. Vedi tutti i siti")
        print("5. Aggiorna entry")
        print("6. Elimina entry")
        print("7. Esci")

        choice = input("Scegli un'opzione: ")

        if choice == "1":
            site = input("Nome sito: ")
            username = input("Username: ")
            password = input("Password: ")
            manager.add_entry(site, username, password)
            print("Entry salvata correttamente")

        elif choice == "2":
            site = input("Nome sito: ")
            username = input("Username: ")
            length = int(input("Numero caratteri password: "))
            password = generate_password(length)
            manager.add_entry(site, username, password)
            print("Entry salvata correttamente")


        elif choice == "3":

            site = input("Nome sito: ")

            entry = manager.get_entry(site)

            if entry:

                print(f"Username: {entry['username']}, Password: {entry['password']}")

            else:

                print("Sito non trovato.")


        elif choice == "4":

            sites = manager.list_sites()

            print("Siti salvati:", ", ".join(sites))


        elif choice == "5":

            site = input("Nome sito da aggiornare: ")

            username = input("Nuovo username (vuoto per mantenere): ")

            password = input("Nuova password (vuoto per mantenere): ")

            updated = manager.update_entry(site, username or None, password or None)

            if updated:

                print("Entry aggiornata!")

            else:

                print("Sito non trovato.")


        elif choice == "6":

            site = input("Nome sito da eliminare: ")

            if manager.delete_entry(site):

                print("Entry eliminata!")

            else:

                print("Sito non trovato.")


        elif choice == "7":

            print("Arrivederci!")

            break

        else:

            print("Opzione non valida!")


if __name__ == "__main__":
    main()
