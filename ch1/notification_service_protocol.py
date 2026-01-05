from typing import Protocol

class Notifier(Protocol):
    def send_notification(self, message: str) -> None:
        ...

class EmailNotifier: # No explicit inheritance like ABC.
    def send_notification(self, message: str) -> None:
        print(f"Sending email: {message}")

class SMSNotifier: # No explict inheritance
    def send_notification(self, message: str) -> None:
        print(f"Sending SMS: {message}")


class NotificationService:
    def __init__(self, notifier: Notifier): # still able to use type hinting
        self.notifier = notifier

    def notify(self, message: str) -> None:
        self.notifier.send_notification(message)


# usage
sms_notifier = SMSNotifier()
sms_service = NotificationService(sms_notifier)
sms_service.notify("Hello via SMS")


