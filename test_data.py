class TestUrls:
    elk = "https://lk.rt.ru/"
    onlime = "https://my.rt.ru/"
    start_web = "https://start.rt.ru/"
    smarthome = "https://lk.smarthome.rt.ru/"
    key_web = "https://key.rt.ru/"
    scandiweb = "https://qatest-dev.indvp.com/"
    vk = "https://vk.com/"
    jquery = "https://jqueryui.com/droppable/"
    flipkart = "https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3DMax"
    asos = "https://www.asos.com/adidas-originals/adidas-originals-oznova-trainers-in-off-white-and-grey/prd/202527704?colourWayId=202527705&cid=1935"
    rediff = "https://mail.rediff.com/cgi-bin/login.cgi"


class TestDataSet:
    test_name = ['9851111111', 'mymail@mail.ru', 'bill_klinton',  '123456789012']
    test_name_ids = ['mobile phone', 'email', 'login', 'personal ID']

    wrong_name = ["", 18, "Щ", "И1", "ч-", "ж_", "Fa", "И@", f'{("Ы" * 31)}']
    wrong_name_ids = ['empty string', '2 digits', 'a Cyrillic consonant',
           'Cyrillic letter with digit', 'Cyrillic letter with hyphen',
           'Cyrillic letter with lower dash', '2 Latin letters',
           'Cyrillic letter and a special key', 'Cyrillic string 31 symbols']

    invalid_phone_or_email = ["", 1, "+1-145-145-11-11", "+7926133111",
                            "+375 12 111-11-0",  f"+7926{('1' * 100)}", f"+375{('1' * 100)}",
                            "myemail@mail", "myemailmail.ru"]
    invalid_phone_or_email_ids = ['empty string', 'single digit', 'US format', 'incomplete Russian number',
                            'incomplete Belarus number', 'too long Russian number', 'too long Belarus number',
                                'incomplete email missing country domain', 'incomplete email missing @']

    invalid_pswd = ["", 1234567, 12345678, "12345678A", "12345678b",
                    "12345678Ъj", "12345678AbCDEfghijklmnopqrstuvwxyz"]
    invalid_pswd_ids = ["empty string", "7 digits", "8 digits", "lower case letter missing", "upper case letter missing",
                        "non-Latin letters", "string over 20 symbols"]


class ScandiLogin:
    user_data = {'firstname': 'Paul', 'lastname': 'Smith', 'email': 'mymail@mail.com', 'password': '12345678J@q'}


class VkCredentials:
    # your valid pass and login should be here
    user_data = {'username': "", "password": ""}
