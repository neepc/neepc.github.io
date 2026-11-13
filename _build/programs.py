# Program data for past NEEPC conferences, transcribed from the printed schedules.
# Run `python3 _build/build_past.py` after editing to regenerate past.html and the year pages.
#
# Each year has a timeline (list of (time, label, session_id or None)) and sessions.
# A session has rooms; a room has a host, an optional topic, and talks as
# (name, affiliation, title) where title may be "" when the program did not list one.

PROGRAMS = {
    2025: {
        "date": "May 2, 2025",
        "venue": "Friedman Hall, Brown University",
        "photo": None,
        "formats": [
            "Presentations: 20 minutes, followed by 5 minutes of questions.",
            "Pitch-an-idea sessions: 5 minutes per pitch, no questions. Discussion follows in the next break.",
        ],
        "timeline": [
            ("9:30–10:10am", "Check-in and coffee", None),
            ("10:10–11:00am", "Presentation Session 1", "p1"),
            ("11:00–11:10am", "Coffee break", None),
            ("11:10am–12:00pm", "Presentation Session 2", "p2"),
            ("12:00–1:00pm", "Lunch", None),
            ("1:00–1:45pm", "Pitch Session 1", "pitch1"),
            ("1:45–2:15pm", "Discussion and coffee", None),
            ("2:15–3:30pm", "Presentation Session 3", "p3"),
            ("3:30–4:00pm", "Break", None),
            ("4:00–4:50pm", "Presentation Session 4", "p4"),
            ("5:00–5:30pm", "Pitch Session 2", "pitch2"),
            ("5:30–6:00pm", "Discussion and drinks, Robinson Hall", None),
        ],
        "sessions": [
            {"id": "p1", "kind": "Presentation", "name": "Presentation Session 1", "time": "10:10–11:00am", "rooms": [
                {"room": "Room 101", "host": "Israel Eruchimovitch", "talks": [
                    ("Israel Eruchimovitch", "Brown", "Breaking Barriers, Building (on) Networks: Lessons from the Jewish Emancipation in Germany"),
                    ("John Fallon", "Boston University", "Fewer Licenses, Similar Teachers: Changing Licensing Tests in Indiana"),
                ]},
                {"room": "Room 102", "host": "Nicolaj Thor", "talks": [
                    ("Simon Essig Aberg", "Harvard", "Tax Elasticities of Top Donors: Evidence from Family Foundations"),
                    ("Corinne Stephens", "Boston University", "Macroeconomic Consequences of Gender Differences in Job Search"),
                ]},
                {"room": "Room 202", "host": "Anya Marchenko", "talks": [
                    ("Anya Marchenko", "Brown", "Excrement as Externality: Hedonic Price of Factory Farms"),
                    ("Mustafa Runyon", "Boston College", "The Effect of Assisted Reproductive Technology Policies on Assortative Mating and Mating Characteristics"),
                ]},
            ]},
            {"id": "p2", "kind": "Presentation", "name": "Presentation Session 2", "time": "11:10am–12:00pm", "rooms": [
                {"room": "Room 101", "host": "Matthew Schaelling", "talks": [
                    ("Jo Ellery", "Harvard", "Audits and Fraud Insurance: Optimizing Borrower Defense to Repayment"),
                    ("Matthew Schaelling", "Brown", "What are the welfare effects of single-family zoning? Evidence from Oregon"),
                ]},
                {"room": "Room 102", "host": "Jiayue Zhang", "talks": [
                    ("William Chen", "MIT", "Disagreement in Production Networks"),
                    ("Yang Liu", "Boston College", "Financial Constraints and Price Rigidities"),
                ]},
                {"room": "Room 202", "host": "Emily Emick", "talks": [
                    ("Jack Hirsch", "Harvard", "Cued to Queue: Information in Waiting-Line Auctions"),
                    ("Yufeng Shi", "Boston College", "Endogenous Social Minimum"),
                ]},
            ]},
            {"id": "pitch1", "kind": "Pitch", "name": "Pitch Session 1", "time": "1:00–1:45pm", "rooms": [
                {"room": "Room 108", "topic": "Applied Microeconomics", "host": "Ben Delgado", "talks": [
                    ("Shreya Dutt", "Boston University", ""),
                    ("Ben Delgado", "Brown", ""),
                    ("Whitney Zhang", "MIT", ""),
                    ("Cameron Deal", "Harvard", ""),
                    ("Srishti Sharma", "Boston University", ""),
                    ("Xinmei Yang", "Harvard", ""),
                    ("Sai Pitre", "Brown", ""),
                    ("Clare Sachsse", "Tufts", ""),
                ]},
                {"room": "Room 202", "topic": "Macroeconomics and Finance", "host": "Olivia Lattus", "talks": [
                    ("Davide Taglialatella", "Harvard", ""),
                    ("Olivia Lattus", "Brown", ""),
                    ("Jiayin Liu", "Boston University", ""),
                    ("Julia Chahine", "Brown", ""),
                    ("Eduardo Bella", "Boston University", ""),
                    ("Sharad Hotha", "Brown", ""),
                    ("Max Guo", "Harvard", ""),
                    ("Marco Olivari", "Boston University", ""),
                ]},
                {"room": "Room 208", "topic": "Econometrics, Behavioral, and Microeconomic Theory", "host": "Juan Yamin Silva", "talks": [
                    ("Bahadir Ulgey", "Boston College", ""),
                    ("Juan Yamin Silva", "Brown", ""),
                    ("Ophir Averbuch", "Harvard", ""),
                    ("Xinyu Dai", "Brown", ""),
                    ("Cassidy Shubatt", "Harvard", ""),
                    ("Eu-Wayne Mok", "Harvard", ""),
                ]},
            ]},
            {"id": "p3", "kind": "Presentation", "name": "Presentation Session 3", "time": "2:15–3:30pm", "rooms": [
                {"room": "Room 108", "host": "Julia Chahine", "talks": [
                    ("Laura Nicolae", "Harvard", "The Effect of Inflation Indexation On Employment: Evidence From Belgium"),
                    ("Alvaro Contreras", "Boston University", "Spatial Banking Competition in the US Deposits Market"),
                    ("Yu Sugisaki", "Boston College", "Population Aging, Retirement, and the Effectiveness of Monetary Policy on Inflation"),
                ]},
                {"room": "Room 202", "host": "Sai Pitre", "talks": [
                    ("Juan Cruz Lopez Del Valle", "Boston University", "Heterogeneous Agents in Developed and Developing Countries"),
                    ("Yu-Jia Wang", "Harvard", "What Do Protesters Know?"),
                    ("Sarah Moon", "MIT", "Optimal Policy Choices Under Uncertainty"),
                ]},
                {"room": "Room 208", "host": "Moritz Poll", "talks": [
                    ("Moritz Poll", "Brown", "Micro-enterprise saturation: Critical mass or overcrowding?"),
                    ("Julia Gilman", "MIT", "Who Benefits from Proximity to Opportunity? Universities, Prestigious Firms, and Student Labor Market Outcomes"),
                    ("Lorena Moreno", "Tufts", "Unsafe Waters: The Hidden Health Costs of Seasonal Drinking Water Contamination in Ecuador"),
                ]},
            ]},
            {"id": "p4", "kind": "Presentation", "name": "Presentation Session 4", "time": "4:00–4:50pm", "rooms": [
                {"room": "Room 108", "host": "Maria Medellin Esguerra", "talks": [
                    ("Shengqi Ni", "Boston University", "Career Incentives and GDP Falsification"),
                    ("Maria Medellin Esguerra", "Brown", "Radio for Progress: Lessons from a Large-Scale Media Education Program in Colombia"),
                ]},
                {"room": "Room 202", "host": "Ruchi Mahadeshwar", "talks": [
                    ("Sanjay Moorjani", "Boston College", "Dissecting Business Cycles"),
                    ("Avi Lipton", "Harvard", "The Inflationary Effects of Large Fiscal Stimulus"),
                ]},
                {"room": "Room 208", "host": "Adrien Foutelet", "talks": [
                    ("Jennifer Walsh", "Harvard", "How do nonprofits use cash windfalls? Evidence from $5B in unrestricted donations"),
                    ("Louis Becker", "MIT", "Spilt Milk: Spillover Effects of Rural-Urban Trade"),
                ]},
            ]},
            {"id": "pitch2", "kind": "Pitch", "name": "Pitch Session 2", "time": "5:00–5:30pm", "rooms": [
                {"room": "Room 108", "topic": "Applied Microeconomics II", "host": "Jiayi Liu", "talks": [
                    ("Sidharth Satya", "Brown", ""),
                    ("Asad Tariq", "Visiting Student, Brown", ""),
                    ("Alberto Cappello", "Boston College", ""),
                    ("Jiayi Liu", "Brown", ""),
                ]},
                {"room": "Room 202", "topic": "Trade and Development", "host": "Bo-Yeon Jang", "talks": [
                    ("Andrew Ghattass", "Tufts", ""),
                    ("Marta Bilghese", "MIT", ""),
                    ("Juan Ignacio Jacoubian", "Boston University", ""),
                    ("Maria Mittelbach", "Boston University", ""),
                    ("Shotaru Beppu", "Harvard", ""),
                ]},
                {"room": "Room 208", "topic": "Applied Microeconomics III", "host": "Camilla Adams", "talks": [
                    ("Everett Stamm", "Boston University", ""),
                    ("Camilla Adams", "Brown", ""),
                    ("Erik Engberg", "MIT", ""),
                ]},
            ]},
        ],
    },

    2026: {
        "date": "May 2, 2026",
        "venue": "Friedman Hall, Brown University",
        "photo": "assets/img/hero-2026.jpg",
        "formats": [
            "Presentations: 30 minutes. Questions welcome after the introduction or after 5 minutes, whichever comes first.",
            "Pitches: 7 minutes, no questions during the pitch. Discussion follows in the next break.",
        ],
        "timeline": [
            ("9:00–10:00am", "Check-in and breakfast", None),
            ("10:00–11:30am", "Presentation Session 1", "p1"),
            ("11:30–11:45am", "Coffee break", None),
            ("11:45am–12:30pm", "Pitch Session 1", "pitch1"),
            ("12:30–1:30pm", "Lunch", None),
            ("1:30–2:30pm", "Presentation Session 2", "p2"),
            ("2:45–3:30pm", "Pitch Session 2", "pitch2"),
            ("3:30–3:45pm", "Coffee break", None),
            ("3:45–5:15pm", "Presentation Session 3", "p3"),
            ("5:30pm", "Happy hour, Track 15", None),
        ],
        "sessions": [
            {"id": "p1", "kind": "Presentation", "name": "Presentation Session 1", "time": "10:00–11:30am", "rooms": [
                {"room": "Room 102", "host": "Emily Emick", "talks": [
                    ("Jessica Mancuso", "Harvard", "When Free Healthcare Meets Gender Norms: The Impact of Public Healthcare on Sex Selection"),
                    ("Yufeng Shi", "Boston College", "One Child Policy and Marriage Market Outcomes"),
                    ("John Fallon", "Boston University", "Competitive Occupational Licensure: Doctors Versus Chiropractors"),
                ]},
                {"room": "Room 108", "host": "Rachel Cummings", "talks": [
                    ("Sai Pitre", "Brown", "The Incidence of Consumption Tax Cuts Under Political Pressure: Evidence from Amazon India"),
                    ("María Medellín Esguerra", "Brown", "Bowling Alone or Together? Discourse after mass shootings"),
                    ("Shengqi Ni", "Boston University", "Revealing the Good, Concealing the Bad: Reporting Bias in Chinese Statistical Bulletins"),
                ]},
                {"room": "Room 202", "host": "Andres Mena", "talks": [
                    ("Shengbin Wei", "Boston College", "Identification and Inference for Treatment Effects with Spillovers in Panel Data"),
                    ("Andreas Petrou-Zeniou", "MIT", "Uncertainty in Compound Decision-Making with Applications to Ranking and Selection"),
                    ("Arlindo Skënderaj", "Brown", "Selling Supplemental Information"),
                ]},
                {"room": "Room 208", "host": "Julia Chahine", "talks": [
                    ("Marta Bilghese", "MIT", "State-Dependent Bank Runs"),
                    ("Zixing Guo", "Boston University", "The Macro Impact of the Debt-Inflation Channel on Investment"),
                    ("Marco Olivari", "Boston University", "Firm Planning Horizon and Monetary Policy Transmission"),
                ]},
            ]},
            {"id": "pitch1", "kind": "Pitch", "name": "Pitch Session 1", "time": "11:45am–12:30pm", "rooms": [
                {"room": "Room 102", "host": "Anna Vinovets", "talks": [
                    ("Everett Stamm", "Boston University", "Coasean Upzonings"),
                    ("Nadia Fitriani", "Boston University", "From Extraction to Power: Trade Policy in Critical Mineral Markets"),
                    ("Vaibhav Ojha", "Boston College", "What Explains Remote-Work Wage Premium?"),
                    ("Matteo Masullo", "Boston College", "Frictions in the Sharing Economy? Evidence from NYC Citi Bike"),
                ]},
                {"room": "Room 202", "host": "Arlindo Skënderaj", "talks": [
                    ("Anirudh Pisharam", "Boston College", "Yellow to Green: Dynamic Competition, Learning, and Firm Survival in the Electric School Bus Transition"),
                    ("Yuxian Chen", "Brown", "Childcare Subsidies and Fertility: Cost-Effective Policy under Heterogeneous Preferences"),
                    ("Cameron Deal", "Harvard", "Treatment Effect Risk with Synthetic Controls"),
                    ("Vaishnavi Agarwal", "Tufts", "Losing an Edge: How Producers Adapt to Comparative Advantage Shocks"),
                ]},
            ]},
            {"id": "p2", "kind": "Presentation", "name": "Presentation Session 2", "time": "1:30–2:30pm", "rooms": [
                {"room": "Room 102", "host": "Emily Emick", "talks": [
                    ("Jiayi Liu", "Brown", "Access to Justice, Trust, and Medical Dispute Mediation in China"),
                    ("Rachel Cummings", "Brown", "The Impact of Dobbs v. Jackson Women’s Health Organization on Births"),
                ]},
                {"room": "Room 108", "host": "Jin Niu", "talks": [
                    ("Scott Lu", "Brown", "Driving Out Supply: The Impact of Removing Minimum Parking Requirements on Housing"),
                    ("Ruby Zhang", "Harvard", "The Returns to Science of Centrally Provisioned GPUs and Optimal Allocation"),
                ]},
                {"room": "Room 202", "host": "Julia Chahine", "talks": [
                    ("Nicolaj Thor", "Brown", "Public Production vs Regulation of Natural Monopolies: Evidence from Water"),
                    ("James Stratton", "Harvard", "Regulating a Monopsonist with Unknown Productivity"),
                ]},
                {"room": "Room 208", "host": "Anna Vinovets", "talks": [
                    ("Cassidy Shubatt", "Harvard", "Designing Experiments to Distinguish Theories"),
                    ("Andres Mena", "Brown", "Distributional Policy Learning via Influence Functions"),
                ]},
            ]},
            {"id": "pitch2", "kind": "Pitch", "name": "Pitch Session 2", "time": "2:45–3:30pm", "rooms": [
                {"room": "Room 102", "host": "Jin Niu", "talks": [
                    ("Samuel Nitkin", "Boston University", "Kumon Up: The Effects of Private Tutoring Centers on Student Achievement"),
                    ("Catherine O’Donnell", "Boston University", "Residency Requirements in Welfare Policy: Implications for Migration and Economic Mobility"),
                    ("Shotaro Beppu", "Harvard", "The Chosen Few: Favoritism in Procurement"),
                    ("Edoardo Bella", "Boston College", "Fiscal-Monetary Interaction In The Market For US Treasuries"),
                    ("Jiayin Liu", "Boston University", "Mutual Legal Assistance Treaties: Home-Country Expropriation Risk and Global Capital Imbalances"),
                ]},
                {"room": "Room 202", "host": "Moritz Greiwe", "talks": [
                    ("Andrés Aradillas Fernández", "MIT", "ϵ-Minimax Approach for Weak IV Testing"),
                    ("Olena Bogdan", "Harvard", "Procuring Disruption: Reconnaissance Drones in Ukraine"),
                    ("Luis Henrique Ribeiro Linhares", "Boston University", "An Axiomatic Approach to Conformity"),
                    ("Sidharth Satya", "Brown University", "Sequential Search Under Summarization"),
                    ("Ke Mao", "Boston University", "From Shares to Ranks: Demand Estimation with Product-Rank Data"),
                ]},
            ]},
            {"id": "p3", "kind": "Presentation", "name": "Presentation Session 3", "time": "3:45–5:15pm", "rooms": [
                {"room": "Room 102", "host": "Leo Zucker", "talks": [
                    ("Ben Delgado", "Brown", "The long-run effects of youth social organizations: Evidence from the historical rollout of the Boy Scouts"),
                    ("Daniele Goffi", "Brown", "Are Amenity Investments and Airline Competition Policy Substitutes?"),
                    ("Sehyun Hong", "MIT", "Richer and Healthier? The Causal Effect of Income on Health"),
                ]},
                {"room": "Room 108", "host": "Sidharth Satya", "talks": [
                    ("Adi Jahić", "Brown", "Investing in Complementarities"),
                    ("Daniel Luo", "MIT", "Fair Commodity Taxation"),
                    ("Leo Zhu", "Harvard", "Information Overload and Rational Shirking With Free Advice"),
                ]},
                {"room": "Room 202", "host": "Julia Chahine", "talks": [
                    ("Yechan Park", "Harvard", "A Design-Based Approach to Testing and Inference in (Quasi-)Experiments with Spillovers"),
                    ("Eric Gao", "MIT", "Multidimensional Sequential Screening"),
                    ("Cole Davis", "Brown", "A Hierarchical Empirical Bayes Model for Two-Way Effects"),
                ]},
                {"room": "Room 208", "host": "Moritz Greiwe", "talks": [
                    ("Vicente Jimenez-Gimpel", "MIT", "Expectations, Uncertainty, and Inefficient Gradualism"),
                    ("Andrew Kao", "Harvard", "Economic Espionage and Innovation Restrictions"),
                    ("Paul Dai", "MIT", "Foreign Exchange Hedging and Currency Invoicing: Theory and Evidence"),
                ]},
            ]},
        ],
    },
}
