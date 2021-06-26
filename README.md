# Company Master :: Maharashtra Dataproject-sqlalchemy

**Open proejct Company Master**
[link](https://companymasters.herokuapp.com/)

## Aim

To convert raw open data into highchart, that tell a story on the state of company registration in Maharashtra.Then present in the highchart in website.

## How to get the data

* The dataset can be downloaded from [link](https://data.gov.in/resources/company-master-data-maharashtra-upto-21st-april-2018)
* Download file change file name run `mv mca_maharashtra_21042018.csv mca_maharashtra.csv`

## Requirements

* You have require a any browser like Chrome,Firefox,safari etc.
* Require internet connectivity.
* All requirements and dependencies run `pip3 install -r requirements.txt`

## How to run project

* Clone a repository in your system `git@gitlab.com:mountblue/cohort-14-python/rakshit_sarkheliya/dataproject-sqlalchemy.git`

* You need to open postgres using this command `sudo -u postgres psql`

* Create a Role and Database in postgres using this script `\i script/createhelper.sql`

* Run command `python engine.py` in the repository folder which get data from
database table and  generate data.json file in public directory.

* Delete a Role and Database in postgres using this script `\i script/drophelper.sql`
* Run command `cd public` to move in public directory.

* Run command `python -m http.server` in the repository folder which start server.

* Open url [http://0.0.0.0:8000/] in Browser.
