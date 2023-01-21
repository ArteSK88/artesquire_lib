import random


class TestUrls:
    scandiweb = "https://qatest-dev.indvp.com/"


class ScandiLogin:
    user_data = [{'firstname': 'Paul', 'lastname': 'Smith', 'email': f'{random.randint(500, 10000)}@mail.com', 'password': '123',
                 'confirming_password': '123', 'ER': 'Password should be at least 8 characters long',
                 'ids': 'too short password'},
                 {'firstname': 'Paul', 'lastname': '', 'email': f'{random.randint(500, 10000)}@mail.com', 'password': '12345678J@q',
                 'confirming_password': '12345678J@q', 'ER': 'This field is required!',
                 'ids': 'empty last name'},
                 {'firstname': 'Paul', 'lastname': 'Smith', 'email': f'{random.randint(500, 10000)}@mail.com', 'password': '12345678J@q',
                 'confirming_password': '12345678J@qA', 'ER': 'Passwords do not match',
                 'ids': 'mismatching passwords'},
                 {'firstname': '$', 'lastname': 'Smith', 'email': f'{random.randint(500, 10000)}@mail.com', 'password': '12345678J@q',
                 'confirming_password': '12345678J@qA', 'ER': 'Invalid input. Please, try again',
                 'ids': 'special character as firstname'},
                 {'firstname': 'Paul', 'lastname': '$', 'email': f'{random.randint(500, 10000)}@mail.com', 'password': '12345678J@q',
                  'confirming_password': '12345678J@qA', 'ER': 'Invalid input. Please, try again',
                  'ids': 'special character as lastname'}]
