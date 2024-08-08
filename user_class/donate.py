class Donate:
    
    total_donation = 0
    
    def __init__(self, amount_to_donate):
        self.amount_to_donate = amount_to_donate
        self.is_donated = False
        Donate.total_donation += amount_to_donate
        
donate1 = Donate(300)
donate2 = Donate(400)
print(Donate.total_donation)