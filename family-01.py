#--------|---------|---------|---------|---------|---------|---------|---------

# The Family Dictionary

# 1. Define a dictionary that contains information about several members of your family. Use the following example as a template.

my_family = {
    'wife': {
        'name': 'Ashley',
        'age': 39
    },
    'eldest daughter': {
        'name': 'Amy',
        'age': 20
    },
    'youngest daughter': {
        'name': 'Margot',
        'age': 3
    },
    'eldest sister': {
        'name': 'Courtney',
        'age': 45
    },
    'older sister': {
        'name': 'Dana',
        'age': 43
    },
    'mother': {
        'name': 'Jane',
        'age': 71
    },
    'father': {
        'name': 'Dan',
        'age': 72
    },
    'me': {
        'name': 'Ben',
        'age': 41
    }
}

jimmy = [data['name'] + " is my " + relation + " and is " + str(data['age']) + " years old." for (relation, data) in my_family.items()]
for jim in jimmy:
    print(jim)
