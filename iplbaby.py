import random as rd
import time as ti
# checking which team lastly bid is a problem
# if this project is more data driven, or it has machine learning shi then its a decent ass project
#                                                                    dataBase
marquee_names = ["R Ashwin", "Trent Boult", "Pat Cummins", "Quinton De Kock", "Shikhar Dhawan", "Faf Du Plessis", "Shreyas Iyer", "Kagiso Rabada", "Mohammad Shami", "David Warner"]
marquee_nationalities = ["🛺", "✈️", "✈️", "✈️", "🛺", "✈️", "🛺", "✈️", "🛺", "✈️"]
marquee_roles = ["Bowler", "Bowler", "Bowler", "Wicketkeeper", "Batter", "Batter", "Batter", "Bowler", "Bowler", "Batter"]
marquee = [marquee_names,marquee_nationalities,marquee_roles,20000000]
ba1_names = ["Shimron Hetmyer", "David Miller", "Devdutt Padikkal", "Manish Pandey", "Suresh Raina", "Jason Roy", "Steve Smith", "Robin Uthappa"]
ba1_nationalities = ["✈️", "✈️", "🛺", "🛺", "🛺", "✈️", "✈️", "🛺"]
ba1_roles = ["Batter", "Batter", "Batter", "Batter", "Batter", "Batter", "Batter", "Batter"]
ba1 = [ba1_names,ba1_nationalities,ba1_roles,10000000]
al1_names = ["Shakib Al Hasan", "Dwayne Bravo", "Wanindu Hasaranga", "Jason Holder", "Mitchell Marsh", "Mohammad Nabi", "Krunal Pandya", "Harshal Patel", "Nitish Rana", "Washington Sundar"]
al1_nationalities = ["✈️", "✈️", "✈️", "✈️", "✈️", "✈️", "✈️", "✈️", "🛺", "🛺"]
al1_roles = ["All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder"]
al1 = [al1_names,al1_nationalities,al1_roles,10000000]
wks1_names = ["Jonny Bairstow","Sam Billings","Dinesh Karthik","Ishan Kishan","Nicholas Pooran","Ambati Rayudu","Wriddhiman Saha","Matthew Wade"]
wks1_nationalities = ["✈️", "✈️", "🛺", "🛺", "✈️", "🛺", "🛺", "✈️"]
wks1_roles = ["Wicketkeeper","Wicketkeeper","Wicketkeeper","Wicketkeeper","Wicketkeeper","Wicketkeeper","Wicketkeeper","Wicketkeeper"]
wks1 = [wks1_names,wks1_nationalities,wks1_roles,10000000]
seamers1_names = ["Deepak Chahar", "Lockie Ferguson", "Josh Hazlewood", "Prasidh Krishna", "Bhuvneshwar Kumar", "T. Natarajan", "Mustafizur Rahman", "Shardul Thakur", "Mark Wood", "Umesh Yadav"]
seamers1_nationalities = ["🛺", "✈️", "✈️", "🛺", "🛺", "🛺", "✈️", "🛺", "✈️", "🛺"]
seamers1_roles = ["Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler"]
seamers1 = [seamers1_names,seamers1_nationalities,seamers1_roles,10000000]
spinners1_names = ["Yuzvendra Chahal", "Rahul Chahar", "Amit Mishra", "Adil Rashid", "Imran Tahir", "Kuldeep Yadav", "Mujeeb Zadran", "Adam Zampa"]
spinners1_nationalities = ["🛺", "🛺", "🛺", "✈️", "✈️", "🛺", "✈️", "✈️"]
spinners1_roles = ["Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler"]
spinners1 = [spinners1_names,spinners1_nationalities,spinners1_roles,10000000]
ba2_names = ["Aaron Finch","Marnus Labuschagne","Dawid Malan","Aiden Markram","Eoin Morgan","Cheteshwar Pujara","Ajinkya Rahane","Mandeep Singh","Saurabh Tiwary"]
ba2_nationalities = ["✈️", "✈️", "✈️", "✈️", "✈️", "🛺", "🛺", "🛺","🛺"]
ba2_roles = ["Batter","Batter","Batter","Batter","Batter","Batter","Batter","Batter","Batter"]
ba2 = [ba2_names,ba2_nationalities,ba2_roles,5000000]
al2_names = ["Dominic Drakes","Shivam Dube","K Gowtham","Marco Jansen","Chris Jordan","Liam Livingstone","James Neesham","Vijay Shankar","Odean Smith","Jayant Yadav"]
al2_nationalities = ["✈️", "🛺", "🛺", "✈️", "✈️", "✈️", "✈️" "🛺", "✈️","🛺"]
al2_roles = ["All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder"]
al2 = [al2_names,al2_nationalities,al2_roles,5000000]
wks2_names = ["Liton Das","Niroshan Dickwella","Andre Fletcher","Rahmanullah Gurbaz","Shai Hope","Heinrich Klaasen","Ben Mcdermott","Kusal Mendis","Kusal Perera","Joshua Phillipe","Glenn Phillips","Tim Seifert"]
wks2_nationalities = ["✈️", "✈️", "✈️", "✈️", "✈️", "✈️", "✈️", "✈️", "✈️", "✈️", "✈️", "✈️"]
wk2_roles =["Wicketkeeper","Wicketkeeper","Wicketkeeper","Wicketkeeper","Wicketkeeper","Wicketkeeper","Wicketkeeper","Wicketkeeper","Wicketkeeper","Wicketkeeper","Wicketkeeper","Wicketkeeper"]
wks2 = [wks2_names,wks2_nationalities,wk2_roles,5000000]
seamers2_names = ["Khaleel Ahmed","Dushmanta Chameera","Sheldon Cottrell","Nathan Coulter-Nile","Lungi Ngidi","Navdeep Saini","Chetan Sakariya","Ishant Sharma","Sandeep Sharma","Jaydev Unadkat"]
seamers2_nationalities = ["🛺", "✈️", "✈️", "✈️", "✈️", "🛺", "🛺", "🛺", "🛺", "🛺"]
seamers2_roles = ["Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler"]
seamers2 = [seamers2_names,seamers2_nationalities,seamers2_roles,5000000]
spinners2_names = ["Qais Ahmad","Piyush Chawla","Mayank Markande","Shahbaz Nadeem","Tabraiz Shamsi","Karn Sharma","Ish Sodhi","Maheesh Theeksana","Noor Ahmad"]
spinners2_nationalities = ["✈️","🛺","🛺","🛺","✈️","🛺","✈️","✈️","✈️"]
spinners2_roles = ["Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler"]
spinners2 = [spinners2_names,spinners2_nationalities,spinners2_roles,5000000]
ba3_names = ["Finn Allen","Devon Convay","Alex Hales","Evin Lewis","Chris Lynn","Karun Nair","Rovman Powell","Rassie Van Der Dussen","Najibullah Zadran"]
ba3_nationalities = ["✈️","✈️","✈️","✈️","✈️","🛺","✈️","✈️"]
ba3_roles = ["Wicketkeepers","Wicketkeeper","Batter","Batter","Batter","Batter","All Rounder","Batter","Batter",]
ba3 = [ba3_names,ba3_nationalities,ba3_roles,5000000]
al3_names = ["Jofra Archer","Charith Asalanka","Rishi Dhawan","George Garton","Daryl Mitchell","Dwaine Pretorius","Sherfane Rutherford","Daniel Sams","Mitchell Santner","Romario Shepherd"]
al3_nationalities = ["✈️", "✈️", "🛺", "✈️", "✈️", "✈️", "✈️", "✈️", "✈️", "✈️"]
al3_roles = ["All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder"]
al3 = [al3_names,al3_nationalities,al3_roles,5000000]
seamers3_names = ["Jason Behrendorff","Nathan Ellis","Fazalhaq Farooqi","Siddarth Kaul","Obed Mccoy","Tymal Mills","Adam Milne","Reece Topley","Andrew Tye","Sandeep Warrier"]
seamers3_nationalities = ["✈️", "✈️", "✈️", "🛺", "✈️", "✈️", "✈️", "✈️", "✈️", "🛺"]   
seamers3_roles = ["Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler"]
seamers3 = [seamers3_names,seamers3_nationalities,seamers3_roles,5000000]
spinners3_names = ["Todd Astle","Akila Dhananjaya","Zahir Khan","Keshav Maharaj","Waqar Salamkheil","Rahul Sharma","Hayden Walsh"]
spinners3_nationalities = ["✈️", "✈️", "✈️", "✈️", "✈️", "🛺", "✈️"]
spinners3_roles = ["Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler"]
spinners3 = [spinners3_names,spinners1_nationalities,spinners3_roles,5000000]
ba4_names = ["Martin Guptill","Usman Khawaja","Brandon King","Janneman Malan","Bhanuka Rajapaksa","Rilee Russouw","Paul Stirling","Hanuma Vihari","James Vince","Hazratullah Zazai"]
ba4_nationalities = ["✈️", "✈️", "✈️", "✈️", "✈️", "✈️", "✈️", "🛺", "✈️", "✈️"]
ba4_roles = ["Batter","Batter","Batter","Batter","Wicketkeeper","Wicketkeeper","Batter","Batter","Batter","Batter"]
ba4 = [ba4_names,ba4_nationalities,ba4_roles,5000000]
al4_names = ["Fabien Allen","Roston Chase","Ben Cutting","Lewis Gregory","Moises Henriques","Akeal Hosein","Karim Janat","Scott Kuggeleijn","Pawan Negi","Gurkeerat Singh"]
al4_nationalities = ["✈️", "✈️", "✈️", "✈️", "✈️", "✈️", "✈️", "✈️", "🛺", "🛺"]
al4_roles = ["All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder"]
al4 = [al4_names,al4_nationalities,al4_roles,5000000]
seamers4_names = ["Sean Abbott","Taskin Ahmed","Merchant De Lange","Alzarri Joseph","Dhawal Kulkarni","Saqib Mahmood","Riley Meredith","Kane Richardson","Tim Southee","Naveen Ul Haq"]
seamers4_nationalities = ["✈️", "✈️", "✈️", "✈️", "🛺", "✈️", "✈️", "✈️", "✈️", "✈️"]
seamers4_roles = ["Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler"]
seamers4 = [seamers4_names,seamers4_nationalities,seamers4_roles,5000000]
al5_names = ["Ashton Agar", "Carlos Brathwaite", "Kedar Jadhav", "Chamika Karunaratne", "Colin Munro", "Gulbadin Naib", "Keemo Paul", "Parvez Rasool", "Dasun Shanaka", "David Willey"]
al5_nationalities = ["✈️", "✈️", "🛺", "✈️", "✈️", "✈️", "✈️", "🛺", "✈️", "✈️"]
al5_roles = ["All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder"]
al5 = [al5_names,al5_nationalities,al5_roles,5000000]
al6_names = ["Curtis Campher", "Colin De Grandhomme", "James Faulkner", "Craig Overton", "Wayne Parnell", "Samit Patel", "Thisara Perera", "Darcy Short", "Murali Vijay"]
al6_nationalities = ["✈️", "✈️", "✈️", "✈️", "✈️", "✈️", "✈️", "✈️", "🛺"]
al6_roles = ["All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","Batter"]
al6 = [al6_names,al6_nationalities,al6_roles,5000000]
uncapped_prospects_names = ["Dewald Brevis","Priyam Garg","Rajat Patidar","Anmolpreet Singh","Rahul Tripathi","Shahbaz Ahamad","Harpreet Brar","Deepak Hooda","Sarfaraz Khan","Shahrukh Khan","Shivam Mavi","Kamlesh Nagarkoti","Riyan Parag","Abhishek Sharma","Rahul Tewatia","KS Bharat","Anuj Rawat","Jitesh Sharma","Prabhsimran Singh","Vishnu Vinod","Akash Deep","Tushar Deshpande","Avesh Khan","Ishan Porel","Ankit Rajpoot","Basil Thampi","Kartik Tyagi","M Ashwin","Shreyas Gopal","Rinku SIngh","Gerald Coetzee","Sai Kishore"]
uncapped_prospects_nationalities = ["✈️", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺","✈️" ,"🛺"]
uncapped_prospects_roles = ["Batter","Batter","Batter","Batter","Batter","All Rounder","All Rounder","All Rounder","Batter","Batter","Bowler","Bowler","All Rounder","All Rounder","All Rounder","Wicketkeeper","Wicketkeeper","Wicketkeeper","Wicketkeeper","Wicketkeeper","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Batter","Bowler","All Rounder"]
uncapped_prospects = [uncapped_prospects_names,uncapped_prospects_nationalities,uncapped_prospects_roles,2000000]


top_bids_csk = ["Deepak Chahar","Ambati Rayudu"]
medium_bids_csk = ["Dwayne Bravo","Shivam Dube","Chris Jordan"]
meh_bids_csk = ["Robin Uthappa","Maheesh Theeksana","Mitchell Santner","Devon Convay"]
csk_bids = [top_bids_csk,medium_bids_csk,meh_bids_csk]
top_bids_dc = ["Shardul Thakur","Mitchell Marsh","David Warner"]
medium_bids_dc = ["Khaleel Ahmed","Chetan Sakariya","Rovman Powell","Mustafizur Rahman"]
meh_bids_dc = ["KS Bharat","Kuldeep Yadav","Kamlesh Nagarkoti"]
dc_bids = [top_bids_dc,medium_bids_dc,meh_bids_dc]
top_bids_gt = ["Lockie Ferguson","Rahul Tewatia","Mohammed Shami"]
medium_bids_gt = ["Yash Dayal","Sai Kishore","David Miller","Matthew Wade","Alzarri Joseph"]
meh_bids_gt = ["Jason Roy","Wriddhiman Saha","Jayant Yadav","Vijay Shankar"]
gt_bids = [top_bids_gt,medium_bids_gt,meh_bids_gt]
top_bids_kkr = ["Shreyas Iyer","Nitish Rana","Pat Cummins"]
medium_bids_kkr = ["Sam Billings","Umesh Yadav"]
meh_bids_kkr = ["Tim Southee","Alex Hales","Mohammad Nabi","Ajinkya Rahane"]
kkr_bids = [top_bids_kkr,medium_bids_kkr,meh_bids_kkr]
top_bids_lsg = ["Avesh Khan","Jason Holder","Krunal Pandya","Mark Wood","Quinton De Kock"]
medium_bids_lsg = ["Deepak Hooda","Manish Pandey","Evin Lewis","Dushmanta Chameera"]
meh_bids_lsg = ["K Gowtham","Shahbaz Nadeem","Kyle Mayers"]
lsg_bids = [top_bids_lsg,medium_bids_lsg,meh_bids_lsg]
top_bids_mi = ["Ishan Kishan","Tim David","Jofra Archer"]
medium_bids_mi = ["Dewald Brevis","Daniel Sams","Tilak Varma","M Ashwin","Tymal Mills"]
meh_bids_mi = ["Jaydev Unadkat","Riley Meredith","Fabian Allen","Mayank Markande"]
mi_bids = [top_bids_mi,medium_bids_mi,meh_bids_mi]
top_bids_pbks = ["Liam Livingstone","Kagiso Rabada","Shahrukh Khan","Shikhar Dhawan","Jonny Bairstow"]
medium_bids_pbks = ["Odean Smith","Rahul Chahar","Harpreet Brar"]
meh_bids_pbks = ["Nathan Ellis","Prabhsimran Singh","Rishi Dhawan","Bhanuka Rajapaksa"]
pbks_bids = [top_bids_pbks,medium_bids_pbks,meh_bids_pbks]
top_bids_rr = ["Prasidh Krishna","Shimron Hetmyer","Trent Boult","Devdutt Padikkal","Yuzvendra Chahal"]
medium_bids_rr = ["R Ashwin","Riyan Parag","Navdeep Saini","Nathan Coulter-Nile"]
meh_bids_rr = ["James Neesham","Karun Nair","Daryl Mitchell"]
rr_bids = [top_bids_rr,medium_bids_rr,meh_bids_rr]
top_bids_rcb = ["Harshal Patel","Wanindu Hasaranga","Josh Hazlewood","Faf du Plessis"]
medium_bids_rcb = ["Dinesh Karthik","Anuj Rawat","Shahbaz Ahmed","David Willey","Sherfane Rutherford"]
meh_bids_rcb = ["Finn Allen","Jason Behrendorff","Siddarth Kaul","Karn Sharma"]
rcb_bids = [top_bids_rcb,medium_bids_rcb,meh_bids_rcb]
top_bids_srh = ["Nicholas Pooran","Washington Sundar","Rahul Tripathi","Romario Shepherd","Abhishek Sharma"]
medium_bids_srh = ["Bhuvneshwar Kumar","Marco Jansen","Kartik Tyagi","T Natarajan","Aiden Markram"]
meh_bids_srh = ["Sean Abbott","Glenn Phillips","Vishnu Vinod","Fazalhaq Farooqi","Priyam Garg"]
srh_bids = [top_bids_srh,medium_bids_srh,meh_bids_srh]

teams = ['csk','dc','gt','kkr','lsg','mi','pbks','rr','rcb','srh']

def wait():
    for i in range(3):
        print(".")
        ti.sleep(0.5)  

def look_around():
    for i in range(3):
        print(".")
        ti.sleep(0.2)  
        
          
class Team:
    squad = []
    def __init__(self,purse,bmen,arounders,bwlrs,overseas,wks,name,strats,squad):
        self.purse = purse
        self.bmen = bmen
        self.arounders = arounders
        self.bwlrs = bwlrs
        self.overseas = overseas
        self.wks = wks
        self.name = name
        self.strats = strats
        self.squad = squad
    
    def bid(self,amount,player):
        player.bidding(amount)
        
    def decision_making(self,player,bids):
        if player in self.strats:
            if player in self.strats[0]:
                options = ['bid','no bid']
                probabilities = [0.7,0.3]
                result = rd.choices(options,probabilities)
                if result[0] == 'bid':
                    bids[self.name] = 'bid'
                    self.bid(2000000,player)
                    print(f'{self.name} has raised the bid by 20 lakh!,{player.price+2000000} please?')
                    look_around()
                else:
                    pass
            elif player in self.strats[1]:
                options = ['bid','no bid']
                probabilities = [0.4,0.6]
                result = rd.choices(options,probabilities)
                if result[0] == 'bid':
                    bids[self.name] = 'bid'
                    self.bid(2000000,player)
                    print(f'{self.name} has raised the bid by 20 lakh!,{player.price+2000000} please?')
                    look_around()
                else:
                    pass
            elif player in self.strats[2]:
                options = ['bid','no bid']
                probabilities = [0.2,0.8]
                result = rd.choices(options,probabilities)
                if result[0] == 'bid':
                    bids[self.name] = 'bid'
                    self.bid(2000000,player)
                    print(f'{self.name} has raised the bid by 20 lakh!,{player.price+2000000} please?')
                    look_around()
                else:
                    pass
        else:
            options = ['bid','no bid']
            probabilities = [0.1,0.9]
            result = rd.choices(options,probabilities)
            if result[0] == 'bid':
                bids[self.name] = 'bid'
                self.bid(2000000,player)
                print(f'{self.name} has raised the bid by 20 lakh!,{player.price+2000000} please?')
                look_around()
            else:
                pass
    

class Player:
    
    isSold = False
    def __init__(self,role,price,nationality,name): 
        self.role = role
        self.price = price
        self.nationality = nationality
        self.name = name

    def bidding(self,amount):
        self.price += amount

your_team = input("What team do you want to play as?(csk,dc,gt,kkr,lsg,mi,pbks,rr,rcb,srh) ")
teams_o = []         # objects of all teams
for i in range(len(teams)):
    if teams[i] == 'csk':
        csk = Team(purse=480000000,bmen=1,arounders=2,bwlrs=0,overseas=1,wks=1,name='csk',strats=csk_bids,squad =["Ravindra Jadeja","MS Dhoni","Moeen Ali","Ruturaj Gaikwad"])
        teams_o.append(csk)
    elif teams[i] == 'dc':
        dc = Team(purse=475000000,bmen=1,arounders=1,bwlrs=1,overseas=1,wks=1,name='dc',strats=dc_bids,squad = ["Rishabh Pant","Axar Patel","Prithvi Shaw","Anrich Nortje"])
        teams_o.append(dc)
    elif teams[i] == 'gt':
        gt = Team(purse=598000000,bmen=1,arounders=1,bwlrs=1,overseas=1,wks=0,name='gt',strats=gt_bids,squad = ["Shubman Gill","Hardik Pandya","Rashid Khan"])
        teams_o.append(gt)
    elif teams[i] == 'kkr':
        kkr = Team(purse=480000000,bmen=0,arounders=3,bwlrs=1,overseas=2,wks=0,name='kkr',strats=kkr_bids,squad = ["Andre Russell","Varun Chakravarthy","Venkatesh Iyer","Sunil Narine"])
        teams_o.append(kkr)
    elif teams[i] == 'lsg':
        lsg = Team(purse=598000000,bmen=0,arounders=1,bwlrs=1,overseas=1,wks=1,name='lsg',strats=lsg_bids,squad = ["KL Rahul","Marcus Stoinis","Ravi Bishnoi"])
        teams_o.append(lsg)
    elif teams[i] == 'mi':
        mi = Team(purse=480000000,bmen=2,arounders=1,bwlrs=1,overseas=1,wks=0,name='mi',strats=mi_bids,squad = ["Rohit Sharma","Jasprit Bumrah","Suryakumar Yadav","Kieron Pollard"])
        teams_o.append(mi)
    elif teams[i] == 'pbks':
        pbks = Team(purse=720000000,bmen=1,arounders=0,bwlrs=1,overseas=0,wks=0,name='pbks',strats=pbks_bids,squad = ["Mayank Agarwal","Arshdeep Singh"])
        teams_o.append(pbks)
    elif teams[i] == 'rr':
        rr = Team(purse=620000000,bmen=1,arounders=0,bwlrs=0,overseas=1,wks=2,name='rr',strats=rr_bids,squad = ["Sanju Samson","Jos Buttler","Yashasvi Jaiswal"])
        teams_o.append(pbks)
    elif teams[i] == 'rcb':
        rcb = Team(purse=570000000,bmen=1,arounders=1,bwlrs=1,overseas=1,wks=0,name='rcb',strats=rcb_bids,squad = ["Virat Kohli","Glenn Maxwell","Mohammed Siraj"])
        teams_o.append(rcb)
    elif teams[i] == 'srh':
        srh = Team(purse=680000000,bmen=2,arounders=0,bwlrs=1,overseas=1,wks=0,name='srh',strats=srh_bids,squad = ["Kane Williamson","Abdul Samad","Umran Malik"])
        teams_o.append(srh)     

for i in range(len(teams_o)):
    if teams_o[i].name == your_team:
        your_team = teams_o[i]
        teams_o.remove(teams_o[i])
        teams.remove(teams[i])

def ai(player,bids):
    for i in range(len(teams_o)):
        teams_o[i].decision_making(player,bids) #this function checks if the player is important and actively bids for the player accordingly
        pass

def adding(player,team):
    team.squad.append(player.name)
    team.purse -= player.price
    if player.role == 'Batter':
        team.bmen += 1
    elif player.role == 'Wicketkeeper':
        team.wks += 1
    elif player.role == 'Bowler':
        team.bwlrs += 1
    elif player.role == 'All Rounder':
        team.arounders += 1
    if player.nationality == "✈️":
        team.overseas += 1

def removing(player,set,index):
    set[0].remove(player)
    set[1].remove(set[1][index])
    set[2].remove(set[2][index])
      
          
def bidding(set):
    for i in range(len(set)):
        active_player = rd.choice(set)
        x = set[0].index(active_player)
        act = Player(name=active_player,role=set[2][x],nationality=set[1][x],price=set[3])
        print(f'It\'s {act.name} from {act.nationality} starting at ₹{act.price} please? ')
        wait()
        bid = input("bid? enter to bid/type no to pass")
        checker = ['no bid','no bid','no bid','no bid','no bid','no bid''no bid','no bid','no bid']  
        if bid == '':
            while act.isSold == False:
                bids = {}
                for i in range(len(teams)):
                    bids[teams[i]] = 'no bid'
                ai(player = active_player,bids = bids)
                if bids.values() == checker:
                    adding(player=act,team = your_team)
                    removing(player=active_player,set=set,index=x)
                    act.isSold = True
                else:
                    pass
                bid = input("bid again?(click enter to bid)/(type anything to skip the bid)")
                if bid == '':
                    continue
                else:
                    print(f'{act.name} will be sold to the (last bidder???) at {act.price}') # need the record of the last bidder
                    removing(player=active_player,set=set,index=x)
                    act.isSold = True
        else:
            wait()
            print(f"{act.name} will remain unsold!, next player please!")
            removing(player=active_player,set=set,index=x)
            act.isSold = True

# executing all the sets
bidding(marquee)
bidding(ba1)
bidding(al1)
bidding(wks1)
bidding(seamers1)
bidding(spinners1)
bidding(ba2)
bidding(al2)
bidding(wks2)
bidding(seamers2)
bidding(spinners2)
bidding(ba3)
bidding(al3)
bidding(seamers3)
bidding(spinners3)
bidding(ba4)
bidding(al4)
bidding(seamers4)
bidding(al5)
bidding(al6)
bidding(uncapped_prospects)            
            

            
            
     
