from flask import Flask, render_template, jsonify

app = Flask(__name__)

profiles = {
    "id" : 1,
    "name" : "Sheldon Cooper",
    "about_me" : "Greetings, potential friends. I am Dr. Sheldon Cooper, a theoretical physicist with an IQ that surpasses the majority of the population. I hold multiple advanced degrees and have an unparalleled expertise in string theory. My interests include comic books, science fiction, video games, and creating highly structured routines.\nI seek companions who can appreciate intellectual conversations, adhere to a rigid schedule, and engage in activities such as \"Fun with Flags\" or \"Klingon Boggle.\" While my social skills may be a work in progress, my loyalty and unique perspective on life make me an extraordinary friend. If you possess a high tolerance for scientific jargon and an appreciation for precise order, I welcome the opportunity to establish a mutually beneficial friendship. Bazinga!",
    "why" : "As a theoretical physicist with an intellect that far surpasses the norm, I begrudgingly acknowledge the necessity of expanding my social circle. Despite my lack of enthusiasm for this endeavor, it is clear that surrounding myself with a wider array of individuals—even those who may not match my intellectual prowess—can provide diverse perspectives and collaborative opportunities. While I don't particularly enjoy socializing with people who often lack the depth of understanding I possess, I recognize that even the most ordinary minds can occasionally offer useful insights. Therefore, I am logically pursuing this endeavor to enrich my life experience, despite my personal reservations."
}
roles = [
    {
    "id" : 1,
    "name" : "Roommate",
    "location" : "Pasadena, California",
    "vacancies" : 1,

    "recuirements" : ["Adherence to the Roommate Agreement",
    "Strict observance of quiet hours from 10 PM to 8 AM",
    "No pets allowed, with the exception of well-behaved imaginary pets",
    "Approval required for all guests, including family members",
    "Agreement to participate in bi-weekly Roommate Meetings",
    "No tampering with the thermostat; it stays at 72°F",
    "Respect for designated spots for each item in the apartment",
    "Willingness to engage in weekly 'Fun with Flags' segments",
    "Preference given to individuals with a background in science or engineering",
    "No consumption of food containing peanuts, due to severe allergy",
    "Agreement to participate in 'Laundry Night' every Saturday at 8 PM",
    "No loud music or disruptive activities",
    "Understanding that the bathroom schedule is non-negotiable",
    "Respect for a mandatory 'Co-op Night' on Tuesdays"],

    "benefits" : ["Access to a meticulously organized living space",
    "Structured routines that promote productivity",
    "Opportunities for engaging intellectual discussions",
    "Exposure to a vast collection of comic books and science fiction memorabilia",
    "Regular movie and TV series nights with a curated selection of content",
    "Participation in 'Fun with Flags' segments",
    "Enhanced problem-solving skills through collaborative activities",
    "Consistent and predictable living environment",
    "Access to a high-speed internet connection",
    "Weekly 'Laundry Night' ensuring clean clothes",
    "Educational board games and activities",
    "Occasional home-cooked meals (following strict hygiene standards)",
    "Guidance on personal organization and time management",
    "Exposure to advanced scientific theories and discussions"]
    },
    {
        "id" : 2,
        "name" : "Movie Partner",
        "location" : "Pasadena, California",
        "vacancies" : 2,
        "requirements" : ["Strict adherence to the movie schedule",
        "Punctual arrival at the designated movie start time",
        "No talking during the movie, except for approved commentary",
        "No use of mobile devices or other distractions during the movie",
        "Respect for Sheldon’s seat selection and seating arrangements",
        "Agreement to watch movies in the predetermined order",
        "Willingness to participate in post-movie discussions and analyses",
        "Approval required for any snacks brought into the movie area",
        "Adherence to a no-spoilers policy",
        "Respect for Sheldon’s preferences in movie genres, primarily science fiction and superhero films",
        "Agreement to Sheldon’s pre-movie trivia and fact-sharing sessions",
        "No unauthorized changes to the movie settings or equipment",
        "Willingness to dress appropriately for themed movie nights",
        "Participation in themed activities related to the movie when applicable"],

        "benefits" : ["Exposure to a carefully curated selection of movies, primarily focusing on science fiction and superhero genres",
        "Insightful pre-movie trivia and interesting facts shared by Sheldon",
        "Post-movie discussions and analyses that enhance understanding and appreciation of the film",
        "Access to a high-quality home theater setup with optimal viewing conditions",
        "A structured and organized movie-watching experience",
        "Opportunities to participate in themed movie nights and related activities",
        "A distraction-free environment ensuring an immersive viewing experience",
        "Potential to learn and appreciate new movie genres and classics",
        "Guidance on the historical and scientific accuracy of films",
        "A chance to engage in intellectual conversations related to movie themes",
        "Consistent movie schedule providing regular entertainment",
        "Opportunities to bond over shared interests in cinema",
        "Exposure to Sheldon's extensive knowledge of the film industry"]
    }
]

@app.route('/')
def hello_world():
    return render_template('home.html', profiles=profiles, roles=roles)

@app.route('/api/roles')
def list_roles():
    return jsonify(roles)

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/apply')
def apply():
    return render_template("applicationForm.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)