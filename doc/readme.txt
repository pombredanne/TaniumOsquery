Tanium Osquery Integration, by James Cobey


CONTENTS
I.	   How to install the content packs
II.	How to use the sensor content packs
III.  How to use the "package" content
IV.	Known issues and workarounds
V.	   How to generate the content packs


I. How to install the content packs

---Sensors---
1. Although the content is broken down in to seperate os content it is best to
   install all the content.
2. Open the Tanium console and select the "Authoring" tab.
3. Click on the "Sensors" sub tab.
4. Click on the "Import from xml" in the upper right corner.
5. Selec the first xml sensor pack and import the content
6. Repeat this process for all sensor packs

---Packages---
1. Select the "Packages" sub tab after all sensor packs are installed.
2. Select "Import from xml" in the upper right corner.
3. Select the package xml collection file


II. How to use the sensor content packs

---Raw Osquery SQL---
1. Review all the tables that Osquery has here. https://osquery.io/docs/tables/
2. To run a specific Osquery sql statement in Tanium issues the question
   "get osquery[SQL statements here no quotes,--line] from all machines"
3. example
   get osquery[select * from uptime,--line] from all machines
   
---Tanium Osquery Natural Language---
1. All of the Osquery base tables have been translated in to normal Tanium
   sensors.
2. To review the names, under the Tanium console, click "Authoring->Sensors"
3. In the search box type "osquery"
4. Once you find a sensory name that matches what you are looking for you can
   ask the question in natural language in the main Tanium question area.
5. example
   "get computer name and osquery uptime from all machines" 

III. How to use the "package" content

1. The "package" content is designed to install Osquery, stop and start the
   osqueryd daemon, and to push a config to osqueryd.
2. An example use would be to do a natural language Tanium search for all
   Linux hosts that do not have osquery installed.
3. On the Tanium result set, right click and apply the package to install
   Osquery (use deb for hosts that use debian packages, rpm for rpm hosts, etc)
4. Once the "package" is complete you will have Osquery installed, but no
   configured or running daemon.
   (YOU DO NOT NEED THE DAEMON RUNNING TO USE THE SENSORS ABOVE!!!!)
   
IV. Known issues and workarounds

1. When using a raw osquery sql command; commas in the sql statement will fail.
   To work around this issue url encode a comma with %2c.
   
V. How to generate the content packs

1. The translation of the Osquery tables in to Tanium sensors is done by
   extracting the osquery table schema.
2. To extract the schema use the command... osqueryi ".schema" > schema.txt
3. The schmea.txt file now contains all the tables for that system,
   ex darwin,linux, common to all os, etc
4. Use the the converter tool in the tools directory to convert the schmea
5. cat schema.txt | python converter_name_here.py > content.xml



