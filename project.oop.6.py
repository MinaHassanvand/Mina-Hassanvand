
import csv
import os


class Vehicle:

    hourIn = 0
    minIn = 0
    hourOut = 0
    minOut = 0
    hourOutFinal = 0
    minOutFinal = 0
    
    def __init__(self, myInputs):
        self.myInputs = myInputs

    def opensCsv(self):

        h = ['Type of Vehicle', 'TIME-IN', 'TIME-OUT', 'PARKING TIME', 'ROUNDED TOTAL', 'TOTAL CHARGES $']

        with open('parkingLog.csv', 'a') as self.myLog: # opens up a log file and prints the header into it if file empty
            myCsvWriter = csv.writer(self.myLog)
            
            if os.stat('parkingLog.csv').st_size == 0:         
                myCsvWriter.writerow(h)
            else:
                pass
#-------------------------------------------------------------------------------------------------------------

    def parkingInfoInputHourIn(self):
        
        flag = True    
        while True:
            
            flag = False

            hourIn = input('Hour vehicle entered lot     (0 - 24)? or press 99 to stop: ')

            if hourIn == '99':
                raise SystemExit
                    
            if hourIn.isdigit() == False:
                print('invalid input, only integer 0 to 24. try again.')
                flag = True
            else:
                hourIn = int(hourIn)
                if hourIn in range(0,25):
                    self.myInputs['hourIn'] = hourIn
                    break

        return hourIn

#-------------------------------------------------------------------------------------------------------------

    def parkingInfoInputMinIn(self):
        
        flag = True            
        while True:
            
            flag = False

            minIn = input('Minute vehicle entered lot     (0 - 60)? or press 99 to stop: ')

            if minIn == '99':
                raise SystemExit
                    
            if minIn.isdigit() == False:
                print('invalid input, only integer 0 to 60. try again.')
                flag = True
            else:
                minIn = int(minIn)
                if minIn in range(0,60):
                    self.myInputs['minIn'] = minIn
                    break
        return minIn
               
#-------------------------------------------------------------------------------------------------------------

    def parkingInfoInputHourOut(self, hourIn):
        
        flag = True
        while flag:
            
            flag = False

            hourOut = input('Hour vehicle left lot     (0 - 24)? or press 99 to stop: ')

            if hourOut == '99':
                raise SystemExit
                    
            if hourOut.isdigit() == False:
                print('invalid input, only integer 0 to 24. try again.')
                flag = True
                
            else:
                hourOut = int(hourOut)
            
                if hourOut < hourIn: # if hour out > hour in, try again
                    
                    print('hour out < Hour in. try again.')
                    flag = True

                elif hourOut > hourIn:
                    if hourOut in range(0,25):
                        self.myInputs['hourOut'] = hourOut
                        break
        return hourOut

#-------------------------------------------------------------------------------------------------------------

    def parkingInfoInputMinOut(self):
        
        flag = True   
        while True:

            flag = False

            minOut = input('Minute vehicle left lot     (0 - 60)? or press 99 to stop: ')

            if minOut == '99':
                raise SystemExit
                    
            if minOut.isdigit() == False:
                print('invalid input, only integer 0 to 60. try again.')
                flag = True           
            else:
                minOut = int(minOut)
                if minOut in range(0,60):
                    self.myInputs['minOut'] = minOut
                    break

            return minOut

