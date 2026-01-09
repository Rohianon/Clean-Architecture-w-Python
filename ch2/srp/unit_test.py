import unittest
from unittest.mock import Mock, patch

from user_post_refactor import PostManager, TimelineService, ProfileManager, User


class TestPostManager(unittest.TestCase):
    def test_create_post_generates_post_with_correct_attributes(self):
        """Test that create_post generates a post with correct attributes including user_id, content, likes, and id"""
        user = User("123", "testuser", "test@example.com")
        post_manager = PostManager()
        
        with patch.object(post_manager, 'generate_post_id', return_value="post_456"):
            post = post_manager.create_post(user, "Hello, World!")
        
        self.assertEqual(post['user_id'], "123")
        self.assertEqual(post['content'], "Hello, World!")
        self.assertEqual(post['likes'], 0)
        self.assertEqual(post['id'], "post_456")
        self.assertIn("id", post)

    def test_generate_post_id_returns_unique_id(self):
        """Test that generate_post_id returns a unique post ID"""
        post_manager = PostManager()
        
        # Mock the generate_post_id to return unique IDs
        with patch.object(post_manager, 'generate_post_id', side_effect=["id_1", "id_2", "id_3"]):
            id1 = post_manager.generate_post_id()
            id2 = post_manager.generate_post_id()
            id3 = post_manager.generate_post_id()
        
        # Verify all IDs are unique
        self.assertNotEqual(id1, id2)
        self.assertNotEqual(id2, id3)
        self.assertNotEqual(id1, id3)


class TestTimelineService(unittest.TestCase):
    def test_get_timeline_returns_list_of_posts(self):
        """Test that get_timeline returns a list of posts for the given user"""
        user = User("123", "testuser", "test@example.com")
        timeline_service = TimelineService()
        
        # Mock the get_timeline method to return a list of posts
        mock_posts = [
            {"id": "post_1", "user_id": "456", "content": "First post", "likes": 5},
            {"id": "post_2", "user_id": "789", "content": "Second post", "likes": 3},
            {"id": "post_3", "user_id": "123", "content": "Third post", "likes": 10}
        ]
        
        with patch.object(timeline_service, 'get_timeline', return_value=mock_posts):
            timeline = timeline_service.get_timeline(user)
        
        self.assertIsInstance(timeline, list)
        self.assertEqual(len(timeline), 3)
        self.assertEqual(timeline[0]['id'], "post_1")
        self.assertEqual(timeline[1]['content'], "Second post")
        self.assertEqual(timeline[2]['likes'], 10)


class TestProfileManager(unittest.TestCase):
    def test_update_profile_updates_username_when_provided(self):
        """Test that update_profile updates the username if new_username is provided"""
        user = User("123", "oldusername", "user@example.com")
        profile_manager = ProfileManager()
        
        profile_manager.update_profile(user, new_username="newusername")
        
        self.assertEqual(user.username, "newusername")
        self.assertEqual(user.email, "user@example.com")  # Email should remain unchanged

    def test_update_profile_updates_email_when_provided(self):
        """Test that update_profile updates the email if new_email is provided"""
        user = User("123", "testuser", "old@example.com")
        profile_manager = ProfileManager()
        
        profile_manager.update_profile(user, new_email="new@example.com")
        
        self.assertEqual(user.email, "new@example.com")
        self.assertEqual(user.username, "testuser")  # Username should remain unchanged

    def test_update_profile_updates_both_username_and_email(self):
        """Test that update_profile can update both username and email simultaneously"""
        user = User("123", "oldusername", "old@example.com")
        profile_manager = ProfileManager()
        
        profile_manager.update_profile(user, new_username="newusername", new_email="new@example.com")
        
        self.assertEqual(user.username, "newusername")
        self.assertEqual(user.email, "new@example.com")


if __name__ == '__main__':
    unittest.main()
