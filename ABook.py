from collections import UserDict


class Field:
    pass


class Name(Field):
    def __init__(self, name) -> None:
        self.value = name

    def __str__(self):
        return str(self.value)


class Phone(Field):
    def __init__(self, phone) -> None:
        self.value = phone

    def __repr__(self):
        return str(self.value)


class Record:
    def __init__(self, name: Name, phone=None) -> None:
        self.name = Name(name)
        self.phones = None
        if phone:
            self.phones = []
            for number in phone:
                self.phones.append(Phone(number))

    def __repr__(self):
        return f"{self.name}: {self.phones}"

    def add_phone(self, phone):
        if self.phones:
            return self.phones.append(phone)
        else:
            self.phones = []
            return self.phones.append(phone)

    def change_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                return f"Phone '{old_phone}' is changed"
        return f"Phone '{old_phone}' is not in AddressBook. Try again!"

    def remove_phone(self, del_phone):
        for phone in self.phones:
            if phone.value == del_phone:
                self.phones.remove(phone)
                return f"Phone '{del_phone}' is delete"
        return f"Phone '{del_phone}' is not in AddressBook. Try again!"


class ABook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
        return self.data

