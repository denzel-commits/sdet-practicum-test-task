import random
import string
from datetime import datetime, timedelta


def get_random_string(length=8):
    return "".join([random.choice(string.ascii_lowercase) for _ in range(length)])


def get_random_number(length=10):
    return "".join([random.choice(string.digits) for _ in range(length)])


def get_random_email(length=8):
    return get_random_string(length) + "@" + get_random_string(length) + random.choice([".com", ".ru", ".net", ".org"])


def get_random_date(start_date, end_date):
    random_days = random.randint(0, (end_date - start_date).days)

    return start_date + timedelta(days=random_days)


def map_user_data(user_data):
    return {
        "Student Name": user_data["firstname"] + " " + user_data["lastname"],
        "Student Email": user_data["email"],
        "Gender": user_data["gender"],
        "Mobile": user_data["mobile"],
        "Date of Birth": datetime(user_data["birthdate"]["year"],
                                  user_data["birthdate"]["month"],
                                  user_data["birthdate"]["date"]).strftime("%d %B,%Y"),
        "Picture": user_data["picture"],
        "Subjects": ", ".join(user_data["subjects"]),
        "Hobbies": ", ".join(user_data["hobbies"]),
        "Address": user_data["address"],
        "State and City": user_data["state"] + " " + user_data["city"]
    }
