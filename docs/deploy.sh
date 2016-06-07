#!/bin/bash
set -e # exit with nonzero exit code if anything fails

# go to the out directory and create a *new* Git repo
mkdir -p _build/html
cd _build/html
git init

# inside this git repo we'll pretend to be a new user
git config user.name "Travis CI"
git config user.email "nathan.bergey@gmail.com"

# Get the old gh-pages branch
git remote add github "https://${GH_TOKEN}@github.com/open-aerospace/jsbsim-manager.git" > /dev/null 2>&1
git fetch github gh-pages
git checkout gh-pages

# Now go back and make the site
cd ../..
make html
cp _config.yml _build/html/
x=$(for i in `git log --all --pretty=format:{\"hash\":\ \"%h\"\,\ \"time\":\"%ad\"},`; do echo -n "${i} "; done| sed 's/, $//') ; echo "["$x"]" > _build/html/git.json

# Now go into the repo and commit whatever happened
cd _build/html
git add .
git commit -m "Travis Deploy to GitHub Pages"
git push --quiet github gh-pages > /dev/null 2>&1
