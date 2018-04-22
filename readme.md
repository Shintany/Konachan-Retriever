# Konachan Retriever

This programm will allow you to downlaod a fixed amount of images from the website https://www.Konachan.com depending on which tags you'll fill the entry

## Requirements

You need python 3 installed on your machine, and the following package :

* Tkinter
* Pillow
* Requests
* urllib
* BeautifulSoup4
* lxml parser

### LINUX (Ubuntu 16.04)

Enter the following command in the Terminal window :

```
sudo apt-get update (if you didn't already did it)
sudo apt-get -y upgrade
sudo apt-get intall -y python3-pip (pip3 is needed)
sudo apt-get install python3-tk
sudo pip3 install Pillow --upgrade
sudo pip3 install lxml
```

You can see that I didn't downloaded 'Requests', 'BeautifulSoup4' and 'urllib', that's because they generally come with python3 package.

If the module isn't found, enter the following command :

```
sudo pip3 install requests --upgrade
sudo pip3 install BeautifulSoup4
```

And it should be fine!

### MacOs (High Sierra)

I downloaded the installer from the Python website (Version 3.6.5)

Normally, pip3, urllib and Tkinter should come with the initial package, so you'll have to type the following command :

```
sudo pip3 install requests
sudo pip3 install bs4 (BeautifulSoup)
sudo pip3 install pillow
sudo pip3 install lxml
```

## Launch

Enter the following command to execute the program :

```
python3 Konachan_Retriever.py
```
