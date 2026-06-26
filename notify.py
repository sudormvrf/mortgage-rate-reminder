from pushover_complete import PushoverAPI
import config
import analyze
from datetime import date




if __name__ == "__main__":
    pushover = PushoverAPI(config.api_key)
    recent_date, recent_rate = analyze.get_latest_rate("./mortgage30us.csv")
    today_date = date.today()
    diff = today_date - recent_date
    if diff.days == 0:
        msg = f"The mortgage rate data updated today, on {recent_date.strftime('%a, %b %d')}. It is at {recent_rate:.2f}%."
    elif diff.days == 1:
        msg = f"The mortgage rate data updated yesterday on {recent_date.strftime('%B %d, %Y')}. It was at {recent_rate:.2f}%."
    else:
        msg = f"The mortgage rate data published {diff.days} days ago. It was at {recent_rate:.2f}%."
    pushover.send_message(config.user_key, msg)

