Welcome home
============

A minimal application created to demo an introductory experience with [Sentry](https://getsentry.com/welcome/), [Jenkins](http://jenkins-ci.org/) and testing in [Flask](http://flask.pocoo.org/).

![welcome_home](https://raw.github.com/RobrechtDR/welcome_home/master/.misc/home.png)

### Quickstart

**Install**       
    `pip install -r requirements.txt`

**Start the server**     
    `python welcome_home.py`

**Run unit tests**    
    `python welcome_home_unit_tests.py`

**Run integration tests**     
    `python welcome_home_integration_tests.py`


### Sentry

**Setup**     
1. Register on https://www.getsentry.com/register/ .    
2. Create a team, fill in `welcome_home` as project name and select `Flask` as platform.    
3. Copy the `SENTRY_DSN` url from the Sentry Flask snippet to a [.env file](https://github.com/kennethreitz/autoenv). An Example of `.env`:    
  `export SENTRY_DSN="https://be440b0a20c269043ea3778:eba819fc@app.getsentry.com/23140"`   
4. Load the environment variable in `.env`:  
  `source .env`    


**See it in action**     
1. Uncomment the line with `1/0` in `welcome_home.py`.    
2. Run the server:     
   `python welcome_home.py`         
3. Go to `http://localhost:5000` in your browser. You should see an `Internal Server Error`.    
4. You should now get a mail on the email address you provided during your registration for Sentry. 
The email contains a link to the Sentry web platform, there the errors are neatly logged.

  > If you didn't get a mail, it's probably because you didn't set the `SENTRY_DSN` environment variable.      

 > Don't forget to run `pip install -r requirements.txt` in your virtual environment before you run the server.


### Jenkins

**Setup**    
1. [Install Jenkins](https://wiki.jenkins-ci.org/display/JENKINS/Installing+Jenkins).    
2. Install the [Git](https://wiki.jenkins-ci.org/display/JENKINS/Git+Plugin), [Github](https://wiki.jenkins-ci.org/display/JENKINS/GitHub+Plugin)(to clone from the Github repo) and [ShiningPanda](https://wiki.jenkins-ci.org/display/JENKINS/ShiningPanda+Plugin)(to enable virtualenv) Plugins on `http://localhost:8080/pluginManager/available` and restart Jenkins.   
You can restart Jenkins via the command line by running `sudo service jenkins restart`.         
3. Create a Jenkins item:      

  1. Click on `New Item`.   

  2. Select `Build a free-style software project` and fill in `welcome_home` as item name and click `Ok`.   

  3. Configure the job:     

      1. Under `Souce Code Management`: select the `Git` radio. As `repository URL` fill in `https://github.com/RobrechtDR/welcome_home.git`.

      2. Under `Build` select `Virtualenv Builder` and paste the following commands:   

              pip install -r requirements.txt    
              python welcome_home_unit_tests.py    

      3. Click `Save`

**See it in action**  
Run the supplied test commands by clicking on the item's `Build Now`.
