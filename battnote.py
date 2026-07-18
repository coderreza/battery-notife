import time 
from plyer import notification
import psutil
import winsound


while True:
    battery = psutil.sensors_battery()
    bat = battery.percent
    if bat <= 20:
        notification.notify(
            title='low battery',
            message='This is a notification from Python',
            app_name='battery notifier',
            timeout=10,  # seconds
            
        )
        winsound.Beep(1000, 500),  
        winsound.Beep(1200, 500)
        
    elif bat >= 80:
        notification.notify(
            title='enough battery',
            message='plug your pc out of charger',
            app_name='battery notifier',
            timeout=10,
            
        )
        winsound.Beep(1000, 500),  
        winsound.Beep(1200, 500)
    
    time.sleep(10)
