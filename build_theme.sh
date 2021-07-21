#!/bin/bash   

echo build theme

git pull 
npm run-script build

git add .
git commit -m "build theme"
git push
