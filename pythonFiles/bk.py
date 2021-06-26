import json
from contextlib import suppress

class task:
    def GeneralHealth(json_object):
        new_object = {}
        

        a_file = open("mish.json", "r") 
        json_object = json.load(a_file)
        a_file.close()
        print(json_object)


        


            
        if "age" in json_object.keys():
            if json_object["age"] > 30:
                
                new_object["age"] = "High"
                
            else:
                new_object["age"] = "Low"
            

        if "Diabetes" in json_object.keys():
            if json_object["Diabetes"] == "Yes":
                new_object["Diabetes"] = "High"
            else:
                new_object["Diabetes"] = "Low"



        if "chemo_radiation_therapy" in json_object.keys():
            if json_object["chemo_radiation_therapy"] == "Yes":
                new_object["chemo_radiation_therapy"] = "High"
            else:
                new_object["chemo_radiation_therapy"] = "Low"





        if "Fluoride exposure" in json_object.keys():
            if json_object["Fluoride exposure"] == "Water" or "Supplements":
                new_object["Fluoride exposure"] = "High"
            else:
                json_object["Fluoride exposure"] = "Low"






        if "Special_healthcare_need" in json_object.keys():
            if json_object["Special_healthcare_need"] == "Physical" or "Mental":
                new_object["Special_healthcare_need"] = "High"
            else:
                new_object["Special_healthcare_need"] = "Low"









        if "medicine_that_reduce_salaiva" in json_object.keys():
            if json_object["medicine_that_reduce_salaiva"] == "Yes":
                new_object["medicine_that_reduce_salaiva"] = "High"
            else:
                new_object["medicine_that_reduce_salaiva"] = "Low"






        if "pregnancy_and_hormonal_changes" in json_object.keys():
            if json_object["pregnancy_and_hormonal_changes"] == "Yes":
                new_object["pregnancy_and_hormonal_changes"] = "High"
            else:
                new_object["pregnancy_and_hormonal_changes"] = "Low"





        if "Acid reflux" in json_object.keys():
            if json_object["Acid reflux"] == "Yes":
                new_object["Acid reflux"] = "High"
            else:
                new_object["Acid reflux"] = "Low"


        if "Drug/Alcohol" in json_object.keys():
            if json_object["Drug/Alcohol"] == "Yes":
                new_object["Drug/Alcohol"] = "Medium"
            else:
                new_object["Drug/Alcohol"] = "Low"



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


        
        print(new_object)


    def Habit(json_object):

        habits_object = {}

        a_file = open("mish.json", "r") 
        json_object = json.load(a_file)
        a_file.close()
        print(json_object)

        if "Sugary food and drinks" in json_object.keys():
            if json_object["Sugary food and drinks"] == "primarily at mealtimes":
                habits_object["Sugary food and drinks"] = "Low"
            else:
                habits_object["Sugary food and drinks"] = "High"



        if "Smoking and tobacco use" in json_object.keys():
            if json_object["Smoking and tobacco use"] == "No":
                habits_object["Smoking and tobacco use"] = "Low"
            else:
                habits_object["Smoking and tobacco use"] = "High"



        if "Toothbrushing" in json_object.keys():
            if json_object["Toothbrushing"] == "twice daily":
                habits_object["Toothbrushing"] = "Low"
            else:
                habits_object["Toothbrushing"] = "High"


        if "Flossing" in json_object.keys():
            if json_object["Flossing"] == "twice daily":
                habits_object["Flossing"] = "Low"
            else:
                habits_object["Flossing"] = "High"


        if "Mouthwash" in json_object.keys():
            if json_object["Mouthwash"] == "twice daily":
                habits_object["Mouthwash"] = "Low"
            else:
                habits_object["Mouthwash"] = "High"
        
        if "Replace toothbrush" in json_object.keys():
            if json_object["Replace toothbrush"] == "once in 3 months":
                habits_object["Replace toothbrush"] = "Low"
            else:
                habits_object["Replace toothbrush"] = "Medium"


        
        print(habits_object)

    def DentalCondtion(josn_object):
        new_dental = {}

        a_file = open("mish.json", "r") 
        json_object = json.load(a_file)
        a_file.close()
        print(json_object)

        if "Cavities or treatment for cavities in last 36 months" in json_object.keys():
            if json_object["Cavities or treatment for cavities in last 36 months"] == "nil":
                new_dental["Cavities or treatment for cavities in last 36 months"] = "Low"
            else:
                new_dental["Cavities or treatment for cavities in last 36 months"] = "Medium"



        if "Dental Scaling/Gum treatment done " in json_object.keys():
            if json_object[ "Dental Scaling/Gum treatment done "] == "within one year":
                new_dental[ "Dental Scaling/Gum treatment done "] = "Low"
            else:
                new_dental[ "Dental Scaling/Gum treatment done "] = "Medium"


        if "Braces/Aligner treatments currently" in json_object.keys():
            if json_object["Braces/Aligner treatments currently"] == "aligner":
                new_dental["Braces/Aligner treatments currently"] = "Medium"
            else:
                new_dental["Braces/Aligner treatments currently"] = "Low"


        if "Missing teeth due to cavities or gum problems in last 36 months" in json_object.keys():
            if json_object["Missing teeth due to cavities or gum problems in last 36 months"] == "no":
                new_dental["Missing teeth due to cavities or gum problems in last 36 months"] = "Low"
            else:
                new_dental["Missing teeth due to cavities or gum problems in last 36 months"] = "high"

        if "Crowns/fixed and removable tooth replacements done before 36 months" in json_object.keys():
            if json_object["Crowns/fixed and removable tooth replacements done before 36 months"] == "no":
                new_dental["Crowns/fixed and removable tooth replacements done before 36 months"] = "Low"
            else:
                new_dental["Crowns/fixed and removable tooth replacements done before 36 months"] = "high"


        if "unhealed mouth ulcer or swelling  currently" in json_object.keys():
            if json_object["unhealed mouth ulcer or swelling  currently"] ==  "10-14 days":
                new_dental["unhealed mouth ulcer or swelling  currently"] = "Low"
            else:
                new_dental["unhealed mouth ulcer or swelling  currently"] = "high"




        if "gum bleeding present currently" in json_object.keys():
            if json_object["gum bleeding present currently"] ==  "occasionally":
                new_dental["gum bleeding present currently"] = "Low"
            else:
                new_dental["gum bleeding present currently"] = "high"



        if "pain/sensitivity in any tooth currently" in json_object.keys():
            if json_object["pain/sensitivity in any tooth currently"] ==  "occasionally":
                new_dental["pain/sensitivity in any tooth currently"] = "Low"
            else:
                new_dental["pain/sensitivity in any tooth currently"] = "high"



        if "food getting stuck in teeth currently" in json_object.keys():
            if json_object["food getting stuck in teeth currently"] ==  "occasionally":
                new_dental["food getting stuck in teeth currently"] = "Low"
            else:
                new_dental["food getting stuck in teeth currently"] = "high"

        
        print(new_dental)


    def MedicalHealth(json_object):
        new_health = {}


        a_file = open("mish.json", "r") 
        json_object = json.load(a_file)
        a_file.close()
        print(json_object)


        if "Endocarditis and Cardiovascular disease" in json_object.keys():
            if json_object["Endocarditis and Cardiovascular disease"] ==  "good dental health":
                new_health["Endocarditis and Cardiovascular disease"] = "Low"
            else:
                new_health["Endocarditis and Cardiovascular disease"] = "High"



        if "Premature birth and low weight in children" in json_object.keys():
            if json_object["Premature birth and low weight in children"] == "good dental health":
                new_health["Premature birth and low weight in children"] = "Low"
            else:
                new_health["Premature birth and low weight in children"] = "High"



        if "Covid complications" in json_object.keys():
            if json_object["Covid complications"] == "good dental health":
                new_health["Covid complications"] = "Low"
            else:
                new_health["Covid complications"] = "High"



        if "Pneumonia" in json_object.keys():
            if json_object["Pneumonia"] == "good dental health":
                new_health["Pneumonia"] = "Low"
            else:
                new_health["Pneumonia"] = "High"



        if "skin problems" in json_object.keys():
            if json_object["skin problems"] == "good dental health":
                new_health["skin problems"] = "Low"
            else:
                new_health["skin problems"] = "High"


    
        print(new_health)




        

        



sample  = task()
sample.GeneralHealth()
sample.Habit()
sample.DentalCondtion()
sample.MedicalHealth()




















  



    










   
        










































