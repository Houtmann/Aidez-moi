import sqlite3
import datetime
import random

s_nouns = ["A dude", "My mom", "The king", "Some guy", "A cat with rabies", "A sloth", "Your homie", "This cool guy my gardener met yesterday", "Superman"]
p_nouns = ["These dudes", "Both of my moms", "All the kings of the world", "Some guys", "All of a cattery's cats", "The multitude of sloths living under your bed", "Your homies", "Like, these, like, all these people", "Supermen"]
s_verbs = ["eats", "kicks", "gives", "treats", "meets with", "creates", "hacks", "configures", "spies on", "retards", "meows on", "flees from", "tries to automate", "explodes"]
p_verbs = ["eat", "kick", "give", "treat", "meet with", "create", "hack", "configure", "spy on", "retard", "meow on", "flee from", "try to automate", "explode"]
infinitives = ["to make a pie.", "for no apparent reason.", "because the sky is green.", "for a disease.", "to be able to make toast explode.", "to know more about archeology."]

def sing_sen_maker():
    '''Makes a random senctence from the different parts of speech. Uses a SINGULAR subject'''
    
    return(random.choice(s_nouns) + random.choice(s_verbs)+ random.choice(s_nouns).lower() or random.choice(p_nouns).lower() + random.choice(infinitives))

status = ['OPEN', 'CLOSED', 'RESOLVED']
priority = ['CRITICAL', 'HIGH', 'NORMAL', 'LOW', 'VERYLOW']
category = ['1', '2']

create_by = ['1']

assign_to = ['1']
types = ['1', '2']
complete = ['0', '1']



conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()

i = 0
print(datetime.datetime.now())
while i < 500:
    sentence = sing_sen_maker()
    cur.execute("""INSERT INTO ticket_tickets (content, title, status, priority, assign_to_id ,
                                               create_by_id, types,
                                               last_edited, created,
                                               category_id,
                                               complete) VALUES
               ('%s', '%s', '%s', '%s', '%s', '%s', '%s' , '%s' , '%s', '%s', '%s')""" %(sentence,
                                                                            sentence,
                                                                            random.choice(status),
                                                                            random.choice(priority),
                                                                            random.choice(assign_to),
                                                                            random.choice(create_by),
                                                                            random.choice(types),
                                                                            datetime.datetime.now(),
                                                                            datetime.datetime.now(),
                                                                            random.choice(category),
                                                                            random.choice(complete)))
    conn.commit()
    i += 1


