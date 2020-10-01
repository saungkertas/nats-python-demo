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

if __name__ == "__main__":
    write_card_holder = WriteCardHolder()
    card_holder_book = holder_pb2.CardHolderBook()
    # Add an address.
    
    f = open("records.txt", "ab")
    for x in range(1):
        a = write_card_holder.PromptForAddress(card_holder_book.card_holders.add())
        # f.write(a.SerializeToString().decode())
        f.write(a.SerializeToString())
    f.close()
    # Write the new address book back to disk.
    # f = open(sys.argv[1], "wb")
    # f.write(card_holder_book.SerializeToString())
    # f.close()
