import socket
import dns.resolver
import dns.query
import dns.message
from pip._vendor.distlib.compat import raw_input

rootServerA = "199.7.91.13"
rootServerB = "199.9.14.20"
rootServerC = '192.33.4.12'
rootServerD = '199.7.91.13'
rootServerE = '192.203.230.10'
rootServerF = '192.5.5.241'
rootServerG = '192.112.36.4'
rootServerH = '198.97.190.53'
rootServerI = '192.36.148.17'
rootServerJ = '192.58.128.30'
rootServerK = '193.0.14.129'
rootServerL = '199.7.83.42'
rootServerM = '202.12.27.33'

rootServer = ''

#I ask the user which website they would like to query about
print("\nPlease provide the website you would like to query about: \n")
web = raw_input()
print("\nWhat query type would you like to look into: \n")
query = raw_input()


def printingLast(ipAddress):
    print ("\nANSWER SECTION:")
    print (web + "\tIN\t" + query + "\t" + ipAddress)


def printingFirst():
    print ("\nQUESTION SECTION:")
    print (web + "\tIN\t" + query)
#I test each name server to see if they work, if they do, I proceed further
#while loop till there is no end --> not name server



def myDig(ipAddress, str):

    #i get the information from the server
    answer = dns.message.make_query(str, query)
    response = dns.query.udp(answer, ipAddress)

    #types of responses
    additionalSection = response.additional
    answerSection = response.answer
    authoritativeSection = response.authority

    #counts
    answerSection_count = 0
    additionalSection_count =0
    authoritativeSection_count = 0

    #I count the lines in all the sections
    for lines in additionalSection:
        additionalSection_count = additionalSection_count + 1


    for lines in answerSection:
        answerSection_count = answerSection_count + 1
        #lines = lines.to_text().split(" ")

    currentCount = len(authoritativeSection)
    if (currentCount!=0):
        authSection = authoritativeSection[0].to_text().splitlines()
        for lines in authSection:
            authoritativeSection_count = authoritativeSection_count +1
            #lines = lines.to_text().split()

    name = ""
    #if there is something in the answer section
    if (answerSection_count >0):
        for x in answerSection:
            x = x.to_text().split(" ")
            #name = ""
            if x[3] == "CNAME":
                #print "FOUND CNMAE"
                name = x[4]
                myDig(rootServer, name)
                break
            if x[3] == "A":
                # we found the answer
                testingCount =1
                #print "WE FOUND THE ANSWER"
                #we found the answer
                printingLast(x[4])
                break

    elif(additionalSection_count>0):
        for lines in additionalSection:
            lines = lines.to_text().split(" ")
            if (lines[3]=="A"):
                ipAddress = lines[4]
                myDig(ipAddress, str)
                break
    elif((answerSection_count==0)and(additionalSection_count==0)):
        #if there is nothing in the answer section or the additional section, I check the authority section

        #print authSection
        for lines in authSection:
            lines = lines.split()
            name = lines[4]
        myDig(rootServer, name)


#myDig(rootServerA, last)
printingFirst()

try:
    rootServer = rootServerA
    myDig(rootServer, web)
except IOError:
    print ("ERROR")
    try:
        rootServer = rootServerB
        myDig(rootServerB, web)
    except IOError:
        print ("ERROR")
        try:
            rootServer = rootServerC
            myDig(rootServer, web)
        except IOError:
            try:
                rootServer = rootServerD
                myDig(rootServer, web)
            except IOError:
                try:
                    rootServer = rootServerE
                    myDig(rootServer, web)
                except IOError:
                    try:
                        rootServer = rootServerF
                        myDig(rootServer, web)
                    except IOError:
                        try:
                            rootServer = rootServerG
                            myDig(rootServer, web)
                        except IOError:
                            try:
                                rootServer = rootServerH
                                myDig(rootServer, web)
                            except IOError:
                                try:
                                    rootServer = rootServerI
                                    myDig(rootServer, web)
                                except IOError:
                                    try:
                                        rootServer = rootServerJ
                                        myDig(rootServer, web)
                                    except IOError:
                                        try:
                                            rootServer = rootServerK
                                            myDig(rootServer, web)
                                        except IOError:
                                            try:
                                                rootServer = rootServerL
                                                myDig(rootServer, web)
                                            except IOError:
                                                try:
                                                    rootServer = rootServerM
                                                    myDig(rootServer, web)
                                                except IOError:
                                                    print ("Nothing is working")



