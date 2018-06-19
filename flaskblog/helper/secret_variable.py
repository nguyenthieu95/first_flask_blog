import os

db_user = "NguyenThieu"
db_pass = "123456789"

dynamic_db_user = os.environ.get('EMAIL_USER')
dynamic_db_pass = os.environ.get('EMAIL_PASS')

print(db_user + "  " + db_pass)
print(dynamic_db_user + "   " + dynamic_db_pass)