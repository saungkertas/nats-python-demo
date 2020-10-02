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

if __name__ == "__main__":
    write_card_holder = WriteCardHolder()
    card_holder_book = holder_pb2.CardHolder()
    # Add an address.
    
    # f = open("records.txt", "wb")
    # a = write_card_holder.PromptForAddress(card_holder_book)
    # f.write(a.SerializeToString())
    # f.close()  

    f = open("records2.txt", "ab")
    for x in range(10):
        a = write_card_holder.PromptForAddress(card_holder_book)
        f.write(a.SerializeToString())
        f.write(b';')
    f.close()   