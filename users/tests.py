# importing TestCase - special build-in Django class to making tests
from django.test import TestCase

# importing models created in our 'users' app
from .models import User, Driver, Company 

# As we currently are in users app, below 'UserTestCase' will be used for testing
# its functionalities. 
# Please spend a few minutes and read about testing basics in Django:
# https://docs.djangoproject.com/en/3.1/topics/testing/overview/

class UserTestCase(TestCase):
    # 'setUp' is a special method to setting up our data before tests
    def setUp(self):
        company = Company(phone_number="+441313131313", name="Melani Ltd")
        company.save()

        driver = Driver(phone_number="+441111111111", first_name="Prem", last_name="Kowalski", company=company, car_model="BWM", car_color="Black", car_license_plate="ABCD1234")
        driver.save()

        customer = User.objects.create_user(email='alex@study.beds.ac.uk', password='secret123', phone_number="+441212121212", first_name="Alex", last_name="Smith")

    # Let's check if users were created
    def test_users_created(self):
        # By 'Model.objects.get()' we can search specific records from database, so let's do it
        company = Company.objects.get(name="Melani Ltd")
        driver = Driver.objects.get(first_name="Prem")
        customer = User.objects.get(first_name="Alex")

        # Now let's check if all users exists
        are_users_created = bool(company) and bool(driver) and bool(customer)
        self.assertEqual(are_users_created, True)

    # We can also check if users can login with their provided email and password
    def test_users_can_login(self):
        # Django will handle login and return us a Boolean value if credentials are correct.
        is_customer_logged = self.client.login(email='alex@study.beds.ac.uk', password='secret123')
        
        # Now let's check if all users exists
        self.assertEqual(is_customer_logged, True)
