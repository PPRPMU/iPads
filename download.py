# Something in lines of http://stackoverflow.com/questions/348630/how-can-i-download-all-emails-with-attachments-from-gmail
# Make sure you have IMAP enabled in your gmail settings.
# Right now it won't download same file name twice even if their contents are different.

import email, getpass, imaplib, os, sys, slate, shutil, re

# Will probablyl need to replace "&" with "and". Make change for all PDFs as well. iPad did not transcribe "&" correctly. Would need to make sure all forms keep same names as this list as well. Taken from list of facilities in Access.
district1 = ["Baldi", "Boyle", "Burholme Golf Center", "Burholme Park", "Chalfont", "District 1 Office", "Enfield Fields", "Fish Hatchery", "Fitzpatrick", "Fluehr Park", "Fox Chase", "Frankford & Pennypack Park", "Gifford", "Glen Foerd", "Hayes", "Holme Crispin Park", "Holmesburg", "Jacobs", "Jardel", "Junod", "Lackman", "Lincoln Pool", "Max Myers", "Mayfair", "McArdle", "Mitchell", "Northeast Lions Park", "Northeast OAC", "Palmer", "Pelbano", "Pennypack Creek Park", "Pennypack Environmental Center", "Pennypack on the Delaware", "Picariello", "Pleasant Hill Park", "Poquessing Creek Park", "Ramp", "Russo Park", "Somerton Woods", "Tarken", "Thomas Holme", "Torresdale", "Trumbette", "Frankford and Pennypack Park"]
district2 = ["American Legion", "Benson Park", "Bridesburg", "Campbell Square", "Carmella", "Cione", "Cohocksink", "Cruz", "Disston", "Disston Park", "District 2 Office", "Dorsey", "Fishtown", "Franklin", "Gambrel", "Glavin", "Hancock", "Harrowgate Park", "Hart Park", "Hedge Street Park", "Heitzman", "Hetzell", "Konrad Square", "Lardner's Point", "Lederer Pool", "Lower Mayfair", "McIlvain", "Monkiewicz", "Moss", "Mullin", "Northern Liberties", "Pop's Playground", "Pulaski Park", "Roosevelt", "Samuel", "Shissler", "Stokely", "Tip Top", "Trenton & Auburn Playground", "Vogt", "Webb Street Play Lot", "Wilmot Park Playground", "Wissinoming", "Trenton & Auburn Playground"]
district3 = ["12th & Cambria", "Barrett", "Butler & Percy Play Lot", "Cherashore", "Clarkson Park", "Daly Park", "Deni", "District 3 Office", "Feltonville", "Ferko", "Fisher Park", "Hissey", "Hope Park", "Houseman", "Hunting Park", "Juniata Park OAC", "Lauretha Vaird Boys/Girls Club", "Lawncrest", "Maguire", "Mann OAC", "McVeigh", "Merrit Square", "Nicetown Park", "Northwood Park", "Olney", "Overington Park", "Piccoli", "Ramblers", "Reed", "Rivera", "Ross Park", "Scanlon", "Schmidt", "Shevchenko Park", "Simpson", "Sturgis", "Tacony Creek Park", "Wissahickon", "Womrath Park", "Ziehler", "12th and Cambria", "Butler and Percy Play Lot",]
district4 = ["20th & Tioga", "20th & Tioga Ballfield", "22nd & Ontario", "22nd & Ontario Playground", "Al Pearlman Sports Center", "Allens Lane Art Center", "Arrow Field", "Awbury", "Belfield", "Blue Bell Park", "Boone Park", "Boyce Field", "Bringhurst Park", "Buckley Park", "Carpenter's Woods", "Clifford Park", "Cliveden Park", "Cloverly Park", "Daisy Fields", "District 4 Office", "Emanuel", "Fairview Park", "Fernhill Park", "Finley", "Gilbert Stuart Park", "Gorgas Park", "Gustine", "Happy Hollow", "Harper's Hollow Park", "Heritage Park", "Hillside", "Houston", "Howell Park", "Inn Yard Park", "Jerome Brown", "Kay Park", "Kelly Park", "Kemble Park", "Kendrick", "La Noce Park", "Lonnie Young", "Loudoun Park", "Mallery", "Market Square Park", "McDevitt", "McMichael Park", "Morris Estate", "Morton", "Mount Airy", "Ned Wolf Park", "Newhall Park", "Old Line Park", "Pachella Fields", "Pastorius Park", "Pickett School Pool", "Pleasant", "Pretzel Park", "Roxborough Reservoir", "Simons", "Stenton Park", "Umbria Golf Center", "Venice Island", "Vernon Park", "Water Tower", "Waterview", "West Oak Lane Senior Center", "Winston Park", "Wissahickon East", "Wissahickon Environmental Center", "Wissahickon Neighbors", "Wissahickon Valley Park", "Wister", "Wister's Woods Park", "Wolf Park", "20th and Tioga", "20th and Tioga Ballfield", "22nd and Ontario", "22nd and Ontario Playground"]
district5 = ["26th & Pennsylvania Playground", "33rd & Oxford Basketball Court", "51st & Parkside", "Aviator Park", "Belmont & Edgely Fields", "Belmont Grove", "Belmont Plateau Fields", "Belmont Plateau Recreation Area", "Benjamin Franklin Parkway", "CASE Building", "Chamounix North Fields", "Chamounix North Tennis Courts", "Chamounix South Fields", "Coxe Park", "Dairy Fields", "Delancey Park", "Edgely Fields", "Fitler Square", "Ford Road North Playground", "Franklin Square", "George's Hill", "Kahn Park", "Korean War Veteran's Memorial", "Lemon Hill Fields", "Lemon Hill Mansion", "Logan Square", "Matthias Baldwin Park", "Memorial Hall Fields", "Ohio House Fields", "One Parkway Building", "Reliance Park", "Rittenhouse Square", "River Field", "Sedgley Woods", "Smith Memorial", "Stewardship Office", "Sweetbriar Fields", "Von Colln Field", "Water Works", "West Park", "26th and Pennsylvania Playground", "33rd and Oxford Basketball Court", "51st and Parkside", "Belmont and Edgely Fields"]
district6 = ["10th & Lemon Playground", "11th & C.B. Moore", "30th & Jefferson", "3rd & Norris", "8th & Diamond", "Amos", "Athletic", "Brewerytown Community Garden", "C.B. Moore", "Cassiano Fields", "Clemente", "Dendy", "Diamond Park", "District 6 Office", "Duckrey School Playground", "East Poplar", "East Poplar Field", "Etting Square", "Fairhill Square", "Fotteral Square", "Francisville", "Gathers", "Hagert Playground", "Hartranft Pool", "Lloyd Hall", "M.L. King", "M.L. King OAC", "Mander", "McPherson Square", "Montgomery & Croskey", "Nelson", "Norris Square", "Palmer Park", "Panati", "Penn Treaty Park", "Penrose", "Powers Park", "Reyburn Park", "Shuler", "Strawberry Mansion Playground", "Towey", "Veterans Playground", "Waterloo", "Winchester", "10th and Lemon Playground", "11th and C.B. Moore", "30th and Jefferson", "3rd and Norris", "8th and Diamond", "Montgomery and Croskey"]
district7 = ["22nd & Catherine Park", "Anderson", "Bainbridge Green", "Bardascino Park", "Barry", "Beck Park", "Burke", "Burke Playground", "Capitolo", "Chew", "Cianfrani Park", "Columbus Square", "D. Finnegan", "Dickinson Square", "DiSilvestro", "District 7 Office", "East Passyunk Community Recreation Center", "FDR  Park Boathouse", "FDR Park", "Ford", "Gold Star Park", "Gray's Ferry Crescent", "Greble Post (War Memorial)", "Guerin", "Hawthorne", "Hawthorne Park", "Herron", "Howard & Reed Park", "Jefferson Square", "Lanier", "Manton Street Park", "Marconi Plaza", "Mario Lanza Park", "Markward", "Mifflin Square", "Mollbore Terrace Park", "Murphy", "O'Connor Pool", "Palumbo", "Palumbo Park", "Paolone Park", "Ralph Brooks Park", "Ridgway Pool", "Rizzo Rink", "Sacks", "Seger", "Shot Tower", "Sims", "Smith", "South Philadelphia OAC", "Starr Garden", "Stinger Square", "Vare", "Weccacoe", "Weinberg Park", "Wharton Square", "22nd and Catherine Park", "Howard and Reed Park"]
district8 = ["33rd & Wallace", "33rd & Wallace Playground", "37th & Mt. Vernon", "39th & Olive", "45th & Sansom Tot Lot", "48th & Woodland", "60th & Baltimore Park", "63rd & Lindbergh", "63rd & Lindbergh Park", "75th & Chelwynde", "Baker", "Ben Barkan Park", "Buist Park", "Carousel House", "Carroll Park", "Cedar Park", "Christy", "Cibotti", "Clark Park", "Clayborn & Lewis", "Clearview Park", "Cobbs Creek", "Cobbs Creek Environmental Education Center", "Conestoga", "Connell Park", "Conshohocken", "Deritis Playground", "District 8 Office", "Eastwick Park", "Eastwick Regional", "Elmwood Park", "Garden Court Tennis Courts", "Granahan", "Horticulture Center", "Horton Street Play Lot", "J. Finnegan", "John Anderson", "Julian Abele Park", "Kelly Pool", "Kingsessing", "Laura Sims", "Lee Cultural Center", "Malcolm X Memorial Park", "McCreesh", "Miles Mack", "Mill Creek", "Morris Park", "Muhammad Square", "Myers", "Nichols Park", "Papa", "Parkside Evans", "Pepper", "Philly Pumptrack", "Rose", "Rose Playground", "Sayre Morris", "Shepard", "Sherwood Park", "Triangle Park", "Tustin", "West Mill Creek", "Woodside Park", "Wright", "33rd and Wallace", "33rd and Wallace Playground", "37th and Mt. Vernon", "39th and Olive", "45th and Sansom Tot Lot", "48th and Woodland", "60th and Baltimore Park", "63rd and Lindbergh", "63rd and Lindbergh Park", "75th and Chelwynde", "Clayborn and Lewis"]

