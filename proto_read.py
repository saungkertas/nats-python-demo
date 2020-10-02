#! /usr/bin/python

import holder_pb2
import sys

# Iterates though all people in the AddressBook and prints info about them.
class ReadCardHolder:
    def __init__(self):
        self.card_holder = holder_pb2.CardHolder()

    def ListPeople(self):
        print("Name:", card_holder.name)
        print("Job:", card_holder.job)
        print("Phone Number:", card_holder.phone_number)
        print("Address:", card_holder.address)
        print("Card Number:", card_holder.card_number)
        print("Card Provider:", card_holder.card_provider)
    
if __name__ == "__main__":
    read_card_holder = ReadCardHolder()
    f = open("records.txt", "rb")
    a = f.read()
    read_card_holder.card_holder.ParseFromString(a)
    read_card_holder.ListPeople()