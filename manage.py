from flask.cli import FlaskGroup
from project.setupDatabseIfo import add_all
from project import app, db 
from project.hotels import bp_hotel

cli = FlaskGroup(app)

# blueprints
app.register_blueprint(bp_hotel)

@cli.command("create_db")
def create_db():
    # destroy all tables and creat new ones
    # this is good for testing, you can delete it if you want full persistency
    db.drop_all()
    db.create_all()
    db.session.commit()
    add_all()
    db.session.commit()
    print("here we go again")


@cli.command("seed_db")
def seed_db():
    db.session.commit()


if __name__ == "__main__":
    cli()