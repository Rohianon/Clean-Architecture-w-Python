import unittest

from user_post_refactor import PostManager, User


class TestPostManager(unittest.TestCase):
    def test_create_post(self):
        user = User("123", "testuser", "test@example.com")
        post_manager = PostManager()
        post = post_manager.create_post(user, "Hello, World!")

        self.assertEqual(post['user_id'], "123")
        self.assertEqual(post['content'], "Hello, World!")
        self.assertEqual(post['likes'], 0)
        self.assertIn("id", post)


if __name__ == '__main__':
    unittest.main()
