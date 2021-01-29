from app import app
from controladores.homeV import home_vista
from controladores.adminV import admin_vista


app.register_blueprint(home_vista)
app.register_blueprint(admin_vista)

if __name__ == "__main__":
    app.run(debug=True)