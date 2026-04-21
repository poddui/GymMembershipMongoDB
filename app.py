from flask import Flask, render_template, request, redirect, url_for
from exercise import create_customer, update_customer, delete_customer_by_id, get_customer_by_id, get_customers, create_membership, update_membership, delete_membership_by_id, get_membership_by_id, get_memberships, get_visitlog_by_membership_id

app = Flask(__name__)

# main page
@app.route("/")
def home():
    customers = list(get_customers())
    memberships = list(get_memberships())
    for i in customers:
        i["_id"] = str(i["_id"])

    single_membership = None
    single_customer = None
    visit_logs = []
    customer_membership = None

    req_customer_id  = request.args.get("customer_id")
    if req_customer_id:
        single_customer = get_customer_by_id(req_customer_id)
        if single_customer and single_customer.get("membershipID"):
            customer_membership = get_membership_by_id(single_customer["membershipID"])

    req_membership_id = request.args.get("membership_id")
    if req_membership_id:
        single_membership = get_membership_by_id(req_membership_id)
        visit_logs = list(get_visitlog_by_membership_id(req_membership_id))

    return render_template("index.html", 
                           customers=customers,
                           memberships=memberships,
                           single_customer=single_customer,
                           single_membership=single_membership,
                           visit_logs=visit_logs,
                           customer_membership=customer_membership
    )

# customer CRUD
@app.route("/add_customer", methods=["POST"])
def add_customer():
    customer = {
        "firstname": request.form["firstname"],
        "lastname": request.form["lastname"],
        "email": request.form["email"],
        "phone": request.form["phone"],
        "membershipID": None
    }
    create_customer(customer)
    return "Customer added ✅ <a href='/'>Back</a>"

@app.route("/edit_customer", methods=["POST"])
def edit_customer():
    customer_id = request.form["customerID"]
    updated_data = {
        "firstname": request.form["firstname"],
        "lastname": request.form["lastname"],
        "email": request.form["email"],
        "phone": request.form["phone"]
    }
    update_customer(customer_id, updated_data)
    return "Customer edited ✅ <a href='/'>Back</a>"

@app.route("/delete_customer", methods=["POST"])
def delete_customer():
    customer_id = request.form["customerID"]
    delete_customer_by_id(customer_id)
    return "Customer deleted ✅ <a href='/'>Back</a>"


@app.route("/find_customer", methods=["POST"])
def find_customer():
    customer_id = request.form["customerID"]
    return redirect(url_for("home", customer_id=customer_id))


# membership CRUD
@app.route("/add_membership", methods=["POST"])
def add_membership():
    membership = {
        "membershipID": int(request.form["membershipID"]),
        "priceCategory": request.form["priceCategory"],
        "startDate": request.form["startDate"],
        "endDate": request.form["endDate"],
        "active": True
    }
    create_membership(membership)
    return "Membership added ✅ <a href='/'>Back</a>"

@app.route("/edit_membership", methods=["POST"])
def edit_membership():
    membership_id = request.form["memberID"]
    updated_data = {
        "membershipID": int(request.form["membershipID"]),
        "priceCategory": request.form["priceCategory"],
        "startDate": request.form["startDate"],
        "endDate": request.form["endDate"],
        "active": "active" in request.form
    }
    update_membership(membership_id, updated_data)
    return "Membership edited ✅ <a href='/'>Back</a>"

@app.route("/delete_membership", methods=["POST"])
def delete_membership():
    membership_id = request.form["membershipID"]
    delete_membership_by_id(membership_id)
    return "Membership deleted ✅ <a href='/'>Back</a>"


@app.route("/find_membership", methods=["POST"])
def find_membership():
    membership_id = request.form["membershipID"]
    return redirect(url_for("home", membership_id=membership_id))


if __name__ == "__main__":
    app.run(debug=True)