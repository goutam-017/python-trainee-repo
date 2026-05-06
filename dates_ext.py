import re
import os
import json

folder_path=r"C:\Users\hp\Desktop\Python Training\raw"
pattern_date=[r"\d{1,2}\s*[/-]\s*\d{1,2}\s*[/-]\s*\d{4}",
              r"\d{4}\s*[/-]\s*\d{1,2}\s*[/-]\s*\d{1,2}"]

date_types = {
    "DOB": "Date of Birth",
    "DOS": "Date of Service",
    "Performed Date": "Performed Date",
    "Date of Study": "Study Date",
    "Date of Read": "Read Date",
    "Generated": "Generated Date",
    "signed": "Signed Date",
    "Onset": "Onset Date",
    "Appointment": "Appointment Date"
}

def get_files(folder_path):
    files=os.listdir(folder_path)
    files_list=[]
    for file in files:
        full_path=os.path.join(folder_path,file)
        if os.path.isfile(full_path):
            files_list.append(full_path)
    return files_list

def read_files(files_list):
    text_list=[]
    for file_path in files_list:
        with open(file_path,'r',encoding='utf-8') as f:
            text=f.read()
            text_list.append({
                "file_name": file_path,
                "text": text
            })
    return text_list

def ext_dates(text_list,pattern_date,date_types):
    results=[]
    for item in text_list:
        file_name=item["file_name"]
        text=item["text"]
        for p in pattern_date:
            for match in re.finditer(p,text):
                date=match.group()
                start=max(0, match.start() - 50)
                end=min(len(text), match.end() + 50)
                context=text[start:end]
                found_type="Unknown"
                for key, value in date_types.items():
                    if key.lower() in context.lower():
                        found_type=value
                        break

                results.append({
                    "file_name": os.path.basename(file_name),
                    "date": date,
                    "type": found_type
                })
    return results


def main(folder_path,pattern_date,date_types):
    f_list=get_files(folder_path)
    text_list=read_files(f_list)
    dates=ext_dates(text_list,pattern_date,date_types)
    all_dates=[]
    for d in dates:
        all_dates.append(d)
    os.makedirs("expected", exist_ok=True)
    with open("expected/final_entities.json", "w") as f:
        json.dump(all_dates, f, indent=4)
    print("JSON file saved successfully")

if __name__=="__main__":
    main(folder_path,pattern_date,date_types)
