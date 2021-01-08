#   Author      : Emin Kartci
#   Class       : 3rd Year - EE393.A
#   Department  : Electrical & Electronics Engineering

# import necessity functions
from math import sin, cos, sqrt, atan2,radians
import random
import numpy
import pandas as pd

# get customer and company classes
from Customer import Customer
from Company import Company

# create another class that holds almost everything
class SimulationEnvironment():

    # Constructor
    def __init__(self,companyCount = 5,customerCount = 10000):

        # By default:
            # 5         Company: 1 Slack Company & 4 Competitors
            # 10000     Customer
        self.companyCount   = companyCount
        self.customerCount  = customerCount

        # initialize the lists
        self.customerList   = []
        self.companyList    = []

        # initialize the log list
        self.simulationLog  = []
        self.summaryStr     = []

        self.createCustomers()
        self.createCompanies()

    # Get the real competitors from Foursquare API as a list
    def define_competitor_companies(self,newCompetitorList):

        # if there is no enough companies create them randomly
        if len(self.companyList)-1 != len(newCompetitorList):
            # Warn the user
            print("You need to provide {} competitors. Instead there are {} competitors.".format(len(self.companyList),len(newCompetitorList)))

            # ask if the user wants to continue with randoms
            randomAnswer = input("Do you want to continue with all random values? (Y/N)")

            # if answer is Y
            if randomAnswer.upper() == "Y":
                # create random companies
                self.createCompanies()
                # end this function
                return
            # otherwise there is no companies
            else:
                # inform the user
                print("The simulation is ended!!")
                # end this method
                return

        # if there is a competitor list iterate them
        for index,competitor in enumerate(newCompetitorList):
            # assign the competitors to the list
            self.companyList[index+1] = newCompetitorList[index]

    # creates random customers
    def createCustomers(self):

        # initialize a list
        customerList = []

        # iterate customer count times
        for i in range(self.customerCount):
            # create a customer
            currentCustomer = Customer(i)
            # append the list
            customerList.append(currentCustomer)

        # assign the objects list
        self.customerList = customerList

    # create random companies
    def createCompanies(self,serviceList = ["dessert","breakfast","coffee","drinks","salad"]):

        # initialize a list
        companyList = []

        # iterate company count times
        for i in range(self.companyCount):
            if i == 0:

                # create a random company
                currentCompany = Company("Main Company" # company name
                                         , random.randint(10, 20)  # long
                                         , random.randint(10, 20),  # lat
                                         [serviceList[random.randint(0, len(serviceList)) - 1],
                                          serviceList[random.randint(0, len(serviceList)) - 1]],
                                         random.randint(20, 30),  # price
                                         random.randint(10, 20),  # cost
                                         random.randint(400, 4000),  # sales Vol
                                         random.randint(10000, 100000),  # fixed cost
                                         random.randint(5, 20) / 100)  # tax rate

            else:

                # create a random company
                currentCompany = Company("Competitor{}".format(i)         # company name
                                         ,random.randint(10,20)     # long
                                         ,random.randint(10,20),    # lat
                                         [serviceList[random.randint(0,len(serviceList))-1],serviceList[random.randint(0,len(serviceList))-1]],
                                         random.randint(20,30),     # price
                                         random.randint(10,20),     # cost
                                         random.randint(400,4000),  # sales Vol
                                         random.randint(10000,100000),# fixed cost
                                         random.randint(5,20)/100)  # tax rate

            # append the list
            companyList.append(currentCompany)

        # assign the class's list
        self.companyList = companyList

    # calculate the distance between customer and company
    def calculateDistance(self,customer,company):

        # return the result
        return self.calculate_distance_lon_lat(customer.longitude,customer.latitude,company.longitude,company.latitude)


    # simulate a customer & company
    def simulate_customer_choice(self,customer,company,willPrint= True):

        # get the distance
        distance = self.calculateDistance(customer,company)

        # optional print
        #print("DISTANCE: {}\nMAX RANGE: {}".format(distance,customer.maxRestaurantRange))

        # if the company is in the customer field
        if customer.maxRestaurantRange > distance:

            # if customer has enough budget for company
            if customer.cash > company.averagePrice*0.8:

                # get a random service fee
                serviceFee = random.randint(int(min(customer.cash*0.5,company.averagePrice*0.7))
                                            ,int(min(customer.cash,company.averagePrice*1.2)))

                # get a random service cost
                serviceCost = serviceFee * (random.randint(30,70)/100)

                # append the price and cost
                company.priceList.append(serviceFee)
                company.costList.append(serviceCost)

                # create a string
                simulationInfo = "\nCustomer {} spend {} tl at {} which has a cost {}.".format(customer.id,serviceFee,company.name,serviceCost)

                # optionalPrint
                if willPrint:
                    print(simulationInfo)

                # add it to the log
                self.simulationLog.append(simulationInfo)

                # add this customer to the company's target
                company.targetCustomers.append(customer)

            else:

                # create a string
                simulationInfo = "\nCustomer {} has not enough budget for {} company.".format(customer.id,company.name)

                # optionalPrint
                if willPrint:
                    print(simulationInfo)

                # add it to the log
                self.simulationLog.append(simulationInfo)

        else:

            # create a string
            simulationInfo = "\nCompany {} is far away from {} customer.".format( company.name, customer.id)

            # optionalPrint
            if willPrint:
                print(simulationInfo)

            # add it to the log
            self.simulationLog.append(simulationInfo)


    # simulate many customers
    def execute_simulation(self,trialTime = 30000):

        # try trialTime times
        for trialIndex in range(trialTime):

            # get random customer and company
            randomCustomer = random.choice(self.customerList)
            randomCompany  = random.choice(self.companyList)

            # simulate them
            self.simulate_customer_choice(randomCustomer,randomCompany)

        # inform the user
        # optional print
        print("\n\nSimulation Completed Successfully !!")

    # after the simulation calculate the results and assign the company
    def calculate_simulation_results(self,willPrint = True):

        # iterate all companies
        for company in self.companyList:

            # convert the prices and costs in numpy array
            currentPrices = numpy.array(company.priceList)
            currentCosts  = numpy.array(company.costList)

            # calculate their averages
            company.averagePrice = numpy.average(currentPrices)
            company.averageUnitCost = numpy.average(currentCosts)

            # get average contribution margin
            company.contributionMargin = company.averagePrice - company.averageUnitCost

            # get new sales volume size
            company.salesVolume = currentCosts.size

            summaryString = "\nCompany: {} \tPROFIT: {:.2f} \tAvg Price: {:.2f}\t Avg Cost: {:.2f}\t Contribution Margin: {:.2f}\t Sales Vol: {}".format(
                company.name,
                company.netIncome,
                company.averagePrice,
                company.averageUnitCost,
                company.contributionMargin,
                company.salesVolume)

            # optional print
            if willPrint:

                print(summaryString)

            # append summary list
            self.summaryStr.append(summaryString)


    # print all companies
    def print_companies(self,printDescription = True,printIncomeStatement = False):

        # iterate companies
        for company in self.companyList:
            # print their description
            if printDescription:

                company.print_company_description()

            # print income statement
            elif printIncomeStatement:
                # print all values
                company.print_income_statement(willPrint=True)

    # print some customers
    def print_customers(self,printAmount = 10):

        # check the limit
        if printAmount > len(self.customerList):
            # warn the user
            print("\nThere are only {} customers. You typed {} customers!".format(len(self.customerList),printAmount))

        # print limited customers
        for customer in self.customerList[:printAmount]:
            # print it
            customer.print_customer()

    # write simulation log
    def report_simulation_log(self,willPrint = False,output_path = "simulation_log_report.txt"):

        # if will print is true
        if willPrint:

            # iterate all steps
            for statement in self.simulationLog:

                # print to the console
                print(statement)

        # create a txt file
        simulation_log_file = open(output_path,"w")

        # iterate all steps
        for statement in self.simulationLog:
            # write to the file
            simulation_log_file.write(statement)

        # close the file properly
        simulation_log_file.close()
        # inform the user
        print("\nThe log file is successfully created as {}".format(output_path))


    # report all companies and summary
    def report_company_results(self,output_path= "simulation_log_report_",targetCustomerLimit= 5):

        # iterate companies
        for company in self.companyList:

            # create a file for each company
            companyFile = open(output_path+company.name+".txt","w")

            # print them
            companyFile.write("\n COMPANY DESCRIPTION")

            companyFile.write(company.print_company_description(willPrint=False))

            companyFile.write("\n----------------------------------------------------------------------------")

            companyFile.write("\n COMPANY INCOME STATEMENT")

            companyFile.write(company.print_income_statement(willPrint=False))

            companyFile.write("\n----------------------------------------------------------------------------")

            companyFile.write("\n TARGET CUSTOMER ANALYSIS")

            # if limit is greater fix it
            if targetCustomerLimit > len(company.targetCustomers):
                # print all customers
                targetCustomerLimit = len(company.targetCustomers)

            # iterate customers
            for customer in company.targetCustomers[:targetCustomerLimit]:
                # write them
                companyFile.write(customer.print_customer(willPrint=False))


            # close the file properly
            companyFile.close()

            print("Company File is successfully created!!")

    # write simulation summary
    def report_simulation_summary(self,output_path="summary_report.txt",willPrint = False):

        # open summary file
        summary_file = open(output_path,"w")

        # write a header
        summary_file.write("\n\n SIMULATION SUMMARY REPORT \n\n")

        # iterate all summaries
        for sum in self.summaryStr:

            # write them
            summary_file.write(sum)

            if willPrint:
                print(sum,"\n\n")

            summary_file.write("\n----------------------------------------------------------------------------")

        # Make Advertisement :)
        summary_file.write("\n\nAll Rights Reserved @2020") # Emin Kartci

        # close the file properly
        summary_file.close()

        # inform the user
        print("Simulation Summary file submitted successfully!!")


    # calculate distance of 2 location
    def calculate_distance_lon_lat(self,lon1,lat1,lon2,lat2):

        # define earth radius
        earthRadius = 6373.0

        # calculate the differences
        difference_lon = lon2 - lon1
        difference_lat = lat2 - lat1


        # inspired from => https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude

        a = (sin(difference_lat / 2)) ** 2 + cos(lat1) * cos(lat2) * (sin(difference_lon / 2)) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = earthRadius * c

        # return the result
        return distance

    # Determine the Present value of money
    def calculate_PV(self, futureValue, period, interestRate):
        # use economy formula
        # PV = FV / (1+i)^period
        return futureValue * (1 + interestRate) ** (-period)

    # Determine the futuve value of money
    def calculate_FV(self, presentValue, period, interestRate):
        # use economy formula
        # FV = PV * (1+i)^period
        return presentValue * (1 + interestRate) ** period

    # report competitor's descriptions
    def save_competitor_descriptions(self,willPrint = False):
        # iterate all competitors
        for competitor in self.companyList[1:]:
            # save their descriptions
            competitor.save_company_description_to()

            if willPrint:
                competitor.print_company_description()

    # report competitor's descriptions
    def save_competitor_income_statements(self,willPrint = False):
        # iterate all competitors
        for competitor in self.companyList[1:]:
            # save their descriptions
            competitor.save_income_statement()

            if willPrint:
                competitor.print_income_statement()


    # Muhammed Ali Kumasoglu - (Emin Kartci Edited)
    def get_closest_competitors(self,centerLon=40.74,centerLat = -73.94,willPrint= True):

        # read data again
        df = pd.read_csv(r"newyorkcoffeewithdetails.csv", error_bad_lines=False)

        # initalize a dictionary
        distance_dict = {}

        # iterate and calculate all distances
        for index in range(len(df)):  # I take latitutude and longitude for every buisness

            # our latitude and longitude of surroindings
            currentLat = radians(df["location.lat"].iloc[index])
            currentLon = radians(df["location.lng"].iloc[index])

            distance = self.calculate_distance_lon_lat(centerLon,centerLat,currentLat,currentLon)

            # hold them at dictionary
            distance_dict[index] = distance

        # sort the values
        sorted_values = sorted(distance_dict.values())  # Sort the values
        sorted_distance_dict = {}

        # I sort my dictionary in terms of values from small to big
        for i in sorted_values:
            for k in distance_dict.keys():
                if distance_dict[k] == i:
                    sorted_distance_dict[k] = i
                    break

        # optional print
        if willPrint:
            print(sorted_distance_dict)

        # prepare a good result
        location_stats = pd.DataFrame(columns=["NAME", "LATITUDE", "LONGITUDE", "DISTANCE"])
        index_number_list = []
        distances_list = []

        # iteare get values
        for i in range(1, 6):
            index_number_list.append(list(sorted_distance_dict.keys())[i])
            distances_list.append(sorted_distance_dict[list(sorted_distance_dict.keys())[i]])

        # construct stats
        for j in range(len(distances_list)):
            location_stats = location_stats.append({"LATITUDE": df["location.lat"].iloc[index_number_list[j]],
                                                    "LONGITUDE": df["location.lng"].iloc[index_number_list[j]],
                                                    "NAME": df["name"].iloc[index_number_list[j]],
                                                    "DISTANCE": distances_list[j]}, ignore_index=True)
        if willPrint:
            print(location_stats.head())

        # return result
        return  location_stats




