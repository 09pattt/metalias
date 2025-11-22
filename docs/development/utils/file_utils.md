# file_utils.py

Dealing with file and directory (Included full features without removing external features to optimizing project).

## Index

## Features

## Packages

This program is using these following packages as a component.

 - **pathlib**
 : to handle general file management.

 - **os**
 : manage system (External feature, for debug and testing)

 - **shutil**
 : to handle extra directory function.

## Functions

#### function: appdir

- **Parameter**
 Not requires for any argument

- **Usage**
 **1. Call** >> Assign no argument

 **2. Execute**
 1. Init pathlib.Path at __file__ (Absolute program file path)
 2. Adjust created object path to root directory 

 **3. Return** > Project root "/metalias" < Always return same path no matter function call from anywhere

#### function: join

- **Parameter**
 1. *args : str >> Path to join

 2. resolve : bool = True >> Option to do resolve function

- **Usage**
 **1. Call** >> Assign argument with path (Any amount)

 **2. Execute** >>

 **3. Return** >> String of joined path

#### function: mkfile

- **Parameter**
 1. path : str >> Path where to create a file

 2. exist_ok : bool >> Option to create if file already existed

- **Usage**
 **1. Call** >> Assign argument
 **2. Execute** >>