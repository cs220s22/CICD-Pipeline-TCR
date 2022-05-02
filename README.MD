# CI/CD Pipeline 
CSCI 220 2A Final Project

## Table of contents
* [Overview](#overview)
* [Technologies](#technologies)
* [Setup](#setup)
* [Background](#background)

## Overview
This project is a representation of how a CI/CD pipeline could be implemented and make a team of indivduals more productive by automating both the testing before production, and deployment there afterwards. The CI/CD Pipeline allowed us to learn github actions, where we would use triggers such as pull requests to both test and lint our code before automating the process of deploying it via our Heroku server. 
	
## Technologies
Project is created with:
* [Github Actions](https://github.com/features/actions?utm_source=google&utm_medium=ppc&utm_campaign=2022q3-adv-WW-Google_Search-eg_brand&scid=7013o000002CdxYAAS&gclid=CjwKCAjwgr6TBhAGEiwA3aVuId1tsoq4Fg3RT5r1iThsSfvMEKzVNH5fmXz2lphZsWUp4yf8WJ1pHRoCg1MQAvD_BwE)
* [Pytest](https://docs.pytest.org/en/7.1.x/)
* [Pylint](https://pypi.org/project/pylint/)
* [Heroku](https://dashboard.heroku.com/apps)
	
## Setup
The steps that were implemented to make this CI/CD Pipeline possible were as follows:

1. Creating our Github Actions Workflow
    1. Creating within our repository the .github/workflows area.
    2. Creating different .yml files for our different workflow actions.
2. Identifying The Triggers
    1. Certain workflows want to be qued at different times, so making sure that actions are called on at the right time is important
    2. This is what allows our pipeline to be automated rather than manually writing a command when we want to test our code (Although we allowed that to be a possibility as well due to our workflow dispatch).
3. Integration
    1. Rather than using one github workflow for both our testing and our linting we decided to create two seperate workflows that would be triggered simulatenously.
    2. The trigger for our testing and linting phase is upon a pull request.
4. Deployment
    1. We Decided to deploy into heroku so using a single workflow we take our flask application and deploy it directly to Heroku.
    2. The difference between our integration and deployment is that our deployment is called once the commit is actually pushed to the main branch.

## Background
The project was created using a variety of sources, but here are some of the sources that we found the most influential during the development phase of our project.
* [Github Actions](https://github.blog/2022-02-02-build-ci-cd-pipeline-github-actions-four-steps/)
* [Github Secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets)
* [Pylint](https://github.com/marketplace/actions/github-action-for-pylint)
* [Pytest](https://www.linkedin.com/pulse/test-automation-how-build-cicd-pipeline-using-pytest-nir-tal)
* [Heroku Deployment](https://github.com/marketplace/actions/deploy-to-heroku)

=======

Dr. Coleman
