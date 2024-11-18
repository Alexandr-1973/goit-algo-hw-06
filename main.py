from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError(f"Invalid phone number: {value}. It must contain exactly 10 digits.")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self,phone):
        self.phones.append(Phone(phone))

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value==old_phone:
                phone.value=new_phone
                return
        raise ValueError(f"Phone number {old_phone} not found")

    def find_phone(self,search_phone):
        for phone in self.phones:
            if phone.value == search_phone:
                return search_phone
        return None

    def remove_phone(self,deleted_phone):
        self.phones = [phone for phone in self.phones if phone.value != deleted_phone]

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def __str__(self):
        return "\n".join(str(self.data.get(name)) for name in self.data.keys())

    def add_record(self,record):
        self.data.update({f"{record.name.value}":record})

    def find(self,name):
        return self.data.get(name) if self.data.get(name) else None

    def delete(self,name):
        self.data.pop(name)


# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
print(book)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

# Видалення запису Jane
book.delete("Jane")
print(book)

# Видалення запису Jone
john.remove_phone("5555555555")
print(john)

print(book)
