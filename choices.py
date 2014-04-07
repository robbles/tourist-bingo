import random

CHOICES = [
    'Backpack on front and back',
    'Taking photos of 7-11',
    'Not reading directions on parking meters',
    'Getting lost',
    'Husband wearing a hat his wife bought for him'
] * 10

def get_choices(num):
    random.shuffle(CHOICES)
    return CHOICES[:num]
