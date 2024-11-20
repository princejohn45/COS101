def physics_formula_menu():
    print('\nPhysics formula option:')
    print('a. gravitational force')
    print('b. specific heat capacity')
    print('c. electric force')
    print('d. magnification')
    print('e. acceleration')

physics_formula_menu()

options = input('pick an option from a to e  ')
print(options)

if options == 'a':
    m1 = int(input('Enter value for q1  '))
    m2 = int(input('Enter value for q2  '))
    K = 9 * (10 ** 9)
    r =  int(input('Enter value for r  '))
    gravitational_force = (K * m1 * m2) / (r ** 2)
    print(gravitational_force)

elif options == 'b':
    quantity_of_heat = int(input('Enter value  '))
    mass = int(input('Enter value   '))
    t1 = int(input('Enter value of t1'))
    t2 =  int(input('Enter value of t2  '))
    specific_heat_capacity = quantity_of_heat / (mass * (t2 - t1))
    print(specific_heat_capacity)

elif options == 'c':
    q1 = int(input('Enter value for q1  '))
    q2 = int(input('Enter value for q2  '))
    K = 9 * (10 ** 9)
    r =  int(input('Enter value for r  '))
    electric_force = (K * q1 * q2) / (r ** 2)
    print(electric_force)

elif options == 'd':
    image_height = int(input('enter image height  '))
    object_height = int(input('enter object height  '))
    magnification = image_height / object_height
    print(magnification)

elif options == 'e':
    velocity = float(input('Enter value for velocity  '))
    time = int(input('Enter value for time  '))
    acceleration = velocity / time
    print(acceleration)

else :
    print('invalid option an option from a to e')