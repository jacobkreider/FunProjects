#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 22:26:30 2019
Simple script for reading tabular text from a pdf
@author: jacobkreider
"""

from tabula import read_pdf

os.chdir('/home/jacob/DataScience/FunProjects/OCR/MedicalFormOCR')

file = 'exampleScan.pdf'

medForm = read_pdf(file)

medForm