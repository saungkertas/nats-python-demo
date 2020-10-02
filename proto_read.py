#! /usr/bin/python

import holder_pb2
import sys

# Iterates though all people in the AddressBook and prints info about them.
class ReadCardHolder:
    def __init__(self):
        self.card_holder = holder_pb2.CardHolder()

    def ListPeople(self):
        print("Name:", self.card_holder.name)
        print("Job:", self.card_holder.job)
        print("Phone Number:", self.card_holder.phone_number)
        print("Address:", self.card_holder.address)
        print("Card Number:", self.card_holder.card_number)
        print("Card Provider:", self.card_holder.card_provider)
    
if __name__ == "__main__":
    read_card_holder = ReadCardHolder()
    f = open("records.txt", "rb")
    a = f.read()
    print(a)
    read_card_holder.card_holder.ParseFromString(a)
    read_card_holder.ListPeople()
    print('============')
    f = open("records2.txt", "rb")
    a = f.read()
    b = a.split(b';')
    for c in b:
        print(c)
        read_card_holder.card_holder.ParseFromString(c)
        read_card_holder.ListPeople()
