# LEARN GOLF

"Learn Golf" is a django based website with the aim to convince people to take up golf. The site informs people on what careers paths are available through golf and also provides information on how to achieve a career as a professional golfer aswell as offering lessons to beginners.  
- - -

## Table of Contents
### [User Experience](#user-experience-ux)
* [Project Goals](#project-goals)
* [Agile Methodology](#agile-methodology)
* [Target Audience](#target-audience)
* [First time user](#first-time-user)
* [Registered user](#registered-user)
* [Admin user](#admin-user)
### [Design](#design-1)
* [Color Scheme](#color-scheme)
* [Cabin Images](#cabin-images)
* [Wireframes](#wireframes)
* [Data Model](#data-models)
* [User Journey](#user-journey)
* [Database Scheme](#database-scheme)
### [Security Features](#security-features-1)
### [Features](#features-1)
* [Existing Features](#existing-features)
* [Features Left to Implement](#features-left-to-implement)
### [Technologies Used](#technologies-used-1)
* [Languages Used](#languages-used)
* [Databases Used](#databases-used)
* [Frameworks Used](#frameworks-used)
* [Programs Used](#programs-used)
### [Deployment and Local developement](#deployment-and-local-developement-1)
* [Local Developement](#local-developement)
* [ElephantSQL Database](#elephantsql-database)
* [Cloudinary](#cloudinary)
* [Heroku Deployment](#heroku-deployment)
### [Testing](#testing-1)
### [References](#references-1)
* [Docs](#docs)
* [Content](#content)
* [Acknowledgments](#acknowledgments)

- - -

## User Experience (UX)


Become captivated by the benefits and career oppurtunities provided by taking up golf. The site offers intuitive navigation, satisfying visuals and a simple, effortless booking system where you can also tailor your experience to what you require. This can be also be done on the go as the site is also mobile friendly!

### Project Goals

The goal of the Learn Golf project is to create an immersive and user-friendly online platform that allows users to learn, book, and experience golf and what it has to offer. The project aims to provide a seamless user experience, promoting the aesthetic of golf through captivating golf themed visuals, extensive information and a booking process for however many lessons the user desires.

### Agile Methodology

Agile Methodology was used to help prioritize and organize tasks, writing the user stories and using Project Boards on Github. A template was created to help write User Stories and define Epics

* Epics were written containing possible user stories and based on that the website was made.
* User stories were created by looking at epics and through iterations the project was advancing.
* Project Board is set to public.
* Project Board was used to track progression of the task through the Todo, In progress and Done columns
* Labels were added to sort the issues based on the importance.

### User Stories

#### Epics
* Initial Deployment
* Home Page
* User Registration
* Website Admin and Bookings
* Maintain consistent design with responsiveness in mind

#### User Stories
1. Initial Deployment
* Create new Heroku application
* Link Github repository to the Heroku app
2. Home Page
* Create a navigation bar
* Create a footer
3. User Registration
* Sign Up page
* User registration, log in, log out
* Display users name
4. Website Admin and Bookings
* Alert messages
* Crud functionality
* Cabin pagination
* Admin panel
* Double bookings
* Book Amenities
* Total Price
4. Maintain consistent design with responsiveness in mind
* Maintain consistent design
* Test responsiveness

Detailed look can be found in the [project board](https://github.com/users/Thomas-Tomo/projects/2)

### Target Audience

* Individuals who are looking to try golf aswell as those who have never thought about it.
* Golfers looking for an effortless booking process for lessons with a PGA pro to help improve their game.
* Users who value a captivating and visually appealing online experience.
* Mobile users who want the convenience of booking their lessons from any device.

### First time user

* Easy and intuitive website navigation.
* Engaging visuals showcasing golf and what it has to offer.
* Informative content providing an insight into what to expect when getting into golf
* User-friendly forms with clear validation messages to ensure correct input.
* Simple Registration process.

### Registered User

* Effortless login process with a secure and personalized user account.
* Access to all of the users bookings with the ability to edit or delete them allowing flexibility and convenience.
* Ability to book as many lessons as the user desires.

### Admin user

* Secure and separate login portal for admin users with appropriate access control.
* Access to an admin dashboard for managing bookings.
* Ability to add, edit, or delete bookings and change availability.
* Ability to delete user accounts, providing the necessary control for managing user data and accounts.