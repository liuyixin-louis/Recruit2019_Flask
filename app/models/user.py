from flask_sqlalchemy import  SQLAlchemy
import datetime

# 创建SQLAlchemy对象,关联app
db = SQLAlchemy()

# 定义映射类User，其继承上一步创建的Base
class User(db.Model):
    # 指定本类映射到users表
    __tablename__ = 'users'

    # 指定id映射到id字段; id字段为整型，为主键
    id = db.Column(db.Integer(), primary_key=True)
    # 指定name映射到name字段; name字段为字符串类形，
    name = db.Column(db.String(20))
    gender = db.Column(db.String(32))
    campus = db.Column(db.String(32))
    grade = db.Column(db.String(32))
    college = db.Column(db.String(32))
    major = db.Column(db.String(32))
    address = db.Column(db.String(32))
    phone = db.Column(db.String(32))
    email = db.Column(db.String(32))
    first_choice = db.Column(db.String(32))
    second_choice = db.Column(db.String(32))
    introduction = db.Column(db.String(1000))
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    state = db.Column(db.BOOLEAN)

    # def __repr__(self):
    #     return "<User(name='%s', gender='%s', grade='%s', college='%s', major='%s', address='%s', phone='%s', " \
    #            "email='%s', first_choice='%s',second_choice='%s',introduction='%s')>" % (
    #                self.name, self.gender, self.grade, self.college, self.major, self.address, self.phone, self.email,
    #                self.first_choice, self.second_choice, self.introduction)

    def __repr__(self):
        return "User(id='%s',name='%s')" % (self.id, self.name)