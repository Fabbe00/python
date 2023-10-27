import sqlite3

def main():
    glosLista = {}

    createTable()

    print("GLOSOR!")
    
    readglosor = input("Vill du läsa in gamla glosor j/n ")
    
    if readglosor == "j":
        lasaglosor = "läsa in från databas gamla glosor"
        glosLista = get_all_glosor()
        print("Läsa från databas")

    else:    
    
        while True:
            svGlosa = input("Ange en svensk glosa: ")
            enGlosa = input("Ange den engelska översättningen: ")

            glosLista.update({svGlosa : enGlosa})
            add_glosa_to_table(svGlosa, enGlosa)

            fortsatt  = input("Vill du ange fler? j/n: ")
            if fortsatt == "n":
                break

    while True:


        print("\n Nu start glosförhöret!")

        for glosa in glosLista:
            svar = input(f"\n {glosa} : ")

            if svar == glosLista[glosa]:
                print(" Rätt svar!")
            else :
                print(f"\nFel svar, det är {glosLista[glosa]}")

        fortsatt2  = input("Vill du köra om? j/n: ")
        if fortsatt2 == "n":
            break


def createTable():
    try:
        sqliteConnection = sqlite3.connect("glosor.db")
        sqlite_question = (''' CREATE TABLE IF NOT EXISTS tabellglosor 
                           id = INTEGER PRIMARY KEY,
                           svglosa TEXT NOT NULL,
                           englosa TEXT NOT NULL
                           ''')

        cursor = sqliteConnection.cursor()
        cursor.execute(sqlite_question)
        sqliteConnection.commit()

        cursor.close() 

        sqliteConnection.close()

    except sqlite3.Error as error:
        print(error)


def add_glosa_to_table(t_svglosa, t_englosa):
                       
    try:
        sqliteConnection = sqlite3.connect("glosor.db")                   
        sqlite_question = (f'''INSERT INTO tabellglosor (svglosa, englosa) VALUES ('{t_svglosa}', '{t_englosa}')''') 

        cursor = sqliteConnection.cursor()

        cursor.execute(sqlite_question)
        sqliteConnection.commit()
        cursor.close()
        
        sqliteConnection.close()

    except sqlite3.Error as error:
        print(error)

def get_all_glosor():

    temp_dict = {}

    try:
        sqliteConnection = sqlite3.connect("glosor.db")                   
        sqlite_question = (f'''SELECT * FROM tabellglosor''')
        cursor = sqliteConnection.cursor()

        cursor.execute(sqlite_question)
        records = cursor.fetchall()

        for row in records:
            temp_dict.update({row[1]: row[2]})
            
        #sqliteConnection.commit()
        cursor.close()      

        sqliteConnection.close()
    
    except sqlite3.Error as error:
        print(error)

    return temp_dict                      
main()
