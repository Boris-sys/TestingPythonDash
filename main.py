from dash import Dash
from dash_bootstrap_components.themes import BOOTSTRAP

from src.components.layout import create_layout

app = Dash(external_stylesheets=[BOOTSTRAP])
server=app.server


def main() -> None:    
    app.title = "Medal dashboard"
    app.layout = create_layout(app)
    app.run()


if __name__ == "__main__":
    main()
