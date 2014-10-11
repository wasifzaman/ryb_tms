from timeclock import Timesheet, Timeclock


class Teacher:

	def __init__(self, **kwargs):
		def apply_attribute(attribute):
			return kwargs[attribute] if attribute in kwargs else False

		self.first_name = apply_attribute('first_name')
		self.last_name = apply_attribute('last_name')
		self.chinese_name = apply_attribute('chinese_name')
		self.date_of_birth = apply_attribute('date_of_birth')
		self.card_printed = apply_attribute('card_printed')
		self.street = apply_attribute('street')
		self.city = apply_attribute('city')
		self.state = apply_attribute('state')
		self.zip_code = apply_attribute('zip_code')
		self.email = apply_attribute('email')
		self.phone = apply_attribute('phone')
		self.phone_2 = apply_attribute('phone_2')
		self.notes = apply_attribute('notes')
		self.timesheet = Timesheet()

	pass


class Database:

	def __init__(self):

		self.database = {}
		self.last_entry = 0

	def add(self):

		self.database[self.last_entry] = Teacher()
		self.last_entry += 1


	pass


teacher_1 = Teacher()