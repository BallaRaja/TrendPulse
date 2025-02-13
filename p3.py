class Company:
    def __init__(self, name, bid_amount, initial_rating=3.0):
        self.name = name
        self.bid_amount = bid_amount
        self.marketing_score = 0
        self.monthly_marketing_score = {}
        self.rating = initial_rating  # Base rating for the product

    def update_marketing_score(self, interaction_type, month):
        if month not in self.monthly_marketing_score:
            self.monthly_marketing_score[month] = 0
        score_increment = {"visit": 1, "like": 2, "dislike": -1}
        self.marketing_score += score_increment[interaction_type]
        self.monthly_marketing_score[month] += score_increment[interaction_type]

        # Adjust rating based on interaction type
        self.adjust_rating(interaction_type)

    def adjust_rating(self, interaction_type):
        if interaction_type == "like":
            self.rating += 0.1  
        elif interaction_type == "dislike":
            self.rating -= 0.1 

        # Clamp the rating between 0 and 10
        self.rating = max(0, min(10, self.rating))
    
    def display_marketing_report(self):
        print(f"\n── Marketing Report for {self.name} ──\n")
        for month, score in self.monthly_marketing_score.items():
            print(f"\t{month}: Marketing Score = {score}")

# --- Module 4: Company Rating Tracking ---
class CompanyRating:
    def __init__(self, company, year):
        self.company = company
        self.initial_rating = 50  # Starting rating before marketing
        self.ratings = {month: self.initial_rating for month in [f"{year}-{month:02d}" for month in range(1, 13)]}

    def update_rating(self, month):
        marketing_score = self.company.monthly_marketing_score.get(month, 0)
        # Simple logic to adjust the rating based on marketing score
        self.ratings[month] += marketing_score

    def display_rating_report(self):
        print(f"\n── Rating Report for {self.company.name} ──\n")
        for month, rating in self.ratings.items():
            print(f"\t{month}: {rating} (Marketing Score: {self.company.monthly_marketing_score.get(month, 0)})")