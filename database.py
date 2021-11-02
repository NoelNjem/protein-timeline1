
import sqlite3
def database():
    database_name = input("Please name your database ")
    conn = sqlite3.connect(database_name)
    c = conn.cursor()

    c.execute("DROP TABLE Entities");
    c.execute("DROP TABLE Relationship_Actions");
    c.execute("DROP TABLE Sub_Relationship_Actions");
    c.execute("DROP TABLE Relationships_1_1");
    c.execute("DROP TABLE Relationships_1_2");
    c.execute("DROP TABLE Relationships_1_3");
    c.execute("DROP TABLE Unknown_Relationships");

    # creates entity table to store entities for visualization
    c.execute("""Create TABLE If Not Exists Entities( 
    Entity_ID TEXT Unique PRIMARY KEY NOT NULL, 
    Origin TEXT, 
    Size TEXT, 
    Color TEXT, 
    Purpose TEXT,
     Start_Time Integer, 
     End_Time Integer,
     Comes_From TEXT)""")
    #creates table for relationship action groups
    c.execute("""CREATE TABLE IF NOT EXISTS RELATIONSHIP_ACTIONS(
    Relationship_GROUP_ID Text PRIMARY KEY NOT NULL)""")
    #creates table for sub groups of relationship types
    c.execute("""CREATE TABLE IF NOT EXISTS SUB_RELATIONSHIP_ACTIONS(
    Sub_Relationship_ID TEXT Primary KEY NOT NULL,
    RELATIONSHIP_GROUP TEXT,
     Foreign KEY (RELATIONSHIP_GROUP) References Relationship_Actions (Relationship_GROUP_ID)
     )""")
    # creates 1:1 Relationships table for relationships from 1 entity to another entity
    c.execute("""CREATE TABLE IF NOT EXISTS Relationships_1_1(
    Entity_ID_1 TEXT,
     Start_Time Text Not Null,
     End_Time Text Not Null,
     Location Text,
     Relationship Text Not Null,
     Sub_Relationship Text,
     Entity_ID_2 Text Not Null,
     Foreign Key (Sub_Relationship) References Sub_Relationship_Actions(Sub_Relationship_ID),
     Foreign Key (Relationship) References Relationship_Actions(Relationship_Group_ID),
     Foreign KEY (Entity_ID_1) References Entities(Entity_ID),
     Foreign Key (Entity_ID_2) References Entities(Entity_ID)
     )""")
    # creates 1:2 Relationships table for relationships from 1 entity to 2 entiies
    c.execute("""CREATE TABLE IF NOT EXISTS Relationships_1_2(
     Entity_ID_1 TEXT,
     Start_Time Text Not Null,
     End_Time Text Not Null,
     Location Text,
     Relationship Text Not Null,
     Sub_Relationship Text,
     Entity_ID_2 Text Not Null,
     Entity_ID_3 Text Not Null,
     Foreign KEY (Entity_ID_1) References Entities(Entity_ID),
     Foreign Key (Relationship) References Relationship_Actions(Relationship_Group_ID),
     Foreign Key (Sub_Relationship) References Sub_Relationship_Actions(Sub_Relationship_ID),
     Foreign Key (Entity_ID_2) References Entities(Entity_ID),
     Foreign Key (Entity_ID_3) References Entities(Entity_ID)
     )""")
#creates 1:3 Relationships table for relationships from 1 entity to 3 entiies
    c.execute("""CREATE TABLE IF NOT EXISTS Relationships_1_3(
    Entity_ID_1 TEXT,
     Start_Time Text Not Null,
     End_Time Text Not Null,
     Location Text,
     Relationship Text Not Null,
     Sub_Relationship Text,
     Entity_ID_2 Text Not Null,
     Entity_ID_3 Text Not Null,
     Entity_ID_4 Text Not Null,
     Foreign KEY (Entity_ID_1) References Entities(Entity_ID),
     Foreign Key (Relationship) References Relationship_Actions(Relationship_Group_ID),
     Foreign Key (Sub_Relationship) References Sub_Relationship_Actions(Sub_Relationship_ID),
     Foreign Key (Entity_ID_2) References Entities(Entity_ID),
     Foreign Key (Entity_ID_3) References Entities(Entity_ID),
     Foreign Key (Entity_ID_4) References Entities(Entity_ID)
     )""")
#creates table for relationships with an unknown number of entities
    c.execute("""CREATE TABLE IF NOT EXISTS Unknown_Relationships(
    Entity_ID_1 TEXT,
     Start_Time Text Not Null,
     End_Time Text Not Null,
     Location Text,
     Relationship Text Not Null,
     Sub_Relationship Text,
     Entity_Other Text Not Null,
     Number_of_Entities Integer Not Null,
     Foreign Key (Relationship) References Relationship_Actions(Relationship_Group_ID),
     Foreign Key (Sub_Relationship) References Sub_Relationship_Actions(Sub_Relationship_ID),
     Foreign KEY (Entity_ID_1) References Entities(Entity_ID)
     )""")
