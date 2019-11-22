# from datetime import datetime
import os

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
        

class TinyWebDB(db.Model):
    __tablename__ = 'tinywebdb'
    tag = db.Column(db.String, primary_key=True, nullable=False)
    value = db.Column(db.String, nullable=False)
    # The 'date' column is needed for deleting older entries, so not really required
    # date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


db.create_all()
db.session.commit()

@app.route('/')
def main_method():
    return 'AsteroidDB works perfectly!'


# -------------------------
#  Store Value
#  - Store a value by using tag.
# -------------------------
@app.route('/store', methods=['POST'])
def store_a_value():
    tag = request.form['tag']
    value = request.form['value']
    getpassword = TinyWebDB.query.filter_by(tag='dbpass').first()
    if tag:
        if tag == 'dbpass':
            return jsonify(action="ERROR",error="Not possible to do any action to password record!")
        else:
            # --------------------
            if getpassword:
                password = request.form['pass']
                if password != getpassword.value:
                    return jsonify(action="ERROR",error="Wrong password!")
            # --------------------
            existing_tag = TinyWebDB.query.filter_by(tag=tag).first()
            if existing_tag:
                existing_tag.value = value
                db.session.commit()
            else:
                data = TinyWebDB(tag=tag, value=value)
                db.session.add(data)
                db.session.commit()
        return jsonify(action="STORED", tag=tag, value=value)
    return jsonify(action="ERROR", error="Not found the tag.")


# -------------------------
#  Get Value
#  - Get the value from tag.
# -------------------------
@app.route('/get', methods=['POST'])
def get_value():
    tag = request.form['tag']
    getpassword = TinyWebDB.query.filter_by(tag='dbpass').first()
    if tag:
        if tag == 'dbpass':
            return jsonify(action="ERROR", error="Not possible to do any action to password record!")
        else:
            # --------------------
            if getpassword:
                password = request.form['pass']
                if password != getpassword.value:
                    return jsonify(action="ERROR",error="Wrong password!")
            # --------------------
            value = TinyWebDB.query.filter_by(tag=tag).first().value
            return jsonify(action="GOT", tag=tag, value=value)
    return jsonify(action="ERROR",error="Not found the tag.")


# -------------------------
#  Get All Data
#  - Return everything from database. This method doesn't include password record tag and value.
# -------------------------
@app.route('/auth/data', methods=['POST'])
def get_data():
    getpassword = TinyWebDB.query.filter_by(tag='dbpass').first()
    if getpassword:
        # --------------------
        password = request.form['pass']
        if password != getpassword.value:
            return jsonify(action="ERROR",error="Wrong password!")
        # --------------------
        tags = TinyWebDB.query.all()
        taglist = []
        valuelist = []
        for tg in tags:
           if tg.tag != 'dbpass':
              taglist.append(tg.tag)
              valuelist.append(tg.value)
        return jsonify(action="DATA", tag=taglist, value=valuelist)
    return jsonify(action="ERROR",error="You need to set a password first to use this feature!")


# -------------------------
#  Get All Tags
#  - Return all tags from database. This method doesn't include password record tag.
# -------------------------
@app.route('/getall', methods=['POST'])
def get_all():
    getpassword = TinyWebDB.query.filter_by(tag='dbpass').first()
    if getpassword:
        # --------------------
        password = request.form['pass']
        if password != getpassword.value:
            return jsonify(action="ERROR",error="Wrong password!")
        # --------------------
    tags = TinyWebDB.query.all()
    taglist = []
    for tg in tags:
        taglist.append(tg.tag)
    # Delete the dbpass tag from result because that record contains the password of database. 
    # Nobody wants to get the tag of that record, right?
    if 'dbpass' in tags:
        taglist.remove('dbpass')
    return jsonify(action="TAGS", tag=taglist)


