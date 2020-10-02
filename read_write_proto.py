#! /usr/bin/python

import holder_pb2
import sys
from faker import Faker

class WriteCardHolder:
    # This function fills in a Person message based on user input.
    def PromptForAddress(self,card_holders):
        fake = Faker()
        card_holders.name = fake.name()
        card_holders.job = fake.job()
        card_holders.phone_number = fake.phone_number()
        card_holders.address = fake.address()
        card_holders.card_number = fake.credit_card_number()
        card_holders.card_provider = fake.credit_card_provider()
        return card_holders

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
    write_card_holder = WriteCardHolder()
    card_holder_book = holder_pb2.CardHolderBook()
    a = write_card_holder.PromptForAddress(card_holder_book.card_holders.add())
    serialize_a = a.SerializeToString()
    read_card_holder = ReadCardHolder()
    read_card_holder.card_holder_book.ParseFromString(serialize_a)
    read_card_holder.ListPeople()