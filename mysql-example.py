import mysql.connector

con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database="ardit700_pm1database"
)

cursor = con.cursor()

word = input("Enter a word: ")

query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " % word)
results = cursor.fetchall() #The method fetches all (or all remaining) rows of a query result set and returns a list of tuples.
# If no more rows are available, it returns an empty list.

#loop extracts tupples, for words with more than 1 definition. And takes them out of a list. add [1] for just definition
if results: #if empty list won't be executed it, considered false
    for meaning in results:
        print(meaning[1])

else: 
    print("No word found!")