all_districts = []
all_districts.append(district1)
all_districts.append(district2)
all_districts.append(district3)
all_districts.append(district4)
all_districts.append(district5)
all_districts.append(district6)
all_districts.append(district7)
all_districts.append(district8)

filed = False

detach_dir = '.'
if 'attachments' not in os.listdir(detach_dir):
    os.mkdir('attachments')

userName = raw_input('Enter your GMail username:')
passwd = getpass.getpass('Enter your password: ')

try:
    imapSession = imaplib.IMAP4_SSL('imap.gmail.com')
    typ, accountDetails = imapSession.login(userName, passwd)
    if typ != 'OK':
        print 'Not able to sign in!'
        raise
    
    imapSession.select('[Gmail]/All Mail')
    typ, data = imapSession.search(None, 'ALL')
    if typ != 'OK':
        print 'Error searching Inbox.'
        raise
    
    # Iterating over all emails
    for msgId in data[0].split():
        typ, messageParts = imapSession.fetch(msgId, '(RFC822)')
        if typ != 'OK':
            print 'Error fetching mail.'
            raise

        emailBody = messageParts[0][1]
        mail = email.message_from_string(emailBody)
        for part in mail.walk():
            if part.get_content_maintype() == 'multipart':
                # print part.as_string()
                continue
            if part.get('Content-Disposition') is None:
                # print part.as_string()
                continue
            fileName = msgId + "-" + part.get_filename()
            # Using slate to extract text and compare text to sort file into the correct folder.

            # Open PDF, extract text in 'pdf', convert text to string in 'text', turn it into a list and remove line breaks with 'field_list'.
            with open(fileName) as f:
                pdf = slate.PDF(f)
                text = str(pdf)
                field_list = text.split("\\n")

            # If statement, checks if title of form is true. First form is Aquatics Audit Control.
            if re.search("AQUATICS AUDIT CONTROL", text):
                # Searches through each district, j, and looks at each facility, i, until file is moved.
                while filed == False:
                    for j in all_districts:
                        district_number = all_districts.index(j) + 1
                        for i in j:
                            for k in field_list:
                                district_number = all_districts.index(j) + 1
                                if i == k:
                                    print "Facility is " + i
                                    rename = str(msgId) + "-" + i + "-" + fileName
                                    shutil.move(fileName, 'iPads/Forms/Aquatics/District ' + str(district_number) + "/" + rename)
                                    print "Aquatics Audit Control for " + i + " moved to District " + str(district_number) + " folder."
                                    filed = True
                                    break

            # Second Form: Site Visit Report                 
            elif re.search("Site Visit Report", text):
                # Searches through each district, j, and looks at each facility, i, until file is moved.
                while filed == False:
                    for j in all_districts:
                        district_number = all_districts.index(j) + 1
                        for i in j:
                            for k in field_list:
                                district_number = all_districts.index(j) + 1
                                if i == k:
                                    print "Facility is " + i
                                    rename = str(msgId) + "-" + i + "-" + fileName
                                    shutil.move(fileName, 'iPads/Forms/SVR/District ' + str(district_number) + "/" + rename)
                                    print "Site Visit Report for " + i + " moved to District " + str(district_number) + " folder."
                                    filed = True
                                    break

            # If form is not recognized, move file to Forms folder
            else:
                while filed == False:
                    for j in all_districts:
                        district_number = all_districts.index(j) + 1
                        for i in j:
                            for k in field_list:
                                district_number = all_districts.index(j) + 1
                                if i == k:
                                    print "Facility is " + i
                                    rename = str(msgId) + "-" + i + "-" + fileName
                                    shutil.move(fileName, 'iPads/Forms/' + rename)
                                    print "File not recognized for " + i + " moved to Forms folder."
                                    filed = True
                                    break
                
            if bool(fileName):
                filePath = os.path.join(detach_dir, 'attachments', fileName)
                if not os.path.isfile(filePath) :
                    print fileName
                    fp = open(filePath, 'wb')
                    fp.write(part.get_payload(decode=True))
                    fp.close()
                
    imapSession.close()
    imapSession.logout()
except :
    print 'Not able to download all attachments.'