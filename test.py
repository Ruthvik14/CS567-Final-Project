import unittest
from database import add_item, update_item, get_item, get_items, delete_item, init_db

class TestInventoryManagement(unittest.TestCase):
    def setUp(self):
        init_db()  # You might want to connect to a test database instead

    def test_add_item(self):
        """Test adding a new item."""
        add_item('Keyboard', 45.00, 20)
        item = get_item('Keyboard')
        self.assertIsNotNone(item)
        self.assertEqual(item[1], 'Keyboard')
        self.assertEqual(item[2], 45.00)
        self.assertEqual(item[3], 20)

    def test_update_item(self):
        """Test updating an existing item."""
        add_item('Keyboard', 45.00, 20)
        update_item('Keyboard', quantity=5, price=50.00)
        item = get_item('Keyboard')
        self.assertEqual(item[3], 25)  # Check quantity
        self.assertEqual(item[2], 50.00)  # Check price

    def test_delete_item(self):
        """Test deleting an item."""
        add_item('Monitor', 200.00, 10)
        delete_item('Monitor')
        item = get_item('Monitor')
        self.assertIsNone(item)

    def test_view_all_items(self):
        """Test viewing all items."""
        add_item('Keyboard', 45.00, 20)
        add_item('Mouse', 25.50, 50)
        items = get_items()
        self.assertEqual(len(items), 2)

    def test_invalid_input_handling(self):
        """Test handling of invalid input."""
        response = add_item('', -100, 0)  # Assume add_item returns some response for invalid input
        self.assertFalse(response)  # Assuming False is returned for failure

if __name__ == '__main__':
    unittest.main()
