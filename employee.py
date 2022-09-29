"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract, commission):
        self.name = name
        self.contract = contract
        self.commission = commission


    def get_pay(self):
        if self.commission:
            return contract.get_pay(self.contract) + commission.get_pay(self.commission)
        else:
            return contract.get_pay(self.contract)

    def __str__(self):
        msg = self.name + " works on a "
        if self.contract.isSalary:
            msg += "monthly salary of " + str(self.contract.perWorkingTime)
        else :
            msg += "contract of " + str(self.contract.workingTime) + " hours at " + str(self.contract.perWorkingTime) + "/hour"

        if self.commission:
            if not self.commission.isBonus:
                msg += " and receives a commission for " + str(self.commission.num_of_contract) + " contract(s) at " + str(self.commission.perCommission) + "/contract"
            else:
                msg += " and receives a bonus commission of " + str(self.commission.perCommission)


        msg += ".  Their total pay is " + str(self.get_pay()) + "."

        return msg

class contract:
    def __init__(self, isSalary, perWorkingTime, workingTime = 1):
        self.isSalary = isSalary
        self.perWorkingTime = perWorkingTime
        self.workingTime = workingTime

    def get_pay(self):
        return self.perWorkingTime*self.workingTime

class commission:
    def __init__(self, perCommission, isBonus = True, num_of_contract = 1):
        self.isBonus = isBonus
        self.perCommission = perCommission
        self.num_of_contract = num_of_contract

    def get_pay(self):
        return self.perCommission*self.num_of_contract



# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', contract(True, 4000), None)
#print(billie.get_pay())
#print(billie.__str__())

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', contract(False, 25, 100), None)
#print(charlie.get_pay())
#print(charlie.__str__())

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', contract(True, 3000), commission(200, False, 4))
#print(renee.get_pay())
#print(renee.__str__())

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', contract(False, 25, 150), commission(220, False, 3))
#print(jan.get_pay())
#print(jan.__str__())

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', contract(True, 2000), commission(1500))
#print(robbie.get_pay())
#print(robbie.__str__())

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', contract(False, 30, 120), commission(600))
#print(ariel.get_pay())
#print(ariel.__str__())
