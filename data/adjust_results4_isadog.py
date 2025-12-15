#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#                                                                             
# PROGRAMMER: David Lauricella
# DATE CREATED: 12/14/2025                                  
# REVISED DATE: 12/14/2025
# PURPOSE: Create a function adjust_results4_isadog that adjusts the results 
#          dictionary to indicate whether or not the pet image label is of-a-dog, 
#          and to indicate whether or not the classifier image label is of-a-dog.
#
##

def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to determine if classifier correctly 
    classified images 'as a dog' or 'not a dog'.
    """
    # Creates dognames dictionary for quick matching
    dognames_dic = dict()

    # Reads in dognames from file, 1 name per line & automatically closes file
    with open(dogfile, "r") as infile:
        # Reads in first line of file
        line = infile.readline()

        # Processes each line in file until reaching EOF (end-of-file)
        while line != "":
            # Process line by stripping newline character
            # THIS IS THE KEY FIX THAT WAS MISSING/BROKEN
            line = line.rstrip()

            # Adds dogname to dognames_dic if it doesn't already exist 
            if line not in dognames_dic:
                dognames_dic[line] = 1

            # Reads in next line in file to be processed with while loop
            line = infile.readline()

    # Iterates through the results dictionary to adjust tags
    for key in results_dic:
        
        pet_label_is_dog = 0
        classifier_label_is_dog = 0

        # Check if the Pet Image Label (index 0) is in dognames_dic
        if results_dic[key][0] in dognames_dic:
            pet_label_is_dog = 1
            
        # Check if the Classifier Label (index 1) is in dognames_dic
        if results_dic[key][1] in dognames_dic:
            classifier_label_is_dog = 1
            
        # Append these results to the dictionary entry
        results_dic[key].extend([pet_label_is_dog, classifier_label_is_dog])