#todo find mass of HIP, add HOP and degradation pathway
    # stores insert values for entities table into an array variable
    many_entities = [
        ('Ricin', 'Castor Beans', '64 kDa', 'Blue', 'Inactivates Ribosome', 0, 300, 'Outside the body'),
        ('Glycoprotein', 'Golgi apparatus', '29KDa', 'Red', 'Class of receptors that ricin binds', 0, 5, 'Golgi Apparatus'),
        ('Vesicle_1', 'Plasma Membrane', '340nm', 'Yellow', 'Transports Ricin', 5, 30, 'plasma membrane'),
        ('Vesicle_2', 'Plasma Membrane', '340nm', 'Yellow', 'Transports Ricin', 5, 30, 'plasma membrane'),
        ('Endosome', 'Cytoplasm', '80nm', 'Green', 'Sorts Ricin for Trafficking', 30, 60, 'Golgi Apparatus'),
        ('Early_Endosome', 'Endsosome', '80nm', 'Green', 'Transports Ricin to Golgi', 60, 90, 'Endosome'),
        ('Late_Endosome', 'Endsosome', '80nm', 'Green', 'Transports Ricin to Lysosome', 60, 90, 'Endosome'),
        ('Lysosome', 'Cytosol', '0.80nm', 'Purple', 'Degrades Ricin', 90, 100, 'Cytoplasm'),
        ('Golgi Apparatus', 'Cytoplasm', '30nm', 'Grey', 'Trafficks Ricin', 90, 140, 'Cytoplasm'),
        ('ER-Golgi Intermediate Complex', 'Cytoplasm', '50nm', 'Pink', 'Trafficks Ricin', 160, 190, 'Cytoplasm'),
        ('Endoplasmic Reticulum', 'Cytoplasm', '50nm', 'Royal Blue', 'Trafficks Ricin', 210, 240, 'Cytoplasm'),
        ('COP1_1', 'Golgi-ER Complex', '50nm', 'Black', 'Creates vesicle for transport', 140, 160, 'Golgi Apparatus'),
        ('COP1_2', 'Golgi-ER Complex', '50nm', 'Black', 'Creates vesicle for transport', 190, 210, 'ER-Golgi Intermediate Complex'),
        ('Arf1', 'Golgi-ER Complex', '50nm', 'Red', 'Modulates formation of COP1 vesicle', 240, 250, 'Golgi Apparatus'),
        ('KXXX Motif', 'Golgi-ER Complex', '50nm', 'Purple', 'Modulates formation of COP1 vesicle', 100, 210, 'ER'),
        ('Ref1', 'ERGIC', '36.5KDa', 'Orange', 'Aids Vesicle Transport to ERGIC', 140, 160, 'ER'),
        ('Thioredocxin reducatase', 'ER', '58KDa', 'Green', 'Breaks Ricin disulfide bond', 220, 230, 'ER'),
        ('Protein disulfide isomerase', 'ER', '107KDa', 'Yellow', 'Breaks Ricin disulfide bond', 220, 230, 'ER'),
        ('Ricin A Chain (RTA)', 'Ricin', '30KDa', 'Red', 'Depurinates Ribosome', 230, 300,'Ricin Holotoxin'),
        ('Ricin B Chain (RTB)', 'Ricin', '32KDa', 'Orange', 'Binds recpetors', 230, 235, 'Ricin Holotoxin'),
        ('Hsp70', 'Cytosol', '70KDa', 'Yellow', 'Aids refolding of RTA', 250, 270, 'Cytosol'),
        ('RTP5', 'Cytosol', '2.5MDa', 'Pink', 'Aids refolding of RTA', 250, 270,'Cytosol'),
        ('RTP4', 'Cytosol', '2.5MDa', 'Pink', 'Aids refolding of RTA', 240, 250, 'Cytosol'),
        ('HIP', 'Cytosol', '?', 'Blue', 'Aids refolding of RTA', 250, 270, 'Cytosol'),
        ('BAG-1', 'Cytosol', '', 'Grey', 'Releases RTA from Hsp70 and HIP', 270,280, 'Cytosol'),
        ('P2 Subunit', 'Ribosome', '8,804 Da', 'Indigo', 'Aids transfer of ricin to the Sarcin-Ricin Loop (SRL) on the 28S rRNA strand', 290, 300, 'Ribosome'),
        ('P1 Subunit', 'Ribosome', '11,514 Da', 'Auburn','Aids transfer of ricin to the Sarcin-Ricin Loop (SRL) on the 28S rRNA strand', 290, 300, 'Ribosome'),
        ('Ribosome', 'Cytosol', '11,514 Da', 'Purple','Aids transfer of ricin to the Sarcin-Ricin Loop (SRL) on the 28S rRNA strand', 290, 300, 'Cytosol'),
        ('Ricin-Sarcin Loop', 'Ribosome', 'Null', 'Grey','Binds Ricin and prevents protein synthesis after depurination of Adenine A4324', 290, 300, '28S rRNA'),
        ('Adenine A4324', 'Sarcin-Ricin Loop', 'Null', 'Red', 'Is cleaved off of the Sarcin-Ricin Loop by Ricin', 295,300, 'Sarcin-Ricin Loop')

    ]

    # inserts records into entities table
    c.executemany("INSERT into Entities values(?,?,?,?,?,?,?,?)", many_entities)
    #stores insert values for relationship actions table in list
    many_relationship_actions = [
        ('Bind',),
        ('Activate',),
        ('Inactivate',),
        ('Degrade',),
        ('Cleave',),
        ('Modify',),
        ('Traffic',),
        ('Fold',),
        ('Unknown',),
        ('Contains',),
        ('Branches',),
    ]
    #insertes relationship actions values
    c.executemany("INSERT into Relationship_Actions values(?)", many_relationship_actions)
    #stores insert valeus for sub relationship actions table in list
    many_sub_relationship_actions = [
        ('Bind', 'Bind'),
        ('Bond', 'Bind'),
        ('Recruit', 'Bind'),
        ('Scaffold', 'Bind'),
        ('Upregulate', 'Activate'),
        ('Activate', 'Activate'),
        ('Downregulate', 'Inactivate'),
        ('Repress', 'Inactivate'),
        ('Inactivate', 'Inactivate'),
        ('Block', 'Inactivate'),
        ('Degrade', 'Degrade'),
        ('Digest', 'Degrade'),
        ('Phagocytize', 'Degrade'),
        ('Cleave', 'Cleave'),
        ('Dissociate', 'Cleave'),
        ('Splice', 'Modify'),
        ('Modify', 'Modify'),
        ('Transcribe', 'Modify'),
        ('Replicate', 'Modify'),
        ('Traffic', 'Traffic'),
        ('Endocytize', 'Traffic'),
        ('Exocytize', 'Traffic'),
        ('Channeling', 'Traffic'),
        ('Fold', 'Fold'),
        ('Unfold', 'Fold')
    ]
    #inserts values into sub relationship actions table
    c.executemany("INSERT into Sub_Relationship_Actions values(?,?)",many_sub_relationship_actions)
    #stores insert values for relatiionship 1:1 table in list
    many_relationships_1_1 = [('Ricin_1', 0,5, 'Cytoplasm', 'Bind', 'Bind', 'Glycoprotein'),
                              ('Ricin_1', 5, 10, 'Plasma_Membrane', 'Traffic', 'Endocytize', 'Vesicle_1'),
                              ('Vesicle_1', 5,30, "Cytosol", 'Contains', 'Null', 'Ricin_1'),
                              ('Vesicle_1', 5,5, 'Cytosol', 'Branches', 'Null', 'Vesicle_2'),
                              ('Ricin_1', 5,5, 'Cytosol', 'Branches', 'Null', 'Ricin_2'),
                              ('Endosome', 30, 60, 'Endosome', 'Contains', 'Null', 'Ricin_1'),
                              ('Early_Endosome', 60,90, 'Cytosol', 'Contains', 'Null', 'Ricin_1'),
                              ('Late_Endosome', 60,90, 'Cytosol', 'Contains', 'Null', 'Ricin_3'),
                              ('Ricin_1', 60, 60, 'Endosome', 'Branches', 'Null', 'Ricin_3'),
                              ('Lysosome', 90, 100, 'Lysosome', 'Contains', 'Null', 'Ricin_3'),
                              ('Lysosome', 93, 100, 'Lysosome', 'Degrades', 'Digest', 'Ricin_3'),
                              ('Golgi Apparatus', 90,140, 'Golgi Apparatus', 'Contains', 'Null', 'Ricin_1'),
                              ('Ricin_1', 100,210, 'Golgi Apparatus', 'Binds', 'Recruits', 'KXXX Motif'),
                              ('COP1_1', 145,160, 'Cytosol', 'Binds', 'Recruits', 'Ref1'),
                              ('Thioredocxin reducatase', 215,220, 'Endoplasmic Reticulum', 'Cleave', 'Dissociate', 'Ricin_1'),
                              ('Ricin A Chain (RTA)', 230, 230, 'Endoplasmic Reticulum', 'Fold', 'Unfold', 'RTA'),
                              ('RTP4',240,250, 'Endoplasmic Reticulum', "Traffic", 'Channeling', 'Ricin A Chain (RTA)'),
                              ('RTP5', 250,270, 'Cytosol', 'Bind', 'Bind', 'Ricin A Chain (RTA)'),
                              ('BAG-1',265,270, 'Cytosol', 'Bind', 'Bind', 'Hsp70'),
                              ('Ricin A Chain (RTA)', 270,290, 'Cytosol', 'Traffic', 'Traffic', 'P1 Subunit'),
                              ('Ricin A Chain (RTA)', 295, 300, 'Ribosome', 'Inactivate', 'Inactivate', 'Ribosome'),
                              ('Ribosome', 290, 296, 'Ribosome', 'Contains', 'Null', 'Ricin A Chain (RTA)')
                              ]
    c.executemany("INSERT into Relationships_1_1 Values(?,?,?,?,?,?,?)", many_relationships_1_1)
    #stores insert values for relationship 1:2 table in list
    many_relationships_1_2 = [('Vesicle_1', 10,30,'Cytosol', 'Traffic', 'Traffic', 'Ricin_1', 'Endosome'),
                              ('Vesicle_2', 10,30,'Cytosol', 'Traffic', 'Traffic', 'Ricin_2', 'Plasma_Membrane'),
                              ('Early_Endosome', 60,90, 'Cytosol', 'Traffic', 'Traffic', 'Ricin_1', 'Golgi Apparatus'),
                              ('Late_Endosome', 60,90, 'Cytosol', 'Traffic', 'Traffic', 'Ricin_3', 'Lysosome'),
                              ('KXXX Motif', 130,140, 'Golgi Apparatus', 'Bind', 'Recruit', 'Arf1', 'COP1_1'),
                              ('COP1_1',140, 160, 'Cytosol', 'Contains', 'Null', 'Ricin_1', 'KXXX Motif'),
                              ('COP1_1',145, 160, 'Cytosol', 'Traffic', 'Traffic', 'Ricin_1', 'ER-Golgi Intermediate Complex'),
                              ('COP1_1',145, 160, 'Cytosol', 'Traffic', 'Traffic', 'KXXX Motif', 'ER-Golgi Intermediate Complex'),
                              ('COP1_2',190, 210, 'Cytosol', 'Traffic', 'Traffic', 'KXXX Motif', 'Endoplasmic Reticulum'),
                              ('COP1_2',190, 210, 'Cytosol', 'Traffic', 'Traffic', 'Ricin_1', 'Endoplasmic Reticulum'),
                              ('ER-Golgi Intermediate Complex', 'ER-Golgi Intermediate Complex', 160,190, 'Contains', 'Null', 'Ricin_1', 'KXXX Motif'),
                              ('Ricin_1', 210,220, 'Endoplasmic Reticulum', 'Binds', 'Binds','Thioredocxin reducatase', 'PID' ),
                              ('Endoplasmic Reticulum', 220, 240, 'Endoplasmic Reticulum', 'Contains', 'Null', 'Ricin A Chain (RTA)', 'RTB'),
                              ('RTP5', 255,270, 'Cytosol', 'Bind', 'Recruits', 'HIP', 'Hsp70'),
                              ('Ricin A Chain (RTA)', 290,291, 'Ribosome', 'Bind', 'Bind', 'P1 Subunit', 'P2 Subunit'),
                              ('Ricin A Chain (RTA)', 293, 294, 'Ribosome', 'Traffic', 'Transfers', 'Ricin A Chain (RTA)', 'Sarcin-Ricin Loop'),
                              ('Ricin A Chain (RTA)', 294, 295, 'Ribosome', 'Cleave', 'Dissociate', 'A4324', 'Ricin-Sarcin Loop'),
                              ('Ribosome', 290, 300, 'Ribosome', 'Contains', 'Null', 'P1 Subunit', 'P2 Subunit')
                              ]
    #inserts values into relationship 1:2 table
    c.executemany("INSERT into Relationships_1_2 Values(?,?,?,?,?,?,?,?)", many_relationships_1_2)
    #stores insert values for relationship 1:3 table
    many_relationships_1_3 = [
        ('Endoplasmic Reticulum', 210, 220, 'Endoplasmic Reticulum', 'Contains', 'Null', 'Ricin_1', 'PID', 'Thioredocxin reducatase'),
        ('BAG-1', 270, 270, 'Cytosol', 'Cleave', 'Dissociate','Ricin A Chain (RTA)', 'Hsp70', 'HIP'),
        ('Ribosome', 290, 300, 'Ribosome', 'Contains', 'Null', 'P1 Subunit', 'P2 Subunit', 'Sarcin-Ricin Loop')
        ]
    #inserts values into relationship 1:3 table
    c.executemany("INSERT into Relationships_1_3 Values(?,?,?,?,?,?,?,?,?)", many_relationships_1_3)
    print('database constructed')
    c.execute("select * from Entities")
    conn.commit()

    conn.close()

database()