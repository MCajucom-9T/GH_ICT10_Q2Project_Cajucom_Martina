# Working with Dictionary
from pyscript import display, document

def socsci_present(e):
    document.getElementById('name').innerHTML = "Name: " #ensures that the output won't ionfinitely show up when the button is clicked
    document.getElementById('time').innerHTML = "Time: " #ensures that the output won't ionfinitely show up when the button is clicked
    document.getElementById('des').innerHTML = "Desription: " #ensures that the output won't ionfinitely show up when the button is clicked
    document.getElementById('ad').innerHTML = "Advisor: " #ensures that the output won't ionfinitely show up when the button is clicked
    document.getElementById('num').innerHTML = "Quota: "
    document.getElementById('category').innerHTML = "Category: "
    document.getElementById('loc').innerHTML = "Location: "
    SocSci = {
    'Name' : 'SocSci Club',
    'Time' : '2:00-4:00',
    'Description' : 'Advocating and leading the youth',
    'Location' : '710',
    'Advisor' : 'Nina Libramonte',
    'Quota' : '20',
    'Category' : 'Academic'
}
    
    display(f'{SocSci['Name']}', target='name')
    display(f'{SocSci['Time']}', target='time')
    display(f'{SocSci['Description']}', target='des')
    display(f'{SocSci['Location']}', target='loc')
    display(f'{SocSci['Advisor']}', target='ad')
    display(f'{SocSci['Quota']}', target='num')
    display(f'{SocSci['Category']}', target='category')

def math_present(e):
    document.getElementById('name').innerHTML = "Name: " #ensures that the output won't ionfinitely show up when the button is clicked
    document.getElementById('time').innerHTML = "Time: " #ensures that the output won't ionfinitely show up when the button is clicked
    document.getElementById('des').innerHTML = "Desription: " #ensures that the output won't ionfinitely show up when the button is clicked
    document.getElementById('ad').innerHTML = "Advisor: " #ensures that the output won't ionfinitely show up when the button is clicked
    document.getElementById('num').innerHTML = "Quota: "
    document.getElementById('category').innerHTML = "Category: "
    document.getElementById('loc').innerHTML = "Location: "
    Math = {
    'Name' : 'Math Guild',
    'Time' : '2:00-4:00',
    'Description' : 'A place to instil math advancement',
    'Location' : '510',
    'Advisor' : 'Louis Ferma',
    'Quota' : '20-30',
    'Category' : 'Academic'
} # specifying dictionaries
    
    display(f'{Math['Name']}', target='name')
    display(f'{Math['Time']}', target='time')
    display(f'{Math['Description']}', target='des')
    display(f'{Math['Location']}', target='loc')
    display(f'{Math['Advisor']}', target='ad')
    display(f'{Math['Quota']}', target='num')
    display(f'{Math['Category']}', target='category')

def glee_present(e):
    document.getElementById('name').innerHTML = "Name: " #ensures that the output won't ionfinitely show up when the button is clicked
    document.getElementById('time').innerHTML = "Time: " #ensures that the output won't ionfinitely show up when the button is clicked
    document.getElementById('des').innerHTML = "Desription: " #ensures that the output won't ionfinitely show up when the button is clicked
    document.getElementById('ad').innerHTML = "Advisor: " #ensures that the output won't ionfinitely show up when the button is clicked
    document.getElementById('num').innerHTML = "Quota: "
    document.getElementById('category').innerHTML = "Category: "
    document.getElementById('loc').innerHTML = "Location: "
    Glee = {
    'Name' : 'Glee Club',
    'Time' : '2:00-4:00',
    'Description' : 'Where song birds unite',
    'Location' : '408',
    'Advisor' : 'Marjorie Loyola',
    'Quota' : '40',
    'Category' : 'Extracuricular'
}
    
    display(f'{Glee['Name']}', target='name')
    display(f'{Glee['Time']}', target='time')
    display(f'{Glee['Description']}', target='des')
    display(f'{Glee['Location']}', target='loc')
    display(f'{Glee['Advisor']}', target='ad')
    display(f'{Glee['Quota']}', target='num')
    display(f'{Glee['Category']}', target='category')



