# 어플리케이션 팩토리

from flask import Flask

def create_app(): #함수명으로 create_app 대신 다른 이름을 사용하면 정상으로 동작하지 않는다. create_app은 플라스크 내부에서 정의된 함수명이다.
    app = Flask(__name__) #__name__ = main

    from .views import main_views
    app.register_blueprint(main_views.bp) #test/module_exam, -2 에서 대충 설명
    # @app.route('/') #url http://127.0.0.1:5000, / 뒤에다 뭐 적으면 url에도 같이 적어줘야된다
    # def hello_pybo():
    #     return 'Hello, Pybo!!!!'
    # 블루프린트 중복되므로 삭제

    # @app.route('/pybo') #url http://127.0.0.1:5000/pybo
    # def hello_pybo():
    #     return 'Hello, flask!!!!'

    return app

# 실행하려면 cmd 창에 pythonproject 디렉토리에서 (파이보 아님) set FLASK_APP=pybo 입력하고 flask run

