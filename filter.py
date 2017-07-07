import slate
import shutil

district1 = ["Max Myers", "Junod"]
district5 = ["Dairy Fields", "Mander"]
# all_districts = combined lists

with open('test.PDF') as f:
    pdf = slate.PDF(f)
    text = str(pdf)
    field_list = text.split("\\n")

if field_list[2] == "AQUATICS AUDIT CONTROL":
    title = field_list[2]
    pool = field_list[12]
    print pool
    print district1[0]
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