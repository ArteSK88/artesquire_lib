import random


class TestUrls:
    scandiweb = "https://qatest-dev.indvp.com/"
    vk = "https://vk.com/"
    jquery = "https://jqueryui.com/droppable/"
    flipkart = "https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3DMax"
    asos = "https://www.asos.com/adidas-originals/adidas-originals-oznova-trainers-in-off-white-and-grey/prd/202527704?colourWayId=202527705&cid=1935"
    rediff = "https://mail.rediff.com/cgi-bin/login.cgi"
    avito = "https://www.avito.ru/all/avtomobili/audi/100-ASgBAgICAkTgtg3elyjitg3gmSg?cd=1"


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


class VkCredentials:
    # your valid pass and login should be here
    user_data = {'username': "", "password": ""}
