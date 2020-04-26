# Deploy Python Web Application to AWS

## using elastic beanstalk CLI
* create python server file
* create requirements.txt

* change directory to the folder which contains above files

create application flask1
```
eb init -p python-3.6 myapp --region us-east-2
```
create environment
```
eb create myapp-env-1
```
start the application, open the browser
```
eb open
```

[AWS elastic beanstalk](https://us-east-2.console.aws.amazon.com/elasticbeanstalk/home?region=us-east-2#/environments)