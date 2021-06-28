import json


json_object = {
    "Age": 35,
    "medicine_that_reduce_salaiva": "Yes",
    "chemo_radiation_therapy": "Yes",
    "Diabetes": "Yes",
    "pregnancy_and_hormonal_changes": "Yes",
    "Acid reflux": "Yes",
    "Fluoride exposure": "Yes",
    "Special_healthcare_need": "No",
    "Drug/Alcohol": "No",
    "Family history of cavities and gum infections": "Yes",
    "osteroporosis in women": "Yes",

    "Daily drinking water consumption": "at mealtimes only",


    "Sugary food and drinks": "primarily at mealtimes",
    "Smoking and tobacco use": "No",
    "Toothbrushing": "twice daily",
    "Flossing": "twice daily",
    "Mouthwash": "twice daily",
    "Replace toothbrush": "once in 3 months",









    "Cavities or treatment for cavities in last 36 months": "more then 3 cavities",
    "Dental Scaling/Gum treatment done ": "within one year",
    "Braces/Aligner treatments currently": "aligner",
    "Missing teeth due to cavities or gum problems in last 36 months": "no",
    "Crowns/fixed and removable tooth replacements done before 36 months": "no",
    "unhealed mouth ulcer or swelling  currently": "10-14 days",
    "gum bleeding present currently": "occasionally",
    "pain/sensitivity in any tooth currently": "occasionally",
    "food getting stuck in teeth currently": "occasionally",








    "Endocarditis and Cardiovascular disease": "good dental health",
    "Premature birth and low weight in children": "good dental health",
    "Covid complications": "good dental health",
    "Pneumonia": "good dental health",
    "skin problems": "good dental health"
}



