#! /usr/bin/python

import holder_pb2
import sys
from faker import Faker

class WriteCardHolder:
    # This function fills in a Person message based on user input.
    def PromptForAddress(self,card_holder):
        fake = Faker()
        card_holder.name = fake.name()
        card_holder.job = fake.job()
        card_holder.phone_number = fake.phone_number()
        card_holder.address = fake.address()
        card_holder.card_number = fake.credit_card_number()
        card_holder.card_provider = fake.credit_card_provider()
        return card_holder

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
    write_card_holder = WriteCardHolder()
    card_holder = holder_pb2.CardHolder()
    a = write_card_holder.PromptForAddress(card_holder.add())
    serialize_a = a.SerializeToString()
    read_card_holder = ReadCardHolder()
    read_card_holder.card_holder.ParseFromString(serialize_a)
    read_card_holder.ListPeople()