from flask import Blueprint
from flask import request, jsonify
from app.models import db
from app.models.user import User
from app.utility.log_tool import logger

api_blueprint =Blueprint('api',__name__,static_folder='static')

# api开发

# 增
@api_blueprint.route('/users/add', methods=['POST'])
def user_add():
    """
    添加新报名同学数据
    :return:
    """
    if request.method=='POST':
        # print('post')

        # print('here')
        # print(request.json)
        # for key,value in request.json:
        #     key = value
        # try:
        # 简化版本添加代码

        # 假定前端传来的数据为校验过的：

        #前端js已经保证输入id字段合法：

        id = request.json['id']
        # print(id)
        if User.query.filter(User.id == id).first():
            print('failed')
            return jsonify({'status': '-1', 'errmsg': '添加失败！学号（ID）重复'})
        else:
            new_user = User()
            for k, v in request.json.items():
                if k in dir(User):
                    exec('new_user.{} = v'.format(k))
            new_user.state = 0
            print(User)
            # new_user = User(
            #         name=request.json['name'],
            #         gender=request.json['gender'],
            #         campus=request.json['campus'],
            #         grade=request.json['grade'],
            #         college=request.json['college'],
            #         major=request.json['major'],
            #         address=request.json['address'],
            #         phone=request.json['phone'],
            #         email=request.json['email'],
            #         first_choice=request.json['first_choice'],
            #         second_choice=request.json['second_choice'],
            #         introduction=request.json['introduction'],
            #         state=0
            # )
            db.session.add(new_user)
            db.session.commit()

            print('add user....', new_user)
            logger.info('Add user {} success!'.format(user_add))
            return jsonify({'status': '0', 'errmsg': '添加成功！'})
            # except Exception as err:
                # print(err)
                # logger.error('Delete user failed!Err:{}'.format(err))
                # return jsonify({'status': '-1', 'errmsg': '添加失败！'})


# 改
@api_blueprint.route('/users/edit/<id>/', methods=['PUT'])
def user_edit(id=None):
    """
    对特定报名同学信息进行改
    :return:
    """
    # print('here')

    if request.method == 'PUT':

        # print(type(data))
        # return make_response('')
        # data = request.form['name']
        # name = request.form.get("name")


        # print(name)
        # return jsonify(
        #     data=json.dumps(name),
        #     extra={
        #         'message': 'success'
        #     }
        # )


        import json
        # 1.通过id获取报名者对象
        edit_user = User.query.get(id)
        if edit_user:
            print('edit...', edit_user)


            # 2.修改数据
            # print(request.data)
            # print(type(request.data))
            # j_data = json.loads(request.data)
            # print(request.json)
            # print(request.get_data())
            # print(request.get_json())
            # jd = j_data
            # 接受前端发来的数据
            data_str = request.get_data(as_text=True)
            data = json.loads(data_str)
            # print(1, data)
            # print(2, jd)
            # print(data)
            # 原修改代码
            # edit_user.name = data.get(keyword = 'name', edit_user.name)
            # edit_user.gender = data.get(keyword = 'gender',edit_user.gender)
            # edit_user.campus = data.get(keyword = 'campus', edit_user.campus)
            # edit_user.grade = data.get(keyword = 'grade', edit_user.grade)
            # edit_user.college = data.get(key = 'college', edit_user.college)
            # edit_user.major = data.get(key = 'major', edit_user.major)
            # edit_user.address = data.get(key = 'address', edit_user.address)
            # edit_user.phone = data.get(key = 'phone', edit_user.phone)
            # edit_user.email = data.get(key = 'email', edit_user.email)
            # edit_user.first_choice = data.get(key = 'first_choice', edit_user.first_choice)
            # edit_user.second_choice = data.get(key = 'second_choice', edit_user.second_choice)
            # edit_user.introduction = data.get(key = 'introduction', edit_user.introduction)
            # 简化版本修改代码
            for k, v in data.items():
                if k in dir(edit_user):
                    exec('edit_user.{} = v'.format(k))

            # 3.提前请求
            db.session.commit()
            logger.info('Edit user {} success!'.format(edit_user))
            return jsonify({'status': '0', 'errmsg': '修改成功！'})

        else:
            logger.info('Edit user(id == {}) failed!'.format(id))
            return jsonify({'status': '-1', 'errmsg': '修改失败！'})

# 删
@api_blueprint.route('/users/del/<id>/', methods=['DELETE'])
def user_del(id=None):
    """
    对特定报名同学信息进行删
    :return:
    """
    # print('here')

    if request.method == 'DELETE':
        # 1.通过id获取报名者对象
        del_user = User.query.get(id)

        if del_user:

            # 2.删除数据
            db.session.delete(del_user)

            # 3.提前请求
            db.session.commit()


            print('del...', del_user)
            logger.info('Delete user {} success!'.format(del_user))
            return jsonify({'status': '0', 'errmsg': '删除成功！'})
        else:
            logger.info('Delete user (id == {}) failed!'.format(id))
            return jsonify({'status': '-1', 'errmsg': '删除用户失败！'})

# 查
@api_blueprint.route('/users/query/all', methods=['GET'])
def user_query_all():
    """
    查询所有已报名同学数据
    :return:
    """
    if request.method=='GET':
        try:
            user_list = User.query.filter(1 == 1).order_by('create_time').all()
            user_id2data = {}
            for user in user_list:
                user_dict = user.__dict__.copy()  # 取对象的属性、值的字典
                user_dict.pop('_sa_instance_state')  # 去除字典中不要的数据
                user_id2data[str(user_dict['id'])] = user_dict

            print('get user_list....', user_list)
            logger.info('Query all users {} success!'.format(user_list))
            return jsonify({'status': '0', 'errmsg': '查询所有用户成功！', "data": user_id2data})
        except Exception as err:
            logger.error('Query all users failed!Err:{}'.format(err))
            return jsonify({'status': '-1', 'errmsg': '查询所有用户失败！', "data": {}})

@api_blueprint.route('/users/query/<int:get_id>/', methods=['GET'])
def user_get(get_id=None):
    """
    查询特定报名同学的数据
    :return:
    """
    # print(get_id)
    if get_id:
        logger.info('Try to get the data of a user whose id =={}'.format(get_id))
        # user = User.query.filter(User.id == int(id))
        user = db.session.query(User).filter_by(id=get_id).first()
        if user:
            # print(user.__dict__)
            user_dict = user.__dict__.copy()  # 取对象的属性、值的字典
            user_dict.pop('_sa_instance_state')  # 去除字典中不要的数据
            # user_json = json.dumps(user_dict)           #转json
            logger.info('Query user {} success!'.format(user))
            return jsonify({'status': '0', 'errmsg': '查询单用户成功！', "data": user_dict})
        else:
            logger.info('Query user (id=={}) failed!'.format(get_id))
            return jsonify({'status': '-1', 'errmsg': '查询单用户失败！', "data": {}})
    else:
        logger.info('Query user failed, No id!')
        return jsonify({'status': '-1', 'errmsg': '未传入查询用户id！', "data": {}})

