# Met with Dr. Mary on 5/8/25 for Unit Test ideas
# Created Unit Test for Contact Module. Tests if record is added to database.

import unittest
from app import app, db, Contact
from datetime import datetime, timezone

class ContactModelTestCase(unittest.TestCase):
    def setUp(self):
        # Set up the test database
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        app.config['TESTING'] = True
        self.app = app.test_client()
        
        # Push application context
        self.app_context = app.app_context()
        self.app_context.push()
        
        db.create_all()

    def tearDown(self):
        # Clean up the test database
        db.session.remove()
        db.drop_all()
        
        # Pop application context
        self.app_context.pop()

    def test_contact_creation(self):
        # Create a new contact
        contact = Contact(name='Carlos Test', email='CarlosTest@example.com', message='Hello, this is a test message.')
        db.session.add(contact)
        db.session.commit()

        # Retrieve the contact from the database
        retrieved_contact = Contact.query.filter_by(name='Carlos Test').first()
        #Testing Results
        self.assertIsNotNone(retrieved_contact)
        self.assertEqual(retrieved_contact.email, 'CarlosTest@example.com')
        self.assertEqual(retrieved_contact.message, 'Hello, this is a test message.')

        # Print all contacts in the database
        all_contacts = Contact.query.all()
        for contact in all_contacts:
            print(contact)

    def test_contact_repr(self):
        # Test the __repr__ method
        contact = Contact(name='Cat Dog', email='CatDog@example.com', message='Another test message.')
        self.assertEqual(repr(contact), '<Contact Cat Dog>')

# Create database tables before running the app
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    unittest.main()