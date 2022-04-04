# She Code Africa application

## How to use

- Clone the repository by running the command `git clone https://github.com/Stefanie-A/SCA-Cloud-School-Application`

- Switch to the `Start` branch by running the  command `git checkout Start`

- `cd` into the `docker` folder and run the command `docker build -t sca-assessment .` to build the docker image.

- Run the docker container with the command `docker run -p 5000:5000 sca-assessment`. This exposes port 5000 as well so we can view the application.

- Finally, navigate to [http://localhost:5000](http://localhost:5000) to view the running application.

You can checkout the docker image on dockerhub as well [here](https://hub.docker.com/repository/docker/stefnie/sca-application)