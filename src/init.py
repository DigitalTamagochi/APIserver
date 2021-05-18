from flask import Flask
from .modules.login_group import loginApp
from .modules.register_group import registerApp
from .modules.server_main_page import mainPage
from .modules.connect_group import connectApp
from .modules.jest_list_group import jestListApp
from .modules.jest_edit_group import jestEditApp


app = Flask(__name__)

app.register_blueprint(connectApp)
app.register_blueprint(loginApp)
app.register_blueprint(registerApp)
app.register_blueprint(mainPage)
app.register_blueprint(jestListApp)
app.register_blueprint(jestEditApp)
