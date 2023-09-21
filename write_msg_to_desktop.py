from plyer import notification, tts


def notify(filename, actionString, timeout = 10):
    notification.notify(title=filename, message=actionString, timeout=timeout, app_icon="/usr/share/icons/gnome/22x22/categories/applications-science.png")

def speek(msg):
    tts.speak(message=msg)