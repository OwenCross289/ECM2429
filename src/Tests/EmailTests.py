import pytest
from Models.Email import Email


def test_given_an_email_when_initialised_then_the_values_are_correct():
    #Arrange #Act
    email = Email("Dear", "I hope you are well", "Many Thanks")
    
    #assert
    assert email.addresser == "Dear"
    assert email.body == "I hope you are well"
    assert email.sign_off == "Many Thanks"
    assert email.to_send == "Dear Customer,\n\nYour Order has been moved to status 'Ready'\n\n I hope you are well\n\nMany Thanks,\nECM2429 Team"

def test_given_an_email_when_the_addresser_is_changed_then_the_email_addresser_is_correct():
    #Arrange
    email = Email("Dear", "I hope you are well", "Many Thanks")
    #Act
    email.addresser = "Hi"
    #assert
    assert email.addresser == "Hi"

def test_given_an_email_when_the_body_is_changed_then_the_email_email_is_correct():
    #Arrange
    email = Email("Dear", "I hope you are well", "Many Thanks")
    #Act
    email.body = "You're great!"
    #assert
    assert email.body == "You're great!"

def test_given_an_email_when_the_sign_off_is_changed_then_the_email_sign_off_is_correct():
    #Arrange
    email = Email("Dear", "I hope you are well", "Many Thanks")
    #Act
    email.sign_off = "Thanks"
    #assert
    assert email.sign_off == "Thanks"

def test_given_an_email_when_update_full_email_is_called_then_the_to_send_is_correct():
    #Arrange #Act
    email = Email("Dear", "I hope you are well", "Many Thanks")
    
    #act 
    email.update_full_email("Test", "Shipping")
    #assert
    assert email.to_send == "Dear Test,\n\nYour Order has been moved to status 'Shipping'\n\n I hope you are well\n\nMany Thanks,\nECM2429 Team"

def test_given_an_email_when_send_email_is_called_then_the_correct_string_is_returned():
    #Arrange #Act
    email = Email("Dear", "I hope you are well", "Many Thanks")
    
    #act 
    email.update_full_email("Test", "Shipping")
    actual = email.send("Test@Gmail.com")
    #assert
    assert actual == "Email with contents \n\n'Dear Test,\n\nYour Order has been moved to status 'Shipping'\n\n I hope you are well\n\nMany Thanks,\nECM2429 Team'\n\nSent to Test@Gmail.com"