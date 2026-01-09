class User:
    def __init__(self, user_id: str, username: str, email: str) -> None:
        self.user_id = user_id
        self.username = username
        self.email = email


class PostManager:
    def create_post(self, user: User, content: str):
        post = {
                "id": self.generate_post_id(),
                "user_id": user.user_id,
                "content": content,
                "likes": 0,
        }
        # logic to save the post goes here
        return post

    def generate_post_id(self):
        # logic to generate a unique post ID
        pass

class TimelineService:
    def get_timeline(self, user: User) -> list:
        # Fetch and return the user's timeline
        # This might involve complex logic to
        # fetch and sort posts from followed users
        pass

class ProfileManager:
    def update_profile(
        self, user: User, new_username: str = None, new_email: str = None ):
        if new_username:
            user.username = new_username
        if new_email:
            user.email = new_email
        # additional logic
        # triggering email verification

