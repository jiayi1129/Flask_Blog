from flaskblog import create_app

app = create_app()
print("app created!")

# runs the app
if __name__ == "__main__":
    app.run()
