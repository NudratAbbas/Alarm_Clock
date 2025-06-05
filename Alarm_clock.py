import datetime
import time
import os
import platform

def ring_alarm():
    print("\n⏰ WAKE UP! Time's up! ⏰")
    if platform.system() == "Windows":
        # Windows beep
        import winsound
        for _ in range(5):
            winsound.Beep(1000, 500)
    else:
        # Mac/Linux beep
        for _ in range(5):
            os.system('echo -e "\a"')
            time.sleep(1)

def main():
    print("=== Python Alarm Clock ===")
    alarm_time = input("Enter alarm time (HH:MM, 24-hour format): ")

    try:
        alarm_hour, alarm_minute = map(int, alarm_time.split(":"))
    except ValueError:
        print("❌ Invalid format. Please use HH:MM (e.g., 06:30).")
        return

    print(f"✅ Alarm set for {alarm_hour:02d}:{alarm_minute:02d}...")

    while True:
        now = datetime.datetime.now()
        if now.hour == alarm_hour and now.minute == alarm_minute:
            ring_alarm()
            break
        time.sleep(10)

if __name__ == "__main__":
    main()
