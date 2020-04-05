#!/usr/bin/env python
# coding: utf-8

# In[19]:


import sqlite3 as lite
import sys


# In[20]:


con = None


# In[21]:


try:
    con = lite.connect('pets.db')
    con.row_factory = lite.Row

    while True:
        PickPerson = raw_input('Please select an ID number: ')

        if PickPerson == '-1':
            sys.exit()
        else:
            try:
                PickPerson = int(PickPerson)
            except:
                print ("Error, please input a number")
                continue

        cur = con.cursor()
        cur.execute("SELECT * FROM person WHERE id =?", [(PickPerson)])
        row = cur.fetchone()

        if row == None:
            print ('Not a valid ID number. Pick again.')
            continue

        print (row['first_name'] + ' ' + row['last_name'] + ' is ' + str(
            row['age']) + ' years old.')


# In[22]:


for row in con.execute(
            "SELECT * FROM person_pet WHERE person_id =?", [(PickPerson)]):

            for name in con.execute(
                "SELECT * FROM person WHERE id =?", [(pickPerson)]):
                owner = name['first_name'] + ' ' + name['last_name']

            for petrow in con.execute(
                "SELECT * FROM pet WHERE id =?", [(row['pet_id'])]):

                if petrow['dead'] == 0:
                    print ('- ' + owner + ' owns ' + petrow[
                        'name'] + ', a ' + petrow['breed'] + ' who is ' + str(
                            petrow['age']) + ' years old.')
                else:
                    print ('- ' + owner + ' owned ' + petrow[
                        'name'] + ', a ' + petrow['breed'] + ' who was ' + str(
                            petrow['age']) + ' years old.')


# In[24]:


except lite.Error as e:
    print ("Closing.")
    print ("Error: %s " % e.args[0])
    sys.exit(1)

finally:
    if con:
        con.close()

