import csv
import json
import datetime
from sqlalchemy import create_engine, and_, func, asc, desc, case
from sqlalchemy.orm import sessionmaker
from schema import Base, Companymaster


def load_csv_to_dbtable(session):
    '''
    Load csv file to database table
    '''

    with open('mca_maharashtra.csv', encoding='latin-1') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            if row[6] == '00-01-1900' or row[6] == 'NA':
                continue
            else:
                date = datetime.datetime.strptime(row[6], '%d-%m-%Y').date()
                rowdata = Companymaster(
                    CORPORATE_IDENTIFICATION_NUMBER=row[0],
                    COMPANY_NAME=row[1],
                    COMPANY_STATUS=row[2],
                    COMPANY_CLASS=row[3],
                    COMPANY_CATEGORY=row[4],
                    COMPANY_SUB_CATEGORY=row[5],
                    DATE_OF_REGISTRATION=date,
                    REGISTERED_STATE=row[7],
                    AUTHORIZED_CAP=row[8],
                    PAIDUP_CAPITAL=row[9],
                    INDUSTRIAL_CLASS=row[10],
                    PRINCIPAL_BUSINESS_ACTIVITY_AS_PER_CIN=row[11],
                    REGISTERED_OFFICE_ADDRESS=row[12],
                    REGISTRAR_OF_COMPANIES=row[13],
                    EMAIL_ADDR=row[14])
                session.add(rowdata)
    session.commit()


def auth_data():
    '''
    Plot the first problem auth data from database table
    '''

    authoried_cap = {'<=1L': 0,
                     '1L to 10L': 0,
                     '10L to 1Cr': 0,
                     '1Cr to 10 Cr': 0,
                     '>10Cr': 0}

    auth = case([
        (Companymaster.AUTHORIZED_CAP <= 100000, '<=1L'),
        (and_(
            Companymaster.AUTHORIZED_CAP > 100000,
            Companymaster.AUTHORIZED_CAP <= 1000000), '1L to 10L'),
        (and_(
            Companymaster.AUTHORIZED_CAP > 1000000,
            Companymaster.AUTHORIZED_CAP <= 10000000), '10L to 1Cr'),
        (and_(
            Companymaster.AUTHORIZED_CAP > 10000000,
            Companymaster.AUTHORIZED_CAP <= 100000000), '1Cr to 10 Cr'),
        (Companymaster.AUTHORIZED_CAP > 100000000, '>10Cr')
    ])

    auth_cap = session.query(auth, func.count(
                auth
               )).group_by(auth)

    for auth in auth_cap:
        if auth[0] in authoried_cap:
            authoried_cap[auth[0]] = auth[1]
    return authoried_cap


def company_register_data():
    '''
    Plot the second problem company register data from database table
    '''

    company_register = session.query(
        func.date_part(
         'YEAR', Companymaster.DATE_OF_REGISTRATION),
        func.count(
         func.date_part(
          'YEAR', Companymaster.DATE_OF_REGISTRATION)
            )
          ).group_by(
           func.date_part(
            'YEAR', Companymaster.DATE_OF_REGISTRATION)).order_by(
                asc(func.date_part(
                        'YEAR', Companymaster.DATE_OF_REGISTRATION
                        ))).limit(10). offset(109)

    return dict(company_register)


def business_activity_data():
    '''
    Plot the third problem businss data from database table
    '''

    business_name_data = session.query(
        Companymaster.PRINCIPAL_BUSINESS_ACTIVITY_AS_PER_CIN,
        func.count(
            Companymaster.PRINCIPAL_BUSINESS_ACTIVITY_AS_PER_CIN)).group_by(
            Companymaster.PRINCIPAL_BUSINESS_ACTIVITY_AS_PER_CIN).order_by(
            desc(
             func.count(
                Companymaster.PRINCIPAL_BUSINESS_ACTIVITY_AS_PER_CIN)
               )
            ).limit(10).all()

    return dict(business_name_data)


def stacked_bar_plot():
    '''
    Plot the fourth problem stackbar data from database table
    '''
    years_data = session.query(
        func.date_part(
           'year', Companymaster.DATE_OF_REGISTRATION)).\
        filter(func.date_part(
            'year', Companymaster.DATE_OF_REGISTRATION) > 2000,
        func.date_part(
            'year', Companymaster.DATE_OF_REGISTRATION) < 2011).distinct()
    year = [int(i) for i, in years_data]
    stack_result = {'year': year}

    ploats = session.query(
        Companymaster.PRINCIPAL_BUSINESS_ACTIVITY_AS_PER_CIN,
        func.count(
                Companymaster.PRINCIPAL_BUSINESS_ACTIVITY_AS_PER_CIN)
            ).group_by(
        func.date_part(
            'year', Companymaster.DATE_OF_REGISTRATION),
        Companymaster.PRINCIPAL_BUSINESS_ACTIVITY_AS_PER_CIN
            ).\
        filter(
        func.date_part(
            'year', Companymaster.DATE_OF_REGISTRATION) > 2000,
        func.date_part(
            'year', Companymaster.DATE_OF_REGISTRATION) < 2011,
        Companymaster.PRINCIPAL_BUSINESS_ACTIVITY_AS_PER_CIN.in_([
                    "Business Services",
                    "Community, personal & Social Services",
                    "Finance",
                    "Manufacturing (Food stuffs)",
                    "Trading"

        ])
            )
    for ploat in ploats:
        stack_result[ploat[0]] = stack_result.get(ploat[0], [])
        if ploat[0] in stack_result:
            stack_result[ploat[0]].append(ploat[1])
    return stack_result


if __name__ == '__main__':

    # Create engine for connecting postgresql
    engine = create_engine('postgresql://rakshit:rakshit@localhost/datasetdb')

    Base.metadata.create_all(engine)

    # Create sesstion
    Session = sessionmaker(bind=engine)
    session = Session()

    # Load csv to database method
    load_csv_to_dbtable(session)

    # Store in dictionary
    data = {
        "authoried_cap": auth_data(),
        "company_register": company_register_data(),
        "number_of_company": business_activity_data(),
        "stack_result": stacked_bar_plot()
    }
    # dump data in json file from database table
    json_object = json.dumps(data, indent=4)

    with open("public/data.json", "w") as outfile:
        outfile.write(json_object)
