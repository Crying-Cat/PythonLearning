import xml.dom.minidom

#读取xml文件
dom =xml.dom.minidom.parse('data.xml')
group = dom.documentElement
persons = group.getElementsByTagName('person')

#遍历查找元素
for person in persons:
    print("-----------------")
    print(f"id:{person.getAttribute('id')}")
    nameE = person.getElementsByTagName('name')
    sexE = person.getElementsByTagName('sex')
    print(f"name: {nameE[0].childNodes[0].nodeValue}")
    print(f"sexE: {sexE[0].childNodes[0].nodeValue}")

#修改元素
persons[1].setAttribute('id','13')
persons[1].setAttribute('id1','113')
persons[1].getElementsByTagName('name')[0].childNodes[0].nodeValue = 'newname'

#添加元素
name = dom.createElement('name')
name.appendChild(dom.createTextNode('new people'))
sex = dom.createElement('sex')
sex.appendChild(dom.createTextNode('unknow'))
newpeople = dom.createElement('people')
newpeople.appendChild(name)
newpeople.appendChild(sex)
group.appendChild(newpeople)

#保存文件
dom.writexml(open('data1.xml','w'))


