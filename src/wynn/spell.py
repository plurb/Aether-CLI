"""
Created on 2023-12-16

This file contains the Spell class.

@author: plurb
"""


class Spell(object):
    def __init__(self,
                 name: str,
                 level: int,
                 school: str,
                 components: list,
                 duration: str,
                 flavor: str,
                 description: str,
                 classes: list) -> None:
        self.name = name
        self.level = level
        self.school = school
        self.components = components
        self.duration = duration
        self.flavor = flavor
        self.description = description
        self.classes = classes

        self.conc = 'C' in components

    def as_markdown(self):
        return f'### {self.name}'
        pass

    def as_json(self):
        pass

    def as_html(self):
        pass