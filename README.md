# theme-creator-crisis-sim

This script is used to create a new theme for the crisis sim.

## Requirements

Python 3.10.x
Virtualenv

## Install directions

Clone this repo.

cd into the repository.

Run `py -m virtualenv venv`
Run `venv/scripts/Activate`
Run `pip install -r requirements.txt`

## Running the script

Ensure the virtualenv is activated and the neccecary dependencies are installed.
Run `py change-theme.py`

The program will ask you `What is the brand name?`

- This is what will show up wherever the brand name is referenced. For instance, if you input `Nestle` the navbar would illustrate `Nestle`, the News page would show `Nestle News` etc.

The program will ask you `What is the brand nav logo file path?`

- This is the logo that shows up in the navbar. Simply copy the realative or absolute path and paste it into the terminal, no quotes required.

The program will ask you `What is the brand profile logo file path?`

- This is the logo that will show up as the profile picture for the brand i,e on facebook / instagram. This can be the same as the one in the nav.

The program will ask you `What is the brand email logo file path?`

- This is the logo that displays on the email page. Example, `NestleMail`

Assuming all the filepaths are correct, the program will make the necceccary changes. It will create a new folder which is named after the brand name that you supplied. This folder has all of the changes required.

Be sure to keep the template repository up to date.
