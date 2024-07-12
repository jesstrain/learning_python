class_data = []

for i in range(3):
    enter_name = input("Enter Name: ")
    enter_score = int(input("Enter Score: "))
    class_data.append({'name': enter_name, 'score': enter_score})

for i in class_data:
    print('Name: ' + i['name'] + ' | score ' + str(i['score']))