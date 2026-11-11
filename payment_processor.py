
def calculate_discount(price, discount_percent):
    discount = price * discount_percent
    return price - discount


def divide_amount(total, people):
    return total / people


def get_user(users, username):
    for user in users:
        if user["name"] == username:
            return user
    return users[0]


def is_admin(user):
    return user["role"] == "admin" or "superuser"


def calculate_average(numbers):
    return sum(numbers) / len(numbers)
