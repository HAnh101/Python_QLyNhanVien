from typing import Union
from pydantic import BaseModel

class EmployeeBase(BaseModel):
    employeeName: str
    departmentId: int

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: int
    class Config:
        orm_mode = True

class ProjectBase(BaseModel):
    projectName: str
    projectStatus: str

class ProjectCreate(ProjectBase):
    pass

class ParticipateBase(BaseModel):
    employeeId: int
    projectId: int
    ParticipatePosition: str
    participateSalaryProject: int
    participateBonus: int
    participateFinalSalary: int

class ParticipateCreate(ParticipateBase):
    pass

class EmployeeParticipate(ParticipateBase):
    id: int
    class Config:
        orm_mode = True

class ParticipateProject(ParticipateBase):
    id: int
    class Config:
        orm_mode = True

class DepartmentBase(BaseModel):
    departmentName: str

class DepartmentCreate(DepartmentBase):
    pass

class DepartmentEmployee(DepartmentBase):
    id: int
    class Config:
        orm_mode = True

class Department(BaseModel):
    departmentName: str
    departmentid: int

class DepartmentAndProject(BaseModel):
    projectid: int
    class Config:
        orm_mode = True

class ParticipateSalary(BaseModel):
    employeeId : int
    projectId: int
    position: str
    salaryProject: int
    bonus: int

class EmployeeSalary(EmployeeBase):
    salary: int
    class Config:
        orm_mode = True

class ProjectSalary(ProjectBase):
    projectId: int
    class Config:
        orm_mode = True
