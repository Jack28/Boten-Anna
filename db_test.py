from boten_anna_db import boten_anna_db

db = boten_anna_db()
db.insert("http://dev-nu11.de","Nothing","Visit IT!","DAU")
print(db.get_links())
