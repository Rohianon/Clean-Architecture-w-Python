class User:
    def __init__(self, user_id: str, username: str, email: str):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.posts = []

    def create_post(self, content: str) -> dict:
        post = {
            "id": len(self.posts) + 1,
            "content": content,
            "likes": 0,
        }
        self.posts.append(post)
        return post

    def get_timeline(self) -> list:
        pass

    def update_profile(self, new_username: str = None, new_email: str = None):
        if new_username:
            self.username = new_username
        if new_email:
            self.email = new_email
