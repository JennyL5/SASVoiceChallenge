# SASVoiceChallenge

At Glasgow University Tech Society's Hachathon - Do You Have the GUTS 2018, we decided to take on the SAS Challenge - Audio Stream Analytics - Make
sense of streams of spoken audio.

Our idea was based around an audio interview. The interviewee will start the program by clicking start, which will lead to a pop-up window with the first question. 
They will have to read the question, then press record. They will be required to speak into a microphone to record their answer to the questions. 
Once they have finished saying their answer, they will press submit to move onto the next question. 

User Interface 1 -
This is a running model of what the program should look like. There are two questions and two lists of potential answers hard-coded into the program, for ongoing test 
the functionality. The potential answers are also hard-coded as at the time the voice recognition was still being compiled.

User Interface 2 - 
This was developed to link the database created and the speech recognition to the program. Our initial idea was to read in the questions and answers at the start, 
and call the functions repeatedly until the maximum number of questions is reached. 

Voice recognition -
We used Sphinx instead of Google API. We were only able to find the American English dictionary for the key phrases. There was difficulty getting consistent accurate 
traslations from voice to text despite even using Google Translate. 

Database - 
We had a database with a table of questions, that mapped each question to a list of potential answers. Those potential answers were linked to a dictionary for the
voice to text translation. However, the connecting of the database did not work for us.

Improvements:
1. Have a timer on the pop-up windows which will display the questions, as this will restrict the amount of time the interviewee has on preparing
for the question. 
2. Another timer is required to keep track/limit the recording of the answer.
3. Maybe another pop-up window or delay can be created between moving on to the next question to allow for breaks.
The database includes a table of different questions, which each links to list of potential answers. 
For the speech recognition, we used Sphinx, we were only able to find the American English dictionary. 
4. Use Google API - however this would have cost money.
