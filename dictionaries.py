'''

dict = {'key':'value', etc.}
    ---> value can have any type (even lists and other dictionaries)


print(dict[key])

dict[new_key] = new_value

del dict[key]

'''
exDict = {
    'Jack': [
        15,
        'blonde'
    ],
    'Bob': [
        22,
        'brown'
    ],
    'Alice': [
        12,
        'black'
    ],
    'Kevin': [
        17,
        'red'
    ]
}

print(exDict)

print(exDict['Jack'])

exDict['Tim'] = 14

print(exDict)

exDict['Tim'] = 15

print(exDict)

del exDict['Tim']

print(exDict)


print(exDict['Jack'][1])