def GeneralHealth(json_object):
    
    new_object = {}

    
    if "Age" in json_object.keys():
        if json_object["Age"] < 30:
            new_object["Age"] = "Low"
            
        else:
            new_object["Age"] = "Medium"
        
        
        
        

    if "Diabetes" in json_object.keys():
        if json_object["Diabetes"] == "Yes":
            new_object["Diabetes"] = "Medium"
        else:
            new_object["Diabetes"] = "Low"



    if "chemo_radiation_therapy" in json_object.keys():
        if json_object["chemo_radiation_therapy"] == "Yes":
            new_object["chemo_radiation_therapy"] = "High"
        else:
            new_object["chemo_radiation_therapy"] = "Low or Medium"

    
   






    if "Fluoride exposure" in json_object.keys():
        if json_object["Fluoride exposure"] == "Yes":
            new_object["Fluoride exposure"] = "Low"
        else:
            json_object["Fluoride exposure"] = "Medium"






    if "Special_healthcare_need" in json_object.keys():
        if json_object["Special_healthcare_need"] == "No":
            new_object["Special_healthcare_need"] = "Low"
        else:
            new_object["Special_healthcare_need"] = "Medium"









    if "medicine_that_reduce_salaiva" in json_object.keys():
        if json_object["medicine_that_reduce_salaiva"] == "Yes":
            new_object["medicine_that_reduce_salaiva"] = "Medium"
        else:
            new_object["medicine_that_reduce_salaiva"] = "Low"






    if "pregnancy_and_hormonal_changes" in json_object.keys():
        if json_object["pregnancy_and_hormonal_changes"] == "Yes":
            new_object["pregnancy_and_hormonal_changes"] = "Medium"
        else:
            new_object["pregnancy_and_hormonal_changes"] = "Low"





    if "Acid reflux" in json_object.keys():
        if json_object["Acid reflux"] == "No":
            new_object["Acid reflux"] = "Low"
        else:
            new_object["Acid reflux"] = "Medium"


    if "Drug/Alcohol" in json_object.keys():
        if json_object["Drug/Alcohol"] == "No":
            new_object["Drug/Alcohol"] = "Low"
        else:
            new_object["Drug/Alcohol"] = "Medium"



    if "Family history of cavities and gum infections" in json_object.keys():
        if json_object["Family history of cavities and gum infections"] == "Yes":
            new_object["Family history of cavities and gum infections"] = "Medium"
        else:
            new_object["Family history of cavities and gum infections"] = "Low"

    if "osteroporosis in women" in json_object.keys():
        if json_object["osteroporosis in women"] == "Yes":
            new_object["osteroporosis in women"] = "Medium"
        else:
            new_object["osteroporosis in women"] = "Low"



    if "Daily drinking water consumption" in json_object.keys():
        if json_object["Daily drinking water consumption"] == "at mealtimes only":
            new_object["Daily drinking water consumption"] = "Medium"
        else:
            new_object["Daily drinking water consumption"] = "Low"


    
    




    

   

    if "Sugary food and drinks" in json_object.keys():
        if json_object["Sugary food and drinks"] == "primarily at mealtimes":
            new_object["Sugary food and drinks"] = "Low"
        else:
            new_object["Sugary food and drinks"] = "High"



    if "Smoking and tobacco use" in json_object.keys():
        if json_object["Smoking and tobacco use"] == "No":
            new_object["Smoking and tobacco use"] = "Low"
        else:
            new_object["Smoking and tobacco use"] = "High"



    if "Toothbrushing" in json_object.keys():
        if json_object["Toothbrushing"] == "twice daily":
            new_object["Toothbrushing"] = "Low"
        else:
            new_object["Toothbrushing"] = "High"


    if "Flossing" in json_object.keys():
        if json_object["Flossing"] == "twice daily":
            new_object["Flossing"] = "Low"
        else:
            new_object["Flossing"] = "High"


    if "Mouthwash" in json_object.keys():
        if json_object["Mouthwash"] == "twice daily":
            new_object["Mouthwash"] = "Low"
        else:
            new_object["Mouthwash"] = "High"
    
    if "Replace toothbrush" in json_object.keys():
        if json_object["Replace toothbrush"] == "once in 3 months":
            new_object["Replace toothbrush"] = "Low"
        else:
            new_object["Replace toothbrush"] = "Medium"


    
    

    

    if "Cavities or treatment for cavities in last 36 months" in json_object.keys():
        if json_object["Cavities or treatment for cavities in last 36 months"] == "more then 3 cavities":
            new_object["Cavities or treatment for cavities in last 36 months"] = "High"
        else:
            new_object["Cavities or treatment for cavities in last 36 months"] = "Medium"



    if "Dental Scaling/Gum treatment done " in json_object.keys():
        if json_object[ "Dental Scaling/Gum treatment done "] == "within one year":
            new_object[ "Dental Scaling/Gum treatment done "] = "Low"
        else:
            new_object[ "Dental Scaling/Gum treatment done "] = "Medium"


    if "Braces/Aligner treatments currently" in json_object.keys():
        if json_object["Braces/Aligner treatments currently"] == "aligner":
            new_object["Braces/Aligner treatments currently"] = "Medium"
        else:
            new_object["Braces/Aligner treatments currently"] = "Low"


    if "Missing teeth due to cavities or gum problems in last 36 months" in json_object.keys():
        if json_object["Missing teeth due to cavities or gum problems in last 36 months"] == "no":
           new_object["Missing teeth due to cavities or gum problems in last 36 months"] = "Low"
        else:
            new_object["Missing teeth due to cavities or gum problems in last 36 months"] = "high"

    if "Crowns/fixed and removable tooth replacements done before 36 months" in json_object.keys():
        if json_object["Crowns/fixed and removable tooth replacements done before 36 months"] == "no":
            new_object["Crowns/fixed and removable tooth replacements done before 36 months"] = "Low"
        else:
            new_object["Crowns/fixed and removable tooth replacements done before 36 months"] = "high"


    if "unhealed mouth ulcer or swelling  currently" in json_object.keys():
        if json_object["unhealed mouth ulcer or swelling  currently"] ==  "10-14 days":
           new_object["unhealed mouth ulcer or swelling  currently"] = "Low"
        else:
            new_object["unhealed mouth ulcer or swelling  currently"] = "High"




    if "gum bleeding present currently" in json_object.keys():
        if json_object["gum bleeding present currently"] ==  "occasionally":
            new_object["gum bleeding present currently"] = "Low"
        else:
            new_object["gum bleeding present currently"] = "High"



    if "pain/sensitivity in any tooth currently" in json_object.keys():
        if json_object["pain/sensitivity in any tooth currently"] ==  "occasionally":
            new_object["pain/sensitivity in any tooth currently"] = "Low"
        else:
            new_object["pain/sensitivity in any tooth currently"] = "High"



    if "food getting stuck in teeth currently" in json_object.keys():
        if json_object["food getting stuck in teeth currently"] ==  "occasionally":
            new_object["food getting stuck in teeth currently"] = "Low"
        else:
            new_object["food getting stuck in teeth currently"] = "High"

    
    


    


    if "Endocarditis and Cardiovascular disease" in json_object.keys():
        if json_object["Endocarditis and Cardiovascular disease"] ==  "good dental health":
           new_object["Endocarditis and Cardiovascular disease"] = "Low"
        else:
            new_object["Endocarditis and Cardiovascular disease"] = "Medium"



    if "Premature birth and low weight in children" in json_object.keys():
        if json_object["Premature birth and low weight in children"] == "good dental health":
            new_object["Premature birth and low weight in children"] = "Low"
        else:
            new_object["Premature birth and low weight in children"] = "Medium"



    if "Covid complications" in json_object.keys():
        if json_object["Covid complications"] == "good dental health":
            new_object["Covid complications"] = "Low"
        else:
            new_object["Covid complications"] = "Medium"



    if "Pneumonia" in json_object.keys():
        if json_object["Pneumonia"] == "good dental health":
            new_object["Pneumonia"] = "Low"
        else:
            new_object["Pneumonia"] = "Medium"



    if "skin problems" in json_object.keys():
        if json_object["skin problems"] == "good dental health":
            new_object["skin problems"] = "Low"
        else:
            new_object["skin problems"] = "Medium"


    print(new_object)
print(GeneralHealth(json_object))
    


    
    
    

    



    






    

    























  



    










   
        










































