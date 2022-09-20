import flask
from dash import Dash
from dash_bootstrap_components.themes import BOOTSTRAP
from src.components.layout import create_layout

server = flask.Flask(__name__)
def main() -> None:    
    
    app = Dash(external_stylesheets=[BOOTSTRAP], server=server)
    # app = Dash(external_stylesheets=[BOOTSTRAP])
    # server=app.server

    app.title = "Medal dashboard"
    app.layout = create_layout(app)
    app.run()


if __name__ == "__main__":
    main()
