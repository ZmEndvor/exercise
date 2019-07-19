# -*- coding: utf-8 -*-
# 2019/04/02
# @Author: JeremyZ

import xml.etree.ElementTree as etree
import json

class JsonConnector:
    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode="r", encoding="utf-8") as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data

class XmlConnector:
    def __init__(self, filrpath):
        self.tree = etree.parse(filrpath)

    @property
    def parsed_data(self):
        return self.tree

def connection_factory(filepath):
    if filepath.endswith("json"):
        connector = JsonConnector
    elif filepath.endswith('xml'):
        connector = XmlConnector
    else:
        raise ValueError("Cannot connect to {}".format(filepath))
    return connector(filepath)

def connect_to(filepath):
    factory = None
    try:
        factory = connection_factory(filepath)
    except ValueError as ve:
        print(ve)
    return factory

def main():
    sqlite_factory = connect_to('example/person.sq3')
    print()

    xml_factory = connect_to('example/person.xml')
    xml_data = xml_factory.parsed_data
    liars = xml_data.findall(".//{}[{}='{}']".format('person', 'firstName', 'John'))
    print('found: {} person'.format(len(liars)))
    for liar in liars:
        print('first name: {}'.format(liar.find('firstName').text))
        print('last name: {}'.format(liar.find('lastName').text))
        [print('phone number ({})'.format(p.attrib['type']), p.text) for p in liar.find('phoneNumbers')]
    print()

    json_factory = connect_to('example/donut.json')
    json_data = json_factory.parsed_data
    print('found: {} donuts'.format(len(json_data)))
    for donut in json_data:
        print('name: {}'.format(donut['name']))
        print('price: ${}'.format(donut['ppu']))
        [print('topping: {} {}'.format(t['id'], t['type'])) for t in donut['topping']]

if __name__ == '__main__':
    main()