# -------------------------
#  Delete Record
#  - Delete a record from tag.
# -------------------------
@app.route('/delete', methods=['POST'])
def delete_entry():
    tag = request.form['tag']
    getpassword = TinyWebDB.query.filter_by(tag='dbpass').first()
    if tag:
        if tag == 'dbpass':
            return jsonify(action="ERROR", error="Not possible to do any action to password record!")
        else:
            # --------------------
            if getpassword:
                password = request.form['pass']
                if password != getpassword.value:
                    return jsonify(action="ERROR",error="Wrong password!")
            # --------------------
            deleted = TinyWebDB.query.filter_by(tag=tag).first()
            db.session.delete(deleted)
            db.session.commit()
            return jsonify(action="DELETED", tag=tag)
    return jsonify(action="ERROR",error="Not found the tag.")


# -------------------------
#  Format Database
#  - Deletes every record from database, and remove password protection.
# -------------------------
@app.route('/format', methods=['POST'])
def delete_all():
    getpassword = TinyWebDB.query.filter_by(tag='dbpass').first()
    if getpassword:
        # --------------------
        password = request.form['pass']
        if password != getpassword.value:
            return jsonify(action="ERROR",error="Wrong password!")
        # --------------------
    try:
        count = db.session.query(TinyWebDB).delete()
        db.session.commit()
        return jsonify(action="FORMATTED", count=count)
    except:
        db.session.rollback()
        return jsonify(action="ERROR",error="Something went wrong while performing this action.")
    


# -------------------------
#  Set/Change Password
#  - If you set a password, you need to type a password when you modify the database.
#  - The password will be saved in the same table along with other data called "dbpass".
#  - If you forgot the password, there is no way to recover it.
# -------------------------
@app.route('/auth/password', methods=['POST'])
def set_key():
    newpassword = request.form['newpass']
    getpassword = TinyWebDB.query.filter_by(tag='dbpass').first()
    if newpassword:
        if getpassword:
            oldpassword = request.form['oldpass']
            if getpassword.value == oldpassword:
                getpassword.value = newpassword
                db.session.commit()
                return jsonify(action="CHANGED PASSWORD", newpassword=newpassword)
            else:
                return jsonify(action="ERROR",error="Wrong old password!")
        else:
            data = TinyWebDB(tag='dbpass', value=newpassword)
            db.session.add(data)
            db.session.commit()
            return jsonify(action="SET PASSWORD", newpassword=newpassword)
    return jsonify(action="ERROR",error="No new password is specified!")


# -------------------------
#  Remove Password
#  - If you type your current password, requests won't require pass parameter anymore. And your password will be deleted.
# -------------------------
@app.route('/auth/unlock', methods=['POST'])
def remove_key():
    password = request.form['pass']
    getpassword = TinyWebDB.query.filter_by(tag='dbpass').first()
    if getpassword:
        if getpassword.value == password:
            deleted = TinyWebDB.query.filter_by(tag='dbpass').first()
            db.session.delete(deleted)
            db.session.commit()
            return jsonify(action="DELETED PASSWORD", password=password)
        else:
            return jsonify(action="ERROR",error="Wrong password!")
    return jsonify(action="ERROR",error="You need to set a password first to use this feature!")


# -------------------------
#  Is Password True?
#  - Useful for applications. Returns 'true' if password is correct. Otherwise; 'false'.
# -------------------------
@app.route('/istrue', methods=['POST'])
def is_true():
    password = request.form['pass']
    getpassword = TinyWebDB.query.filter_by(tag='dbpass').first()
    if getpassword:
        # --------------------
        if password != getpassword.value:
            return jsonify(action="IS CORRECT",result="false")
        # --------------------
    return jsonify(action="IS CORRECT",result="true")
        

# -------------------------
#  Count All Records
#  - Returns a number that tells you how many records there are in database. 
#  - Decrease the number with 1 if you do not want the dbpass record to be included.
# -------------------------
@app.route('/count')
def count_all():
    tags = TinyWebDB.query.all()
    resl = len(tags)
    return jsonify(action="COUNT", count=resl)


# -------------------------
#  Is Locked?
#  - Gives information about current lock status.
# -------------------------
@app.route('/islocked')
def is_locked():
    getpassword = TinyWebDB.query.filter_by(tag='dbpass').first()
    if getpassword:
        return jsonify(action="IS LOCKED",result="true")
    else:
        return jsonify(action="IS LOCKED",result="false")
        

if __name__ == '__main__':
    app.run()
