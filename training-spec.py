#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from should_dsl import should, should_not
from training import Ball, Square, Rectangle, Person, TV, BankAccount, GasStation, GeometricShape, Carnivorous


class TestBall(unittest.TestCase):

    def setUp(self):
        self.a_ball = Ball(5, "red") #Ball(radius, color)

    def it_creates_a_ball(self):
        self.a_ball |should| be_instance_of(Ball)

    def it_changes_the_size_of_the_ball(self):
        self.a_ball.size = 7
        self.a_ball.size |should| be(7)

    def it_changes_and_check_the_color_of_the_ball(self):
        self.a_ball.color = "blue"
        self.a_ball.color |should| be("blue")


class TestSquare(unittest.TestCase):

    def setUp(self):
        self.a_square = Square(2) #Square(side_weight)

    def it_creates_a_square(self):
        self.a_square |should| be_instance_of(Square)

    def it_changes_and_check_the_side_of_the_square(self):
        self.a_square.side = 3
        self.a_square.side |should| be(3)

    def it_takes_the_square_of_the_side(self):
        self.a_square.side = 5
        self.a_square.square() |should| be(25)


class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.a_rectangle = Rectangle(3, 2) #Rectangle(base, height)

    def it_creates_a_rectangle(self):
        self.a_rectangle |should| be_instance_of(Rectangle)

    def it_changes_the_side_of_the_rectangle(self):
        self.a_rectangle.base = 5
        self.a_rectangle.base |should| be(5)
        self.a_rectangle.height = 4
        self.a_rectangle.height |should| be(4)

    def it_takes_the_perimeter_of_the_rectangle(self):
        self.a_rectangle.base = 6
        self.a_rectangle.height = 4
        self.a_rectangle.perimeter() |should| be(20)

    def it_takes_the_area_of_the_rectangle(self):
        self.a_rectangle.base = 5
        self.a_rectangle.height = 3
        self.a_rectangle.area() |should| be(15)


class TestPerson(unittest.TestCase):

    def setUp(self):
        self.a_person = Person(12, 50, 140) #People(age, weight, height in centimeters)

    def it_creates_a_person(self):
        self.a_person |should| be_instance_of(Person)

    def it_changes_the_weight_of_the_person(self):
        self.a_person.weight = 45
        self.a_person.weight |should| be(45)
        self.a_person.weight = 55
        self.a_person.weight |should| be(55)

    def it_ages_the_person(self):
        self.a_person.get_old(13)
        self.a_person.age |should| be(13)
        self.a_person.height |should| be(155)
        self.a_person.get_old(12)
        self.a_person.age |should| be(13)
        self.a_person.height |should| be(155)


class Testtv(unittest.TestCase):

    def setUp(self):
        self.a_tv = TV()

    def it_creates_a_TV(self):
        self.a_tv |should| be_instance_of(TV)

    def it_changes_the_status(self):
        self.a_tv.status = True
        self.a_tv.status |should| be(True)

    def it_changes_the_channel(self):
        self.a_tv.change_channel(4)
        self.a_tv.current_channel |should| be(4)
        self.a_tv.change_channel(2)
        self.a_tv.current_channel |should| be(3)
        self.a_tv.change_channel(26)
        self.a_tv.current_channel |should| be(25)

    def it_changes_the_volume(self):
        self.a_tv.change_volume(3)
        self.a_tv.current_volume |should| be(3)
        self.a_tv.change_volume(-1)
        self.a_tv.current_volume |should| be(0)
        self.a_tv.change_volume(101)
        self.a_tv.current_volume |should| be(100)


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.an_account = BankAccount("Foo", "1234-5")

    def it_crates_an_account(self):
        self.an_account |should| be_instance_of(BankAccount)

    def it_takes_the_name_of_the_client(self):
        self.an_account.client_name |should| be("Foo")

    def it_takes_the_number_of_the_account(self):
        self.an_account.account_number |should| equal_to("1234-5")

    def it_makes_account_operations(self):
        self.an_account.deposit(100)
        self.an_account.average_credit |should| be(100)
        self.an_account.draw(25)
        self.an_account.average_credit |should| be(75)


class TestGasStation(unittest.TestCase):

    def setUp(self):
        self.a_gas_station = GasStation(100, 2.0)

    def it_creates_a_gas_station(self):
        self.a_gas_station |should| be_instance_of(GasStation)

    def it_verify_the_state_of_the_fuel_pump(self):
        self.a_gas_station.maximum_capacity |should| be(100)
        self.a_gas_station.current_state |should| be(100)
        self.a_gas_station.price_per_liter |should| equal_to(2.0)

    def it_supply_the_vehicle(self):
        self.a_gas_station.supply(10) |should| equal_to(20.0)
        self.a_gas_station.current_state |should| be(90)
        self.a_gas_station.supply(10.0) |should| equal_to(5)
        self.a_gas_station.current_state |should| be(85)
        self.a_gas_station.supply("hi") |should| equal_to("Invalid Input")

    def it_refuel_the_pump(self):
        self.a_gas_station.refuel()
        self.a_gas_station.current_state |should| be(100)


class TestGeometry(unittest.TestCase):
    pass


class TestCarnivorous(unittest.TestCase):

    def setUp(self):
        self.a_carnivorous = Carnivorous()

    def it_creates_a_carnivorous(self):
        self.a_carnivorous |should| be_instance_of(Carnivorous)

    def it_feeds_the_carnivorous(self):
        self.a_carnivorous.eat("s")
        self.a_carnivorous.stomach |should| contain("s")
        self.a_carnivorous.eat(2)
        self.a_carnivorous.stomach |should| contain(2)
        self.a_carnivorous.stomach |should| equal_to(["s", 2])

    def it_digest_the_feed(self):
        self.a_carnivorous.eat("s")
        self.a_carnivorous.eat(2.0)
        self.a_carnivorous.digest()
        self.a_carnivorous.stomach |should_not| contain("s")
        self.a_carnivorous.stomach |should| contain(2.0)
