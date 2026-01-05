from abc import ABC, abstractmethod


class Notifier(ABC):
    @abstractmethod
    def send_notification(self, message: str) -> None:
        ...


class EmailNotifier(Notifier):
    def send_notification(self, message: str) -> None:
        print(f"Sending email: {message}")


class SMSNotifier(Notifier):
    def send_notification(self, message: str) -> None:
        print(f"Sending SMS: {message}")

class NotificationService:
    def __init__(self, notifier: Notifier):
        self.notifier = notifier

    def notify(self, message: str) -> None:
        self.notifier.send_notification(message)



# usage
email_notifier = EmailNotifier()
sms_notifier = SMSNotifier()
NotificationService(email_notifier).notify("Hello via emal")
NotificationService(sms_notifier).notify("Hello va sms")

