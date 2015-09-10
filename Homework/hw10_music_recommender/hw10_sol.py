'''
Created on Apr 14, 2015
@author:	Kelvin Rodriguez
'''
# Full disclosure, I didn't use any of the functions written in the book.
import time
import sys

FILE_NAME = 'musicrecplus.txt'				# file name for database
OPTIONS = {'e', 'r', 'p', 'h', 'm', 'q'}	# user options for features
DATABASE = {}								# database to hold users

def menu():
	'''	Prompts the user with the menu for the program.
	'''
	print '''Enter a letter to choose an option:
   e - enter preferences
   r - get recommendations
   p - show most popular artists
   h - how popular is the most popular
   m - which user has the most likes
   q - save and quit\n'''

def get_choice(choice):
	''' Used to validate boolean in main().
		Returns true is user input is invalid, else calls features.
	'''
	while (1):
		if choice == 'q': 
			quit()
			break
		elif choice in OPTIONS : call_feature(choice)
		else: 
			print '\nError! Incorrect input.\n'
			return True

def call_feature(option):
	'''	Function used to call the features based on user input.
	'''
	if option == 'e' : get_preferences()
	if option == 'r' : get_recommendation()
	if option == 'p' : popular_artists()
	if option == 'h' : artist_popularity()
	if option == 'm' : most_likes()
	
def loadUsers(file_name):
	'''	Returns a dictionary with all the users and their inputs.
		Dictionary obtained from FILE_NAME.
	'''
	my_file = open(file_name, 'r')
	line = my_file.read()
	my_file.close()
	line = line.split('\n')
	line = filter(lambda artist: len(artist) != 0, line)

	elements = []
	for i in range(len(line)):
		x = line[i]
		l = x.split(':')
		l2 = l[1].split(',')
		elements.append(l2)
		DATABASE[l[0]] = l2

	return DATABASE

def save():
	'''	Saves the current database to FILE_NAME.
	'''
	my_file = open(FILE_NAME, 'w')
	for user in DATABASE:
		save = str(user) + ':' + ','.join(DATABASE[user]) + '\n'
		my_file.write(save)
	my_file.close()

def num_matches(lst1, lst2):
    '''	Returns the number of elements that the two list have in common.
    '''
    matches = 0
    i = 0
    j = 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] == lst2[j]:
            matches += 1
            i += 1
            j += 1
        elif lst1[i] < lst2[j]:
            i += 1
        else: 
            j += 1     
    return matches

def drop_matches(lst1, lst2):
    '''	Returns a new list that contains only the elements in 
    	lst2 that are Not in lst1.
    '''
    result = []
    i = 0
    j = 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] == lst2[j]:
            i += 1
            j += 1
        elif lst1[i] < lst2[j]:
            i += 1
        else: 
            result.append(lst2[j])
            j += 1
    while j < len(lst2):
        result.append(lst2[j])
        j += 1
    return result

def get_recommendation():
	'''	Returns a list of recommendations to the user based on 
		similar likes from other users (i.e. based of most common user).
	'''
	
	print "You've chosen to get recommendations!\n"
	
	userName = raw_input('Please enter your name: ')
	userName = userName.strip().title()

	recommender = ''
	artist_list = DATABASE[userName]
	database_names = DATABASE

	if len(database_names) == 1:
		print '\nSorry, ' + userName + " you're our only user :("
	else:
		most_matches = 0
		matches = 0
		for user in database_names:
			if user != userName:
				user_list = DATABASE[user]
				matches = num_matches(artist_list, user_list)
			if matches > most_matches:
				most_matches = matches
				recommender = user

		if most_matches == 0:
			print '\nSorry ' + userName + ", I have no recommendations."
		else:
			i = 1
			rec = drop_matches(artist_list, DATABASE[recommender])
			print "Here are some recommendations for you", userName + '!'
			for artist in rec:
				print str(i) + '.' + artist
				i += 1

	return main()

def get_preferences():
	'''	Prompts the user to enter their preferences (i.e., the artists
		they like). If this user already present in database, the new 
		preferences are added to the old ones. Does not allow for
		repetitive inputs. Typing 'END' terminates the input.

		returns back to main() to display options.
	'''
	
	newPref = ''
	print "\nYou've chosen to enter preferences!"
	print '\nRemember if you add a "$" at the end of your name,'
	print 'you opt out the most likes feature.'
	userName = raw_input('\nPlease enter your name: ')
	userName = userName.strip().title()

	if userName in DATABASE:
		prefs = DATABASE[userName]		# list of artists for user
		print '\nHey', userName + '! Here are your preferences:'
		for i in range(len(prefs)):
			print str(i + 1) + '.' + prefs[i]
	else:
		prefs = []						# empty for new user
		print '\nHello ' + userName + '! I see that you are a new user!'
		print 'Please enter the name of an artist or band that you like:',
		newPref = raw_input('')

	# loop to append new entries for userName
	while newPref != 'End':
		
		prefs.append(newPref.strip().title())
		
		print '\nPlease enter another artist or band that you like,'
		print 'or type "END" to finish',
		
		newPref = raw_input('and see your recommendations: ')
		newPref = newPref.strip().title()

		# validate user input, check if entry already in preferences
		if newPref not in prefs:
			prefs = filter(lambda artist: len(artist) != 0, prefs) #filter blank entries
			prefs.sort()
			#prefs.append(newPref.strip().title())
			DATABASE[userName] = prefs
		else:
			print "\nI'm sorry, but you've already added that band or artist."
			
	prefs = list(set(prefs))
	prefs.sort()
	DATABASE[userName] = prefs

	print "\nGreat! We've added your new preferences, which are now:"
	for i in range(len(DATABASE[userName])):
		print str(i + 1) + '.' + DATABASE[userName][i]

	save()
	return main()

