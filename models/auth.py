from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Table, ForeignKey
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from models.db import Base, session

class BaseModels:
    is_delete = Column(Boolean, default=False)  #逻辑删除
    update_time = Column(DateTime, default=datetime.now) #修改时间
    create_time = Column(DateTime, default=datetime.now)  # 创建时间


class User(Base, BaseModels):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(30), nullable=False, unique=True)
    password = Column(String(200), nullable=False)
    activation = Column(Boolean, default=False) #激活
    email = Column(String(100))
    phone = Column(String(30))

    @classmethod
    def add_user(cls, username, password, **kwargs):
        user = User(username=username, password=password, **kwargs)
        session.add(user) #添加到缓存
        session.commit()  #提交
        session.close()

    @classmethod  #cls代表User,判断数据库内用户是否唯一
    def check_username(cls, username):
        return session.query(cls).filter_by(username=username).first()

    def __repr__(self):
        return "User:username=%s,password=%s" % (self.username, self.password)




class Post(Base, BaseModels):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    image_url = Column(String(300))

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", backref="posts", uselist=False, cascade="all")

    def __repr__(self):
        return "Post:user_id=%s" % self.user_id

    @classmethod
    def add_post(cls, image_url, username):
        user = User.check_username(username)  # 返回user实例
        post = Post(image_url=image_url, user_id=user.id)
        session.add(post)
        session.commit()
        session.close()


# backref="posts"原理如下
#图片实例.user===>拿到对应的user实例
#用户实例.posts===>拿到对应的posts（图片）实例