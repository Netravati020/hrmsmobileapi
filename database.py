from sqlalchemy import *
# from msilib import Table
# from sqlalchemy.orm import pwiz
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import insert
import pymysql
from sqlalchemy.ext.declarative import declarative_base

sql_database_url= "mysql+pymysql://root@localhost:3360/hrms_am"
engine= create_engine(sql_database_url)
SessionLocal= sessionmaker(autocommit=False,autoflush=False, bind=engine)
conn=engine.connect()
Base= declarative_base()
# Base.prepare(autoload_with=engine)
print("connected")
metadata=MetaData(bind=engine)

