# cs178-Project

UCR Capstone Project

Title: Testing Center Scheduling System

Description: The Testing Center Scheduling System will allow for students to sign up for a seat in a proctored exam session on campus. This system gives students the opportunity to make up missed exams and give instructors a convenient way to schedule a quiz/exam time outside of regular lecture hours. The proctored session prevents the possibility of cheating and interruptions.

Team members: Kyle Damschen, Gregory Griffith, Eric Chu, Kathleen Dario

Tools that will be used:

Django
Vue
PostgreSQL
Javascript
Python

Schedule for daily meetings: Tentative 1:00pm - 1:15pm daily

Final Vision: Our final vision for the testing center scheduling is to make an accessible web app for UCR faculty and students. This web application will allow professors to set times for their students to book to take the exam in a proctored setting. Once the professor sets these times it will send information to the web servers and allow those students in the class to book those seats during a desired time frame if seats are available. Each time frame will have 5 reserved seats that are for emergency situations. Once a student books a desired time our web application will send that information to the canvas/classroom setting to edit when that exam is released for that student and when it has to be turned in by. Once a student arrives to the proctored environment we will have a feature so that the proctor can login and check off which students are present during the exam, if the student is not marked present the exam shouldn’t be released to them on canvas so we can keep the exam secure.

Vision for the end of this quarter (178A): The vision for the end of this quarter is to have a MVP, that is a simple scheduler for students to book the testing center room. We want to have a working scheduler system that allows professors to set a time to set aside a room/rooms. A proctor should be able to check off students from a registered list. An administrator should be able to designate at what times a room will be available and how many seats will be available and finally the student shouldn’t be able to choose a time if a seat isn’t available.

# Setting up dev enviorment

1. Download and setup docker

2. Once docker is installed and setup clone the repo to your local machine

3. once the repo is cloned run the dev docker compose file and build dev container and run

command: docker compose -f docker-compose.dev.yml up

4. Download Dev containers extension on vs code made by microsoft

extension id: ms-vscode-remote.remote-containers

5. Open up remote explorer to access your dev container in a new window and you are ready to start development
