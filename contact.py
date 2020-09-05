import pyperclip

class Contact:
	""" 
	Class that generates new instances of contacts
	"""

	# Class variables
	contact_list = []  # empty contact list
	def __init__(self,first_name,last_name,phone_number,email):

		'''
			__init__ method helps us define
			properties for our objects
		'''

		# Instance Variables
		self.first_name = first_name
		self.last_name = last_name
		self.phone_number = phone_number
		self.email = email
#save function
def save_contact(self):
		'''
        save_contact method saves contact objects into contact_list
        '''
		Contact.contact_list.append(self)
new_contact=Contact("Silas","Sakwa","0740912099","silas2016.com")
print(new_contact.__dict__)