#-------------------------------------------------------------------------------------------------------------

    def parkingDurationPlusChargeCalc(self, carType):
            
        if self.myInputs['minOut'] > self.myInputs['minIn']:  # calculates the duration of parking
            
            minOutUpdate = self.myInputs['minOut'] 
            hourOutUpdate = self.myInputs['hourOut']
            self.myInputs['hourOutFinal'] = hourOutUpdate - self.myInputs['hourIn']
            self.myInputs['minOutFinal'] = minOutUpdate - self.myInputs['minIn']
            self.myInputs['durationRounded'] = self.myInputs['hourOutFinal'] + 1
            self.myInputs['charge'] = 6

        elif self.myInputs['minOut'] == self.myInputs['minIn']:
            
            minOutUpdate = self.myInputs['minOut'] + 60
            hourOutUpdate = self.myInputs['hourOut'] - 1
            self.myInputs['hourOutFinal'] = hourOutUpdate - self.myInputs['hourIn']
            self.myInputs['minOutFinal'] = minOutUpdate - self.myInputs['minIn']
            self.myInputs['durationRounded'] = self.myInputs['hourOutFinal'] + 1
            self.myInputs['charge'] = 6
            
        elif self.myInputs['minOut'] < self.myInputs['minIn']:
            
            minOutUpdate = self.myInputs['minOut'] + 60
            hourOutUpdate = self.myInputs['hourOut']
            self.myInputs['hourOutFinal'] = hourOutUpdate - self.myInputs['hourIn'] - 1
            self.myInputs['minOutFinal'] = minOutUpdate - self.myInputs['minIn']        
            self.myInputs['durationRounded'] = self.myInputs['hourOutFinal'] + 1
            self.myInputs['charge'] = 6

        if myInputs['carType'] == 1:
            
            if self.myInputs['durationRounded'] >= 0 and self.myInputs['durationRounded']  <= 3: # calculates car fee
                self.myInputs['charge'] = 0
                
            elif self.myInputs['durationRounded']  > 3:
                self.myInputs['charge'] = self.myInputs['durationRounded'] * 1.5

        if myInputs['carType']  == 2:
            if self.myInputs['durationRounded']  >= 0 and self.myInputs['durationRounded']  <= 2: # calculates truck fee
                self.myInputs['charge'] = self.myInputs['durationRounded'] * 1   
                
            elif self.myInputs['durationRounded']  > 2:
                self.myInputs['charge'] = self.myInputs['durationRounded']  * 2.3

        if myInputs['carType']  == 3:

            if self.myInputs['durationRounded']  <= 1.00: # calculates bus fee
                self.myInputs['charge'] = 2
            
            elif self.myInputs['durationRounded']  > 1.00:
                self.myInputs['charge'] = self.myInputs['durationRounded']  * 3.7
            
        return self.myInputs
#-------------------------------------------------------------------------------------------------------------

    def parkingBill(self):
        
        print("\t'PARKING LOT CHARGES") # prints out the bill
        print('Type of Vehicle:', self.myInputs['carType'])
        print('TIME-IN:', self.myInputs['hourIn'],':', self.myInputs['minIn'])
        print('TIME-OUT:', self.myInputs['hourOut'],':', self.myInputs['minOut'], "\n")
        print('PARKING TIME:', self.myInputs['hourOutFinal'], ':', self.myInputs['minOutFinal'])
        print('ROUNDED TOTAL:', self.myInputs['durationRounded'], "\n")
        print('TOTAL CHARGES $', self.myInputs['charge'], "\n")

#-------------------------------------------------------------------------------------------------------------
        
    def parkingLog(self):

        entring = str(self.myInputs['hourIn'] ) + ':' + str(self.myInputs['minIn']) 
        exiting = str( self.myInputs['hourOut']) + ':' + str(self.myInputs['minOut'])

        if self.myInputs['hourOutFinal'] == 60:
            durations = self.myInputs['hourOutFinal']  , ':', self.myInputs['minOutFinal'] 
        else:
            durations = str(self.myInputs['hourOutFinal'] ) +  ':' + str(self.myInputs['minOutFinal'] )
            
        myHrRounded = str(self.myInputs['durationRounded'] )
        myCharges = str(round(self.myInputs['charge'],2))

        with open('parkingLog.csv', 'a') as self.myLog: # prints results into a log file
            myCsvWriter = csv.writer(self.myLog)
            rows = [self.myInputs['carType'] , entring, exiting, durations, myHrRounded, myCharges]
            myCsvWriter.writerow(rows)

#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------

carTypeCode = [1, 2, 3]
hourIn = 0
myInputs = dict()
flag = False

def parkingInfoInputCarType(myInputs):
    carType = 0
    flag = True
    
    while flag:
        try:
            carType = int(input('Car types? 1 for car, 2 for bus, or 3 for truck. Press 99 to stop: '))
            myInputs['carType'] = carType
            if carType in carTypeCode:
                break
        except:
            print('only enter type of vehicle as car, truck, or bus')
            flag = True

        if carType == 99:
            raise SystemExit

    return myInputs

while True:

    if parkingInfoInputCarType(myInputs):
        carType = Vehicle(myInputs)
        carType.parkingInfoInputHourIn()
        carType.parkingInfoInputMinIn()
        carType.parkingInfoInputHourOut(hourIn)
        carType.parkingInfoInputMinOut()
        carType.parkingDurationPlusChargeCalc(carType)                          
        carType.parkingBill()
        carType.parkingLog()
    
    else:
        raise SystemExit
    
    
#-------------------------------------------------------------------------------------------------------------

