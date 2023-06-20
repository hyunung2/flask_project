from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/') #url_prefix -> bp.route, 변경하면 같이 변경해줘야 하므로 고칠필요 없으나 나중에 복잡해지면 모듈명으로 붙여주기도 한다

@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'


@bp.route('/')
def index():
    return 'Pybo index'