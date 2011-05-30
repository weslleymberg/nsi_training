#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Ball(object):

    def __init__(self, size, color):
        self.size = size
        self.color = color


class Square(object):

    def __init__(self, side):
        self.side = side

    def square(self):
        return self.side ** 2


class Rectangle(object):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def perimeter(self):
        return 2 * (self.base + self.height)

    def area(self):
        return self.base * self.height


class Person(object):

    def __init__(self, age, weight, height):
        self.age = age
        self.weight = weight
        self.height = height

    def get_old(self, new_age):
        while new_age - self.age > 0:
            if new_age > self.age:
                if self.age < 21:
                    self.height += 15
                self.age = new_age
            new_age -= 1


class TV(object):

    def __init__(self):
        self.status = False
        self.channels = (3, 25)
        self.current_channel = 3
        self.volume = (0, 100)
        self.current_volume = 0

    def change_channel(self, new_channel):
        self.current_channel = self.channels[1]
        if new_channel < self.channels[0]:
            self.current_channel = self.channels[0]
        if new_channel >= self.channels[0] and new_channel <= self.channels[1]:
            self.current_channel = new_channel

    def change_volume(self, new_volume):
        self.current_volume = self.volume[1]
        if new_volume < self.volume[0]:
            self.current_volume = self.volume[0]
        if new_volume >= self.volume[0] and new_volume <= self.volume[1]:
            self.current_volume = new_volume


class BankAccount(object):

    def __init__(self, name, account_number):
        self.client_name = name
        self.account_number = account_number
        self.average_credit = 0

    def deposit(self, value):
        self.average_credit += value

    def draw(self, value):
        self.average_credit -= value

    def report(self):
        return self.client_name, self.account_number, self.average_credit


class GasStation(object):

    def __init__(self, capacity, price_per_liter):
        self.maximum_capacity = capacity
        self.current_state = capacity
        self.price_per_liter = price_per_liter

    def supply(self, value):
        if type(value) == int:
            if value <= self.current_state:
                price = value * self.price_per_liter
                self.current_state -= value
                return price
            return "The pump only contains %i liters" % self.current_state
        elif type(value) == float:
            if int(value / self.price_per_liter) <= self.current_state:
                fuel = int(value / self.price_per_liter)
                self.current_state -= fuel
                return fuel
            return "The pump only contains $i liters" % self.current_state
        return "Invalid Input"

    def refuel(self):
        self.current_state = self.maximum_capacity


class GeometricShape(object):
    pass


class Carnivorous(object):

    def __init__(self):
        self.stomach = []

    def eat(self, feed):
        self.stomach.append(feed)

    def digest(self):
        self.stomach.remove(self.stomach[0])


class ComplexNumber(object):

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __repr__(self):
        return '%s + %si' % (self.real, self.imaginary)

    def __eq__(self, _object):
        return self.real == _object.real and self.imaginary == _object.imaginary

    def __add__(self, _object):
        sum_real = self.real + _object.real
        sum_imaginary = self.imaginary + _object.imaginary
        return ComplexNumber(sum_real, sum_imaginary)

    def __sub__(self, _object):
        subtraction_real = self.real - _object.real
        subtraction_imaginary = self.imaginary - _object.imaginary
        return ComplexNumber(subtraction_real, subtraction_imaginary)

    def __mul__(self, _object):
        multiplication_real = (self.real * _object.real - self.imaginary * _object.imaginary)
        multiplication_imaginary = (self.imaginary * _object.real + self.real * _object.imaginary)
        return ComplexNumber(multiplication_real, multiplication_imaginary)

    def __div__(self, _object):
        division_real = ((self.real * _object.real + self.imaginary * _object.imaginary) / float(_object.real ** 2 + _object.imaginary ** 2))
        division_imaginary = ((self.imaginary * _object.real - self.real * _object.imaginary) / float(_object.real ** 2 + _object.imaginary ** 2))
        return ComplexNumber(division_real, division_imaginary)
