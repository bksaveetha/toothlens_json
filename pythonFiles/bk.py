import json


json_object = {
    "Age": 30,
    "medcines that reduce salaiva" : "Yes",
    "medicine_that_reduce_salaiva": "Yes",
    "chemo_radiation_therapy": "Yes",
    "Fluoride exposure": "Yes",
    "Diabetes": "Yes(good control)",
    "pregnancy_and_hormonal_changes": "Yes",
    "Acid reflux": "Yes",
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
    "Dental Scaling/Gum treatment done": "within one year",
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
    "skin problems": "poor dental health"
}



def GeneralHealth(json_object):
    
    new_object = {}

    
    if "Age" in json_object.keys():
        if json_object["Age"] < 30:
            new_object["Age"] = "Low"

        elif json_object["Age"] > 60:
            new_object["Age"] = "High"
           
        else:
            new_object["Age"] = "Medium"


    if "medcines that reduce salaiva" in json_object.keys():
        if json_object["medcines that reduce salaiva"] == "Yes":
            new_object["medcines that reduce salaiva"] = "Medium"

        elif json_object["medcines that reduce salaiva"] == "Nil":
            new_object["medcines that reduce salaiva"]= "High"
        else:
            new_object["medcines that reduce salaiva"]= "Low"


    if "chemo_radiation_therapy" in json_object.keys():
        if json_object["chemo_radiation_therapy"] == "Yes":
            new_object["chemo_radiation_therapy"] = "High"
        elif json_object["chemo_radiation_therapy"] == "Nil":
            new_object["chemo_radiation_therapy"]= "High"
        else:
            new_object["chemo_radiation_therapy"] = "Low"
    
    
    
    if "pregnancy_and_hormonal_changes" in json_object.keys():
        if json_object["pregnancy_and_hormonal_changes"] == "Yes":
            new_object["pregnancy_and_hormonal_changes"] = "Medium"
        elif json_object["pregnancy_and_hormonal_changes"] == "Nil":
            new_object["pregnancy_and_hormonal_changes"]= "High"
        else:
            new_object["pregnancy_and_hormonal_changes"] = "Low"
        
        
        
        

    if "Diabetes" in json_object.keys():
        if json_object["Diabetes"] == "Yes(good control)":
            new_object["Diabetes"] = "Medium"
        elif json_object["Diabetes"] == "Yes(poor control)":
            new_object["Diabetes"]= "High"
        else:
            new_object["Diabetes"] = "Low"




    if "Acid reflux" in json_object.keys():
        if json_object["Acid reflux"] == "Yes":
            new_object["Acid reflux"] = "Medium"
        elif json_object["Acid reflux"] == "Nil":
            new_object["Acid reflux"]= "High"
        else:
            new_object["Acid reflux"] = "Low"


    
    if "Fluoride exposure" in json_object.keys():
        if json_object["Fluoride exposure"] == "Yes":
            new_object["Fluoride exposure"] = "Low"
        elif json_object["Fluoride exposure"] == "No":
            new_object["Fluoride exposure"]= "Medium"
        else:
            json_object["Fluoride exposure"] = "High"






    if "Special_healthcare_need" in json_object.keys():
        if json_object["Special_healthcare_need"] == "No":
            new_object["Special_healthcare_need"] = "Low"
        elif json_object["Special_healthcare_need"] == "Yes":
            new_object["Special_healthcare_need"]= "Medium"
        else:
            new_object["Special_healthcare_need"] = "High"



    if "Drug/Alcohol" in json_object.keys():
        if json_object["Drug/Alcohol"] == "No":
            new_object["Drug/Alcohol"] = "Low"
        elif json_object["Drug/Alcohol"] == "Yes":
            new_object["Drug/Alcohol"]= "Medium"
        else:
            new_object["Drug/Alcohol"] = "High"


    if "Family history of cavities and gum infections" in json_object.keys():
        if json_object["Family history of cavities and gum infections"] == "No":
            new_object["Family history of cavities and gum infections"] = "Low"
        elif json_object["Family history of cavities and gum infections"] == "Yes":
            new_object["Family history of cavities and gum infections"]= "Medium"
        else:
            new_object["Family history of cavities and gum infections"] = "High"

    if "osteroporosis in women" in json_object.keys():
        if json_object["osteroporosis in women"] == "No":
            new_object["osteroporosis in women"] = "Low"
        elif json_object["osteroporosis in women"] == "Yes":
            new_object["osteroporosis in women"]= "Medium"
        else:
            new_object["osteroporosis in women"] = "High"



    if "Daily drinking water consumption" in json_object.keys():
        if json_object["Daily drinking water consumption"] == "frequent in between meals":
            new_object["Daily drinking water consumption"] = "Low"
        elif json_object["Daily drinking water consumption"] == "at mealtimes only":
            new_object["Daily drinking water consumption"]= "Medium"
        else:
            new_object["Daily drinking water consumption"] = "High"


    
    




    

   

    if "Sugary food and drinks" in json_object.keys():
        if json_object["Sugary food and drinks"] == "primarily at mealtimes":
            new_object["Sugary food and drinks"] = "Low"
        elif json_object["Sugary food and drinks"] == "frequent in between meals":
            new_object["Sugary food and drinks"]= "High"
        else:
            new_object["Sugary food and drinks"] = "Medium"



    if "Smoking and tobacco use" in json_object.keys():
        if json_object["Smoking and tobacco use"] == "No":
            new_object["Smoking and tobacco use"] = "Low"
        elif json_object["Smoking and tobacco use"] == "Yes":
            new_object["Smoking and tobacco use"]= "High"
        else:
            new_object["Smoking and tobacco use"] = "Medium"



    if "Toothbrushing" in json_object.keys():
        if json_object["Toothbrushing"] == "twice daily":
            new_object["Toothbrushing"] = "Low"
        elif json_object["Toothbrushing"] == "once daily":
            new_object["Toothbrushing"]= "High"
        else:
            new_object["Toothbrushing"] = "Medium"


    if "Flossing" in json_object.keys():
        if json_object["Flossing"] == "twice daily":
            new_object["Flossing"] = "Low"
        elif json_object["Flossing"] == "once daily":
            new_object["Flossing"]= "Medium"
        else:
            new_object["Flossing"] = "High"


    if "Mouthwash" in json_object.keys():
        if json_object["Mouthwash"] == "twice daily":
            new_object["Mouthwash"] = "Low"
        elif json_object["Mouthwash"] == "once daily":
            new_object["Mouthwash"]= "Medium"
        else:
            new_object["Mouthwash"] = "High"
    
    if "Replace toothbrush" in json_object.keys():
        if json_object["Replace toothbrush"] == "once in 3 months":
            new_object["Replace toothbrush"] = "Low"
        elif json_object["Replace toothbrush"] == "3-6 months":
            new_object["Replace toothbrush"]= "Medium"
        else:
            new_object["Replace toothbrush"] = "High"


    
    

    

    if "Cavities or treatment for cavities in last 36 months" in json_object.keys():
        if json_object["Cavities or treatment for cavities in last 36 months"] == "more then 3 cavities":
            new_object["Cavities or treatment for cavities in last 36 months"] = "High"
        elif json_object["Cavities or treatment for cavities in last 36 months"] == "less than 3 cavities":
            new_object["Cavities or treatment for cavities in last 36 months"]= "Medium"
        else:
            new_object["Cavities or treatment for cavities in last 36 months"] = "Low"



    if "Dental Scaling/Gum treatment done " in json_object.keys():
        if json_object["Dental Scaling/Gum treatment done"] == "within one year":
            new_object["Dental Scaling/Gum treatment done"] = "Low"
        elif json_object["Dental Scaling/Gum treatment done"] == "more than a year":
            new_object["Dental Scaling/Gum treatment done"]= "High"
        else:
            new_object[ "Dental Scaling/Gum treatment done "] = "Medium"


    if "Braces/Aligner treatments currently" in json_object.keys():
        if json_object["Braces/Aligner treatments currently"] == "aligner":
            new_object["Braces/Aligner treatments currently"] = "Medium"
        elif json_object["Braces/Aligner treatments currently"] == "braces":
            new_object["Braces/Aligner treatments currently"]= "High"
        else:
            new_object["Braces/Aligner treatments currently"] = "Low"


    if "Missing teeth due to cavities or gum problems in last 36 months" in json_object.keys():
        if json_object["Missing teeth due to cavities or gum problems in last 36 months"] == "No":
           new_object["Missing teeth due to cavities or gum problems in last 36 months"] = "Low"
        elif json_object["Missing teeth due to cavities or gum problems in last 36 months"] == "Yes":
            new_object["Missing teeth due to cavities or gum problems in last 36 months"]= "Medium"
        else:
            new_object["Missing teeth due to cavities or gum problems in last 36 months"] = "High"

    if "Crowns/fixed and removable tooth replacements done before 36 months" in json_object.keys():
        if json_object["Crowns/fixed and removable tooth replacements done before 36 months"] == "No":
            new_object["Crowns/fixed and removable tooth replacements done before 36 months"] = "Low"
        elif json_object["Crowns/fixed and removable tooth replacements done before 36 months"] == "Yes":
            new_object["Crowns/fixed and removable tooth replacements done before 36 months"]= "Medium"
        else:
            new_object["Crowns/fixed and removable tooth replacements done before 36 months"] = "High"


    if "unhealed mouth ulcer or swelling  currently" in json_object.keys():
        if json_object["unhealed mouth ulcer or swelling  currently"] ==  "10-14 days":
           new_object["unhealed mouth ulcer or swelling  currently"] = "Low"
        elif json_object["unhealed mouth ulcer or swelling  currently"] == "14 days-1 month":
            new_object["unhealed mouth ulcer or swelling  currently"]= "Medium"
        elif json_object["unhealed mouth ulcer or swelling  currently"] == "more than a month":
            new_object["unhealed mouth ulcer or swelling  currently"]= "High"
        else:
            new_object["unhealed mouth ulcer or swelling  currently"] = "Nil"




    if "gum bleeding present currently" in json_object.keys():
        if json_object["gum bleeding present currently"] ==  "occasionally":
            new_object["gum bleeding present currently"] = "Low"
        elif json_object["gum bleeding present currently"] == "regularly":
            new_object["gum bleeding present currently"]= "High"
        else:
            new_object["gum bleeding present currently"] = "Medium"



    if "pain/sensitivity in any tooth currently" in json_object.keys():
        if json_object["pain/sensitivity in any tooth currently"] ==  "occasionally":
            new_object["pain/sensitivity in any tooth currently"] = "Low"
        elif json_object["pain/sensitivity in any tooth currently"] == "regularly":
            new_object["pain/sensitivity in any tooth currently"]= "High"
        else:
            new_object["pain/sensitivity in any tooth currently"] = "Medium"



    if "food getting stuck in teeth currently" in json_object.keys():
        if json_object["food getting stuck in teeth currently"] ==  "occasionally":
            new_object["food getting stuck in teeth currently"] = "Low"
        elif json_object["food getting stuck in teeth currently"] == "regularly":
            new_object["food getting stuck in teeth currently"]= "High"
        else:
            new_object["food getting stuck in teeth currently"] = "Medium"

    
    


    


    if "Endocarditis and Cardiovascular disease" in json_object.keys():
        if json_object["Endocarditis and Cardiovascular disease"] ==  "good dental health":
           new_object["Endocarditis and Cardiovascular disease"] = "Low"
        elif json_object["Endocarditis and Cardiovascular disease"] == "poor dental health":
            new_object["Endocarditis and Cardiovascular disease"]= "Medium"
        else:
            new_object["Endocarditis and Cardiovascular disease"] = "High"



    if "Premature birth and low weight in children" in json_object.keys():
        if json_object["Premature birth and low weight in children"] == "good dental health":
            new_object["Premature birth and low weight in children"] = "Low"
        elif json_object["Premature birth and low weight in children"] == "poor dental health":
            new_object["Premature birth and low weight in children"]= "Medium"
        else:
            new_object["Premature birth and low weight in children"] = "High"



    if "Covid complications" in json_object.keys():
        if json_object["Covid complications"] == "good dental health":
            new_object["Covid complications"] = "Low"
        elif json_object["Covid complications"] == "poor dental health":
            new_object["Covid complications"]= "Medium"
        else:
            new_object["Covid complications"] = "High"



    if "Pneumonia" in json_object.keys():
        if json_object["Pneumonia"] == "good dental health":
            new_object["Pneumonia"] = "Low"
        elif json_object["Pneumonia"] == "poor dental health":
            new_object["Pneumonia"]= "Medium"
        
        else:
            new_object["Pneumonia"] = "High"



    if "skin problems" in json_object.keys():
        if json_object["skin problems"] == "good dental health":
            new_object["skin problems"] = "Low"
        elif json_object["skin problems"] == "poor dental health":
            new_object["skin problems"]= "Medium"
        else:
            new_object["skin problems"] = "High"


    print(new_object)
