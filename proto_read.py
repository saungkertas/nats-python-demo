#! /usr/bin/python

import holder_pb2
import sys

# Iterates though all people in the AddressBook and prints info about them.
class ReadCardHolder:
    def __init__(self):
        self.card_holder_book = holder_pb2.CardHolderBook()

    def ListPeople(self):
        for card_holder in self.card_holder_book.card_holders:
            print("Name:", card_holder.name)
            print("Job:", card_holder.job)
            print("Phone Number:", card_holder.phone_number)
            print("Address:", card_holder.address)
            print("Card Number:", card_holder.card_number)
            print("Card Provider:", card_holder.card_provider)
    
if __name__ == "__main__":
    read_card_holder = ReadCardHolder()
    a = b'\n\x9b\x01\n\x0fNicholas Rivera\x12\x17Clinical cytogeneticist\x1a\n7523889213"409558 Brooks Fields Suite 354\nJasonchester, TX 39801*\x1035243937086347792\x1bDiners Club / Carte Blanche'
    read_card_holder.card_holder_book.ParseFromString(a)
    read_card_holder.ListPeople()
    # card_holder_book = holder_pb2.CardHolderBook()

    # # Read the existing address book.
    # f = open(sys.argv[1], "rb")
    # card_holder_book.ParseFromString(f.read())
    # f.close()

    # #ListPeople(card_holder_book)
