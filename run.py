from application import init_app

app = init_app()

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
