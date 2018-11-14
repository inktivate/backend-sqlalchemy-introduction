from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from rdbms.models.users import user_model
from rdbms.models.accounts import account_model
from rdbms.models.addresses import address_model
from rdbms.models.education import education_model
from dotenv import load_dotenv
from mimesis import Person, Internet, Address, Datetime, Business
import os
import random
import string

account_id = 0
address_id = 0
education_id = 0


def main():
    session = establish_session()
    create_data(session)
    session.commit()


def establish_session():
    load_dotenv('./.env')
    engine = create_engine(os.environ['DATABASE'], echo=True)
    connection = engine.connect()
    Session = sessionmaker(bind=connection)
    session = Session()
    return session


def create_data(session):
    for i in range(50):
        generate_user(session, i)
        for y in range(10):
            generate_account(session, i)
            generate_address(session, i)
            generate_education(session, i)


def generate_user(session, user_id):
    person = Person('en')
    new_user = user_model(
        id=user_id,
        username=(
            person.name().lower() +
            person.surname().lower() +
            str(random.randint(00, 99))
        ),
        password=generate_password(),
        email=person.email()
    )
    session.add(new_user)


def generate_password():
    length = 13
    chars = string.ascii_letters + string.digits + '!@#$%^&*()'
    random.seed = (os.urandom(1024))
    return ''.join(random.choice(chars) for i in range(length))


def generate_account(session, user_id):
    global account_id
    new_internet = Internet('en')
    new_account = account_model(
        id=account_id,
        user_id=user_id,
        social_media_url=new_internet.home_page()
    )
    session.add(new_account)
    account_id += 1


def generate_address(session, user_id):
    global address_id
    address = Address('en')
    datetime = Datetime('en')
    new_address = address_model(
        id=address_id,
        user_id=user_id,
        street_address='%s %s %s' % (
            address.street_number(),
            address.street_name(),
            address.street_suffix()
        ),
        street_address_two='%s %s %s' % (
            address.street_number(),
            address.street_name(),
            address.street_suffix()
        ),
        city=address.city(),
        state=address.state(),
        postal_code=address.postal_code(),
        country=address.country(),
        start_date=datetime.datetime(),
        end_date=datetime.datetime()
    )
    session.add(new_address)
    address_id += 1


def generate_education(session, user_id):
    global education_id
    business = Business('en')
    datetime = Datetime('en')
    new_education = education_model(
        id=education_id,
        user_id=user_id,
        school=business.company(),
        start_date=datetime.datetime(),
        end_date=datetime.datetime(),
        graduated=random.choice([True, False]),
        gpa=float(random.randint(20, 50))/10
    )
    session.add(new_education)
    education_id += 1


if __name__ == '__main__':
    main()
