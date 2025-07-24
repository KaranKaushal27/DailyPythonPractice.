from datetime import datetime

def write_log(message):
    current_time = datetime.now().strftime("%y-%m-%d %H:%M:%S")
    log_entry = f"[{current_time}] {message}\n"
    with open("system_log.txt", "a") as file:
        file.write(log_entry) 

write_log("system initialized")
write_log("user initialized at 10:00 AM")
write_log("user performed backup operation")

