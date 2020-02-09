from flaskblog import create_app

app = create_app()
app.run()

# runs the app in debug mode
if __name__ == "__main__":
    app.run(debug=True)
