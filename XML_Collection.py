import xml.etree.ElementTree as ET
import pandas as pd
import os
import re
d =[{'Test_Case':'Test_Case','node_order':'node_order','version':'version','summary':'summary','preconditions':'preconditions',
                      'execution_type':'execution_type','importance':'importance','estimated_exec_duration':'estimated_exec_duration','status':'status',
                      'steps':'steps','requirements':'requirements','actions':'actions','doc_id':'doc_id','expectedresults':'expectedresults','req_spec_title':'req_spec_title',
                      'title':'title'}]
dfn = pd.DataFrame(d)
Files = [File for File in os.walk(os.getcwd())]
for File in Files[0][2]:
    match = re.search('.xml',File[-4:])
    if match:
        tree = ET.parse(File)
        root = tree.getroot()
        dic = dict()
        a = list()
        for TCS in root.iter('testcase'):
            Test_Case = TCS.get('name')
            for TC in TCS.iter():
                #print(TC.tag)
                for i in TC.itertext():
                    if TC.tag == 'node_order':
                        #node_order.append(i)
                        node_order = i
                    elif TC.tag == 'version':
                        #version.append(i)
                        version=  i
                    elif TC.tag == 'summary':
                        #summary.append(i)
                        summary = i
                    elif TC.tag == 'version':
                        #version.append(i)
                        version = i
                    elif TC.tag == 'preconditions':
                        #preconditions.append(i)
                        preconditions = i
                    elif TC.tag == 'execution_type':
                        #execution_type.append(i)
                        execution_type = i
                    elif TC.tag == 'importance':
                        #importance.append(i)
                        importance = i
                    elif TC.tag == 'estimated_exec_duration':
                        #estimated_exec_duration.append(i)
                        estimated_exec_duration = i
                    elif TC.tag == 'status':
                        #status.append(i)
                        status = i
                    elif TC.tag == 'steps':
                        #steps.append(i)
                        steps= i
                    elif TC.tag == 'requirements':
                        #requirements.append(i)
                        requirements = i
                    elif TC.tag == 'actions':
                        #actions.append(i)
                        actions = i
                    elif TC.tag == 'doc_id':
                        #doc_id.append(i)
                        doc_id = i
                    elif TC.tag == 'expectedresults':
                        #expectedresults.append(i)
                        expectedresults = i
                    elif TC.tag == 'req_spec_title':
                        #req_spec_title.append(i)
                        req_spec_title = i
                    elif TC.tag == 'title':
                        #title.append(i)
                        title = i
                    #print(i)
            try:
                a.append({'Test_Case':Test_Case,'node_order':node_order,'version':version,'summary':summary,'preconditions':preconditions,
                      'execution_type':execution_type,'importance':importance,'estimated_exec_duration':estimated_exec_duration,'status':status,
                      'steps':steps,'requirements':requirements,'actions':actions,'doc_id':doc_id,'expectedresults':expectedresults,'req_spec_title':req_spec_title,
                      'title':title})
            except NameError:
                pass
        df = pd.DataFrame(a)
        dfn = dfn.append(df)
dfn.to_excel('Final.xlsx',sheet_name= 'Sheet1')