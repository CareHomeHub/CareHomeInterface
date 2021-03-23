import json
# -*- coding: utf-8 -*-
"""Example Google style docstrings.

This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

Example:
    Examples can be given using either the ``Example`` or ``Examples``
    sections. Sections support any reStructuredText formatting, including
    literal blocks::

        $ python example_google.py

Section breaks are created by resuming unindented text. Section breaks
are also implicitly created anytime a new section starts.

Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

        Either form is acceptable, but the two should not be mixed. Choose
        one convention to document module level variables and be consistent
        with it.

Todo:
    * For module TODOs
    * You have to also use ``sphinx.ext.todo`` extension

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""


# import logging

def findByRef(ref="", dataset=[]):
    """Summary or Description of the Function

    Parameters:
    argument1 (int): Description of arg1

    Returns:
    int:Returning value

   """
    
    if ref=="":
        # logger.info("No Reference Supplied to findByRef function")
        return {"result":  "error1"}
    if (dataset==[]):
        # logger.info("No Dataset Supplied to findByRef function")
        return {"result":  "error2"}
    
    if ref in dataset:
        return {"result":  "IN"}
    else:
        return {"result":  "OUT"}
    
   
ans = findByRef(4, [1,2,3,4]) 
print(f"{ans['result']}")

ans = findByRef(5, [1,2,3,4]) 
print(f"{ans['result']}")


with open('mocks/CQC_data.json') as f: 
    cqc_data = json.load(f)


def getSpecialisms(cqc_data):
    cnt = 0
    count = len(cqc_data)
    print(count)
    for element in cqc_data:
        cnt += 1
        # print(f"cqc_data ratings: {element['loc']}\n")
        # print(f"cqc_data ratings overall: {element['loc']['currentRatings']['overall']}\n\n\n")
        # ratings = element['loc']
        print(f"cnt = {cnt}")
        if 'currentRatings' in element['loc']:
            print(f"cqc_data ratings overall: {element['loc']['currentRatings']['overall']}\n\n\n")
        else:
            print(f"currentRatings missing")
            print(f"cqc_data ratings overall: {element['loc']}")
    
    
    print(f"\n\n\nlast record :\n\n {cqc_data[-1]['loc']}")        
            
            
            
            
getSpecialisms(cqc_data)
    
    


