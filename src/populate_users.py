from django.contrib.auth import get_user_model

# List of test users
test_users = [
    {"email": "gustavo@supermarket.com", "password": "admin123", "is_admin": True},
    {"email": "maria@supermarket.com", "password": "manager123", "is_admin": False},
    {"email": "pedro@supermarket.com", "password": "operator123", "is_admin": False},
]

# Get the User model
User = get_user_model()

for user_data in test_users:
    email = user_data["email"]
    password = user_data["password"]
    is_admin = user_data["is_admin"]

    # Check if the user already exists
    if not User.objects.filter(email=email).exists():
        user = User.objects.create_user(email=email, password=password)

        # Set admin privileges for Gustavo
        if is_admin:
            user.is_staff = True
            user.is_superuser = True
            user.save()

        print(f"{email.split('@')[0].capitalize()} ID: {user.id}")
    else:
        print(f"User with email {email} already exists.")