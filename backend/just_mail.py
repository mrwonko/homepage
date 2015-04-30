from twisted.mail import smtp
from twisted.internet import defer, reactor
from email.mime.text import MIMEText
from StringIO import StringIO

import local_config

def send( subject, body ):
    if not local_config.MAIL_ENABLED:
        return defer.succeed( None )
    
    finished = defer.Deferred()
    
    msg = MIMEText( body, "html" )
    msg[ "Subject" ] = subject
    msg[ "From" ] = local_config.MAIL_FROM
    msg[ "To" ]  = ", ".join( local_config.MAIL_TO )
    
    senderFactory = smtp.ESMTPSenderFactory(
        local_config.SMTP_USER,
        local_config.SMTP_PASS,
        local_config.MAIL_FROM,
        ", ".join( local_config.MAIL_TO ),
        StringIO( str( msg ) ),
        finished
    )

    reactor.connectTCP( local_config.SMTP_SERVER, 25, senderFactory )

    return finished
