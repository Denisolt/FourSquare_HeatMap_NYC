# New York City Heat Map based on FourSquare
![alt tag](https://github.com/Denisolt/FourSquare_HeatMap_NYC/blob/master/static/images/image2.png)</br>
## Project Scope:
This project is data visualization of Four Square Check-ins in New York City. The used dataset is from Kaggle.. This dataset contains check-ins in NYC and Tokyo collected for about 10 month (from 12 April 2012 to 16 February 2013). It contains 227,428 check-ins in New York city and 573,703 check-ins in Tokyo. Each check-in is associated with its time stamp, its GPS coordinates and its semantic meaning (represented by fine-grained venue-categories). This dataset is originally used for studying the spatial-temporal regularity of user activity in LBSNs. This project uses Pandas to extract the information from .csv file and Flask in order to render the template. For more info check the repo on github.
</br>

## Resources:
- FourSquare - NYC and Tokyo Check-ins Dataset from <a href="https://www.kaggle.com/chetanism/foursquare-nyc-and-tokyo-checkin-dataset">Kaggle</a>
- Google Maps JS API

<h3>This is what the dataset looks like: </h3>

|    userId  |    venueId   | venueCategoryId | venueCategory | latitude | longitude | timezoneOffset | utcTimestamp |
| :--------- | :----------: | ---------: | :----------: | :----------: | :----------: | :----------: | ---------: |
|470|49bbd6c0f964a520f4531fe3|4bf58dd8d48988d127951735|Arts & Crafts Store|40.71981038|-74.00258103|-240|Tue Apr 03 18:00:09 +0000 2012|
|979|4a43c0aef964a520c6a61fe3|4bf58dd8d48988d1df941735|Bridge|40.60679958|-74.04416981|-240|Tue Apr 03 18:00:25 +0000 2012|
|69|4c5cc7b485a1e21e00d35711|4bf58dd8d48988d103941735|Home (private)|40.71616168|-73.88307006|-240|Tue Apr 03 18:02:24 +0000 2012|
|395|4bc7086715a7ef3bef9878da|4bf58dd8d48988d104941735|Medical Center|40.7451638|-73.98251878|-240|Tue Apr 03 18:02:41 +0000 2012|
|87|4cf2c5321d18a143951b5cec|4bf58dd8d48988d1cb941735|Food Truck|40.74010383|-73.98965836|-240|Tue Apr 03 18:03:00 +0000 2012|
|484|4b5b981bf964a520900929e3|4bf58dd8d48988d118951735|Food & Drink Shop|40.69042712|-73.95468678|-240|Tue Apr 03 18:04:00 +0000 2012|
|...|...|...|...|...|...|...|...|

## Installation:
Downloading the project:
```bash
git clone https://github.com/Denisolt/FourSquare_HeatMap_NYC.git
cd FourSquare_HeatMap_NYC-master

```
Activation of virtual environment:
```bash
source local/bin/activate
pip install -r /path/to/requirements.txt
```
## Execution:
```bash
python main.py
```
Output will be:
```bash
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 150-657-841
 ```
