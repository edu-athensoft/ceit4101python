"""
python logging

using logging

"""

import logging

logbase = './logs/'
logfile = logbase + 'logging_5_example_1.log'
logformat = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

logging.basicConfig(level=logging.DEBUG, filename=logfile, filemode='w',
                    format=logformat)


class Employee:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

        logging.info(f'Created employee: {firstname} {lastname}.')

    @property
    def email(self):
        return f'{self.firstname}.{self.lastname}@athensoft.com'

    @property
    def fullname(self):
        return f'{self.firstname}.{self.lastname}'


# test
emp1 = Employee("Athens", "Zhang")
emp2 = Employee("Peter", "Lee")
emp3 = Employee("Jack", "White")
