#!/usr/bin/python3
"""
Module that defines a class called Base
"""
import json


class Base:
    """
    The Base class for all other objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Instantiation of base instance

        Attributes:
            id (int): id number for base

        Returns:
        None
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns a JSON string representation of list_dictionaries

        Args:
            list_dictionaries ([]): a list of dictionaries
        """
        if not list_dictionaries or list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes JSON string represenatation of list_objs
        """
        with open('{}.json'.format(cls.__name__),
                  'w', encoding='utf-8') as a_file:
            ob_list = []
            if len(list_objs) == 0 or list_objs is None:
                ob_list = []
            else:
                for idx in list_objs:
                    ob_list.append(idx.to_dictionary())
            ob_str = cls.to_json_string(ob_list)
            a_file.write(ob_str)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns a JSON string representation in a list

        Args:
            json_string(str): String that contains a list of dictionaries
        """
        if json_string:
            return json.loads(json_string)
        return []

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes set

        Args:
            dictionary (**dict...): pointer to a dictionary
        """
        from models.rectangle import Rectangle
        from models.square import Square

        if cls.__name__ is 'Rectangle':
            newBlok = Rectangle(1, 1)
            newBlok.update(**dictionary)
            return newBlok
        if cls.__name__ is 'Square':
            newBlok = Square(1)
            newBlok.update(**dictionary)
            return newBlok

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances

        Args:
            cls: class currently using method
        """
        instList = []
        try:
            with open(cls.__name__ + '.json', 'r', encoding='utf-8') as a_file:
                newList = json.dumps(json.load(a_file))
        except FileNotFoundError:
            return instList
        list_dictionaries = cls.from_json_string(newList)
        for dic in list_dictionaries:
            instList.append(cls.create(**dic))
        return instList
