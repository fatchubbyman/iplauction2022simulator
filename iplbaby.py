import random as rd
import time as ti
import numpy as np
#                                                                    dataBase
marquee_names = ["R Ashwin", "Trent Boult", "Pat Cummins", "Quinton De Kock", "Shikhar Dhawan", "Faf Du Plessis", "Shreyas Iyer", "Kagiso Rabada", "Mohammad Shami", "David Warner"]
marquee_nationalities = ["🛺", "✈️", "✈️", "✈️", "🛺", "✈️", "🛺", "✈️", "🛺", "✈️"]
marquee_roles = ["Bowler", "Bowler", "Bowler", "Wicketkeeper", "Batter", "Batter", "Batter", "Bowler", "Bowler", "Batter"]
marquee = [marquee_names,marquee_nationalities,marquee_roles]
ba1_names = ["Shimron Hetmyer", "David Miller", "Devdutt Padikkal", "Manish Pandey", "Suresh Raina", "Jason Roy", "Steve Smith", "Robin Uthappa"]
ba1_nationalities = ["✈️", "✈️", "🛺", "🛺", "🛺", "✈️", "✈️", "🛺"]
ba1_roles = ["Batter", "Batter", "Batter", "Batter", "Batter", "Batter", "Batter", "Batter"]
ba1 = [ba1_names,ba1_nationalities,ba1_roles]
al1_names = ["Shakib Al Hasan", "Dwayne Bravo", "Wanindu Hasaranga", "Jason Holder", "Mitchell Marsh", "Mohammad Nabi", "Krunal Pandya", "Harshal Patel", "Nitish Rana", "Washington Sundar"]
al1_nationalities = ["✈️", "✈️", "✈️", "✈️", "✈️", "✈️", "✈️", "✈️", "🛺", "🛺"]
al1_roles = ["All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder"]
al1 = [al1_names,al1_nationalities,al1_roles]
wks1_names = ["Jonny Bairstow","Sam Billings","Dinesh Karthik","Ishan Kishan","Nicholas Pooran","Ambati Rayudu","Wriddhiman Saha","Matthew Wade"]
wks1_nationalities = ["✈️", "✈️", "🛺", "🛺", "✈️", "🛺", "🛺", "✈️"]
wks1_roles = ["Wicketkeeper","Wicketkeeper","Wicketkeeper","Wicketkeeper","Wicketkeeper","Wicketkeeper","Wicketkeeper","Wicketkeeper"]
wks1 = [wks1_names,wks1_nationalities,wks1_roles]
seamers1_names = ["Deepak Chahar", "Lockie Ferguson", "Josh Hazlewood", "Prasidh Krishna", "Bhuvneshwar Kumar", "T. Natarajan", "Mustafizur Rahman", "Shardul Thakur", "Mark Wood", "Umesh Yadav"]
seamers1_nationalities = ["🛺", "✈️", "✈️", "🛺", "🛺", "🛺", "✈️", "🛺", "✈️", "🛺"]
seamers1_roles = ["Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler"]
seamers1 = [seamers1_names,seamers1_nationalities,seamers1_roles]
spinners1_names = ["Yuzvendra Chahal", "Rahul Chahar", "Amit Mishra", "Adil Rashid", "Imran Tahir", "Kuldeep Yadav", "Mujeeb Zadran", "Adam Zampa"]
spinners1_nationalities = ["🛺", "🛺", "🛺", "✈️", "✈️", "🛺", "✈️", "✈️"]
spinners1_roles = ["Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler"]
spinners1 = [spinners1_names,spinners1_nationalities,spinners1_roles]
ba2_names = ["Aaron Finch","Marnus Labuschagne","Dawid Malan","Aiden Markram","Eoin Morgan","Cheteshwar Pujara","Ajinkya Rahane","Mandeep Singh","Saurabh Tiwary"]
ba2_nationalities = ["✈️", "✈️", "✈️", "✈️", "✈️", "🛺", "🛺", "🛺","🛺"]
ba2_roles = ["Batter","Batter","Batter","Batter","Batter","Batter","Batter","Batter","Batter"]
ba2 = [ba2_names,ba2_nationalities,ba2_roles]
al2_names = ["Dominic Drakes","Shivam Dube","K Gowtham","Marco Jansen","Chris Jordan","Liam Livingstone","James Neesham","Vijay Shankar","Odean Smith","Jayant Yadav"]
al2_nationalities = ["✈️", "🛺", "🛺", "✈️", "✈️", "✈️", "✈️" "🛺", "✈️","🛺"]
al2_roles = ["All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder"]
al2 = [al2_names,al2_nationalities,al2_roles]
wks2_names = ["Liton Das","Niroshan Dickwella","Andre Fletcher","Rahmanullah Gurbaz","Shai Hope","Heinrich Klaasen","Ben Mcdermott","Kusal Mendis","Kusal Perera","Joshua Phillipe","Glenn Phillips","Tim Seifert"]
wks2_nationalities = ["✈️", "✈️", "✈️", "✈️", "✈️", "✈️", "✈️", "✈️", "✈️", "✈️", "✈️", "✈️"]
wk2_roles =["Wicketkeeper","Wicketkeeper","Wicketkeeper","Wicketkeeper","Wicketkeeper","Wicketkeeper","Wicketkeeper","Wicketkeeper","Wicketkeeper","Wicketkeeper","Wicketkeeper","Wicketkeeper"]
wls2 = [wks2_names,wks2_nationalities,wk2_roles]
seamers2_names = ["Khaleel Ahmed","Dushmanta Chameera","Sheldon Cottrell","Nathan Coulter-Nile","Lungi Ngidi","Navdeep Saini","Chetan Sakariya","Ishant Sharma","Sandeep Sharma","Jaydev Unadkat"]
seamers2_nationalities = ["🛺", "✈️", "✈️", "✈️", "✈️", "🛺", "🛺", "🛺", "🛺", "🛺"]
seamers2_roles = ["Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler"]
seamers2 = [seamers2_names,seamers2_nationalities,seamers2_roles]
spinners2_names = ["Qais Ahmad","Piyush Chawla","Mayank Markande","Shahbaz Nadeem","Tabraiz Shamsi","Karn Sharma","Ish Sodhi","Maheesh Theeksana","Noor Ahmad"]
spinners2_nationalities = ["✈️","🛺","🛺","🛺","✈️","🛺","✈️","✈️","✈️"]
spinners2_roles = ["Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler"]
spinners2 = [spinners2_names,spinners2_nationalities,spinners2_roles]
ba3_names = ["Finn Allen","Devon Convay","Alex Hales","Evin Lewis","Chris Lynn","Karun Nair","Rovman Powell","Rassie Van Der Dussen","Najibullah Zadran"]
ba3_nationalities = ["✈️","✈️","✈️","✈️","✈️","🛺","✈️","✈️"]
ba3_roles = ["Wicketkeepers","Wicketkeeper","Batter","Batter","Batter","Batter","All Rounder","Batter","Batter",]
ba3 = [ba3_names,ba3_nationalities,ba3_roles]
al3_names = ["Jofra Archer","Charith Asalanka","Rishi Dhawan","George Garton","Daryl Mitchell","Dwaine Pretorius","Sherfane Rutherford","Daniel Sams","Mitchell Santner","Romario Shepherd"]
al3_nationalities = ["✈️", "✈️", "🛺", "✈️", "✈️", "✈️", "✈️", "✈️", "✈️", "✈️"]
al3_roles = ["All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder"]
al3 = [al3_names,al3_nationalities,al3_roles]
seamers3_names = ["Jason Behrendorff","Nathan Ellis","Fazalhaq Farooqi","Siddarth Kaul","Obed Mccoy","Tymal Mills","Adam Milne","Reece Topley","Andrew Tye","Sandeep Warrier"]
seamers3_nationalities = ["✈️", "✈️", "✈️", "🛺", "✈️", "✈️", "✈️", "✈️", "✈️", "🛺"]   
seamers3_roles = ["Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler"]
seamers3 = [seamers3_names,seamers3_nationalities,seamers3_roles]
spinners3_names = ["Todd Astle","Akila Dhananjaya","Zahir Khan","Keshav Maharaj","Waqar Salamkheil","Rahul Sharma","Hayden Walsh"]
spinners3_nationalities = ["✈️", "✈️", "✈️", "✈️", "✈️", "🛺", "✈️"]
spinners3_roles = ["Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler"]
spinners3 = [spinners3_names,spinners1_nationalities,spinners3_roles]
ba4_names = ["Martin Guptill","Usman Khawaja","Brandon King","Janneman Malan","Bhanuka Rajapaksa","Rilee Russouw","Paul Stirling","Hanuma Vihari","James Vince","Hazratullah Zazai"]
ba4_nationalities = ["✈️", "✈️", "✈️", "✈️", "✈️", "✈️", "✈️", "🛺", "✈️", "✈️"]
ba4_roles = ["Batter","Batter","Batter","Batter","Wicketkeeper","Wicketkeeper","Batter","Batter","Batter","Batter"]
ba4 = [ba4_names,ba4_nationalities,ba4_roles]
al4_names = ["Fabien Allen","Roston Chase","Ben Cutting","Lewis Gregory","Moises Henriques","Akeal Hosein","Karim Janat","Scott Kuggeleijn","Pawan Negi","Gurkeerat Singh"]
al4_nationalities = ["✈️", "✈️", "✈️", "✈️", "✈️", "✈️", "✈️", "✈️", "🛺", "🛺"]
al4_roles = ["All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder"]
al4 = [al4_names,al4_nationalities,al4_roles]
seamers4_names = ["Sean Abbott","Taskin Ahmed","Merchant De Lange","Alzarri Joseph","Dhawal Kulkarni","Saqib Mahmood","Riley Meredith","Kane Richardson","Tim Southee","Naveen Ul Haq"]
seamers4_nationalities = ["✈️", "✈️", "✈️", "✈️", "🛺", "✈️", "✈️", "✈️", "✈️", "✈️"]
seamers4_roles = ["Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler"]
seamers4 = [seamers4_names,seamers4_nationalities,seamers4_roles]
al5_names = ["Ashton Agar", "Carlos Brathwaite", "Kedar Jadhav", "Chamika Karunaratne", "Colin Munro", "Gulbadin Naib", "Keemo Paul", "Parvez Rasool", "Dasun Shanaka", "David Willey"]
al5_nationalities = ["✈️", "✈️", "🛺", "✈️", "✈️", "✈️", "✈️", "🛺", "✈️", "✈️"]
al5_roles = ["All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder"]
al5 = [al5_names,al5_nationalities,al5_roles]
al6_names = ["Curtis Campher", "Colin De Grandhomme", "James Faulkner", "Craig Overton", "Wayne Parnell", "Samit Patel", "Thisara Perera", "Darcy Short", "Murali Vijay"]
al6_nationalities = ["✈️", "✈️", "✈️", "✈️", "✈️", "✈️", "✈️", "✈️", "🛺"]
al6_roles = ["All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","Batter"]
al6 = [al6_names,al6_nationalities,al6_roles]
uncapped_prospects_names = ["Dewald Brevis","Priyam Garg","Rajat Patidar","Anmolpreet Singh","Rahul Tripathi","Shahbaz Ahamad","Harpreet Brar","Deepak Hooda","Sarfaraz Khan","Shahrukh Khan","Shivam Mavi","Kamlesh Nagarkoti","Riyan Parag","Abhishek Sharma","Rahul Tewatia","KS Bharat","Anuj Rawat","Jitesh Sharma","Prabhsimran Singh","Vishnu Vinod","Akash Deep","Tushar Deshpande","Avesh Khan","Ishan Porel","Ankit Rajpoot","Basil Thampi","Kartik Tyagi","M Ashwin","Shreyas Gopal","Rinku SIngh","Gerald Coetzee","Sai Kishore"]
uncapped_prospects_nationalities = ["✈️", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺","✈️" ,"🛺"]
uncapped_prospects_roles = ["Batter","Batter","Batter","Batter","Batter","All Rounder","All Rounder","All Rounder","Batter","Batter","Bowler","Bowler","All Rounder","All Rounder","All Rounder","Wicketkeeper","Wicketkeeper","Wicketkeeper","Wicketkeeper","Wicketkeeper","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Batter","Bowler","All Rounder"]
uncapped_prospects = [uncapped_prospects_names,uncapped_prospects_nationalities,uncapped_prospects_roles]


top_bids_csk = ["Deepak Chahar","Ambati Rayudu"]
medium_bids_csk = ["Dwayne Bravo","Shivam Dube","Chris Jordan"]
meh_bids_csk = ["Robin Uthappa","Maheesh Theeksana","Mitchell Santner","Devon Convay"]
top_bids_dc = ["Shardul Thakur","Mitchell Marsh","David Warner"]
medium_bids_dc = ["Khaleel Ahmed","Chetan Sakariya","Rovman Powell","Mustafizur Rahman"]
meh_bids_dc = ["KS Bharat","Kuldeep Yadav","Kamlesh Nagarkoti"]
top_bids_gt = ["Lockie Ferguson","Rahul Tewatia","Mohammed Shami"]
medium_bids_gt = ["Yash Dayal","Sai Kishore","David Miller","Matthew Wade","Alzarri Joseph"]
meh_bids_gt = ["Jason Roy","Wriddhiman Saha","Jayant Yadav","Vijay Shankar"]
top_bids_kkr = ["Shreyas Iyer","Nitish Rana","Pat Cummins"]
medium_bids_kkr = ["Sam Billings","Umesh Yadav"]
meh_bids_kkr = ["Tim Southee","Alex Hales","Mohammad Nabi","Ajinkya Rahane"]
top_bids_lsg = ["Avesh Khan","Jason Holder","Krunal Pandya","Mark Wood","Quinton De Kock"]
medium_bids_lsg = ["Deepak Hooda","Manish Pandey","Evin Lewis","Dushmanta Chameera"]
meh_bids_lsg = ["K Gowtham","Shahbaz Nadeem","Kyle Mayers"]
top_bids_mi = ["Ishan Kishan","Tim David","Jofra Archer"]
medium_bids_mi = ["Dewald Brevis","Daniel Sams","Tilak Varma","M Ashwin","Tymal Mills"]
meh_bids_mi = ["Jaydev Unadkat","Riley Meredith","Fabian Allen","Mayank Markande"]
top_bids_pbks = ["Liam Livingstone","Kagiso Rabada","Shahrukh Khan","Shikhar Dhawan","Jonny Bairstow"]
medium_bids_pbks = ["Odean Smith","Rahul Chahar","Harpreet Brar"]
meh_bids_pbks = ["Nathan Ellis","Prabhsimran Singh","Rishi Dhawan","Bhanuka Rajapaksa"]
top_bids_rr = ["Prasidh Krishna","Shimron Hetmyer","Trent Boult","Devdutt Padikkal","Yuzvendra Chahal"]
medium_bids_rr = ["R Ashwin","Riyan Parag","Navdeep Saini","Nathan Coulter-Nile"]
meh_bids_rr = ["James Neesham","Karun Nair","Daryl Mitchell"]
top_bids_rcb = ["Harshal Patel","Wanindu Hasaranga","Josh Hazlewood","Faf du Plessis"]
medium_bids_rcb = ["Dinesh Karthik","Anuj Rawat","Shahbaz Ahmed","David Willey","Sherfane Rutherford"]
meh_bids_rcb = ["Finn Allen","Jason Behrendorff","Siddarth Kaul","Karn Sharma"]
top_bids_srh = ["Nicholas Pooran","Washington Sundar","Rahul Tripathi","Romario Shepherd","Abhishek Sharma"]
medium_bids_srh = ["Bhuvneshwar Kumar","Marco Jansen","Kartik Tyagi","T Natarajan","Aiden Markram"]
meh_bids_srh = ["Sean Abbott","Glenn Phillips","Vishnu Vinod","Fazalhaq Farooqi","Priyam Garg"]

csk_ai_top = ["bid","bid","bid","bid","bid","bid","bid","bid","no","no","no"] #7/10 based off how bad they want these players
csk_ai_mid = ["bid","bid","bid","bid","no","no","no","no","no","no"] #4/10 based off how bad they want these players
csk_ai_meh = ["bid","bid","bid","no","no","no","no","no","no","no"] #3/10 based off how bad they want these players
csk_ai_f_around = ["no","no","no","no","no","no","no","no","no","bid"] #1/10 based off how bad they want these players
dc_ai_top = ["bid","bid","bid","bid","bid","bid","bid","bid","no","no","no"] #7/10 based off how bad they want these players
dc_ai_mid = ["bid","bid","bid","bid","no","no","no","no","no","no"] #4/10 based off how bad they want these players
dc_ai_meh = ["bid","bid","bid","no","no","no","no","no","no","no"] #3/10 based off how bad they want these players
dc_ai_f_around = ["no","no","no","no","no","no","no","no","bid","bid"] #2/10 based off how bad they want these players
gt_ai_top = ["bid","bid","bid","bid","bid","bid","bid","bid","no","no","no"] #7/10 based off how bad they want these players
gt_ai_mid = ["bid","bid","bid","bid","no","no","no","no","no","no"] #4/10 based off how bad they want these players
gt_ai_meh = ["bid","bid","bid","no","no","no","no","no","no","no"] #3/10 based off how bad they want these players
gt_ai_f_around = ["no","no","no","no","no","no","no","no","no","bid"] #1/10 based off how bad they want these players 
kkr_ai_top = ["bid","bid","bid","bid","bid","bid","bid","bid","no","no","no"] #7/10 based off how bad they want these players
kkr_ai_mid = ["bid","bid","bid","bid","no","no","no","no","no","no"] #4/10 based off how bad they want these players
kkr_ai_meh = ["bid","bid","bid","no","no","no","no","no","no","no"] #3/10 based off how bad they want these players
kkr_ai_f_around = ["no","no","no","no","no","no","no","no","no","bid"] #1/10 based off how bad they want these players
lsg_ai_top = ["bid","bid","bid","bid","bid","bid","bid","bid","no","no","no"] #7/10 based off how bad they want these players
lsg_ai_mid = ["bid","bid","bid","bid","no","no","no","no","no","no"] #4/10 based off how bad they want these players
lsg_ai_meh = ["bid","bid","bid","no","no","no","no","no","no","no"] #3/10 based off how bad they want these players
lsg_ai_f_around = ["no","no","no","no","no","no","no","no","no","bid"] #1/10 based off how bad they want these players
mi_ai_top = ["bid","bid","bid","bid","bid","bid","bid","bid","no","no","no"] #7/10 based off how bad they want these players
mi_ai_mid = ["bid","bid","bid","bid","no","no","no","no","no","no"] #4/10 based off how bad they want these players
mi_ai_meh = ["bid","bid","bid","no","no","no","no","no","no","no"] #3/10 based off how bad they want these players
mi_ai_f_around = ["no","no","no","no","no","no","no","no","no","bid"] #1/10 based off how bad they want these players
pbks_ai_top = ["bid","bid","bid","bid","bid","bid","bid","bid","no","no","no"] #7/10 based off how bad they want these players
pbks_ai_mid = ["bid","bid","bid","bid","no","no","no","no","no","no"] #4/10 based off how bad they want these players
pbks_ai_meh = ["bid","bid","bid","no","no","no","no","no","no","no"] #3/10 based off how bad they want these players
pbks_ai_f_around = ["no","no","no","no","no","no","no","no","no","bid"] #1/10 based off how bad they want these players
rr_ai_top = ["bid","bid","bid","bid","bid","bid","bid","bid","no","no","no"] #7/10 based off how bad they want these players
rr_ai_mid = ["bid","bid","bid","bid","no","no","no","no","no","no"] #4/10 based off how bad they want these players
rr_ai_meh = ["bid","bid","bid","no","no","no","no","no","no","no"] #3/10 based off how bad they want these players
rr_ai_f_around = ["no","no","no","no","no","no","no","no","no","bid"] #1/10 based off how bad they want these players
rcb_ai_top = ["bid","bid","bid","bid","bid","bid","bid","bid","no","no","no"] #7/10 based off how bad they want these players
rcb_ai_mid = ["bid","bid","bid","bid","no","no","no","no","no","no"] #4/10 based off how bad they want these players
rcb_ai_meh = ["bid","bid","bid","no","no","no","no","no","no","no"] #3/10 based off how bad they want these players
rcb_ai_f_around = ["no","no","no","no","no","no","no","no","no","bid"] #1/10 based off how bad they want these players
srh_ai_top = ["bid","bid","bid","bid","bid","bid","bid","bid","no","no","no"] #7/10 based off how bad they want these players
srh_ai_mid = ["bid","bid","bid","bid","no","no","no","no","no","no"] #4/10 based off how bad they want these players
srh_ai_meh = ["bid","bid","bid","no","no","no","no","no","no","no"] #3/10 based off how bad they want these players
srh_ai_f_around = ["no","no","no","no","no","no","no","no","no","bid"] #1/10 based off how bad they want these players

teams = ['csk','dc','gt','kkr','lsg','mi','pbks','rr','rcb','srh']

class Team:
    def __init__(self,purse,bmen,arounders,bwlrs,overseas,wks,name):
        self.purse = purse
        self.bmen = bmen
        self.arounders = arounders
        self.bwlrs = bwlrs
        self.overseas = overseas
        self.wks = wks
        self.name = name
    
    def decision_making(self,team):
        pass
        

class Player:
    def __init__(self,role,price,nationality,name): 
        self.role = role
        self.price = price
        self.nationality = nationality
        self.name = name

    def bid(self):
        self.price += 2500000

your_team = input("What team do you want to play as? ")
teams.remove(your_team)
for i in range(len(teams)):
    teams[i] = Team()  # creating objects of all the teams for the shit they can do       
# making all players into objects

def ai(i = 0):
    for i in range(9):
        pass
    
          
def bidding(set,i = 0):
    for i in range(len(set)):
        active_player = rd.choice(set)
        x = set[0].index(active_player)
        act = Player(name=active_player,role=set[2][x],nationality=set[1][x],price=)
        print(f'It\'s {act.name} from {act.nationality} starting at ₹{act.price} please? ')
        # your input bid
        for i in range(9):
            # a function that probably takes in the bids of the other teams
            pass

            
            
    
