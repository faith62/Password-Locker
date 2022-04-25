# Password Locker
### Project description

An application that will help us manage our passwords and even generate new password for us. Touches on Test Driven Development using unittest (Python test framework).

### By Faith Chemutai ,21/03/2022
## Setup/instalation Requirements
*You need to have a vs code/ atom , python installed
*Access to Internet
*You need access to a computer, laptop.

## Technologies Used

- Python3.9
- unittest (Python test framework)
- PyperClip

##### Setup Instructions and Installation

- Clone this repository to a location in your file system. `git clone https://github.com/faith62/Password-Locker.git`
- Open terminal command line then navigate to the root folder of the application. `cd Password-Locker`
- Run `./run.py` 


## Behaviour Driven Development

1. Displays Intro Message to user
    - OUTPUT: "Hello Welcome to your Password locker. What is your name"
   - INPUT: "Faith"
   - OUTPUT: "Hello faith. what would you like to do? 
    Use the short codes: ca - create an account, li - login to an existing account "
2. Enter Short Code
   - INPUT: "ca"
   - INPUT: "user_name","password" -prompt user to enter username and password
   - OUTPUT: faith ,your new account has been created successfully! Your password is 123456 
3. Enter Short Code
   - INPUT: "li" 
   - INPUT: "user_name","password" -prompt user to enter username and password
   - OUTPUT: "faith .Welcome to Password Locke
   - OUTPUT: "Welcome to Password Locker manager, what would you like to do?:"
   -OUTPUT: "Use these short codes : cc - create a new credentials, dc - display credentials, fc -find a credentials, ex -exit the credentials list"
4. Enter Short Code
   - INPUT: "cc"
   - INPUT: "account""username""password"
   - OUTPUT: "New credential instagram fefe fch1234"-create new credentials by providing required properties
5. Enter Short Code
   - INPUT: "dc" 
   - OUTPUT: "here is a list of all your credentials"
   - OUTPUT:"Account:Instangram, Username:fefe, Password:fc12h"
4. Enter Short Code
   - INPUT: "fc"
   - INPUT: "Instagram" - Search by account
   - OUTPUT: "Instangram, Username:fefe, Password:fc12h" - Returns credentials if exists

## Known Bugs

Have you seen any bug? Contact me.
### License

*MIT*
Copyright (c) 2022 **Faith Chemutai**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
