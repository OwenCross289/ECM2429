import pytest
from Models.Item import Item

def test_given_an_item_when_the_id_is_changed_then_the_item_id_is_correct():
    #Arrange
    item = Item(1, "test name", 22.22,1,77)
    #Act
    item.item_id = 2
    #assert
    assert item.item_id == 2

def test_given_an_item_when_the_name_is_changed_then_the_item_name_is_correct():
    #Arrange
    item = Item(1, "test name", 22.22,1,77)
    #Act
    item.name = "Test"
    #assert
    assert item.name == "Test"

def test_given_an_item_when_the_price_is_changed_then_the_item_price_is_correct():
    #Arrange
    item = Item(1, "test name", 22.22,1,77)
    #Act
    item.price = 33.33
    #assert
    assert item.price == 33.33

def test_given_an_item_when_the_location_is_changed_then_the_item_location_is_correct():
    #Arrange
    item = Item(1, "test name", 22.22,1,77)
    #Act
    item.warehouse_location = 2
    #assert
    assert item.warehouse_location == 2

def test_given_an_item_when_the_stock_is_changed_then_the_item_stock_is_correct():
    #Arrange
    item = Item(1, "test name", 22.22,1,77)
    #Act
    item.stock = 70
    #assert
    assert item.stock == 70