from website import create_app


app = create_app()


if __name__ == '__main__':
    app.run(debug=True)
    #running a webserver only if you are running the main.py file ---> creates only one instance
    #Default port is 5000
