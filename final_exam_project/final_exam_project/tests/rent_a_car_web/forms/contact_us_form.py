from django.test import TestCase
from final_exam_project.rent_a_car_web.forms import ContactUsForm


class ContactUsFormTest(TestCase):
    def test_contact_us_form_valid_data(self):
        form_data = {
            'full_name': 'John Doe',
            'email': 'johndoe@example.com',
            'subject': 'Test Subject',
            'message': 'This is a test message.',
        }
        form = ContactUsForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_contact_us_form_blank_data(self):
        form = ContactUsForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 4)  # Test all fields are required

    def test_contact_us_form_email_validation(self):

        form_data = {
            'full_name': 'John Doe',
            'email': 'invalid_email',
            'subject': 'Test Subject',
            'message': 'This is a test message.',
        }
        form = ContactUsForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors) # Invalid email test

        form_data['email'] = 'johndoe@example.com'
        form = ContactUsForm(data=form_data)
        self.assertTrue(form.is_valid()) # Valid email test
