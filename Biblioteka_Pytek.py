# -*- coding: cp1250 -*-
class Book:
    # Zmienna klasowa działająca analogicznie do statycznej listy w C#
    zbiory = []

    def __init__(self, title, author):
        self.id = len(Book.zbiory)
        self.tytul = title
        self.autor = author
        self.wypozyczona = False # Domyślnie dodawana książka nie jest wypożyczona

    @staticmethod
    def dodajKsiazke(title, author):
        nowa = Book(title, author)
        Book.zbiory.append(nowa)

    @staticmethod
    def wyswietlKsiazki():
        print("\n\n=== Dostępne książki ===")
        for i, ksiazka in enumerate(Book.zbiory):
            if ksiazka is not None:
                status = "Wypożyczona" if ksiazka.wypozyczona else "Dostępna"
                print(f"{i}. {ksiazka.tytul} - {ksiazka.autor} - ID Książki: {i} [{status}]")


class Person:
    # Zmienna klasowa działająca analogicznie do statycznej listy w C#
    klienci = []

    def __init__(self, name):
        self.imieNazwisko = name
        self.wypozyczone = []

    @staticmethod
    def nowyKlient(name):
        nowy = Person(name)
        Person.klienci.append(nowy)
        print(f"Dodano nowego klienta: {name}")

    @staticmethod
    def wypozyczKsiazke(pozyczajacy, idKsiazki):
        if len(pozyczajacy.wypozyczone) < 10:
            pozyczajacy.wypozyczone.append(Book.zbiory[idKsiazki])
            Book.zbiory[idKsiazki].wypozyczona = True # Oznaczamy książkę jako wypożyczoną
        else:
            print("Nie można wypożyczyć więcej niż 10 książek.")

    def zwrocKsiazke(self, zwracajacy, idKsiazki):
        ksiazka = Book.zbiory[idKsiazki]
        if ksiazka in zwracajacy.wypozyczone:
            zwracajacy.wypozyczone.remove(ksiazka)
            ksiazka.wypozyczona = False # Oznaczamy książkę jako dostępna
        else:
            print("Ta książka nie jest wypożyczona przez tego klienta.")

    @staticmethod
    def wyswietlWypozyczone(id):
        klient = Person.klienci[id]
        print(f"\n\n=== Wypożyczone książki przez {klient.imieNazwisko} ===")
        for i, ksiazka in enumerate(klient.wypozyczone):
            idKsiazki = Book.zbiory.index(ksiazka)
            print(f"{i+1}. {ksiazka.tytul} - {ksiazka.autor} - ID Książki: {idKsiazki}")

    @staticmethod
    def wyswietlKlientow():
        print("\n\n=== Wypożyczający ===")
        for i, klient in enumerate(Person.klienci):
            print(f"{i}. {klient.imieNazwisko}")


def populator():
    # Funkcja, aby nie trzeba było przy każdym odpaleniu "z palca" populować
    Person.nowyKlient("Spejson")
    Person.nowyKlient("Wojtas")
    Person.nowyKlient("KubaC")
    Person.nowyKlient("Bibliotekarz")
    
    Book.dodajKsiazke("Chlopi", "Reymont")
    Person.wypozyczKsiazke(Person.klienci[0], 0)
    
    Book.dodajKsiazke("Ogniem i Mieczem", "Sienkiewicz")
    Person.wypozyczKsiazke(Person.klienci[0], 1)
    
    Book.dodajKsiazke("Naprawa Poloneza", "FSO")
    Person.wypozyczKsiazke(Person.klienci[1], 2)
    
    Book.dodajKsiazke("Jak zdac cwiczenia z PPO?", "Praca zbiorowa studentow")
    Person.wypozyczKsiazke(Person.klienci[2], 3)
    
    Book.dodajKsiazke("C# dla opornych", "Jakiś Programista")


def menu():
    print("\n\n=== Biblioteka => Projekt Jakuba Czerwika ===")
    print("Co chcesz zrobic?")
    print("1. Dodaj nowego Uzytkownika")
    print("2. Wypożycz/zwróć książkę")
    print("3. Raporty")
    print("4. Zakoncz program")
    
    wybor_str = input()
    try:
        wybor = int(wybor_str)
        if wybor >= 5:
            wybor = 0
    except ValueError:
        wybor = 0 # Niepoprawny wybór, ustawiamy na 0, aby nie było wyjątku
        
    return wybor


def main():
    populator()
    opcja = 0
    
    while opcja != 4:
        opcja = menu()
        
        if opcja == 1:
            print("Podaj imię i nazwisko nowego klienta")
            Person.nowyKlient(input())
            
        elif opcja == 2:
            print("Naciśnij 1 aby wypożyczyć książkę lub dowolny inny klawisz żeby ją zwrócić")
            wypozyczZwroc = input()
            
            if wypozyczZwroc == "1":
                Person.wyswietlKlientow()
                print("Podaj id klienta")
                idKlienta = int(input())
                print("Podaj id książki")
                Book.wyswietlKsiazki()
                idKsiazki = int(input())
                Person.wypozyczKsiazke(Person.klienci[idKlienta], idKsiazki)
            else:
                Person.wyswietlKlientow()
                print("Podaj id klienta")
                idKlienta = int(input())
                Person.wyswietlWypozyczone(idKlienta)
                print("Podaj id książki")
                idKsiazki = int(input())
                Person.klienci[idKlienta].zwrocKsiazke(Person.klienci[idKlienta], idKsiazki)
                
        elif opcja == 3:
            print("Naciśnij 1 aby zobaczyć raport dostępnych książek lub dowolny inny klawisz żeby zobaczyć raport wypożyczeń klienta")
            raport = input()
            
            if raport == "1":
                Book.wyswietlKsiazki()
            else:
                Person.wyswietlKlientow()
                id_do_raportu = int(input()) 
                Person.wyswietlWypozyczone(id_do_raportu)
                
        elif opcja == 4:
            pass # Pętla zakończy się po tym kroku
            
        else:
            print("Niepoprawna opcja, spróbuj ponownie.")


if __name__ == "__main__":
    main()
