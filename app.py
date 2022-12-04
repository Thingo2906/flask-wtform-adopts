from flask import Flask, request, render_template,  redirect, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db,  connect_db, Pet
from forms import AddForm, EditPetForm


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def home_page():
    pets = Pet.query.all()
    return render_template('home.html', pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Pet add form; handle adding."""
    form = AddForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        pet = Pet(name = name, species = species, photo_url= photo_url, 
                age = age, notes = notes)
        db.session.add(pet)
        db.session.commit()
        return redirect("/")
    else:
        return render_template("add_form.html", form=form)

@app.route("/pet/<int:id>")
def display_pet(id):
    """Display pet """
    pet = Pet.query.get_or_404(id)
    return render_template("pet_detail.html", pet = pet)

@app.route("/pet/<int:id>/edit", methods=["GET", "POST"] )
def edit_pet(id):
    """Edit pet"""
    pet = Pet.query.get_or_404(id)
    form = EditPetForm(obj=pet)
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect("/")
    else:
        return render_template("edit_form.html", form = form, pet=pet)

@app.route("/api/pet/<int:id>", methods=['GET'])
def api_get_pet(id):
    """Return basic info about pet in JSON."""

    pet = Pet.query.get_or_404(id)
    info = {"name": pet.name, "age": pet.age}

    return jsonify(info)




    
