from django.test import TestCase
from restaurant.models import Menu
class MenuViewTest(TestCase):
    
    def setUp(self):
        menuItems = Menu.objects.all()
        menuItems.delete()

        menu1 = Menu(title="Fufu", price=23, inventory=1)
        menu1.save()
        menu2 = Menu(title="Bankye", price=34, inventory=3)
        menu2.save()
    
    def test_getall(self):
        menuItems  = list(Menu.objects.all())
        self.assertEquals(len(menuItems), 2)