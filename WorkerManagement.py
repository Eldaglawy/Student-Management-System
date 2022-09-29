from Student import  Student
from Worker import  Worker

OurWorkers = []

def add_worker(worker):
    OurWorkers.append(worker)

def find_worker_by_name(name):
    for worker in OurWorkers:
        if worker.getName() == name:
            return worker.description()
    return "Worker not found"


def find_worker_by_id(ID):
    for worker in OurWorkers:
        if worker.getID() == ID:
            return worker.description() 
    return "Worker not found"              


def sort_worker_by_name():
    OurWorkers = sorted(OurWorkers, key = lambda x:x.name) 

def sort_worker_by_id():
    OurWorkers = sorted(OurWorkers, key = lambda x:x.id)