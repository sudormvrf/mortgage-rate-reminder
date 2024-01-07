from pushover import Pushover
import excelwork
import config

po = Pushover(config.api_key)
po.user(config.user_key)

msg = po.msg(excelwork.push_message)

msg.set("title", f"Weekly Mortgage Rate Update")

po.send(msg)