print(GeneralHealth(json_object))




sheet_object = {"Brushing-normal toothbrush": "recommend to brush for 2 minutes in morning and night",
"Brushing-power toothbrush" :"recommend to brush for 2 minutes in morning and night",
"Regular floss": "once a day",
"Waterfloss": "2-3 times a  week",
"Antibacterial rinse" : "twice a day for severe cavities/gum infection and bad breadth",
"Sugary food/drinks": "at meal times only",
"Drinking plain water":"multiple times a day",
"Rinsing of mouth with water": "multiple times a day",
"Change of toothbrush": "3 months back",
"Smoking": "daily",
"Dental Visit": "within last 6 months",
"Medical issue": "Good control",
"Toothlens check": "once per week"
}


def DailyDentalHealth(sheet_object):
    Dental_object = {}




    if "Brushing-normal toothbrush" in sheet_object.keys():
        if sheet_object["Brushing-normal toothbrush"] == "recommend to brush for 2 minutes in morning and night":
            Dental_object["Brushing-normal toothbrush"] = 1
        else:
            Dental_object["Brushing-normal toothbrush"] = 0




    if "Brushing-power toothbrush" in sheet_object.keys():
        if sheet_object["Brushing-power toothbrush"] == "recommend to brush for 2 minutes in morning and night":
            Dental_object["Brushing-power toothbrush"] = 2
        else:
            Dental_object["Brushing-power toothbrush"] = 0


    if "Regular floss" in sheet_object.keys():
        if sheet_object["Regular floss"] == "once a day":
            Dental_object["Regular floss"] = 1
        else:
            Dental_object["Regular floss"] = 0

    if "Waterfloss" in sheet_object.keys():
        if sheet_object["Waterfloss"] == "2-3 times a  week":
            Dental_object["Waterfloss"] = 2
        else:
            Dental_object["Waterfloss"] = 0



    if "Antibacterial rinse" in sheet_object.keys():
        if sheet_object["Antibacterial rinse"] == "twice a day for severe cavities/gum infection and bad breadth":
            Dental_object["Antibacterial rinse"] = 1
        else:
            Dental_object["Antibacterial rinse"] = 0



    if "Sugary food/drinks" in sheet_object.keys():
        if sheet_object["Sugary food/drinks"] == "at meal times only":
            Dental_object["Sugary food/drinks"] = 2
        else:
            Dental_object["Sugary food/drinks"] = 0



    if "Drinking plain water" in sheet_object.keys():
        if sheet_object["Drinking plain water"] == "multiple times a day":
            Dental_object["Drinking plain water"] = 2
        else:
            Dental_object["Drinking plain water"] = 0



    if "Rinsing of mouth with water" in sheet_object.keys():
        if sheet_object["Rinsing of mouth with water"] == "multiple times a day":
            Dental_object["Rinsing of mouth with water"] = 2
        else:
            Dental_object["Rinsing of mouth with water"] = 0
    



    if "Change of toothbrush" in sheet_object.keys():
        if sheet_object["Change of toothbrush"] == "3 months back":
            Dental_object["Change of toothbrush"] = 2
        elif sheet_object["Change of toothbrush"] == "6 months back":
            Dental_object["Change of toothbrush"] = 1
        else:
            Dental_object["Change of toothbrush"] = 0




    if "Smoking" in sheet_object.keys():
        if sheet_object["Smoking"] == "daily":
            Dental_object["Smoking"] = -2
        if sheet_object["Smoking"] == "a few times in a week":
            Dental_object["Smoking"] = 2
        else:
            Dental_object["Smoking"] = 0



    if "Dental Visit" in sheet_object.keys():
        if sheet_object["Dental Visit"] == "within last 6 months":
            Dental_object["Dental Visit"] = 2
        elif sheet_object["Dental Visit"] == "one year back":
            Dental_object["Dental Visit"] = 1
        elif sheet_object["Dental Visit"] == "more than a year":
            Dental_object["Dental Visit"] = -1
        else:
            Dental_object["Dental Visit"] = 0


    if "Medical issue" in sheet_object.keys():
        if sheet_object["Medical issue"] == "Good control":
            Dental_object["Medical issue"] = 5
        elif sheet_object["Medical issue"] == "Moderate control":
            Dental_object["Medical issue"] = 3
        elif sheet_object["Medical issue"] == "Poor control":
            Dental_object["Medical issue"] = -1
        else:
            Dental_object["Medical issue"] = 0


    if "Toothlens check" in sheet_object.keys():
        if sheet_object["Toothlens check"] == "once per week":
            Dental_object["Toothlens check"] = 5
        elif sheet_object["Toothlens check"] == "once every 14 days":
            Dental_object["Toothlens check"] = 4
        elif sheet_object["Toothlens check"] == "once every month":
            Dental_object["Toothlens check"] = 3

        else:
            Dental_object["Toothlens check"] = 0

    print(Dental_object)
print(DailyDentalHealth(sheet_object))


    
    
    

    



    






    

    























  



    










   
        










































