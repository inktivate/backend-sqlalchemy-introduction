from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from rdbms.models.users import user_model
from rdbms.models.accounts import account_model
from rdbms.models.addresses import address_model
from rdbms.models.education import education_model
from rdbms.models.employments import employment_model
from rdbms.models.languages import language_model
from rdbms.models.profiles import profile_model
from rdbms.models.telephones import telephone_model
from rdbms.models.vitals import vital_model
from dotenv import load_dotenv
from mimesis import Person, Address, Datetime, Business
import os
import random

account_id = 0
address_id = 0
education_id = 0
employment_id = 0
language_id = 0
profile_id = 0
telephone_id = 0
vital_id = 0

person = Person('en')
address = Address('en')
business = Business('en')
datetime = Datetime('en')


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
            generate_employment(session, i)
            generate_language(session, i)
            generate_profile(session, i)
            generate_telephone(session, i)
            generate_vital(session, i)


def generate_user(session, user_id):
    new_user = user_model(
        id=user_id,
        username=(
            person.name().lower() +
            person.surname().lower() +
            str(random.randint(00, 99))
        ),
        password=person.password(),
        email=person.email()
    )
    session.add(new_user)


def generate_account(session, user_id):
    global account_id
    new_account = account_model(
        id=account_id,
        user_id=user_id,
        social_media_url=person.social_media_profile()
    )
    session.add(new_account)
    account_id += 1


def generate_address(session, user_id):
    global address_id
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
    new_education = education_model(
        id=education_id,
        user_id=user_id,
        school=person.university(),
        start_date=datetime.datetime(),
        end_date=datetime.datetime(),
        graduated=random.choice([True, False]),
        gpa=float(random.randint(20, 50))/10
    )
    session.add(new_education)
    education_id += 1


def generate_employment(session, user_id):
    global employment_id
    new_employment = employment_model(
        id=employment_id,
        user_id=user_id,
        company=business.company(),
        occupation=person.occupation(),
        start_date=datetime.datetime(),
        end_date=datetime.datetime()
    )
    session.add(new_employment)
    employment_id += 1


def generate_language(session, user_id):
    global language_id
    new_language = language_model(
        id=language_id,
        user_id=user_id,
        language=person.language()
    )
    session.add(new_language)
    language_id += 1


def generate_profile(session, user_id):
    global profile_id
    new_profile = profile_model(
        id=profile_id,
        user_id=user_id,
        nationality=person.nationality()
    )
    session.add(new_profile)
    profile_id += 1


def generate_telephone(session, user_id):
    global telephone_id
    new_telephone = telephone_model(
        id=telephone_id,
        user_id=user_id,
        telephone_number=person.telephone()
    )
    session.add(new_telephone)
    telephone_id += 1


def generate_vital(session, user_id):
    global vital_id
    new_vital = vital_model(
        id=vital_id,
        user_id=user_id,
        height=person.height(),
        weight=person.weight()
    )
    session.add(new_vital)
    vital_id += 1


if __name__ == '__main__':
    main()
