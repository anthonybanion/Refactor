from run import create_app
from flask_login import LoginManager


app = create_app()
login_manager = LoginManager(app)

if __name__ == "__main__":
    app.run(debug=True)