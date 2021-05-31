from flask import render_template, url_for, flash, redirect, request
from flaskapp import app, db, bcrypt
from flaskapp.forms import RegistrationForm, LoginForm, BookingForm
from flaskapp.models import User,Booking
from flask_login import login_user, current_user, logout_user, login_required




@app.route('/')
@app.route('/home')
def home():
    bookings = Booking.query.all()
    return render_template("home.html", bookings = bookings)


@app.route('/about')
def about():
    return("<h1>About page!<h1>")

@app.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("Your account has been created, You can now login!", "success")
        return redirect(url_for('login'))
    return render_template("register.html", form = form)

@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash("Login Unsuccessful", "danger")
    return render_template("login.html", form = form)
    

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/account')
@login_required
def account():
    return render_template("account.html")

@app.route('/booking/new', methods=['GET','POST'])
@login_required
def new_booking():
    form = BookingForm()
    if form.validate_on_submit():
        booking = Booking(Day = form.Day.data, Time = form.Time.data, Name = form.Name.data )
        db.session.add(booking)
        db.session.commit()
        flash('Your Booking has been created!', 'success')
        return redirect(url_for('home'))
    return render_template("create_booking.html", form=form)

@app.route('/booking/<int:booking_id>')
def booking(booking_id):
    booking = Booking.query.get_or_404(booking_id)
    return render_template('booking.html', booking=booking)

@app.route('/booking/<int:booking_id>/update', methods=['GET','POST'])
@login_required
def update_booking(booking_id):
    booking = Booking.query.get_or_404(booking_id)
    form = BookingForm()
    if form.validate_on_submit():
        booking.Day = form.Day.data
        booking.Time = form.Time.data
        booking.Name = form.Name.data
        db.session.commit()
        flash("Your booking has been confirmed", "success")
        return redirect(url_for('booking',booking_id=booking.id))
    elif request.method == 'GET':
        form.Day.data = booking.Day
        form.Time.data = booking.Time
        form.Name.data = booking.Name
    return render_template("create_booking.html", form=form)