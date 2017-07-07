import slate
import shutil

with open('test.PDF') as f:
    doc = slate.PDF(f)
    text = str(doc)
    title = text[37:59]

if title == "AQUATICS AUDIT CONTROL":
    with open('move.PDF') as m:
        shutil.move('test.PDF', 'iPads/')
else:
    print "Not Aquatics Audit Control"