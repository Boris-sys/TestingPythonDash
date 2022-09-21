import flask
from dash import Dash
from dash_bootstrap_components.themes import BOOTSTRAP
from src.components.layout import create_layout
from src.data.loader import load_transaction_data

DATA_PATH = "./data/transactions.csv"

data = load_transaction_data(DATA_PATH) 
app = Dash(external_stylesheets=[BOOTSTRAP]) #define the dash app with a bootstrap template
app.title = "Boris Dashboard"
app.layout = create_layout(app, data)
server = app.server #this definition is important for the Heroku deployment

def main() -> None:    
    # app = Dash(external_stylesheets=[BOOTSTRAP])
    # server=app.server
    #app.title = "Medal dashboard"
    app.run()


if __name__ == "__main__":
    main()
