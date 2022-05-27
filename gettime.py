from datetime import datetime
import pytz
from flask import Flask

app = Flask("time now")

@app.route('/now', defaults={'timezone': ''})
@app.route("/now/<path:timezone>")

def timenow(timezone):
	try:
		if not timezone:
			zone = pytz.utc
		else:
			zone = pytz.timezone(timezone)
		now = datetime.now(zone)
		return now.strftime("%Y-%m-%d %H:%M:%S %z %Z\n")

	except pytz.exceptions.UnknownTimeZoneError:
		return f"Unknown timezone: {timezone}\n"

app.run()
