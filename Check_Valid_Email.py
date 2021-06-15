import socket
import smtplib
import dns
import dns.resolver


class Main:

    # def __init__(self,e):
    #     self.email=e


    def valid_email(self,email):

        try:
            domain = email.split('@')[1]
            mxRecord = dns.resolver.resolve(domain, 'MX')
            priority = []
            server = []
            for i in mxRecord:
                t = i.to_text().split(' ')
                priority.append(int(t[0]))
                server.append(t[1])
            mxRecord = server[priority.index(min(priority))]
            # Get local server hostname
            host = socket.gethostname()

            # SMTP lib setup (use debug level for full output)
            server = smtplib.SMTP()
            server.set_debuglevel(0)

            # SMTP Conversation
            server.connect(mxRecord)
            server.helo(host)
            server.mail('sovek82878@moxkid.com')
            code, message = server.rcpt(email)
            server.quit()

            # Assume 250 as Success
            if code == 250:

                return True
            else:
                return False

        except Exception as e:
            print(e)
            pass


if __name__ == '__main__':
    t = Main()
    t.valid_email('jainish@detasecure.com')
