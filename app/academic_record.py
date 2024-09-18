# -*- coding: utf-8 -*-
"""
    academic_record.py: Deploying the Machine Learning Model using FastAPI
"""
__author__ = "Abdul Rahuman Aslam"
__version__ = "1.0"
__file__ = "academic_record.py"

# Importing the required packages
from typing import List
from pydantic import BaseModel

# Class with input paramaters for predicting placement result
class AcademicRecord(BaseModel):
    """
    Input parameters for predicting the placement result
    """

    gender: List[str]
    ssc_p: List[float]
    ssc_b: List[str]
    hsc_p: List[float]
    hsc_b: List[str]
    hsc_s: List[str]
    degree_p: List[float]
    degree_t: List[str]
    workex: List[str]
    etest_p: List[float]
    specialisation: List[str]
    mba_p: List[float]
