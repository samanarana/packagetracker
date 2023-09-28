from flask import Blueprint, render_template, redirect, url_for
from .shipping_form import ShippingForm
from .models import db, Package

bp = Blueprint('package', __name__, url_prefix="")

@bp.route('/')
def index():
    packages = Package.query.all()
    return render_template('package_status.html', packages=packages)


@bp.route('/new-package', methods=['GET', 'POST'])
def new_package():
    form = ShippingForm()
    if form.validate_on_submit():
        new_package= Package(sender=form.sender.data,
                         recipient=form.recipient.data,
                         origin=form.origin.data,
                         destination=form.destination.data,
                         location=form.origin.data)

        db.session.add(new_package)
        db.session.commit()

        Package.advance_all_locations()

        return redirect(url_for('package.index'))
    return render_template('shipping_request.html', form=form)
