from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# 需要安装sqlalchemy和pymysql包
HOSTNAME = '192.168.2.162'
PORT = '3306'
DATABASE = 'instagram'
USERNAME = 'admin'
PASSWORD = 'Root110qwe'

db_url = 'mysql+pymysql://{}:{}@{}/{}?charset=utf8'.format(
    USERNAME,
    PASSWORD,
    HOSTNAME,
    DATABASE
)


engine = create_engine(db_url)  #引擎
Base = declarative_base(engine) #基类

Session = sessionmaker(engine)
session = Session()  #会话

if __name__ == '__main__':
    print(dir(Base))
    print(dir(session))
