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

    def GetRowToInsert(self):
        row_to_insert = {
            "name": self.card_holder.name,
            "job": self.card_holder.job,
            "phone_number": self.card_holder.phone_number,
            "address": self.card_holder.address,
            "card_number": self.card_holder.card_number,
            "card_provider": self.card_holder.card_provider
        }
        return row_to_insert
    
if __name__ == "__main__":
    read_card_holder = ReadCardHolder()
    print('============')
    f = open("records.txt", "rb")
    a = f.read()
    b = a.split(b';')
    for c in b:
        read_card_holder.card_holder.ParseFromString(c)
        read_card_holder.ListPeople()
