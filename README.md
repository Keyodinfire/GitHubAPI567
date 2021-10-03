# GitHubAPI567
[![build status of main](https://travis-ci.org/Keyodinfire/GitHubAPI567.svg?branch=main)](https://app.travis-ci.com/github/Keyodinfire/GitHubAPI567)



Deliverable 2 for Homework 4a:

When I first started writing the code for this assignment, I had not worked with REST API in a while and did not have much experience working with
JSON objects in Python, so I needed to do some research before being able to progress with the assignment. I decided to write a helper function for 
gathering input from the user in the form of their GitHub username and returning the input, which would then be used in two other helper functions
and the main function. I then designed two helper functions, one which would return a list of repo names and one that would return the number of commits
for a given repo. Then, in the main function, I stored each repo's number of commits into a list and appended both the repo name and corresponding number
of commits to an empty list and returned that list. 

This was important to making the program easy to test, since having a callable main function makes writing test cases very easy. It also becomes possible to test the helper functions separately and determine that they are working properly, rather than having to test the main function multiple times and attempt to determine from the output or error messages why it is not working properly. Having multiple helper functions makes testing the main function and determining errors a much easier process. 

There were two main challenges I faced with testing the program. The first main challenge was the limit on GitHub API requests, which made the process of writing code and testing the program much slower than it would have been if the limit was higher. Since each function call of the main program calls the API multiple times, I was only able to test the main function a handful of times before my tests resulted in errors. The second main challenge was testing the program on Travis CI. Since the program requires user input, I had to perform research on how testing a function with input was possible on Travis CI. Through my research, I found that I could make a txt file with the desired inputs and link the txt file to my test function call in the 
.travis.yml file, to instantly fill in the inputs. 