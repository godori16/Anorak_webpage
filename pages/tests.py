from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView, IntroductionPageView, ProductPageView, ContactPageView

class HomepageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'The die is cast')

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')

    def test_homepage_url_resolves_homepageview(self): # new
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)

class IntroductionPageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('introduction')
        self.response = self.client.get(url)

    def test_introduction_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_introduction_template(self):
        self.assertTemplateUsed(self.response, 'introduction.html')

    def test_introduction_contains_correct_html(self):
        self.assertContains(self.response, 'Introduction')

    def test_introduction_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')

    def test_introduction_url_resolves_introductionpageview(self): # new
        view = resolve('/introduction/')
        self.assertEqual(view.func.__name__, IntroductionPageView.as_view().__name__)

class ProductPageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('product')
        self.response = self.client.get(url)

    def test_product_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_product_template(self):
        self.assertTemplateUsed(self.response, 'product.html')

    def test_product_contains_correct_html(self):
        self.assertContains(self.response, 'Product')

    def test_product_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')

    def test_product_url_resolves_productpageview(self): # new
        view = resolve('/product/')
        self.assertEqual(view.func.__name__, ProductPageView.as_view().__name__)

class ContactPageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('contact')
        self.response = self.client.get(url)

    def test_contact_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_contact_template(self):
        self.assertTemplateUsed(self.response, 'contact.html')

    def test_contact_contains_correct_html(self):
        self.assertContains(self.response, 'Location')

    def test_contact_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')
    
    def test_contact_url_resolves_contactpageview(self): # new
        view = resolve('/contact/')
        self.assertEqual(view.func.__name__, ContactPageView.as_view().__name__)

