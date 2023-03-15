# gdal_ogr
Python geoprocessing library built with the GDAL/OGR translator library


GDAL (Geospatial Data Abstraction Library) and OGR (Simple Features Library) are open-source librares for reading, writing, and manipulating GIS data. Over 200 raster and vector data formats are supported. The library is written in C++ and has bindings for many other programming languages such as Python.
While numerous GIS Python libraries are built on top of the GDAL/OGR library, using the library directly in Python has some advantages. 
  1. Performance - GDAL/OGR is a lower-level library versus higher level libraries such as GeoPandas. This can have advantages for processing larger      datasets. 
  2. Flexibility - GDAL/OGR provides for detailed control over geospatial and supports a wider range of formats versus GeoPandas
  3. Integration - GDAL/OGR is a widley used GIS library that is supported by many other GIS tools and applications. 
  
Installation:
This documentation covers installation on MacOS only. However it is encouraged to modify these instructions to also include Windows and Linux.
Currently we do not know of a way to install GDAL/OGR library directly into a Python virutal environment without prior installation of the libraries on the local machine first. Therefore we will first install GDAL/OGR the local machine, followed by creating a Python virtual environment for a specific project.

The installation steps originally came from this web article: https://medium.com/@egiron/how-to-install-gdal-and-qgis-on-macos-catalina-ca690dca4f91

These installation steps have been tested on a MacBook Pro with the following specs:
  - macOS Ventura 13.2.1 with 
  - Apple M1 Chip
  - Memory: 16 GB
  
 1. Install Python 3.11.2 (if not already installed): https://www.python.org/downloads/
  - Python by default gets installed here: /Library/Frameworks/Python.framework/Versions/3.11/bin/python3
  - Verify your Python installation by opening your zprofile: nano ~/.zprofile
  
  
 2. Install Homebrew (if not already installed): https://brew.sh/
  - /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  - Add Homebrew to your path: eval "$(/opt/homebrew/bin/brew shellenv)"
 
 3. Install GDAL header files
  - brew update
  - brew upgrade
  - brew install gdal --HEAD (ignore any error that may occur)
  - brew install gdal
  - Verify install: gdal-config --version 
 
 4. Install GDAL Python bindings
  - python -m pip install --upgrade pip
  - pip install gdal==3.6.2 (version must match your GDAL installed version. This can be obtained by running gdal-config --version)
  - verify install: pip list

GDAL should now be included in your global Python environment. The next step is to create a Python virtual environment for your specific project. When creating the new virtual environment, you will need to include the option to install system site packages (if you want to use GDAL/OGR)

Create Python Virtual Environment

  1. Switch to project directory: (ex. cd /Users/justinhawley/repos/tutorial)
  2. python -m venv venv --system-site-packages
  3. Activate virtual environment: source venv/bin/activate
  4. Verify environment has GDAL package: pip list (can upgrade pip here as well: pip install --upgrade pip) 




