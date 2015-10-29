#DARWIN ONLY

import re
import sys

QRY_TEMPL="""<query>#!/bin/bash
/usr/local/bin/osqueryi --csv "select * from %s" | /usr/bin/tail -n +2</query>"""

COL_TEMPL="""<column>
        <name>%s</name>
        <column_index>%s</column_index>
        <hidden_flag>0</hidden_flag>
        <ignore_case_flag>1</ignore_case_flag>
        <exclude_from_parse>1</exclude_from_parse>
        <result_type>1</result_type>
      </column>"""

SEN_TEMPL ="""<sensor>
    <name>%s</name>
    <result_type>1</result_type>
    <seconds>86400</seconds>
    <seconds_never_flag>1</seconds_never_flag>
    <qseconds>60</qseconds>
    <event_flag>0</event_flag>
    <ignore_case_flag>1</ignore_case_flag>
    <weight>0</weight>
    <category>Operating System</category>
    <exclude_from_parse>1</exclude_from_parse>
    <delimiter>|</delimiter>
    <description>Osquery Sensor</description>
    <what_hash></what_hash>
    <hidden_flag>0</hidden_flag>
    <columns>
      %s
    </columns>
    <queries>
      <sensor_query>
        %s
        <sensor_type>6</sensor_type>
        <os>2</os>
        <signature/>
      </sensor_query>
    </queries>
    <meta_data/>
    <parameters/>
  </sensor>
"""


SLN_STRING = """<sensors>
"""

for line in sys.stdin:
   
   matches = re.search("CREATE TABLE (.*)\((.*)\)",line)
   
   table_nam = matches.group(1)
   sen_nam   = "Osquery Darwin " + table_nam.replace("_"," ").title()
   col_lst   = map(lambda x: x.split()[0],matches.group(2).split(','))
   
   tmp_cols = ""
   tmp_qry  = ""
   tmp_sen  = ""
   
   for i in range(0,len(col_lst)):
      tmp_cols = tmp_cols + COL_TEMPL%(col_lst[i].replace("_"," ").title(),i)
   
   tmp_qry = QRY_TEMPL%(table_nam)
   tmp_sen = SEN_TEMPL%(sen_nam,tmp_cols,tmp_qry)
   
   SLN_STRING = SLN_STRING + tmp_sen


SLN_STRING = SLN_STRING +"""</sensors>"""
print SLN_STRING