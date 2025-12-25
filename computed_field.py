from pydantic import BaseModel,EmailStr,computed_field
from typing import List,Dict

class Patient(BaseModel):
    name:str
    email:EmailStr
    age:int
    weight:float
    height:float
    married:bool
    allergies:List[str]
    contact_details:Dict[str,str]

    @computed_field
    @property
    def bmi(self)->float:
        bmi=round(self.weight/(self.height**2),2)
        return bmi
    
def updated_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('BMI',patient.bmi)
    print('updated')

patient_info={'name':'prathvika','email':'abc@gmail.com','age':'65','weight':75.2,'height':1.72,'married':True,'allergies':['pollen','dust'],'contact_details':{'phone':'123345','emergency':'439894388'}}
patient1=Patient(**patient_info)
updated_patient_data(patient1)