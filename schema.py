from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Float, String, Date


Base = declarative_base()


class Companymaster(Base):
    __tablename__ = 'companymaster'

    CORPORATE_IDENTIFICATION_NUMBER = Column(String(30), primary_key=True)
    COMPANY_NAME = Column(String(150))
    COMPANY_STATUS = Column(String(50))
    COMPANY_CLASS = Column(String(50))
    COMPANY_CATEGORY = Column(String(50))
    COMPANY_SUB_CATEGORY = Column(String(50))
    DATE_OF_REGISTRATION = Column(Date)
    REGISTERED_STATE = Column(String(50))
    AUTHORIZED_CAP = Column(Float)
    PAIDUP_CAPITAL = Column(Float)
    INDUSTRIAL_CLASS = Column(String)
    PRINCIPAL_BUSINESS_ACTIVITY_AS_PER_CIN = Column(String)
    REGISTERED_OFFICE_ADDRESS = Column(String)
    REGISTRAR_OF_COMPANIES = Column(String)
    EMAIL_ADDR = Column(String(50))
