'''Banking classes implementation'''
#!/usr/bin/env python3

from abc import ABC, abstractmethod
import pytest


class Address:
    '''Address class'''
    def __init__(self, street_init: str, city_init: str, state_init: str, zip_init: str):
        '''__init__'''
        self._street = street_init
        self._city = city_init
        self._state = state_init
        self._zip = zip_init

    @property
    def street(self):
        return self._street
    
    @property
    def city(self):
        return self._city

    @property
    def state(self):
        return self._state

    @property
    def zip(self):
        return self._zip

    def __eq__(self, other: object):
        '''Compare 2 addresses'''
        if self._street == other._street and self._city == other._city and self._state == other._state and self._zip == other._zip:
            return True
        else:
            return False

    def __str__(self):
        '''__str method'''
        return "{}\n{}, {} {}".format(self._street, self._city, self._state, self._zip)


class Customer:
    '''Customer class'''
    def __init__(self, name_init: str, dob_init: str, address_init: object):
        '''Constructor'''
        self._name = name_init
        self._dob = dob_init
        self._address = address_init
    @property
    def name(self):
        return self._name

    @property
    def dob(self):
        return self._dob 

    @property
    def address(self):
        return self._address

    def move(self, new_address: object):
        '''Change address'''
        self._address = new_address
        

    def __str__(self):
        '''__str'''
        return "{}".format(self._name) + " (" + "{}".format(self._dob) + ")" + "\n" + "{}".format(self._address.street) + "\n" \
                                + "{}".format(self._address.city) + ", " + "{}".format(self._address.state) + " " + "{}".format(self._address.zip)


class Account(ABC):
    '''Account class'''
    @abstractmethod
    def __init__(self, owner_init: object, balance_init: float=0):
        '''Constructor'''
        self._owner = owner_init
        self._balance = balance_init

    # TODO: Implement data members as properties

    def deposit(self, amount: float):
        '''Add money'''
        if amount > 0:
            self._balance = self._balance + amount
        else:
            raise ValueError('Must deposit positive amount')
    def close(self):
        '''Close account'''
        self._balance = 0

    def __str__(self):
        '''__str__'''
        pass


class CheckingAccount(Account):
    '''CheckingAccount class'''
    def __init__(self, owner_init: object, fee_init: float, balance_init: float=0):
        '''Constructor'''
        super().__init__(owner_init, balance_init)
        self._insufficient_funds_fee = fee_init

    @property
    def balance(self):
        return self._balance
    @property
    def owner(self):
        return self._owner
    
    def process_check(self, amount: float):
        '''Process a check'''
        if amount > self._balance:
            self._balance = self._balance - self._insufficient_funds_fee
        
        else:
            self._balance = self._balance - amount

    def __str__(self):
        '''__str__'''
        result = "Checking account\n" + "Owner: {} ({})\n".format(self._owner.name,self._owner.dob) + \
                self._owner.address.street + "\n" + self._owner.address.city + "," + " " + \
                self._owner.address.state + " " + self._owner.address.zip + "\n" + "Balance: " + format(self._balance, '.2f')
        return result

class SavingsAccount(Account):
    '''CheckingAccount class'''
    def __init__(self, owner_init: object, interest_rate_init: float, balance_init: float=0):
        '''Constructor'''
        super().__init__(owner_init, balance_init)
        self._annual_interest_rate = interest_rate_init
    
    @property
    def balance(self):
        return self._balance
    
    @property
    def owner(self):
        return self._owner

    def yield_interest(self):
        '''Yield annual interest'''
        self._balance = self._balance + self._balance * (self._annual_interest_rate/100)
        return self._balance

    def __str__(self):
        '''__str__'''
        result = "Savings account\n" + "Owner: {} ({})\n".format(self._owner.name,self._owner.dob) + \
                self._owner.address.street + "\n" + self._owner.address.city + "," + " " + \
                self._owner.address.state + " " + self._owner.address.zip + "\n" + "Balance: " + format(self._balance, '.2f')
        return result

