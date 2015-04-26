import smtplib
from email.mime.text import MIMEText
import logging

import local_config

logger = logging.Logger( __name__ )
logger.addHandler( logging.StreamHandler() ) # output to stdout/stderr

def send( subject, body ):
    try:
        server = smtplib.SMTP( local_config.SMTP_SERVER )
    except Exception, e:
        logger.error( "Failed to connect to %s: %s", local_config.SMTP_SERVER, str( e ) )
        return False
        
    code, msg = server.ehlo()
    if code / 100 != 2:
        logger.error( "EHLO failed: %s", msg )
        server.close()
        return False
        
    code, msg = server.starttls()
    if code / 100 != 2:
        logger.error( "Failed to start TLS: %s", msg )
        server.close()
        return False
        
    code, msg = server.ehlo()
    if code / 100 != 2:
        logger.error( "EHLO in TLS failed: %s", msg )
        server.close()
        return False
        
    code, msg = server.login( local_config.SMTP_USER, local_config.SMTP_PASS )
    if code / 100 != 2:
        logger.error( "SMTP login failed: %s", msg )
        server.close()
        return False
    
    msg = MIMEText( body )
    msg[ "Subject" ] = subject
    msg[ "From" ] = local_config.MAIL_FROM
    msg[ "To" ]  = ", ".join( local_config.MAIL_TO )
    try:
        server.sendmail( local_config.MAIL_FROM, local_config.MAIL_TO, msg.as_string() )
    except Exception, e:
        logger.error( "Failed to send mail: %s", str( e ) )
        return False
    server.close()
    return True