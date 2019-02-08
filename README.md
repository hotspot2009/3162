## Project

Aspect-Based Recommendation Search Engine for Hotels

## Description 

Aim of the search engine is to recommend users hotels based on the criteria that they want. For example: room, food etc. 

## Demo

Existing Hosted Web App hosted

[http://hotel-recommendation-engine.herokuapp.com](http://hotel-recommendation-engine.herokuapp.com)

## Code Deliverables

The code deliverables report has been put in the same directory as README.md . It contains all the required information for the codes.


## Run Search Engine in Localhost

Instructions
Install [Git Bash](https://git-scm.com/downloads) in Operating System

Download the [Current GitHub Repository](https://github.com/hotspot2009/3162) and unzip it. 

Open Git Bash

```bash
cd "unzipped folder"
python routes.py
```
Open web browser and type in URL below

```bash
http://localhost:2550
```


## Execute Jupyter Notebook Scripts

Install [Conda](https://www.anaconda.com/distribution/#download-section) in Operating System

Open command prompt (Windows) or shell (Linux) in the folder location


```bash
cd 'codes/' 
jupyter notebook   # Will open Notebook project in localhost
```


Open any *.ipynb files to see the codes. To run the code select the cell and press Shift + Enter

## Execute Aspect Extraction .jar file

Download the folder from the [Google Drive Link](https://drive.google.com/drive/folders/1gSnSdm3i6M1x8ZbHy58C4SlUX1MX3SEg?usp=sharing)

From the shell, navigate to the jar folder


In the following command replace <inputfile.txt> and <output.txt> with your filenames and then run it

```java
java -jar StanfordAspectExtraction.jar <inputfile.txt> <output.txt>
```

