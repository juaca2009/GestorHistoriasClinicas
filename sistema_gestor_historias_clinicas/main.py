from app import app
from vistas.homeV import home_vista


app.register_blueprint(home_vista)

if __name__ == "__main__":
    app.run(debug=True)