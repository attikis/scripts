#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : Strictly an input module to be used in other executable scripts
# Definition  : My very first generic functions class, to be used for simple coding.
 
''' 
Usage:
import python_myFunctions as myFs

Description:
In this python module I define some generic functions that can be used in many executable scripts. 
The list of functions defined here will grow significantly over time, at which stage I should perhaps
consider its further break-down to more classes and functions.
''' 
from datetime import datetime
import time 
import os

class CreateObject:
    def __init__(self):
        self.OutCounter = 0
        self.InCounter = 0
        self.TimeStart = datetime.now()
        self.TimeStop = datetime.now()
        self.Delay = -1
        self.Verbose = False
        
    def DisplayMatchObject(self, match):
        ''' DisplayMatchObject(self, match):
        A function to display match objects
        '''
        if match is None:
            return None
        print "match.group() = %r, match.groups() = %r>" % (match.group(), match.groups())
    # Loop over all groups and print them
        for iMatch in range (0, len(match.groups())+1):
            print 'group(%r) = %r' % (iMatch, match.group(iMatch))
            print 'groupdict(%r) = ' % (match.groupdict(iMatch))
        return 0
        
    def Cout(self, text):
        ''' Cout(self, text):
        A function to cout, keeping track of number of lines.
        '''
        self.OutCounter = self.OutCounter+1
        print "Out[%s] %s" % (self.OutCounter, text)
        return 0

    def Cin(self, text):
        ''' Cin(self, text):
        A function to cin, keeping track of number of lines.
        '''
        self.InCounter = self.InCounter+1
        myRawInput = raw_input("In[%s] %s: " % (self.InCounter, text) )
        return myRawInput
    
    def sortedDictKeys(self, dict):
        ''' sortedDictKeys(dict):
        A function to sort keys of a dictionary. A mapping (such as a "dictionary) has NO order, thus it cannot be sorted. Still, its keys can be extracted as a list, which can then be sorted.
        '''
        keys = dict.keys()
        keys.sort()
        return [key for key in keys]

    def sortedDictValues(self, dict):
        ''' sortedDictKeys(dict):
        A function to sort values of a dictionary, according to sorted keys. A mapping (such as a "dictionary) has NO order, thus it cannot be sorted. Still, its keys can be extracted as a list, which can then be sorted.
        '''
        
        keys = dict.keys()
        keys.sort()
        return [dict[key] for key in keys]
    
    def obscureString(self, inputString):
        ''' obscureString(dict):
        A function to obscure a string by replacing all ascii printable characters with asterisks (*). This is mainly used in cases when you want to print a password without revealing its meaning, but just the number of characters.
        '''
        import string

        outputString = inputString
        # Create a characters list
        CharactersList = []
        
        # Fill the list with all printable ascii characters
        for item in string.printable:
            CharactersList.append(item)
        # Now loop over all readable characters and replace those in the input string with an asterisk
        for char in CharactersList:
            outputString = outputString.replace(char, "*")
        # Return the asterisk-obscured string
        return outputString
    
    def sendEmailNoAttachment(self, server):
        ''' sendEmail(host_server):
        This module is a simple interface to send emails using the gmail or cern SMTP servers. When calling the module the only thing that needs to be specified is 
        which server is to be used (cern or gmail). Just follow the prompt commands once launched. The "smtplib" is a low-level package interface for the Simple Mail
        Transfer Protocol (SMTP) protocol. The "email" package assists with parsing (analyzing a sentence into its parts and describe their syntactic roles) and
        generating emails.
        '''

        # Import modules here
        import traceback
        from smtplib import SMTP
        from email.MIMEText import MIMEText
        import sys
        import datetime
        import getpass 
        
        # Declaration here
        myFunc = CreateObject()
        # Decide which of the two servers to use
        if server == "cern":
            smtpHost = "smtp.cern.ch"
            emailAddress = "@cern.ch"
            smtpUsername = "attikis@cern.ch"
        elif server == "gmail":
            smtpHost = "smtp.gmail.com"
            emailAddress = "@gmail.com"
            smtpUsername = "alexandros.attikis@gmail.com"
        else:
            self.Cout('ERROR! The server argument %s is invalid. Please select between "cern" and "gmail". Exiting python shell.')
            print self.sendEmailNoAttachment.__doc__
            sys.exit(1)
        smtpPort = 587 #or 25

        self.Cout("Please provide your login credentials for %s to continue:" % (smtpUsername))
        smtpPassword = getpass.getpass("\tPassword = ")
        sender = smtpUsername

        # First get user input regarding email details
        self.Cout("Please provide the email details:")
        recipients = raw_input("\tTo: ")
        Cc = raw_input("\tCc: ")
        Bcc = raw_input("\tBcc (self excluded): ")
        subject = raw_input("\tSubject: ")
        content = raw_input("\tContent: ")
        
        # Define return value as 0==success,  1==failure
        retval = 1
        # Take care of recipient lists
        if not(hasattr(recipients, "__iter__")):
            recipients = [recipients]
        if not(hasattr(Cc, "__iter__")):
            Cc = [Cc]
        if not(hasattr(Bcc, "__iter__")):
            Bcc = [Bcc]
            Bcc.append(smtpUsername)
            
        try:
            # Assign message details
            text_subtype = 'plain'
            msg = MIMEText(content, text_subtype)
            msg['From'] = sender # Some SMTP servers will do this automatically, but not all
            msg['To']   = ", ".join(recipients)
            msg['cc']   = ", ".join(Cc)
            msg['Bcc']  = ", ".join(Bcc)
            msg['Subject'] = subject

            # Connect to host using specified port
            self.Cout("Attempting to connect to:\n\thost = %s\n\tport = %s" % (smtpHost, smtpPort))
            connection = SMTP(host=smtpHost, port=smtpPort)
            connection.set_debuglevel(True)
            try:
                if smtpUsername is not False:
                    connection.ehlo()
                    if smtpPort != 25:
                        connection.starttls()
                        connection.ehlo()
                    if smtpUsername and smtpPassword:
                        connection.login(smtpUsername, smtpPassword)
                        self.Cout("Succesfully logged on to:\n\tusername = %s\n\tpassword = %s" % (smtpUsername, self.obscureString(smtpPassword)))
                    else:
                        self.Cout("Unsuccesfull login. False credentials provided:\n\tusername = %s\n\tpassword = %s" % (smtpUsername, self.obscureString(smtpPassword)))
                        print self.sendEmailNoAttachment.__doc__
                        sys.exit(1)
                # Send emails
                self.Cout("Sending email to %s" % (recipients) )
                connection.sendmail(sender, recipients+Cc+Bcc, msg.as_string())
                # Set return value to 0 (success)
                retval = 0
            except Exception, e:
                self.Cout("Got %s %s.\n\tShowing traceback:\n%s" % (type(e), e, traceback.format_exc()))
                # Set return value to 1 (failure)
                retval = 1
                print self.sendEmailNoAttachment.__doc__
            finally:
                self.Cout("Closing connection.")
                connection.close()
                
        except Exception, e:
            self.Cout("Got %s %s.\n\tShowing traceback:\n%s" % (type(e), e, traceback.format_exc()))
            # Set return value to 1 (failure)        
            retval = 1
            print self.sendEmailNoAttachment.__doc__
            
        return retval


    def getEmail(self, server):
        ''' getEmail(host_server):
        This module is a simple interface to check for new emails in the inbox of Gmail or CERN pop servers. In a nutshell the module retrieves all of the email that is stored on the specified server (Gmail or CERN) and wrties it to a set of files on disk. If new emails are present they will be opened before the script exits the shell. All new emails will be written as .eml files to dedicated paths. A time-stamp text file provides information of the last check for email. When calling the module the only thing that needs to be specified is which server is to be used (cern or gmail). Just follow the prompt commands once launced. Only thing the script does not do is to delete each email from the server after retrieving it. This is however possible by calling the connection.dele(i) after the connection.retr(i) command.
        '''
        # Import modules here
        import poplib
        from email import parser as eParser
        import traceback
        import sys
        import getpass 
        import time 
        from datetime import datetime
        from dateutil import parser 
        import os
        import pydoc
        
        # Declarations here
        myPath = "/Users/administrator/my_work/programming/python/inbox/" + server + "/"
        iNewMail = 0
        newMailFiles = []
        timeStampFile = "timestamp.txt"    
        today = datetime.now()

        # Get time elaplsed since last email check
        if not os.path.isfile(myPath + timeStampFile):
            try:
                myTimeStampFile = open(myPath + timeStampFile, "w")
                myTimeStampFile.write(str(today))
            finally:
                myTimeStampFile.close()
        try:
            myTimeStampFile = open(myPath + timeStampFile, "r")
            lastCheckTime = myTimeStampFile.readline().lstrip().strip().rstrip()
            lastTime = parser.parse(lastCheckTime)
            dt = today - lastTime
        finally:
            myTimeStampFile.close()
            days = dt.days
            hours   = int((dt.seconds - dt.seconds%3600.0) / 3600)
            minutes = int((dt.seconds - hours*3600) / 60)
            seconds = int(dt.seconds - hours*3600 - minutes*60.0)

        # Inform user of last inbox check
        self.Cout("Current date and time (yyyy:mm:dd hh:mm:ss):\n\t%s" % (today))
        self.Cout("Last inbox check was (yyyy:mm:dd hh:mm:ss):\n\t%s" % (lastCheckTime) )
        self.Cout("Time elapsed since last check:\n\t%s days, %s hours, %s minutes, %s seconds ago" % (days, hours, minutes, seconds) )

        # Decide which of the two servers to use
        if server == "cern":
            popHost = "pop.cern.ch"
            emailAddress = "@cern.ch"
            popUsername = "attikis@cern.ch"
        elif server == "gmail":
            popHost = "pop.gmail.com"
            emailAddress = "@gmail.com"
            popUsername = "alexandros.attikis@gmail.com"
        else:
            self.Cout('ERROR! The server argument %s is invalid. Please select between "cern" and "gmail". Exiting python shell.')
            print self.getEmail.__doc__
            sys.exit(1)

        # Prompt user to provide his login password
        self.Cout("Please provide your login password for %s to continue:" % (popUsername))
        popPassword = getpass.getpass("\tPassword = ")
    
        # Connect to host server using login credentials
        self.Cout("Attempting to connect to:\n\thost = %s." % (popHost))
        connection = poplib.POP3_SSL(popHost)
        connection.user(popUsername)
        connection.pass_(popPassword)
        self.Cout(connection.getwelcome())

        # Get number of messages and mailbox status: Result is tuple of 2 ints (message count, mailbox size)
        numMessages = len(connection.list()[1])
        messageCount = connection.stat()[0] 
        mailboxSize = connection.stat()[1]
        if messageCount > 0:
            self.Cout("Your inbox has %s messages in total (%s Mbytes)." % (numMessages, mailboxSize/1000000.0) )
        else:
            self.Cout("You have no mail. Exiting python shell.")
            sys.exit(1)
        
        # Get messages from server in the form of a list ([ ])
        messages = [connection.retr(i) for i in range(1, numMessages + 1)]
        
        # Concat message pieces
        messages = ["\n".join(mssg[1]) for mssg in messages]

        # Parse message into an email object. The email.parser.Parser method creates an in-memory object tree representing the email message, 
        # which can then be manipulated and turned over to a Generator to return the textual representation of the message.
        messages = [eParser.Parser().parsestr(mssg) for mssg in messages]
        
        # Loop over all messages and get subject+content of email
        for message in messages:
            sender = str(message['From'])
            subject = str(message['subject'])
            content = str(message.get_payload())
            fileName = "%s.eml" % (subject.replace(": ", "-").replace("/", "-") ) #.replace(" ", "_")
            
            # Check if email has already been saved 
            if os.path.isfile(myPath + fileName):
                continue
            else:
                try:
                    iNewMail = iNewMail+1
                    newMailFiles.append(fileName)
                    saveFile = open(myPath + fileName, "w")
                    saveFile.write( "From: %s" % (sender) )
                    saveFile.write( "\n")
                    saveFile.write( "Subject: %s" % (subject) )
                    saveFile.write( "\n")
                    saveFile.write( "Content: %s" % (content) )
                finally:
                    saveFile.close()
                
        if iNewMail > 0:
            self.Cout("You have %s NEW mails:\n\t%s" % (iNewMail, [item for item in newMailFiles]) )
            self.Cout('Saving NEW mail to "%s":' % (myPath))
        else:
            self.Cout("No NEW mail.")

        # Before exiting save a time-stamp file to keep track of last time I checked my email
        try:
            fileName = "timestamp.txt"
            self.Cout('Updating time-stamp file "%s".' % (myPath + fileName) )
            newTimeStampFile = open(myPath + fileName, "w")
            newTimeStampFile.write(str(today))
        finally:
            newTimeStampFile.close()
    
        # Before closing program ask user if he wants to open the new emails for the user
        openMail = self.Cin('To open NEW mail press "y"')
        if openMail == "y":
            self.Cout('Paging NEW emails. Press "q" to read the next email.')
            for mail in newMailFiles:
                myNewMail = open(myPath + mail, "r")
                pydoc.pager(myNewMail.read()) # similar to | less in shell. Press "q" to move to next email
        self.Cout('Done! Exiting python shell.')
        connection.quit()


    def getEmailImap(self, server):
        ''' getEmail(host_server):
        This module is a simple interface to check for new emails in the inbox of Gmail or CERN imap servers. 
        This is a simple example of how to use the IMAP protocol to receive emails. As I understand, the IMAP protocol is more involved in the python libraries 
        than the POP3 analogue, with more complicated/obscure modules. It does however offer a mean of accessing unread email, unlike the POP3 protocol for which I had to 
        create a time-stamp support to know when it was the last time I checked my inbox. Nevertheless, at present I prefer POP3.
        '''
        # Import modules here
        import python_myFunctions as myFunctions
        import imaplib
        import email
        import traceback
        import sys
        import getpass 
        import time 
        from datetime import datetime
        from dateutil import parser 
        import os
        import pydoc
        
        # Declaration here
        f = myFunctions.CreateObject()
        newMailFiles = []
        myPath = "/Users/administrator/my_work/programming/python/inbox/" + server + "/imap/"
        
        # Decide which of the two servers to use
        if server == "cern":
            imapHost = "imap.cern.ch"
            emailAddress = "@cern.ch"
            imapUsername = "attikis@cern.ch"
        elif server == "gmail":
            imapHost = "imap.gmail.com"
            emailAddress = "@gmail.com"
            imapUsername = "alexandros.attikis@gmail.com"
        else:
            self.Cout('ERROR! The server argument %s is invalid. Please select between "cern" and "gmail". Exiting python shell.')
            print self.getEmail.__doc__
            sys.exit(1)
            
        # Prompt user to provide his login password
        self.Cout("Please provide your login password for %s to continue:" % (imapUsername))
        imapPassword = getpass.getpass("\tPassword = ")

        # Connect to IMAP host server over SSL using login credentials
        self.Cout("Attempting to connect to:\n\thost = %s." % (imapHost))
        connection = imaplib.IMAP4_SSL(imapHost)
        connection.login(imapUsername, imapPassword)
        self.Cout("Connecting to INBOX.")
        print connection.select("INBOX", readonly=True) # connect to inbox.
        self.Cout(connection.welcome)

        # Search messages on server "INBOX" [search(self, charset, *criteria)] and get total number of messages in mailbox (both seen and unseen)
        AllMail = connection.search(None, "ALL")[1][0].split()  # returns a nice list of messages
        UnseenMail = connection.search(None, "UNSEEN")[1][0].split()  # returns a nice list of messages
        numAllMail = len(AllMail)
        numUnseenMail = len(UnseenMail)
        self.Cout( "You have %s messages (%s NEW) in your inbox." % (numAllMail, numUnseenMail) )

        # Loop over all messages and write them down to files
        self.Cout('Saving NEW mail to "%s":' % (myPath))
        for mailId in UnseenMail:
            try:
                fileName = "%s.eml" % (mailId)
                newMailFiles.append(fileName)
                saveFile = open(myPath + fileName, "w")
                mailBody = connection.fetch(mailId, '(RFC822)')[1][0][1]
                saveFile.write(mailBody)
            finally:
                saveFile.close()
        self.Cout("\t%s" % ([item for item in newMailFiles]) )

        # Before closing program ask user if he wants to open the new emails for the user
        openMail = self.Cin('To open NEW mail press "y"')
        if openMail == "y":
            self.Cout('Paging NEW emails. Press "q" to read the next email.')
            for mail in newMailFiles:
                myNewMail = open(myPath + mail, "r")
                pydoc.pager(myNewMail.read()) # similar to | less in shell. Press "q" to move to next email
        self.Cout('Done! Exiting python shell.')
        connection.logout()


    def sendEmail(self, server):
        ''' sendEmail(host_server):
        This module is a simple interface to send emails (with attachments) using the gmail or cern SMTP servers. When calling the module the only thing that needs 
        to be specified is which server is to be used (cern or gmail). Just follow the prompt commands once launched. The "smtplib" is a low-level package interface 
        for the Simple Mail Transfer Protocol (SMTP) protocol. The "email" package assists with parsing (analyzing a sentence into its parts and describe their 
        syntactic roles) and  generating emails.
        '''

        # Import modules here
        import traceback
        import email
        from smtplib import SMTP
        from email.MIMEText import MIMEText
        from email.MIMEMultipart import MIMEMultipart
        from email.MIMEBase import MIMEBase
        from email import encoders
        import mimetypes
        import sys
        import datetime
        import getpass 
        
        # Define SMTP port to use and decide which of the two servers to use
        smtpPort = 587 #or 25
        if server == "cern":
            smtpHost = "smtp.cern.ch"
            emailAddress = "@cern.ch"
            smtpUsername = "attikis@cern.ch"
        elif server == "gmail":
            smtpHost = "smtp.gmail.com"
            emailAddress = "@gmail.com"
            smtpUsername = "alexandros.attikis@gmail.com"
        else:
            self.Cout('ERROR! The server argument %s is invalid. Please select between "cern" and "gmail". Exiting python shell.')
            print self.getEmail.__doc__
            sys.exit(1)
        
        # Get SMTP authorisation details
        self.Cout("Please provide your login credentials for %s to continue:" % (smtpUsername) )
        sender = smtpUsername
        smtpPassword = getpass.getpass("\tPassword = ")

        # Connect to host using specified port
        self.Cout("Attempting to connect to:\n\thost = %s\n\tport = %s" % (smtpHost, smtpPort))
        connection = SMTP(host=smtpHost, port=smtpPort)
        connection.set_debuglevel(False) #True
        if smtpUsername is not False:
            connection.ehlo()
            if smtpPort != 25:
                connection.starttls()
                connection.ehlo()
                if smtpUsername and smtpPassword:
                    connection.login(smtpUsername, smtpPassword)
                    self.Cout("Succesfully logged on to:\n\tusername = %s\n\tpassword = %s" % (smtpUsername, self.obscureString(smtpPassword)))
                else:
                    self.Cout("Unsuccesfull login. False credentials provided:\n\tusername = %s\n\tpassword = %s" % (smtpUsername, self.obscureString(smtpPassword)))
                    print __doc__
                    sys.exit(1)

        # Get user input regarding email details
        self.Cout("Please provide the email details:")
        recipients = raw_input("\tTo: ")
        Cc = raw_input("\tCc: ")
        Bcc = raw_input("\tBcc (self excluded): ")
        subject = raw_input("\tSubject: ")
        content = raw_input("\tContent: ")
        attachment = raw_input("\tAttachment: ")
        if attachment == "":
            self.Cout("Nothing to attach.")
            bAttach = False
        else:
            self.Cout("Attachment file:\n\t%s" % (attachment) )
            bAttach = True
    
        # Define return value as success == 0,  failure == 1
        retVal = 1
        # Take care of recipient lists
        if not(hasattr(recipients, "__iter__")):
            recipients = [recipients]
        if not(hasattr(Cc, "__iter__")):
            Cc = [Cc]
        if not(hasattr(Bcc, "__iter__")):
            Bcc = [Bcc]
            Bcc.append(smtpUsername)
            
        # Define message details, including attachments
        try:
            if bAttach == False:
                text_subtype = 'plain'
                mainMsg = MIMEText(content, text_subtype)
            else:
                mainMsg = MIMEMultipart()
                # Guess the type of a file based on its filename or URL, given by url. 
                ctype, encoding = mimetypes.guess_type(attachment)
                print "ctype, encoding = %s, %s" % (ctype, encoding)
                maintype, subtype = ctype.split("/", 1)
                print "maintype, subtype = %s, %s" % (maintype, subtype)

            # The following do not depend on attachment
            mainMsg['From'] = sender # Some SMTP servers will do this automatically, but not all
            mainMsg['To']   = ", ".join(recipients)
            mainMsg['cc']   = ", ".join(Cc)
            mainMsg['Bcc']  = ", ".join(Bcc)
            mainMsg['Subject'] = subject
        
            # Send emails body and attachments
            self.Cout("Sending email to %s" % (recipients) )
            try:
                if bAttach:
                    mainMsg.attach(subMsg)
                    fp = open(attachment, "rb") # open attachment in read/binary mode
                    subMsg = MIMEBase(maintype, subtype)
                    subMsg.set_payload(fp.read())
                    fp.close()
                    encoders.encode_base64(subMsg)
                    subMsg.add_header("Content-Disposition", "attachment", filename=attachment)
                    mainMsg.attach(MIMEText(content))
                # Connect to server and send complete email
                connection.sendmail( sender, recipients+Cc+Bcc, mainMsg.as_string() )
                retVal = 0 # (success)
            except Exception, e:
                self.Cout("Got %s %s.\n\tShowing traceback:\n%s" % (type(e), e, traceback.format_exc()))
                retVal = 1 # (failure)
                print self.sendEmail.__doc__
            finally:
                self.Cout("Closing connection.")
                connection.close()
        
        except Exception, e:
            self.Cout("Got %s %s.\n\tShowing traceback:\n%s" % (type(e), e, traceback.format_exc()))
            retVal = 1 # (failure)
            print self.sendEmail.__doc__
            
        return retVal


    def StopWatchStart(self):
        self.TimeStart = datetime.now()


    def StopWatchStop(self):
        self.TimeStop = datetime.now()
        elapsedTime = self.TimeStop - self.TimeStart
        days = elapsedTime.days
        hours   = int((elapsedTime.seconds - elapsedTime.seconds%3600.0) / 3600)
        minutes = int((elapsedTime.seconds - hours*3600) / 60)
        seconds = elapsedTime.seconds - hours*3600 - minutes*60.0
        self.Cout("Done! Script Execution time:\n\t%s days, %s hours, %s minutes, %s seconds." % (days, hours, minutes, seconds) )
    
    # This function check if a local path is a directory.
    def EnsureIsDir(self, path):
        d = os.path.dirname(path)
        if not os.path.exists(d):
            os.makedirs(d)
        
    # This function checks if a remote path is a directory.
    def IsRemoteDir(self, sftp, remotePath):
        from stat import S_ISDIR
        try:
            return S_ISDIR(sftp.stat(remotePath).st_mode)
        except IOError:
            # Path does not exist, so by definition not a directory
            return False

    # This function checks if a local path is a directory.
    def IsLocalDir(self, path):
        if os.path.isdir(path):
            return True
        else:
            return False

