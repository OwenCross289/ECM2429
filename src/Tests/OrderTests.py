import pytest
import os
from Models.Order import Order
from Models.Item import Item

def test_given_an_order_when_the_id_is_changed_then_the_order_id_is_correct():
    #Arrange
    item = Item(1, "Item Name", 22.22, 1, 66)
    order = Order(1, "Customer Name", "10 Address Road", "GL2 9RB", "Customer@gmail.com", item, "Ready")
    #Act
    order.order_id = 2
    #assert
    assert order.order_id == 2

def test_given_an_order_when_the_customer_name_is_changed_then_the_customer_name_is_correct():
    #Arrange
    item = Item(1, "Item Name", 22.22, 1, 66)
    order = Order(1, "Customer Name", "10 Address Road", "GL2 9RB", "Customer@gmail.com", item, "Ready")
    #Act
    order.customer_name = "Hello"
    #assert
    assert order.customer_name == "Hello"

def test_given_an_order_when_the_customer_address_is_changed_then_the_customer_address_is_correct():
    #Arrange
    item = Item(1, "Item Name", 22.22, 1, 66)
    order = Order(1, "Customer Name", "10 Address Road", "GL2 9RB", "Customer@gmail.com", item, "Ready")
    #Act
    order.customer_address = "11 Address Road"
    #assert
    assert order.customer_address == "11 Address Road"

def test_given_an_order_when_the_post_code_is_changed_then_the_post_code_is_correct():
    #Arrange
    item = Item(1, "Item Name", 22.22, 1, 66)
    order = Order(1, "Customer Name", "10 Address Road", "GL2 9RB", "Customer@gmail.com", item, "Ready")
    #Act
    order.post_code = "GL7 8RB"
    #assert
    assert order.post_code == "GL7 8RB"

def test_given_an_order_when_the_email_is_changed_then_the_email_is_correct():
    #Arrange
    item = Item(1, "Item Name", 22.22, 1, 66)
    order = Order(1, "Customer Name", "10 Address Road", "GL2 9RB", "Customer@gmail.com", item, "Ready")
    #Act
    order.email = "Customer7@Gmail.com"
    #assert
    assert order.email == "Customer7@Gmail.com"

def test_given_an_order_when_the_item_is_changed_then_the_item_is_correct():
    #Arrange
    item = Item(1, "Item Name", 22.22, 1, 66)
    order = Order(1, "Customer Name", "10 Address Road", "GL2 9RB", "Customer@gmail.com", item, "Ready")
    #Act
    item2 = Item(7, "Item 33", 40.75, 8, 76)
    order.item = item2
    #assert
    assert order.item == item2

def test_given_an_order_when_the_status_is_changed_then_the_status_is_correct():
    #Arrange
    item = Item(1, "Item Name", 22.22, 1, 66)
    order = Order(1, "Customer Name", "10 Address Road", "GL2 9RB", "Customer@gmail.com", item, "Ready")
    #Act
    order.Status = "Shipping"
    #assert
    assert order.Status == "Shipping"

def test_given_an_order_when_print_pdf_is_called_then_a_pdf_is_created():
    #Arrange
    item = Item(1, "Item Name", 22.22, 1, 66)
    order = Order(1, "Customer Name", "10 Address Road", "GL2 9RB", "Customer@gmail.com", item, "Ready")
    #Act
    order.print_pdf(os.path.expanduser("~"))
    #assert
    assert os.path.isfile(f'{os.path.expanduser("~")}/Customer Name1.pdf')
    os.remove(f'{os.path.expanduser("~")}/Customer Name1.pdf')
