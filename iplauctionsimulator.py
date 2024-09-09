#                                                          ideas/scrapped ideas
#random (with probability)
#find a way to skip players that will be bought by other teams
#this is gonna be a big fckn nest of random numbers
#squads of 15
#retentions(maybe?)
#upload excel sheet(try to make python read it himself or ask chatgpt to make a list)
#squad of 15(3 all rounders,5 batsmen, 2wk, 5 bowlers)
#make rounds of maqruee players, .etc
#starting purse start from 90 cr/ after retention money
#to make probability using random, you can make the sample size more frequent,less frequently according to that you can make random more biased and all
#study 8 hours of ipl auction footage and draw conclusions about auction behavior and how teams manage new players and study auction strategies
#we have all seen how important having a good auction is to winning a tournament like the indian premier league, like kkr did and won by that margin
#use emojis to make your code look more playable
#every team has styles of auctioning, make tables on when what teams bid for what people and when they stop
#after all this code we would have an ai of ourselves after taking in training data from that footage
# https://www.jiocinema.com/sports/tata-ipl-auction-2023-replay/3477762
# https://www.jiocinema.com/sports/cricket/ipl-2024-auction-replay/3875876
#have fun lmao
#we are making an ai with a number of binary statements which are numberized with different to proportions to reflect their chance of getting selected and our computer will make random choices off them
# you need to exactly know how this shit will start out and end
# learn how to append and extend lists properly
# parameters could be marquee players,players_that_xyz_likes
# make a function for every bidder
# make a function to display every player
# top bids of owners get 8/10 chances of bidding higher up for them
# medium bids get 5/10
# sluggish bids get 3/10
# before playing use this list to have an idea to get an idea of whos in whose set
# https://documents.iplt20.com/documents/IPL/document/2022/02/IPL2022PlayerAuction_List_Sets.pdf
import random as rd
#                                                                    dataBase
marquee = ["R Ashwin", "Trent Boult", "Pat Cummins", "Quinton De Kock", "Shikhar Dhawan", "Faf Du Plessis", "Shreyas Iyer", "Kagiso Rabada", "Mohammad Shami", "David Warner"]
marquee_nationalities = ["🛺", "✈️", "✈️", "✈️", "🛺", "✈️", "🛺", "✈️", "🛺", "✈️"]
marquee_roles = ["Bowler", "Bowler", "Bowler", "Wicketkeeper", "Batter", "Batter", "Batter", "Bowler", "Bowler", "Batter"]
ba1 = ["Shimron Hetmyer", "David Miller", "Devdutt Padikkal", "Manish Pandey", "Suresh Raina", "Jason Roy", "Steve Smith", "Robin Uthappa"]
ba1_nationalities = ["✈️", "✈️", "🛺", "🛺", "🛺", "✈️", "✈️", "🛺"]
ba1_roles = ["Batter", "Batter", "Batter", "Batter", "Batter", "Batter", "Batter", "Batter"]
al1 = ["Shakib Al Hasan", "Dwayne Bravo", "Wanindu Hasaranga", "Jason Holder", "Mitchell Marsh", "Mohammad Nabi", "Krunal Pandya", "Harshal Patel", "Nitish Rana", "Washington Sundar"]
al_nationalities = ["✈️", "✈️", "✈️", "✈️", "✈️", "✈️", "✈️", "✈️", "🛺", "🛺"]
al_roles = ["All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder"]
wks1 = ["Jonny Bairstow","Sam Billings","Dinesh Karthik","Ishan Kishan","Nicholas Pooran","Ambati Rayudu","Wriddhiman Saha","Matthew Wade"]
wks1_nationalities = ["✈️", "✈️", "🛺", "🛺", "✈️", "🛺", "🛺", "✈️"]
wks1_roles = ["Wicketkeeper","Wicketkeeper","Wicketkeeper","Wicketkeeper","Wicketkeeper","Wicketkeeper","Wicketkeeper","Wicketkeeper"]
seamers1 = ["Deepak Chahar", "Lockie Ferguson", "Josh Hazlewood", "Prasidh Krishna", "Bhuvneshwar Kumar", "T. Natarajan", "Mustafizur Rahman", "Shardul Thakur", "Mark Wood", "Umesh Yadav"]
seamers1_nationalities = ["🛺", "✈️", "✈️", "🛺", "🛺", "🛺", "✈️", "🛺", "✈️", "🛺"]
seamers1_roles = ["Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler"]
spinners1 = ["Yuzvendra Chahal", "Rahul Chahar", "Amit Mishra", "Adil Rashid", "Imran Tahir", "Kuldeep Yadav", "Mujeeb Zadran", "Adam Zampa"]
spinners1_nationalities = ["🛺", "🛺", "🛺", "✈️", "✈️", "🛺", "✈️", "✈️"]
spinners1_roles = ["Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler"]
ba2 = ["Aaron Finch","Marnus Labuschagne","Dawid Malan","Aiden Markram","Eoin Morgan","Cheteshwar Pujara","Ajinkya Rahane","Mandeep Singh","Saurabh Tiwary"]
ba1_nationalities = ["✈️", "✈️", "✈️", "✈️", "✈️", "🛺", "🛺", "🛺","🛺"]
ba1_roles = ["Batter","Batter","Batter","Batter","Batter","Batter","Batter","Batter","Batter"]
al2 = ["Dominic Drakes","Shivam Dube","K Gowtham","Marco Jansen","Chris Jordan","Liam Livingstone","James Neesham","Vijay Shankar","Odean Smith","Jayant Yadav"]
al2_nationalities = ["✈️", "🛺", "🛺", "✈️", "✈️", "✈️", "✈️" "🛺", "✈️","🛺"]
al2_roles = ["All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder"]
wks2 = ["Liton Das","Niroshan Dickwella","Andre Fletcher","Rahmanullah Gurbaz","Shai Hope","Heinrich Klaasen","Ben Mcdermott","Kusal Mendis","Kusal Perera","Joshua Phillipe","Glenn Phillips","Tim Seifert"]
wks2_nationalities = ["✈️", "✈️", "✈️", "✈️", "✈️", "✈️", "✈️", "✈️", "✈️", "✈️", "✈️", "✈️"]
wk2_roles =["Wicketkeeper","Wicketkeeper","Wicketkeeper","Wicketkeeper","Wicketkeeper","Wicketkeeper","Wicketkeeper","Wicketkeeper","Wicketkeeper","Wicketkeeper","Wicketkeeper","Wicketkeeper"]
seamers2 = ["Khaleel Ahmed","Dushmanta Chameera","Sheldon Cottrell","Nathan Coulter-Nile","Lungi Ngidi","Navdeep Saini","Chetan Sakariya","Ishant Sharma","Sandeep Sharma","Jaydev Unadkat"]
seamers2_nationalities = ["🛺", "✈️", "✈️", "✈️", "✈️", "🛺", "🛺", "🛺", "🛺", "🛺"]
seamers2_roles = ["Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler"]
spinners2 = ["Qais Ahmad","Piyush Chawla","Mayank Markande","Shahbaz Nadeem","Tabraiz Shamsi","Karn Sharma","Ish Sodhi","Maheesh Theeksana","Noor Ahmad"]
spinners2_nationalities = ["✈️","🛺","🛺","🛺","✈️","🛺","✈️","✈️","✈️"]
spinners2_roles = ["Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler"]
ba3 = ["Finn Allen","Devon Convay","Alex Hales","Evin Lewis","Chris Lynn","Karun Nair","Rovman Powell","Rassie Van Der Dussen","Najibullah Zadran"]
ba3_nationalities = ["✈️","✈️","✈️","✈️","✈️","🛺","✈️","✈️"]
ba3_roles = ["Wicketkeeper","Wicketkeeper","Batter","Batter","Batter","Batter","All Rounder","Batter","Batter",]
al3 = ["Jofra Archer","Charith Asalanka","Rishi Dhawan","George Garton","Daryl Mitchell","Dwaine Pretorius","Sherfane Rutherford","Daniel Sams","Mitchell Santner","Romario Shepherd"]
al3_nationalities = ["✈️", "✈️", "🛺", "✈️", "✈️", "✈️", "✈️", "✈️", "✈️", "✈️"]
al3_roles = ["All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder"]
seamers3 = ["Jason Behrendorff","Nathan Ellis","Fazalhaq Farooqi","Siddarth Kaul","Obed Mccoy","Tymal Mills","Adam Milne","Reece Topley","Andrew Tye","Sandeep Warrier"]
seamers3_nationalities = ["✈️", "✈️", "✈️", "🛺", "✈️", "✈️", "✈️", "✈️", "✈️", "🛺"]   
seamers3_roles = ["Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler"]
spinners3 = ["Todd Astle","Akila Dhananjaya","Zahir Khan","Keshav Maharaj","Waqar Salamkheil","Rahul Sharma","Hayden Walsh"]
spinners3_nationalities = ["✈️", "✈️", "✈️", "✈️", "✈️", "🛺", "✈️"]
spinners3_roles = ["Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler"]
ba4 = ["Martin Guptill","Usman Khawaja","Brandon King","Janneman Malan","Bhanuka Rajapaksa","Rilee Russouw","Paul Stirling","Hanuma Vihari","James Vince","Hazratullah Zazai"]
ba4_nationalities = ["✈️", "✈️", "✈️", "✈️", "✈️", "✈️", "✈️", "🛺", "✈️", "✈️"]
ba4_roles = ["Batter","Batter","Batter","Batter","Wicketkeeper","Wicketkeeper","Batter","Batter","Batter","Batter"]
al4 = ["Fabien Allen","Roston Chase","Ben Cutting","Lewis Gregory","Moises Henriques","Akeal Hosein","Karim Janat","Scott Kuggeleijn","Pawan Negi","Gurkeerat Singh"]
al4_nationalities = ["✈️", "✈️", "✈️", "✈️", "✈️", "✈️", "✈️", "✈️", "🛺", "🛺"]
al4_roles = ["All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder"]
seamers4 = ["Sean Abbott","Taskin Ahmed","Merchant De Lange","Alzarri Joseph","Dhawal Kulkarni","Saqib Mahmood","Riley Meredith","Kane Richardson","Tim Southee","Naveen Ul Haq"]
seamers4_nationalities = ["✈️", "✈️", "✈️", "✈️", "🛺", "✈️", "✈️", "✈️", "✈️", "✈️"]
seamers4_roles = ["Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler"]
al5 = ["Ashton Agar", "Carlos Brathwaite", "Kedar Jadhav", "Chamika Karunaratne", "Colin Munro", "Gulbadin Naib", "Keemo Paul", "Parvez Rasool", "Dasun Shanaka", "David Willey"]
al5_nationalities = ["✈️", "✈️", "🛺", "✈️", "✈️", "✈️", "✈️", "🛺", "✈️", "✈️"]
al5_roles = ["All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder"]
al6 = ["Curtis Campher", "Colin De Grandhomme", "James Faulkner", "Craig Overton", "Wayne Parnell", "Samit Patel", "Thisara Perera", "Darcy Short", "Murali Vijay"]
al6_nationalities = ["✈️", "✈️", "✈️", "✈️", "✈️", "✈️", "✈️", "✈️", "🛺"]
al6_roles = ["All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","All Rounder","Batter"]
uncapped_prospects = ["Dewald Brevis","Priyam Garg","Rajat Patidar","Anmolpreet Singh","Rahul Tripathi","Shahbaz Ahamad","Harpreet Brar","Deepak Hooda","Sarfaraz Khan","Shahrukh Khan","Shivam Mavi","Kamlesh Nagarkoti","Riyan Parag","Abhishek Sharma","Rahul Tewatia","KS Bharat","Anuj Rawat","Jitesh Sharma","Prabhsimran Singh","Vishnu Vinod","Akash Deep","Tushar Deshpande","Avesh Khan","Ishan Porel","Ankit Rajpoot","Basil Thampi","Kartik Tyagi","M Ashwin","Shreyas Gopal","Rinku SIngh","Gerald Coetzee","Sai Kishore"]
uncapped_prospects_nationalities = ["✈️", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺", "🛺","✈️" ,"🛺"]
uncapped_prospects_roles = ["Batter","Batter","Batter","Batter","Batter","All Rounder","All Rounder","All Rounder","Batter","Batter","Bowler","Bowler","All Rounder","All Rounder","All Rounder","Wicketkeeper","Wicketkeeper","Wicketkeeper","Wicketkeeper","Wicketkeeper","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Bowler","Batter","Bowler","All Rounder"]

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
csk_ai_mid = [""] #7/10 based off how bad they want these players
csk_ai_meh = [""] #7/10 based off how bad they want these players
csk_ai_f_around = ["no","no","no","no","no","no","no","no","no","bid"] #7/10 based off how bad they want these players
dc_ai_top = [""] #7/10 based off how bad they want these players
dc_ai_mid = [""] #7/10 based off how bad they want these players
dc_ai_meh = [""] #7/10 based off how bad they want these players
dc_ai_f_around = ["no","no","no","no","no","no","no","no","bid","bid"] #7/10 based off how bad they want these players
gt_ai_top = [""] #7/10 based off how bad they want these players
gt_ai_mid = [""] #7/10 based off how bad they want these players
gt_ai_meh = [""] #7/10 based off how bad they want these players
gt_ai_f_around = ["no","no","no","no","no","no","no","no","no","bid"] #7/10 based off how bad they want these players 
kkr_ai_top = [""] #7/10 based off how bad they want these players
kkr_ai_mid = [""] #7/10 based off how bad they want these players
kkr_ai_meh = [""] #7/10 based off how bad they want these players
kkr_ai_f_around = ["no","no","no","no","no","no","no","no","no","bid"] #7/10 based off how bad they want these players
lsg_ai_top = [""] #7/10 based off how bad they want these players
lsg_ai_mid = [""] #7/10 based off how bad they want these players
lsg_ai_meh = [""] #7/10 based off how bad they want these players
lsg_ai_f_around = ["no","no","no","no","no","no","no","no","no","bid"] #7/10 based off how bad they want these players
mi_ai_top = [""] #7/10 based off how bad they want these players
mi_ai_mid = [""] #7/10 based off how bad they want these players
mi_ai_meh = [""] #7/10 based off how bad they want these players
mi_ai_f_around = ["no","no","no","no","no","no","no","no","no","bid"] #7/10 based off how bad they want these players
pbks_ai_top = [""] #7/10 based off how bad they want these players
pbks_ai_mid = [""] #7/10 based off how bad they want these players
pbks_ai_meh = [""] #7/10 based off how bad they want these players
pbks_ai_f_around = ["no","no","no","no","no","no","no","no","no","bid"] #7/10 based off how bad they want these players
rr_ai_top = [""] #7/10 based off how bad they want these players
rr_ai_mid = [""] #7/10 based off how bad they want these players
rr_ai_meh = [""] #7/10 based off how bad they want these players
rr_ai_f_around = ["no","no","no","no","no","no","no","no","no","bid"] #7/10 based off how bad they want these players
rcb_ai_top = [""] #7/10 based off how bad they want these players
rcb_ai_mid = [""] #7/10 based off how bad they want these players
rcb_ai_meh = [""] #7/10 based off how bad they want these players
rcb_ai_f_around = ["no","no","no","no","no","no","no","no","no","bid"] #7/10 based off how bad they want these players
srh_ai_top = [""] #7/10 based off how bad they want these players
srh_ai_mid = [""] #7/10 based off how bad they want these players
srh_ai_meh = [""] #7/10 based off how bad they want these players
srh_ai_f_around = ["no","no","no","no","no","no","no","no","no","bid"] #7/10 based off how bad they want these players

# function of displaying player and his price
# function of few lines of code suiting each owner's auction habits
# function to check what role does the player play and increment it in the squad

#                                                                         simulator
#instructions :
# press enter to bid .5 cr/move to the next round, type "over" to end your bid
team = (input("Which Team would you like to represent? CSK/DC/GT/KKR/LSG/MI/PBKS/RR/RCB/SRH " )).lower()
if team == "csk":
    squad = ["Ravindra Jadeja","MS Dhoni","Moeen Ali","Ruturaj Gaikwad"]
    purse = 480000000
elif team == "dc":
    squad = ["Rishabh Pant","Axar Patel","Prithvi Shaw","Anrich Nortje"]
    purse = 475000000
elif team == "gt":
    squad = ["Shubman Gill","Hardik Pandya","Rashid Khan"]
    purse = 598000000
elif team == "kkr":
    squad = ["Andre Russell","Varun Chakravarthy","Venkatesh Iyer","Sunil Narine"]
    purse = 480000000
elif team == "lsg":
    squad = ["KL Rahul","Marcus Stoinis","Ravi Bishnoi"]
    purse = 598000000
elif team == "mi":
    squad = ["Rohit Sharma","Jasprit Bumrah","Suryakumar Yadav","Kieron Pollard"]
    purse = 480000000
elif team == "pbks":
    squad = ["Mayank Agarwal","Arshdeep Singh"]
    purse = 720000000
elif team == "rr":
    squad = ["Sanju Samson","Jos Buttler","Yashasvi Jaiswal"]
    purse = 620000000
elif team == "rcb":
    squad = ["Virat Kohli","Glenn Maxwell","Mohammed Siraj"]
    purse = 570000000
elif team == "srh":
    squad = ["Kane Williamson","Abdul Samad","Umran Malik"]
    purse = 680000000

print("These players have been retained by your franchise for this year. You need to build a competent squad with %d more players" % (15 - len(squad)))
print(squad)
print("You have %d INR left in the bank to purchase players from the auction against 9 other owners" % purse)

#                                                                  functions
def marquee_set_selection_display(random_marquee):
    """display random player from marquee set and remove"""
    print("%s %s \n %s \n" % (random_marquee,marquee_nationalities[marquee.index(random_marquee)],marquee_roles[marquee.index(random_marquee)]))
    print("Would you like to bid for this player starting at 2crores, 2 crores for %s please? " % random_marquee)

def marquee_set_selection(random_marquee):
    """adding bought player into your squad"""
    squad.append(random_marquee)
    purse - price      

        
def marquee_set_deletion(random_marquee):
        """deleting all data related to the player to keep our indexes working and while loop functioning"""
        marquee_nationalities.remove(marquee_nationalities[marquee.index(random_marquee)])
        marquee_roles.remove(marquee_roles[marquee.index(random_marquee)])
        marquee.remove(random_marquee)
    
def pbks_ai_response(random_marquee):
    """Study habits of pbks auction tactics and what players they bid for more often"""
    if random_marquee in top_bids_pbks:
        if rd.choice(pbks_ai_top) == "bid":
            price += 5000000
            print("PBKS! %d? " % (price+5000000))
            bid_history[6] += 1
    elif random_marquee in medium_bids_pbks:
        if rd.choice(pbks_ai_mid) == "bid":
            price += 5000000
            print("PBKS! %d? " % (price+5000000))
            bid_history[6] += 1
    elif random_marquee in meh_bids_pbks:
        if rd.choice(pbks_ai_meh) == "bid":
            price += 5000000
            print("PBKS! %d? " % (price+5000000))
            bid_history[6] += 1
    else:
        if rd.choice(pbks_ai_f_around) == "bid":
            price += 5000000
            print("PBKS! %d? " % (price+5000000))
            bid_history[6] += 1
def dc_ai_response(random_marquee):
    """Study habits of dc auction tactics and what players they bid for more often"""
    if random_marquee in top_bids_dc:
        if rd.choice(dc_ai_top) == "bid":
            price += 5000000
            print("DC! %d? " % (price+5000000))
            bid_history[1] += 1
    elif random_marquee in medium_bids_dc:
        if rd.choice(dc_ai_mid) == "bid":
            price += 5000000
            print("DC! %d? " % (price+5000000))
            bid_history[1] += 1
    elif random_marquee in meh_bids_dc:
        if rd.choice(dc_ai_meh) == "bid":
            price += 5000000
            print("DC! %d? " % (price+5000000))
            bid_history[1] += 1
    else:
        if rd.choice(dc_ai_f_around) == "bid":
            price += 5000000
            print("DC! %d? " % (price+5000000))
            bid_history[1] += 1      
def mi_ai_response(random_marquee):
    """Study habits of mi auction tactics and what players they bid for more often"""
    if random_marquee in top_bids_mi:
        if rd.choice(mi_ai_top) == "bid":
            price += 5000000
            print("MI! %d? " % (price+5000000))
            bid_history[5] += 1
    elif random_marquee in medium_bids_mi:
        if rd.choice(mi_ai_mid) == "bid":
            price += 5000000
            print("MI! %d? " % (price+5000000))
            bid_history[5] += 1 
    elif random_marquee in meh_bids_mi:
        if rd.choice(mi_ai_meh) == "bid":
            price += 5000000
            print("MI! %d? " % (price+5000000))
            bid_history[5] += 1
    else:
        if rd.choice(mi_ai_f_around) == "bid":
            price += 5000000
            print("MI! %d? " % (price+5000000))
            bid_history[5] += 1      
def gt_ai_response(random_marquee):
    """Study habits of gt auction tactics and what players they bid for more often"""
    if random_marquee in top_bids_gt:
        if rd.choice(gt_ai_top) == "bid":
            price += 5000000
            print("GT! %d? " % (price+5000000))
            bid_history[2] += 1   
    if random_marquee in medium_bids_gt:
        if rd.choice(gt_ai_mid) == "bid":
            price += 5000000
            print("GT! %d? " % (price+5000000))
            bid_history[2] += 1   
    if random_marquee in meh_bids_gt:
        if rd.choice(gt_ai_meh) == "bid":
            price += 5000000
            print("GT! %d? " % (price+5000000))
            bid_history[2] += 1   
    else:
        if rd.choice(gt_ai_f_around) == "bid":
            price += 5000000
            print("GT! %d? " % (price+5000000))
            bid_history[2] += 1   
def kkr_ai_response(random_marquee):
    """Study habits of kkr auction tactics and what players they bid for more often"""
    if random_marquee in top_bids_kkr:
        if rd.choice(kkr_ai_top) == "bid":
            price += 5000000
            print("KKR! %d? " % (price+5000000))
            bid_history[3] += 1   
    if random_marquee in medium_bids_kkr:
        if rd.choice(kkr_ai_mid) == "bid":
            price += 5000000
            print("KKR! %d? " % (price+5000000))
            bid_history[3] += 1   
    if random_marquee in meh_bids_kkr:
        if rd.choice(kkr_ai_meh) == "bid":
            price += 5000000
            print("KKR! %d? " % (price+5000000))
            bid_history[3] += 1   
    else:
        if rd.choice(kkr_ai_f_around) == "bid":
            price += 5000000
            print("KKR! %d? " % (price+5000000))
            bid_history[3] += 1       
def srh_ai_response(random_marquee):
    """Study habits of srh auction tactics and what players they bid for more often"""
    if random_marquee in top_bids_srh:
        if rd.choice(srh_ai_top) == "bid":
            price += 5000000
            print("SRH! %d? " % (price+5000000))
            bid_history[9] += 1          
    if random_marquee in medium_bids_srh:
        if rd.choice(csk_ai_mid) == "bid":
            price += 5000000
            print("SRH! %d? " % (price+5000000))
            bid_history[9] += 1        
    if random_marquee in meh_bids_srh:
        if rd.choice(srh_ai_meh) == "bid":
            price += 5000000
            print("SRH! %d? " % (price+5000000))
            bid_history[9] += 1    
    else:
        if rd.choice(srh_ai_f_around) == "bid":
            price += 5000000
            print("SRH! %d? " % (price+5000000))
            bid_history[9] += 1       
def rr_ai_response(random_marquee):
    """Study habits of rr auction tactics and what players they bid for more often"""
    if random_marquee in top_bids_rr:
        if rd.choice(rr_ai_top) == "bid":
            price += 5000000
            print("RR! %d? " % (price+5000000))
            bid_history[7] += 1  
    if random_marquee in medium_bids_rr:
        if rd.choice(rr_ai_mid) == "bid":
            price += 5000000
            print("RR! %d? " % (price+5000000))
            bid_history[7] += 1  
    if random_marquee in meh_bids_rr:
        if rd.choice(rr_ai_meh) == "bid":
            price += 5000000
            print("RR! %d? " % (price+5000000))
            bid_history[7] += 1  
    else:
        if rd.choice(rr_ai_f_around) == "bid":
            price += 5000000
            print("RR! %d? " % (price+5000000))
            bid_history[7] += 1  
def lsg_ai_response(random_marquee):
    """Study habits of lsg auction tactics and what players they bid for more often"""
    if random_marquee in top_bids_lsg:
        if rd.choice(lsg_ai_top) == "bid":
            price += 5000000
            print("LSG! %d? " % (price+5000000))
            bid_history[4] += 1  
    if random_marquee in medium_bids_lsg:
        if rd.choice(lsg_ai_mid) == "bid":
            price += 5000000
            print("LSG! %d? " % (price+5000000))
            bid_history[4] += 1
    if random_marquee in meh_bids_lsg:
        if rd.choice(lsg_ai_meh) == "bid":
            price += 5000000
            print("LSG! %d? " % (price+5000000))
            bid_history[4] += 1
    else:
        if rd.choice(lsg_ai_f_around) == "bid":
            price += 5000000
            print("LSG! %d? " % (price+5000000))
            bid_history[4] += 1
def rcb_ai_response(random_marquee):
    """Study habits of rcb auction tactics and what players they bid for more often"""
    if random_marquee in top_bids_rcb:
        if rd.choice(rcb_ai_top) == "bid":
            price += 5000000
            print("RCB! %d? " % (price+5000000))
            bid_history[8] += 1
    if random_marquee in medium_bids_rcb:
        if rd.choice(rcb_ai_mid) == "bid":
            price += 5000000
            print("RCB! %d? " % (price+5000000))
            bid_history[8] += 1
    if random_marquee in meh_bids_rcb:
        if rd.choice(rcb_ai_meh) == "bid":
            price += 5000000
            print("RCB! %d? " % (price+5000000))
            bid_history[8] += 1
    else:
        if rd.choice(rcb_ai_f_around) == "bid":
            price += 5000000
            print("RCB! %d? " % (price+5000000))
            bid_history[8] += 1
def csk_ai_response(random_marquee):
    """Study habits of csk auction tactics and what players they bid for more often"""
    if random_marquee in top_bids_csk:
        if rd.choice(csk_ai_top) == "bid":
            price += 5000000
            print("CSK! %d? " % (price+5000000))
            bid_history[0] += 1
    if random_marquee in medium_bids_csk:
        if rd.choice(csk_ai_mid) == "bid":
            price += 5000000
            print("CSK! %d? " % (price+5000000))
            bid_history[0] += 1
    if random_marquee in meh_bids_csk:
        if rd.choice(csk_ai_meh) == "bid":
            price += 5000000
            print("CSK! %d? " % (price+5000000))
            bid_history[0] += 1
    else:
        if rd.choice(csk_ai_f_around) == "bid":
            price += 5000000
            print("CSK! %d? " % (price+5000000))
            bid_history[0] += 1

def sequence_of_functions():
    """this is to remove the team you picked and only get responses from the teams you havent picked"""
    if team.lower() == "rcb":
        csk_ai_response(random_marquee)
        dc_ai_response(random_marquee)
        gt_ai_response(random_marquee)
        kkr_ai_response(random_marquee)
        lsg_ai_response(random_marquee)
        mi_ai_response(random_marquee)
        pbks_ai_response(random_marquee)
        rr_ai_response(random_marquee)
        srh_ai_response(random_marquee)
    elif team.lower() == "dc":
        csk_ai_response(random_marquee)
        gt_ai_response(random_marquee)
        kkr_ai_response(random_marquee)
        lsg_ai_response(random_marquee)
        mi_ai_response(random_marquee)
        pbks_ai_response(random_marquee)
        rr_ai_response(random_marquee)
        rcb_ai_response(random_marquee)
        srh_ai_response(random_marquee)
    elif team.lower() == "rr":
        csk_ai_response(random_marquee)
        dc_ai_response(random_marquee)
        gt_ai_response(random_marquee)
        kkr_ai_response(random_marquee)
        lsg_ai_response(random_marquee)
        mi_ai_response(random_marquee)
        pbks_ai_response(random_marquee)
        rcb_ai_response(random_marquee)
        srh_ai_response(random_marquee)
    elif team.lower() == "csk":
        dc_ai_response(random_marquee)
        gt_ai_response(random_marquee)
        kkr_ai_response(random_marquee)
        lsg_ai_response(random_marquee)
        mi_ai_response(random_marquee)
        pbks_ai_response(random_marquee)
        rr_ai_response(random_marquee)
        rcb_ai_response(random_marquee)
        srh_ai_response(random_marquee)
    elif team.lower() == "gt":
        csk_ai_response(random_marquee)
        dc_ai_response(random_marquee)
        kkr_ai_response(random_marquee)
        lsg_ai_response(random_marquee)
        mi_ai_response(random_marquee)
        pbks_ai_response(random_marquee)
        rr_ai_response(random_marquee)
        rcb_ai_response(random_marquee)
        srh_ai_response(random_marquee)
    elif team.lower() == "lsg":
        csk_ai_response(random_marquee)
        dc_ai_response(random_marquee)
        gt_ai_response(random_marquee)
        kkr_ai_response(random_marquee)
        mi_ai_response(random_marquee)
        pbks_ai_response(random_marquee)
        rr_ai_response(random_marquee)
        rcb_ai_response(random_marquee)
        srh_ai_response(random_marquee)
    elif team.lower() == "pbks":
        csk_ai_response(random_marquee)
        dc_ai_response(random_marquee)
        gt_ai_response(random_marquee)
        kkr_ai_response(random_marquee)
        lsg_ai_response(random_marquee)
        mi_ai_response(random_marquee)
        rr_ai_response(random_marquee)
        rcb_ai_response(random_marquee)
        srh_ai_response(random_marquee)
    elif team.lower() == "srh":
        csk_ai_response(random_marquee)
        dc_ai_response(random_marquee)
        gt_ai_response(random_marquee)
        kkr_ai_response(random_marquee)
        lsg_ai_response(random_marquee)
        mi_ai_response(random_marquee)
        pbks_ai_response(random_marquee)
        rr_ai_response(random_marquee)
        rcb_ai_response(random_marquee)
    elif team.lower() == "mi":
        csk_ai_response(random_marquee)
        dc_ai_response(random_marquee)
        gt_ai_response(random_marquee)
        kkr_ai_response(random_marquee)
        lsg_ai_response(random_marquee)
        pbks_ai_response(random_marquee)
        rr_ai_response(random_marquee)
        rcb_ai_response(random_marquee)
        srh_ai_response(random_marquee)
    elif team.lower() == "kkr":
        csk_ai_response(random_marquee)
        dc_ai_response(random_marquee)
        gt_ai_response(random_marquee)
        lsg_ai_response(random_marquee)
        mi_ai_response(random_marquee)
        pbks_ai_response(random_marquee)
        rr_ai_response(random_marquee)
        rcb_ai_response(random_marquee)
        srh_ai_response(random_marquee)

def bidding(bid_history,list2,list3):
    result = [x - y for x, y in zip(bid_history, list2)]
    while result != [0,0,0,0,0,0,0,0,0,0]:
        list3 = bid_history
        sequence_of_functions()
        list2 = list3
        bid_again = input("Press Enter to bid another 5000000 to %d" % price)
        if bid_again == "":
            price += 5000000
            continue
        else:
            print("This player is sold to the opposing team for %d! Here comes the next bid! " % price)
            marquee_set_deletion(random_marquee)
            sold = False
    if sold == True:
        print("%s is sold to %s(you) for %d! " % (random_marquee,team,price))
        marquee_set_selection(random_marquee)
        marquee_set_deletion(random_marquee)
    elif sold == False:
        print("This player is sold to the opposing team for %d! Here comes the next bid! " % price)
        marquee_set_deletion(random_marquee)
        
#                                                            the actual simulator
for i in range (len(marquee)+1):
    price = 20000000
    random_marquee = rd.choice(marquee)
    csk_bid = 0
    dc_bid = 0
    gt_bid = 0
    kkr_bid = 0
    lsg_bid = 0
    mi_bid = 0
    pbks_bid = 0
    rr_bid = 0
    rcb_bid = 0
    srh_bid = 0
    bid_history = [csk_bid,dc_bid,gt_bid,kkr_bid,lsg_bid,mi_bid,pbks_bid,rr_bid,rcb_bid,srh_bid]
    marquee_set_selection_display(random_marquee)
    decision = input("Bid? (Press Enter to bid .5cr or back out by typing no) ")
    sold = False
    if decision == "":
        price += 5000000
        while sold != True:
            sequence_of_functions()
            if bid_history == [0,0,0,0,0,0,0,0,0,0]:
                print("%s is sold to %s(you)! " % (random_marquee,team))
                marquee_set_selection(random_marquee)
                marquee_set_deletion(random_marquee)
                sold = True
            elif bid_history != [0,0,0,0,0,0,0,0,0,0]:
                list2 = [0,0,0,0,0,0,0,0,0,0]
                list3 = []
                bidding(bid_history,list2,list3)
                continue
    else:
        print("%s is unsold for tonight! " % random_marquee)
        marquee_set_deletion(random_marquee)
print(squad)



