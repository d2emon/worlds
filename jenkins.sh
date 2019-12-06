docker run\
  --rm\
  -u root\
  -p 8080:8080\
  -v "$(pwd)/jenkins-data:/var/jenkins_home"\
  -v /var/run/docker.sock:/var/run/docker.sock\
  -v "$HOME/jenkins:/home"\
  -v "$HOME/projects/py/flask/worlds:/home/worlds"\
  jenkinsci/blueocean