def flatten_list(lst):
	'''	Returns a flattened list of elements in the nested list
		of lists lst.
	'''
	return list(y for x in lst for y in x)

def popular_artists():
	'''	Returns the artist liked by the most users.
	'''
	artist_list = []
	num_occurances = []
	artist_dic = {}
	
	for user in DATABASE:
		artist_list.append(DATABASE[user])
	
	artist_list = flatten_list(artist_list) # list of all artists
	artist_lst = list(set(artist_list)) 	# list w/o duplicates

	for artist in artist_lst:
		artist_dic[artist] = 0

	for artist in artist_dic:
		artist_dic[artist] = artist_list.count(artist)
		num_occurances.append(artist_list.count(artist))

	if num_occurances != [] : num = max(num_occurances)
	else : num = 0

	if num == 0: 
		print '\nThere are no artists in the program. Please add some :)'
	elif num == 1: 
		print '\nThe most popular artists are: '

		i = 1
		for artist in artist_lst:
			print str(i) + '.' + artist
			i += 1
	else:
		print '\nThe most popular artist(s) are: '

		i = 1
		for artist in artist_lst:
			if artist_dic[artist] == num:
				print str(i) + '.' + artist
				i += 1

	return main()

def artist_popularity():
	'''	Returns how many users like the most popular artist.

		If there is a tie, program will output the artists.
	'''	
	artist_list = []
	num_occurances = []
	artist_dic = {}
	
	for user in DATABASE:
		artist_list.append(DATABASE[user])
	
	artist_list = flatten_list(artist_list) # list of all artists
	artist_lst = list(set(artist_list)) 	# list w/o duplicates

	for artist in artist_lst:
		artist_dic[artist] = 0

	for artist in artist_dic:
		artist_dic[artist] = artist_list.count(artist)
		num_occurances.append(artist_list.count(artist))

	if num_occurances != [] : num = max(num_occurances)
	else : num = 0

	if num == 0: 
		print '\nThere are currently no artists in our system. Please add some :)'
	elif num == 1: 
		print '\nThe most popular artists are: '

		i = 1
		for artist in artist_lst:
			print str(i) + '.' + artist
			i += 1
	else:
		print '\nThe most popular artist(s) are liked by', num, 'users!'
		print 'The artists are: '

		i = 1
		for artist in artist_lst:
			if artist_dic[artist] == num:
				print str(i) + '.' + artist
				i += 1

	return main()

def most_likes():
	'''	Returns the name of the user with the most artists in 
		their preferences, and prints their preferences too.

		If user has 'opted out' of this feature, their name is not
		printed. Example, 'JoeSmith$' has opted out but 'JoeSmith' has
		not.
	'''
	print "\nYou've chosen to view the user with the most likes!"
	print 'Remember if your name ends with a $ you opt out of this feature.'
	
	user = ''
	max_likes = 0
	artist_list = []
	num_likes = []

	for users in DATABASE:
		if users[-1] != '$':
			artist_list = DATABASE[users]
			likes = len(artist_list)
			num_likes.append(likes)			# used to validate ties
			if likes > max_likes:
				max_likes = likes
				user = users				

	if num_likes.count(max_likes) > 1:
		print '\nThere seems to be a couple of people with',
		print 'the same number of likes.'
		return main()
	else:
		print '\nThe user with the most likes is', user + '.'
		print '\nThe preferences are: '

		i = 0
		for artists in DATABASE[user]:
			print str(i + 1) + '.' + artists
			i += 1

		return main()

def quit():
	''' Terminates the program based off user input.
	'''	
	print '\nSaving file ' + '"' + FILE_NAME + '"' + '...'
	save()			# not really necessary here, but assignment asks for it
	time.sleep(1)	# add the feel of saving
	print 'Thank you for using Recommender+!'
	sys.exit(0)		# exit successfully

def main():
	''' Main recommendation function.
	'''
	DATABASE = loadUsers(FILE_NAME)
	print '\nWelcome to Recommender+!\n'

	boolean = True
	while (boolean):
		menu()
	 	choice = raw_input('')
		boolean = get_choice(choice)

if __name__ == '__main__' : main()