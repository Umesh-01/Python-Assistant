import datetime
import winsound                      # pip install playsound


def alarm(Timing):
    altime = str(datetime.datetime.now().strptime(Timing, "%I:%M %p"))

    altime = altime[11:-3]
    print(altime)
    Hr_real = altime[:2]
    Hr_real = int(Hr_real)
    Min_real = altime[3:5]
    Min_real = int(Min_real)
    print(f"Done, alarm is set for {Timing}")

    while True:
        if Hr_real == datetime.datetime.now().hour:
            if Min_real == datetime.datetime.now().minute:
                print("Alarm is Ringing...")
                winsound.PlaySound('abc', winsound.SND_LOOP)

            elif Min_real < datetime.datetime.now().minute:
                break


if __name__ == '__main__':
    alarm('09:21 PM')
