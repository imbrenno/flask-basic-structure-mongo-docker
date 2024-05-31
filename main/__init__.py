from main.settings.settings import app
from main.controllers import blueprints_ctrl


for bp in blueprints_ctrl:
    app.register_blueprint(
        bp,
    )
