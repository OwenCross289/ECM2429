class Email:

    def __init__(self, addresser: str, body: str, sign_off: str):
        '''Data represnation of a item
        :param addresser: str: adresser of the email e.g. `Dear, Hi, etc
        :param body: str: Body of the email
        :param sign_off: float: Sign off of email e.g 'Many Thanks'
        '''
        self.addresser = addresser
        self.body = body
        self.sign_off = sign_off
        self.to_send = ""
        self.update_full_email()
    
    def update_full_email(self, customer_name = "Customer", order_status = "Ready"):
        '''Updates to send with values passed in
        :param customer_name: str: Name of customer to be added into the full email to send
        :param order_status: float: Status of order to be added into the full email to send
        '''
        self.to_send = f"{self.addresser} {customer_name}, \n\nYour Order has been moved to status '{order_status}' \n\n {self.body}\n\n {self.sign_off}\n ECM2429 Team"
    
    def send(self, email):
        print(f"sent to {email}\n\n {self.to_send}")