# This function checks if a local path is a directory.
    def IsDir(self, path):
        if os.path.isdir(path):
            return True
        else:
            return False

# This function checks if a remote path is a directory.
    def IsFile(self, path):
        if os.path.isfile(path):
            return True
        else:
            return False

# This function creates a progress bar and continuously updates it. Call this function before executing a potentially long function/module.
    def StartProgressBar(self, maxValue):
        import progressbar
        widgets = [progressbar.FormatLabel(''), ' ', progressbar.Percentage(), ' ', progressbar.Bar('/'), ' ', progressbar.RotatingMarker()]
        pBar = progressbar.ProgressBar(widgets=widgets, maxval=maxValue)
        def CallBack(transferred, total):
            if pBar.start_time is None:
                pBar.start()
            pBar.update(transferred)
            return
        return pBar, CallBack

# This function tells the progress bar when to stop. Call this function right after executing the potentially long function/module.
    def StopProgressBar(self, pBar):
        pBar.finish()


    def WalkPaths(self, path):
        '''
        Returns a list of the path to all files in a directory and all sub-directories, recursively.
        '''
        import os
        path_collection = []
        # For each directory in the tree rooted at directory "path" (including "path" itself), the os.walk(path) yields a 3-tuple (dirpath, dirnames, filenames).
        for dir_path, dir_names, file_names in os.walk(path):
            #self.Cout( 'Files found in path "%s":' % (dir_path) )
            if len(file_names) == 0:
                 #print "\tNo file found."
                continue
            else:
                for file in file_names:
                    #print "\t%s" % (file)
                    full_path = os.path.join(dir_path, file)
                    path_collection.append(full_path)
                    
        return path_collection


    def WalkFiles(self, path):
        ''' 
        Returns a list of all the files in a directory. Does exactly the same thing as the WalkPaths(path) function, but instead of the full path it only prints the standalone
        file name.
        '''
        import os
        file_collection = []
        # For each directory in the tree rooted at directory "path" (including "path" itself), the os.walk(path) yields a 3-tuple (dirpath, dirnames, filenames).
        for dir_path, dir_names, file_names in os.walk(path):
            #self.Cout( 'Files found in path "%s":' % (dir_path) )
            if len(file_names) == 0:
                #print "\tNo file found."
                continue
            else:
                for file in file_names:
                    #print "\t%s" % (file)
                    file_collection.append(file)
                
        return file_collection


    def WalkDir(self, path):
        '''
        Returns a list of all the directories in a given directory.
        ''' 
        import os
        dir_collection = []
        # For each directory in the tree rooted at directory "path" (including "path" itself), the os.walk(path) yields a 3-tuple (dirpath, dirnames, filenames).
        for dir_path, dir_names, file_names in os.walk(path):
            #self.Cout( 'Directories found in path "%s":' % (dir_path) )
            if len(dir_names) == 0:
                continue #print "\tNo dir found."
            else:
                for dir in dir_names:
                    #print "\t%s" % (dir)
                    dir_collection.append(dir)
                    
        return dir_collection


    def md5Checksum(self, path):
        '''
        Reads in file and creates checksum of file, line by line. Returns a complete checksum total for file.
        '''
        import hashlib
        file = open(path)
        checksum = hashlib.md5()
        while True:
            # Read the files in 8192 byte chunks. Thus, at any given time this function is using little more than 8 kilobytes of memory.
            buffer = file.read(8192)
            # Break if there is nothing left to read from the file
            if not buffer:
                break
            # Update the hash object with the string argument. Repeated calls are equivalent to a single call with the concatenation of all the arguments.
            checksum.update(buffer)
        file.close()
        # Return the digest of the strings passed to the update() method so far.
        checksum = checksum.digest()
        return checksum


    def CompareFiles(self, fileName1, fileName2):
        '''
        Uses CreateChecksum(self, path) function to see whether two files are identical or not. Returns boolean.
        '''
        bFilesAreSame = False
        # Open files to enable reading them
        file1 = open(fileName1)
        file2 = open(fileName2)
        
        # Create checksum objects
        checksum1 = self.md5Checksum(fileName1)
        checksum2 = self.md5Checksum(fileName2)
        if checksum1 == checksum2:
            bFilesAreSame = True
            #self.Cout("Files %s and %s are identical." % (fileName1, fileName2) )
        else:
            bFilesAreSame = False
            #self.Cout("Files %s and %s are different." % (fileName1, fileName2) )
            
        return bFilesAreSame


    def FindDuplicateFiles(self, path):
        ''' 
        This function performs an md5 checksum on a directory tree to find file duplicates. It returns two lists of files that were found to be duplicated, 
        containing their full path.
        '''
        # Create empty lists and dictionaries here
        dupList = []
        dupListMatch = []
        record = {}
        
        # Perform walk on input "path" to get the list paths for the directory tree
        pathList = self.WalkPaths(path)
        
        # Use progress bar to know how much time is left to finish
        maxValue = len(pathList)
        pBar, CallBack = self.StartProgressBar(maxValue)
        
        # Loop over all paths and create a dictionary, mapping a unique key to the fileName
        for index, fileName in enumerate(pathList):
            # Create a compound key (size, checksum) for file under investigation
            key = ( os.path.getsize(fileName), self.md5Checksum(fileName) )
            
            # Check if the generate key(size, checksum )is found in the record. If yes add file into the duplicate list and matching duplicate file in the mathcing duplicate list
            if key in record:
                dupList.append(fileName)
                dupListMatch.append(record[key])
            else: # If key is not found in record add it to it
                record[key] = fileName
            # Update progress bar
            CallBack(index, maxValue)

        self.StopProgressBar(pBar)
        return dupList, dupListMatch

    
    def DeleteFile(self, path):
        '''
        This very simple function delete the input parameter file. Warning! This is silent and permanent, so use with great caution!
        '''
        import os

        rawInput = self.Cin('Delete file:\n\t"%s"?' % (path) )
        if rawInput == "y":
            os.remove(path)
            self.Cout('Deleted "%s".' % (path) )
        else:
            self.Cout("Deleting file:\n\t%s" % (path) )

        
    def CreateFile(self, path, fileName, nLines):
	'''
        Create a dumbie text file. For educational purposes.
        '''      
        # First check that dir exists. If not, create it.
        self.EnsureIsDir(path)

        # Then create fileName on the specified path
	fullPath = path + fileName
        try:
            file = open(fullPath, "w")
            # For loop here to write a few number of lines on the text file.
            for i in range(1, nLines):
                string = "Line %s. This is a dumbie txt file.\n" % (i)
                file.write(string)
        finally:
            file.close()
        self.Cout("Created file %s." % (fullPath))

        
    def FindFiles(self, path, fileName):
        ''' 
        Looks for a file in a specified dir tree. Returns a list containing all the matching paths!
        '''
        from fnmatch import fnmatch
        
        # First Walk the dir tree of the specified path and create list of all files
        fileList = self.WalkFiles(path)
        pathList = self.WalkPaths(path)
        matchList = []

        # Loop over the file list 
        for index, file in enumerate(fileList):
            if fnmatch(file, fileName):
                #self.Cout("Found file:\n\t%s" % (pathList[index]) )
                matchList.append(pathList[index])
                
        return matchList


    def RenameFiles(self, path, fileExt, fileExtNew):
        ''' 
        Looks for a certain file extension in a specified dir tree. Renames all files to a new file extension.
        '''
        import shutil

        # Get the list of files matching the specified extension
        findList = self.FindFiles(path, "*"+fileExt)
        
        # Rename all matching files to the new file extension
        for file in findList:
            self.Cout( "Moving file %s to %s." % (file, file.replace(fileExt, fileExtNew)))
            shutil.move( file, file.replace(fileExt, fileExtNew) )
            
    def Rsync(self, source, target):
        '''
        This module can be used to "rsync" target directory tree with a source directory tree. In case of failure it prints out a failure message.
        '''
        import subprocess
        import sys
        import os
        
        # Declarations here
        rsync = "rsync"
        # Option definition:
        # -a = archive mode; a shortcut to skip having to enter a bunch of switches that you'll normally use if you're using rsync to make backups (a common task).
        # -v = increase verbosity
        # --delete = delete extraneous (unrelated) files from destination directories
        argument = "-av --delete"
        cmd = "%s %s %s %s" % (rsync, argument, source, target)

        # Before executing command, check if the target and source directories exist
        if self.IsDir(source) == False:
            self.Cout("ERROR! The source directory %s does not exist. Please read docstrings. Exiting python shell." % (source))
            print self.rsync.__doc__
            sys.exit(1)
        if self.IsDir(target) == False:
            self.Cout("ERROR! The target directory %s does not exist. Please read docstrings. Exiting python shell." % (target))
            print self.rsync.__doc__
            sys.exit(1)

        # Execute rsync shell command
        retVal = subprocess.call(cmd, shell=True)

        # Make sure you handle errors
        if retVal !=0:
            self.Cout("Rsyncing of target %s with source %s failed. Please read docstrings. Exiting python shell.")
            print self.rsync.__doc__
            sys.exit(1)
        else:
            self.Cout("Rsync of target %s with source %s was succesful." % (target, source))

        return retVal
            
    def Rsync2(self, source, target):
        '''
        This module can be used to "rsync" target directory tree with a source directory tree. It will not quite until it is finished. 
        In case of failure it prints out a failure message. 
        '''
        import subprocess
        import sys
        import os
        import time 
        
        # Declarations here
        rsync = "rsync"
        argument = "-av"
        cmd = "%s %s %s %s" % (rsync, argument, source, target)

        # Before executing command, check if the target and source directories exist
        if self.IsDir(source) == False:
            self.Cout("ERROR! The source directory %s does not exist. Please read docstrings. Exiting python shell." % (source))
            print self.rsync.__doc__
            sys.exit(1)
        if self.IsDir(target) == False:
            self.Cout("ERROR! The target directory %s does not exist. Please read docstrings. Exiting python shell." % (target))
            print self.rsync.__doc__
            sys.exit(1)

        # Execute rsync shell command
        while True:
            retVal = subprocess.call(cmd, shell=True)
            # Make sure you handle errors
            if retVal !=0:
                self.Cout("Rsyncing of target %s with source %s failed. Resubmitting rsync command.")
                time.sleep(30)
            else:
                message = "Rsync of target %s with source %s was succesful." % (target, source)
                self.Cout(message)
                self.sendEmail("cern")
                #subprocess.call("mail -s '%s' %s" % (message, email), shell = True) %doesn't work. it hungs. why?
                sys.exit(0)                
        return retVal

                
    def CreateTarball(self, myPath, tarballName, cType = "tar"):
        '''
        This module can be used to create a tarball of a given directory tree. 
        The compression type (cType) can either be default "w", or the powerful (yet slow and cpu-demanding bzip2.
        Available compression types (extensions): w (.tar), w|bz2 (.tar.bzip2), w|gz (.tar.gzip)
        '''
        import tarfile
        import os
        import subprocess
        import sys

        # Make a list of available compression types (extensions): w (.tar), w|bz2 (.tar.bzip2), w|gz (.tar.gzip)
        cTypeList = {}
        cTypeList["tar"] = "w"
        cTypeList["bzip2"] = "w|bz2"
        cTypeList["gzip"] = "w|gz"

        # First check that cType is valid, by looping over dictionary
        if not cTypeList.has_key(cType):
            self.Cout("ERROR! Unknown TAR archive type. Printing available formats:")
            for key in cTypeList:
                print "\t" + key + " (" + cTypeList[key] + ")"
            sys.exit(1)

        # Make sure path ends with a "/" symbol
        if not myPath.endswith("/"):
            myPath = myPath + "/"

        # Chck that target directory in fact exists. If yes create a path list of all files in the directory tree
        if self.IsDir(myPath) == False:
            self.Cout("ERROR! The path %s does not exist. Please read docstrings. Exiting python shell." % (myPath))
            print self.CreateTarball.__doc__
            sys.exit(1)
        else:
            pathList = self.WalkPaths(myPath)
    
        # Create tarball    
        fullTarballName = myPath+tarballName+"."+cType
        self.Cout("Creating tarball %s." % (fullTarballName) )            
        tarball = tarfile.open(fullTarballName,  cTypeList[cType])

        # Loop over all files and add them to the tarball
        for file in pathList:
            self.Cout("Adding file %s" % (file) )
            tarball.add(file)

        self.Cout("Tarball succesfully created:")
        subprocess.call("du -csh %s" % (fullTarballName), shell=True)
        tarball.close()
        

    def UnpackTarball(self, source, destination):
        '''
        This module can be used to untar a tarball to a given directory tree.
        '''
        import tarfile
        import os
        import subprocess
        
        # Check if myPath is in fact a tarball. Returns True if name is a tar archive file, that the tarfile module can read.
        if not tarfile.is_tarfile(source):
            self.Cout("ERROR! The specified path %s is either not a tar archive file, or one that the python tarfile module cannot read. Please read docstings. Exiting python shell." % (myPath))
            print self.UnpackTarball.__doc__
            sys.exit(1)            
        else:
            self.Cout("Attempting to unpack:\n\t %s\nto:\n\t %s" % (source, destination))
            try:
                myTarFile  = tarfile.open(source, "r")

                # Get dir listing of destination before extracting
                prevDirList = os.listdir(destination)

                # Extrall all files to destination
                myTarFile.extractall(destination)

                # Get dir listing of destination after extracting
                newDirList = os.listdir(destination)

                # Cast lists as sets in order to be able to subtract them (to find differences). Use the extracted folder for the "du -csh" command later
                diff = set(newDirList) - set(prevDirList)
                diffDirList = list(diff)
                if not diff:
                    newDir = ""
                else:
                    newDir = diffDirList[len(diffDirList)-1]
                
                # Get name of tarball file by stripping the source from the remaining path. Not needed but keep for infromative reasons
                tmpList = source.rsplit("/")
                tarballName = tmpList[len(tmpList)-1] 
                self.Cout("Tarball %s succesfully unpacked:" % (tarballName))
                subprocess.call("du -csh %s" % (destination + newDir), shell=True)

            finally:
                myTarFile.close()
    
                
    def ExamineTarball(self, source, tarballName):
        '''
        This module can be used to examine the contents of a tarball.
        '''
        import tarfile
        import os
        
        # Check if myPath is in fact a tarball. Returns True if name is a tar archive file, that the tarfile module can read.
        if not source.endswith("/"):
            source  = source + "/"
        else:
            self.Cout("Attempting to read:\n\t%s" % (source+tarballName))
            
        if not tarfile.is_tarfile(source+tarballName):
            self.Cout("ERROR! The specified path %s is either not a tar archive file, or one that the python tarfile module cannot read. Please read docstings. Exiting python shell." % (source+tarballName))
            print self.ExamineTarball.__doc__
            sys.exit(1)            
        else:
            try:
                myTarFile  = tarfile.open(source+tarballName, "r")
                self.Cout("Examining tarball:\n\t%s" % ( myTarFile.name ) )
                # Print tarball contents 
                myTarFile.list()
                self.Cout("Printing list of names:\n\t%s" % ( myTarFile.getnames() ) )
                
            finally:
                myTarFile.close()

    def SysReport(self):
        '''
        This module can be used to print a system report on any platform. Returns a dictionary object.
        '''
        import platform

        # Define a dictionary mapping command string with actual python command to perform
        profile = {
            "architecture":platform.architecture(),
            "dist":platform.dist(),
            "libc_ver":platform.libc_ver(),
            "mac_ver":platform.mac_ver(),
            "machine":platform.machine(),
            "node":platform.node(),
            "platform":platform.platform(),
            "processor":platform.processor(),
            "python_build":platform.python_build(),
            "python_compiler":platform.python_compiler(),
            "python_version":platform.python_version(),
            "system":platform.system(),
            "uname":platform.uname(),
            "version":platform.version(),
            }

        # Loop over all dictionary and print dictionary key and corresponding value
        self.Cout( "Printing system report:")
        for key in profile:
            print "\t%s = %s" % (key, profile[key] )

        return profile        

    def checkExitCode(self, exitCode):
        ''' 
        This is a simple function that prints informative statements to the user relating to the exit code of a command execution.
        '''

        # Create empty exit-code - meaning dictionary
        exitCodeDict = {
            0:"Success",
            1:"General Error",
            2:"Misuse of shell built-ins",
            126:"Command invoked cannon execute",
            #127:"Command not found",
            128:"Invalid argument to exit",
            130:"Script terminated by Ctrl-C",
            225:"Exit status out of range",
            }

        if not exitCodeDict.has_key(exitCode):
            retVal = "Failure (%s): Unknown exit code" % (exitCode)
            self.Cout(retVal)
            return retVal
        elif exitCode !=0:
            self.Cout("Failure (%s): %s" % (exitCode, exitCodeDict[exitCode]) )
        else:
            self.Cout("Success")
        
        return exitCodeDict[exitCode]

    
    def CmdPipe(self, *args):
        '''
        This module is an example of using subprocess as a piping factory. It will execute a given number of shell commands in a loop, will capture stdout and returns it.
        System administrators frequently need to run a sequence of commands, so this module enables the use of such a barrage of commands with the use of a simple code.
        '''
        import subprocess
        
        # Loop over all commands
        for cmd in args:
            self.Cout('Executing command:\n\t"%s"' % (cmd) )
            p = subprocess.Popen(cmd, shell = True, stdout = subprocess.PIPE)
            out =  p.stdout.read()
            print out
            
        return out

    
    def Runner(self, *args, **kwargs):
        '''
        This module is closely related to the python built-in subprocess module. It sequentially executes a list of commands in a simplified and automatic way, 
        while supporting verbose and delay options.
        '''
        import time
        import subprocess
        import sys
        
        # Take care of the delay argument (in seconds)
        if kwargs.has_key("delay"):
            self.Delay = kwargs["delay"]
        else:
            self.Delay = 0

        # Check whether to use verbose option or silend-mode instead
        if kwargs.has_key("verbose"):
            self.Cout("Verbose = %s" % (kwargs["verbose"]))
            self.Verbose = kwargs["verbose"]
        else:
            self.Verbose = False
                    
        # Loop over all commands and execute them
        for cmd in args:
            # Print informative message only if verbose is enabled
            if self.Verbose:
                self.Cout("Running command:\n\t%s (delay = %s)" % (cmd, self.Delay))
            
            time.sleep(self.Delay)
            subprocess.call(cmd, shell = True)
        

    def RunScreenCmd(self, cmd, pName, detach = False):
        '''
        This module is dedicated for executing shell commands with GNU screen. The screen application allows you to detach from a long-running process and come back to it at 
        any point in time. By default the process is run detached with a user-defined session name (pName), although there is an option (boolean) to run attached from which 
        one can detach at any time by pressing "Ctrl-a" "Ctrl-d". Here's some info on GNU's screen options:
        
        1. "screen -d CommandToLaunch" does not start screen, but detaches the elsewhere running screen session. It has the same effect as typing  "C-a d" from 
        
        2. "screen -d CommandToLaunch" causes  screen  to ignore the $STY environment variable. With "screen -m" creation of a new session is 
        enforced, regardless whether screen is called from within another screen session or not. This flag has a special meaning in connection with the `-d' option 
        (i.e. screen -d -m)  which starts screen in "detached" mode. This creates a new session but doesn't attach to it. This is useful for system startup scripts.
        
        3 "screen -S CommandName CommandToLaunch" means the CommandName (-S) can be used  for creating  a  new  session. This option can be used to specify a meaningful name for 
        the session. This name identifies the session for "screen -list" and "screen -r" actions. It substitutes the default [tty.host] suffix.
        '''
        import subprocess
        import os
        import time
        import sys
        
        fullCmd = "screen -dmS " + pName + " " + cmd
        reAttachCmd = "screen -r " + pName
        # Launch command 
        self.CmdPipe(fullCmd)
        
        # Ask user if he wants to re-attach session immediately. Unless he explicitly chose to detach
        if detach == False:
            # Inform user
            self.Cout('Re-attaching session %s:\n\t"%s"' % (pName, reAttachCmd))
            self.Cout('Press "Ctr-A" "Ctrl-D" at any point to detach session')
            # Delay launch for 3 seconds as "screen" will erase all stdout
            self.CountDown(3)
            # Re-attach command
            self.CmdPipe(reAttachCmd)
        else:
            self.Cout('To re-attach at any time type:\n\t"screen -r %s"' % (pName))


    def CountDown(self, seconds):
        '''
        Simple module that prints a countdown in seconds.
        '''
        import sys

        overwrite = 0        
        # Delay launch for 3 seconds as "screen" will erase all stdout
        for sec in range(seconds,0,-1):
            sys.stdout.write("Starting in: %s seconds%s\r" % (sec, " "*overwrite ))
            sys.stdout.flush()
            time.sleep(1)
            overwrite = len("seconds")

    def CountDown(self, string, seconds):
        '''
        Simple module that prints a countdown in seconds.
        '''
        import sys

        overwrite = 0        
        # Delay launch for 3 seconds as "screen" will erase all stdout
        for sec in range(seconds,0,-1):
            sys.stdout.write(string + " %s seconds%s\r" % (sec, " "*overwrite ))
            sys.stdout.flush()
            time.sleep(1)
            overwrite = len("seconds")
        print
