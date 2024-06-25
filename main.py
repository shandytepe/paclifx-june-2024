from tabulate import tabulate
from typing import Dict

data = {
    "Shandy": ["Basic Plan", 12, "shandy-2134"],
    "Cahya": ["Standard Plan", 24, "cahya-abcd"],
    "Ana": ["Premium Plan", 5, "ana-2f9g"],
    "Bagus": ["Basic Plan", 11, "bagus-9f92"]
}

class User:
    
    # define attribute username
    def __init__(self, username: str):
        self.username = username
        
    # create method to check all plan PacFlix
    def check_benefit(self) -> None:
        
        # init columns names
        headers = ["Basic Plan", "Standard Plan", "Premium Plan", "Benefit"]
        
        # init data
        tables = [
             [True, True, True, "Bisa Stream"],
             [True, True, True, "Bisa Download"],
             [True, True, True, "Kualitas SD"],
             [False, True, True, "Kualitas HD"],
             [False, False, True, "Kualitas UHD"],
             [1, 2, 4, "Number of Devices"],
             ["3rd party Movie only", "Basic Plan Content + Sports", "Basic Plan + Standard Plan + PacFlix Original Series", "Jenis Konten"],
             [120_000, 160_000, 200_000, "Harga"]
        ]
        
        print("===== PacFlix Plan List =====")
        print("")
        print(tabulate(tables, headers, tablefmt = "github"))
    
    # method to check current plan based on username
    def check_plan(self) -> None:
        # iterate keys and values based on data
        for keys, values in data.items():
            
            # branching to filter username
            if self.username == keys:
                
                # create variable to store the values
                get_current_plan = values[0]
                get_duration_plan = values[1]
                
                print(f"Username: {self.username}")
                print(f"Current Plan: {get_current_plan}")
                print(f"Duration Plan: {get_duration_plan}")
                
    # method to upgrade plan
    def upgrade_plan(self, upgrade_plan: str) -> float:
        
        # define constant for discount
        DISCOUNT_UPGRADE = 0.05
        
        # iterate keys and values based on data
        for keys, values in data.items():
            
            # branching based on username for get current_plan and duration_plan
            if self.username == keys:
                
                # get current plan and duration plan data
                get_current_plan = values[0]
                get_duration_plan = values[1]
                
                # logic to filter not pick the same plan
                if upgrade_plan != get_current_plan:
                    
                    # branching if duration_plan >= 12 month
                    if get_duration_plan >= 12:
                        # logic discount
                        
                        if upgrade_plan == "Basic Plan":
                            total_price = 120_000 - (120_000 * DISCOUNT_UPGRADE)
                            
                            return total_price
                        
                        elif upgrade_plan == "Standard Plan":
                            total_price = 160_000 - (160_000 * DISCOUNT_UPGRADE)
                            
                            return total_price
                        
                        elif upgrade_plan == "Premium Plan":
                            total_price = 200_000 - (200_000 * DISCOUNT_UPGRADE)
                            
                            return total_price
                        
                        else:
                            raise Exception("Plan tidak ada!!")
                            
                    else:
                        # branching if not discount
                        if upgrade_plan == "Basic Plan":
                            total_price = 120_000
                            
                            return total_price
                        
                        elif upgrade_plan == "Standard Plan":
                            total_price = 160_000
                            
                            return total_price
                        
                        elif upgrade_plan == "Premium Plan":
                            total_price = 200_000
                            
                            return total_price
                        
                        else:
                            raise Exception("Plan tidak ada!!")
                        
class NewUser:
    
    # create empty list to store referral_code
    referral_code = []
    
    def __init__(self, username: str):
        self.username = username
        
    # method to generate referral code based on data
    def generate_referral_code(self, data: Dict[str, str]) -> None:
        # iterate data
        for value in data.values():
            # store the ref code to vars
            get_ref_code = value[2]
            
            # append to empty list class attribute
            self.referral_code.append(get_ref_code)
            
    # method to new user pick plan
    def pick_plan(self, new_plan: str, referral_code: str) -> float:
        # init discount
        DISCOUNT_NEW_USER = 0.04
        
        # valid referral code
        if referral_code in self.referral_code:
            # discount logic
            if new_plan == "Basic Plan":
                total_price = 120_000 - (120_000 * DISCOUNT_NEW_USER)
                
                return total_price
            
            elif new_plan == "Standard Plan":
                total_price = 160_000 - (160_000 * DISCOUNT_NEW_USER)
                
                return total_price
            
            elif new_plan == "Premium Plan":
                total_price = 200_000 - (200_000 * DISCOUNT_NEW_USER)
                
                return total_price
            
            else:
                raise Exception("Plan belum tersedia")
        
        # not input referral code get normal price
        elif (referral_code == "") or (referral_code == None):
            # get normal price
            if new_plan == "Basic Plan":
                total_price = 120_000
                
                return total_price
            
            elif new_plan == "Standard Plan":
                total_price = 160_000
                
                return total_price
            
            elif new_plan == "Premium Plan":
                total_price = 200_000
                
                return total_price
            
            else:
                raise Exception("Plan belum tersedia")
            
        # not valid referral code
        else:
            raise Exception("Referral code didn't exists!")
        
# test dummy object
user_1 = User(username = "Bagus")

user_1.check_plan()

# upgrade plan
calculate_bagus_plan = user_1.upgrade_plan(upgrade_plan = "Premium Plan")

print(f"Plan baru yang harus Bagus bayar adalah: Rp {calculate_bagus_plan}")