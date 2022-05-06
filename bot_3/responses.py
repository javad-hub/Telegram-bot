from datetime import datetime

def sample_response(input_text):
	user_message = str(input_text).lower()

	if user_message in ('سلام', 'hi', 'hello',):
		return "سلام چه خبر؟"
	
	if user_message in ('سلامتی تو چه خبر؟'):
		return "واسه اخبار میتونی به microsoft news مراجعه کنی"

	if user_message in ('ممنون'):
		return "خواهش می کنم من واسه خدمت اینجام"

	if user_message in ('تو که هستی', 'تو که هستی؟'):
		return 'من ddr298 bot هستم'

	if user_message in ('time', 'زمان'):
		now = datetime.now()
		date_time = now.strftime("%d/%m/%y, %H:%M:%S")

		return str(date_time)

	return 'من متوجه نمیشم چه میگی'