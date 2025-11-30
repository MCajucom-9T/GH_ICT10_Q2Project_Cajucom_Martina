from pyscript import display, document

subjects = ['Math:', 'English:', 'Science:', 'Filipino:', 'ICT:', 'PE:']

display(f'{subjects[0]}', target='mlabel')
display(f'{subjects[1]}', target='elabel')
display(f'{subjects[2]}', target='slabel')
display(f'{subjects[3]}', target='flabel')
display(f'{subjects[4]}', target='ilabel')
display(f'{subjects[5]}', target='plabel')

def generating_grade(e):
    units = (5,3,2,1) # all the different amount of units
    z,y,x,w = units
    first = document.getElementById('fname').value # collecting value from an input field
    last = document.getElementById('lname').value # collecting value from an input field
    math = int(document.getElementById('mvalue').value) * z # initial grade times number of units
    english = int(document.getElementById('evalue').value) * z # initial grade times number of units
    science = int(document.getElementById('svalue').value) * z # initial grade times number of units
    filipino = int(document.getElementById('fvalue').value) * y # initial grade times number of units
    ict = int(document.getElementById('ivalue').value) * x # initial grade times number of units
    pe = int(document.getElementById('pvalue').value) * w # initial grade times number of units
    inmath = int(document.getElementById('mvalue').value) # intial value without unit
    inenglish = int(document.getElementById('evalue').value) # intial value without unit
    inscience = int(document.getElementById('svalue').value) # intial value without unit
    infilipino = int(document.getElementById('fvalue').value) # intial value without unit
    inict = int(document.getElementById('ivalue').value) # intial value without unit
    inpe = int(document.getElementById('pvalue').value) # intial value without unit
    GWA = round((math + english + science + filipino + ict + pe)/21, 2) # total of all grades divided by total number of units until 2 decimal points

    #displays student info
    display(f'{GWA}', target='GWA')
    display(f'{first} {last}', target='name')
    display(f'{subjects[0]} {inmath}', target='math')
    display(f'{subjects[1]} {inenglish}', target='eng')
    display(f'{subjects[2]} {inscience}', target='sci')
    display(f'{subjects[3]} {infilipino}', target='fil')
    display(f'{subjects[4]} {inict}', target='ict')
    display(f'{subjects[5]} {inpe}', target='pe')