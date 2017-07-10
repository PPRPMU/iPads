import slate
import shutil

district1 = ["Baldi", "Boyle", "Burholme Golf Center", "Burholme Park", "Chalfont", "District 1 Office", "Enfield Fields", "Fish Hatchery", "Fitzpatrick", "Fluehr Park", "Fox Chase", "Frankford & Pennypack Park", "Gifford", "Glen Foerd", "Hayes", "Holme Crispin Park", "Holmesburg", "Jacobs", "Jardel", "Junod", "Lackman", "Lincoln Pool", "Max Myers", "Mayfair", "McArdle", "Mitchell", "Northeast Lions Park", "Northeast OAC", "Palmer", "Pelbano", "Pennypack Creek Park", "Pennypack Environmental Center", "Pennypack on the Delaware", "Picariello", "Pleasant Hill Park", "Poquessing Creek Park", "Ramp", "Russo Park", "Somerton Woods", "Tarken", "Thomas Holme", "Torresdale", "Trumbette"]
district2 = ["American Legion", "Benson Park", "Bridesburg", "Campbell Square", "Carmella", "Cione", "Cohocksink", "Cruz", "Disston", "Disston Park", "District 2 Office", "Dorsey", "Fishtown", "Franklin", "Gambrel", "Glavin", "Hancock", "Harrowgate Park", "Hart Park", "Hedge Street Park", "Heitzman", "Hetzell", "Konrad Square", "Lardner's Point", "Lederer Pool", "Lower Mayfair", "McIlvain", "Monkiewicz", "Moss", "Mullin", "Northern Liberties", "Pop's Playground", "Pulaski Park", "Roosevelt", "Samuel", "Shissler", "Stokely", "Tip Top", "Trenton & Auburn Playground", "Vogt", "Webb Street Play Lot", "Wilmot Park Playground", "Wissinoming"]
district3 = ["12th & Cambria", "Barrett", "Butler & Percy Play Lot", "Cherashore", "Clarkson Park", "Daly Park", "Deni", "District 3 Office", "Feltonville", "Ferko", "Fisher Park", "Hissey", "Hope Park", "Houseman", "Hunting Park", "Juniata Park OAC", "Lauretha Vaird Boys/Girls Club", "Lawncrest", "Maguire", "Mann OAC", "McVeigh", "Merrit Square", "Nicetown Park", "Northwood Park", "Olney", "Overington Park", "Piccoli", "Ramblers", "Reed", "Rivera", "Ross Park", "Scanlon", "Schmidt", "Shevchenko Park", "Simpson", "Sturgis", "Tacony Creek Park", "Wissahickon", "Womrath Park", "Ziehler"]
district4 = ["20th & Tioga", "20th & Tioga Ballfield", "22nd & Ontario", "22nd & Ontario Playground", "Al Pearlman Sports Center", "Allens Lane Art Center", "Arrow Field", "Awbury", "Belfield", "Blue Bell Park", "Boone Park", "Boyce Field", "Bringhurst Park", "Buckley Park", "Carpenter's Woods", "Clifford Park", "Cliveden Park", "Cloverly Park", "Daisy Fields", "District 4 Office", "Emanuel", "Fairview Park", "Fernhill Park", "Finley", "Gilbert Stuart Park", "Gorgas Park", "Gustine", "Happy Hollow", "Harper's Hollow Park", "Heritage Park", "Hillside", "Houston", "Howell Park", "Inn Yard Park", "Jerome Brown", "Kay Park", "Kelly Park", "Kemble Park", "Kendrick", "La Noce Park", "Lonnie Young", "Loudoun Park", "Mallery", "Market Square Park", "McDevitt", "McMichael Park", "Morris Estate", "Morton", "Mount Airy", "Ned Wolf Park", "Newhall Park", "Old Line Park", "Pachella Fields", "Pastorius Park", "Pickett School Pool", "Pleasant", "Pretzel Park", "Roxborough Reservoir", "Simons", "Stenton Park", "Umbria Golf Center", "Venice Island", "Vernon Park", "Water Tower", "Waterview", "West Oak Lane Senior Center", "Winston Park", "Wissahickon East", "Wissahickon Environmental Center", "Wissahickon Neighbors", "Wissahickon Valley Park", "Wister", "Wister's Woods Park", "Wolf Park"]
district5 = ["26th & Pennsylvania Playground", "33rd & Oxford Basketball Court", "51st & Parkside", "Aviator Park", "Belmont & Edgely Fields", "Belmont Grove", "Belmont Plateau Fields", "Belmont Plateau Recreation Area", "Benjamin Franklin Parkway", "CASE Building", "Chamounix North Fields", "Chamounix North Tennis Courts", "Chamounix South Fields", "Coxe Park", "Dairy Fields", "Delancey Park", "Edgely Fields", "Fitler Square", "Ford Road North Playground", "Franklin Square", "George's Hill", "Kahn Park", "Korean War Veteran's Memorial", "Lemon Hill Fields", "Lemon Hill Mansion", "Logan Square", "Matthias Baldwin Park", "Memorial Hall Fields", "Ohio House Fields", "One Parkway Building", "Reliance Park", "Rittenhouse Square", "River Field", "Sedgley Woods", "Smith Memorial", "Stewardship Office", "Sweetbriar Fields", "Von Colln Field", "Water Works", "West Park"]
district6 = ["10th & Lemon Playground", "11th & C.B. Moore", "30th & Jefferson", "3rd & Norris", "8th & Diamond", "Amos", "Athletic", "Brewerytown Community Garden", "C.B. Moore", "Cassiano Fields", "Clemente", "Dendy", "Diamond Park", "District 6 Office", "Duckrey School Playground", "East Poplar", "East Poplar Field", "Etting Square", "Fairhill Square", "Fotteral Square", "Francisville", "Gathers", "Hagert Playground", "Hartranft Pool", "Lloyd Hall", "M.L. King", "M.L. King OAC", "Mander", "McPherson Square", "Montgomery & Croskey", "Nelson", "Norris Square", "Palmer Park", "Panati", "Penn Treaty Park", "Penrose", "Powers Park", "Reyburn Park", "Shuler", "Strawberry Mansion Playground", "Towey", "Veterans Playground", "Waterloo", "Winchester"]
district7 = ["22nd & Catherine Park", "Anderson", "Bainbridge Green", "Bardascino Park", "Barry", "Beck Park", "Burke", "Burke Playground", "Capitolo", "Chew", "Cianfrani Park", "Columbus Square", "D. Finnegan", "Dickinson Square", "DiSilvestro", "District 7 Office", "East Passyunk Community Recreation Center", "FDR  Park Boathouse", "FDR Park", "Ford", "Gold Star Park", "Gray's Ferry Crescent", "Greble Post (War Memorial)", "Guerin", "Hawthorne", "Hawthorne Park", "Herron", "Howard & Reed Park", "Jefferson Square", "Lanier", "Manton Street Park", "Marconi Plaza", "Mario Lanza Park", "Markward", "Mifflin Square", "Mollbore Terrace Park", "Murphy", "O'Connor Pool", "Palumbo", "Palumbo Park", "Paolone Park", "Ralph Brooks Park", "Ridgway Pool", "Rizzo Rink", "Sacks", "Seger", "Shot Tower", "Sims", "Smith", "South Philadelphia OAC", "Starr Garden", "Stinger Square", "Vare", "Weccacoe", "Weinberg Park", "Wharton Square"]
district8 = ["33rd & Wallace", "33rd & Wallace Playground", "37th & Mt. Vernon", "39th & Olive", "45th & Sansom Tot Lot", "48th & Woodland", "60th & Baltimore Park", "63rd & Lindbergh", "63rd & Lindbergh Park", "75th & Chelwynde", "Baker", "Ben Barkan Park", "Buist Park", "Carousel House", "Carroll Park", "Cedar Park", "Christy", "Cibotti", "Clark Park", "Clayborn & Lewis", "Clearview Park", "Cobbs Creek", "Cobbs Creek Environmental Education Center", "Conestoga", "Connell Park", "Conshohocken", "Deritis Playground", "District 8 Office", "Eastwick Park", "Eastwick Regional", "Elmwood Park", "Garden Court Tennis Courts", "Granahan", "Horticulture Center", "Horton Street Play Lot", "J. Finnegan", "John Anderson", "Julian Abele Park", "Kelly Pool", "Kingsessing", "Laura Sims", "Lee Cultural Center", "Malcolm X Memorial Park", "McCreesh", "Miles Mack", "Mill Creek", "Morris Park", "Muhammad Square", "Myers", "Nichols Park", "Papa", "Parkside Evans", "Pepper", "Philly Pumptrack", "Rose", "Rose Playground", "Sayre Morris", "Shepard", "Sherwood Park", "Triangle Park", "Tustin", "West Mill Creek", "Woodside Park", "Wright"]

all_districts = []
all_districts.append(district1, district2, district3, district4, district5, district6, district7, district8)

with open('test.PDF') as f:
    pdf = slate.PDF(f)
    text = str(pdf)
    field_list = text.split("\\n")

if field_list[2] == "AQUATICS AUDIT CONTROL":
    title = field_list[2]
    pool = field_list[12]
    # For loop to find district, try to see if any() can be used.
    for i in district1:
        if i == pool:
            shutil.move('test.PDF', 'iPads/Aquatics/District 1')
            print "Aquatics Audit Control moved to District 1"
    #if pool == any(district1):
        #shutil.move('test.PDF', 'iPads/Aquatics/District 1')
    #elif pool == any(district5):
     #   shuitl.move('test.PDF', 'iPads/Aquatics/District 5')
    #else:
     #   print "District not found."
    
elif field_list[0] == "['Philadelphia Recreation Department Site Visit Report ":
    shutil.move('test.PDF', 'iPads/')

else:  
    print "This file is not recognized."
