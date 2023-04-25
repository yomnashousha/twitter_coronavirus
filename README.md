# Coronavirus Twitter Dataset Analysis

This project utilizes the MapReduce divide-and-conquer paradigm to create parallel code for the purpose of scanning all geotagged tweets sent in 2020. This allows the monitoring for the spread of the coronavirus on social media.


The following processes allow us to conduct this project

**Map**

The `map.py` file processes the zip file for an individual day.
It tracks the usage of the hashtags on both a language and country level.
The output of it running for each day is two files, one that ends in `.lang` for the language dictionary and one that ends in `.country` for the country dictionary.
```
$ ./src/map.py --input_path=/data/Twitter\ dataset/geoTwitter20-02-16.zip
```
This command creates a folder `outputs` that contains the files `/geoTwitter20-02-16.zip.lang` and `/geoTwitter20-02-16.zip.country`, which are files that contain JSON formatted information summarizing the tweets from 16 February.

In order to process the zip file for every single day in 2020, the file `run_maps.sh` was created. It loops over each file in the dataset and runs the `map.py` command on that file.
The glob `*` was implemented in order to select only the tweets from 2020 and not all tweets.

```
$ nohup sh run_maps.sh &
```
This `nohup` command was used to ensure that the program continued to run after server disconnection and the `&` operator ensured that all `map.py` commands ran in parallel.


**Reduce**

The `reduce.py` file merges the outputs generated by the `map.py` file so that the combined files can be visualized. To do so, you can use the glob to merge all output files with the command
```
$ ./src/reduce.py --input_paths outputs/geoTwitter*.lang --output_path=reduced.lang
```
and 
```
$ ./src/reduce.py --input_paths outputs/geoTwitter*.lang --output_path=reduced.country
```
which generate two files `reduced.lang` and `reduced.country` that contain data for all of the hashtag usage by language and country for all of 2020, respectively.

**Visualize**

The `visualize.py` file contains `--input_path` (which can =language or =country) and `--key` as inputs and generates a bar graph of the top 10 languages or countries depending on what the input is specified as. 

# #coronavirus Usage By Language
<img src=coronavirus_lang.png width=95% />

# #coronavirus Usage By Country
<img src=coronavirus_country.png width=95% />

# #코로나바이러스 Usage By Language
<img src=코로나바이러스_lang.png width=95% />

# #코로나바이러스 Usage By Country
<img src=코로나바이러스_country.png width=95% />

The difference between the commands for each of these graphs is whether the `--input_path` was =language or =country and if `--key` = '#coronavirus' or ='#코로나바이러스' 

**Alternative Reduce**

This is a file that takes as input on the command line a list of hashtags,
and outputs a line plot where:
1. There is one line per input hashtag.
1. The x-axis is the day of the year.
1. The y-axis is the number of tweets that use that hashtag during the year.

# Usage of Hashtags in 2020
<img src=line_plot.png width=95% />
