from datetime import date, timedelta
import xml.etree.ElementTree as ET


# Method which takes two arguments and updates dept and return fields
def update_date(x, y):
    currentdate = date.today()

    dep_updated_date = currentdate + timedelta(days=x)
    dep_updated_date = dep_updated_date.strftime("%Y%m%d")
    print(dep_updated_date)

    ret_updated_date = currentdate + timedelta(days=y)
    ret_updated_date = ret_updated_date.strftime("%Y%m%d")
    print(ret_updated_date)

    mytree = ET.parse('Problem1/test_payload1.xml')
    myroot = mytree.getroot()

    for d in myroot.iter('DEPART'):
        d.text = dep_updated_date

    for d in myroot.iter('RETURN'):
        d.text = ret_updated_date

    mytree.write('output.xml')