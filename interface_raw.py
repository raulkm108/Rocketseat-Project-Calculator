from abc import ABC, abstractmethod

class NotificationSender(ABC):

    @abstractmethod
    def send_notification(self, message: str) -> None:
        pass

class EmailNotificationSender(NotificationSender):

    def send_notification(self, message: str) -> None:
        print(f"Email message - {message}")

class SMSNotificationSender(NotificationSender):

    def send_notification(self, message: str) -> None:
        print(f"SMS message - {message}")

obj = EmailNotificationSender()
obj.send_notification( "Hello World!")