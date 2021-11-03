import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
import calendar
import time

#First and last slot numbers
first_slot_number=1
last_slot_number=4

#Add Slot numbers to the list of slots
def addSlotNumbers(start,end,slot_list):
    for i in range(start,end+1):
        slot_list.append(i)


#Checks the free slots in the database
def checkFreeSlot(slot_list,db):
    for slot in slot_list:
        slot_info=db.collection('car').document(str(slot)).get().to_dict()
        if slot_info['ASSIGNED']==False:
            return slot
    return -1        


#Gets the registration number from car 
def getREG_NO():
    pass

#Assign a car a slot by editing REGISTRATION NUMBER of the car to the slot in firestore
def assignParkingSlot(REG_NO,db,slot_list):
    free_slot_no=checkFreeSlot(slot_list,db)
    pass


#Clear all the slots in the firestore and set the values to default values 
def clearAllSlots(slot_list,db):
    gmt=time.gmtime()
    ts=calendar.timegm(gmt)
    
    for i in slot_list:
        slot=db.collection('car').document(str(i))
        slot.set({
            'ASSIGNED':False,
            'EMPTY':True,
            'REG_NO':'',
            'TIME_IN':firestore.firestore.SERVER_TIMESTAMP,
            'TIME_OUT':-1  
        })  



if __name__=="__main__":
    cred = credentials.Certificate('smartparkingsystem-5ffb7-2f4717e68ead.json')
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    slot_list=[]
    addSlotNumbers(first_slot_number,last_slot_number,slot_list)
    #print(checkFreeSlot(slot_list,db))

    clearAllSlots(slot_list,db)
