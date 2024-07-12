contact = {}

name = input("Enter Name: ")
address = (input("Enter Address: "))
telephone = (input("Enter Telephone Number: "))
contact.update({'name': name, 'address': address, 'telephone': telephone})
print({'Full Name: ' + contact['name'] + ' | Address: ' + contact['address'] + '| Telephone Number:' + contact['telephone']})