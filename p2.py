from p1 import *
top_influencers_heap = MaxHeap()
class Influencer:
    def __init__(self, name):
        self.name = name
        self.likes = 0
        self.dislikes = 0
        self.visits = {}
        self.monthly_likes = {}
        self.monthly_dislikes = {}
        top_influencers_heap.add_influencer(self)

    def calculate_score(self):
        self.score = self.likes - self.dislikes + sum(self.visits.values())
        return self.score

    def record_visit(self, month, visits):
        self.visits[month] = self.visits.get(month, 0) + visits
        top_influencers_heap.update_influencer(self)

    def record_like(self, month):
        self.likes += 1
        self.monthly_likes[month] = self.monthly_likes.get(month, 0) + 1
        top_influencers_heap.update_influencer(self)

    def record_dislike(self, month):
        self.dislikes += 1
        self.monthly_dislikes[month] = self.monthly_dislikes.get(month, 0) + 1
        top_influencers_heap.update_influencer(self)

    def display_details(self):
        details = f"""
                                ── Influencer: {self.name} ──
        \tLikes: {self.likes}, Dislikes: {self.dislikes}, Total Score: {self.calculate_score()}
        \tMonthly Visits: {self.visits}
        \tMonthly Likes: {self.monthly_likes}
        \tMonthly Dislikes: {self.monthly_dislikes}
        """
        print(details)

    # Adding comparison methods for heapq operations
    def __lt__(self, other):
        return self.calculate_score() < other.calculate_score()

    def __eq__(self, other):
        return self.calculate_score() == other.calculate_score()

class UserInteractions:
    """Tracks user interactions with influencers."""
    def __init__(self):
        self.user_history = {}

    def track_search(self, user_id, influencer_name):
        if user_id not in self.user_history:
            self.user_history[user_id] = Stack()
        self.user_history[user_id].push(influencer_name)

    def display_user_history(self):
        print("── User Search Histories ──")
        text = ""
        for user_id, history_stack in sorted(self.user_history.items()):
            text += f"{user_id} Search History: {history_stack.get_all()}\n"
        return text
