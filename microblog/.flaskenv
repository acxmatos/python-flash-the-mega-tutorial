FLASK_APP=microblog.py
FLASK_ENV=development
FLASK_DEBUG=1

# For local SMTP mail test
#
# Run: python -m smtpd -n -c DebuggingServer localhost:8025
#
# Set: FLASK_DEBUG=0 (above)
#
# Uncomment lines below:
# MAIL_SERVER=localhost
# MAIL_PORT=8025