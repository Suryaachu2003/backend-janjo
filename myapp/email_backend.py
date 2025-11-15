import ssl
from django.core.mail.backends.smtp import EmailBackend as SmtpEmailBackend

class EmailBackend(SmtpEmailBackend):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def open(self):
        if self.connection:
            return False
        try:
            self.connection = self.connection_class(self.host, self.port, timeout=self.timeout)
            if self.use_tls:
                self.connection.starttls(context=ssl._create_unverified_context())
            if self.username and self.password:
                self.connection.login(self.username, self.password)
            return True
        except Exception:
            if not self.fail_silently:
                raise
