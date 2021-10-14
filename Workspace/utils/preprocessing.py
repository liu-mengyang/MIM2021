import pandas as pd
import copy

from Flight import Flight
from Employee import Employee


class DataLoader():
    def __init__(self, path_employees, path_flights):
        self.df_employees = pd.read_csv(path_employees).fillna(0)
        self.df_flights = pd.read_csv(path_flights).fillna(0)

    def dump_data(self):
        # dump employees
        employees = []
        for row in self.df_employees.iterrows():
            EmpNo = row[1][0]
            if row[1][1] == 'Y':
                Caption = True
            else:
                Caption = False
            if row[1][2] == 'Y':
                FirstOfficer = True
            else:
                FirstOfficer = False
            if row[1][3] == 'Y':
                Deadhead = True
            else:
                Deadhead = False
            Base = row[1][4]
            DutyCostPerHour = row[1][5]
            ParingCostPerHour = row[1][6]
            employees.append(Employee(EmpNo, Caption, FirstOfficer, Deadhead, Base, 
                                    DutyCostPerHour, ParingCostPerHour))
        # dump flights
        flights = []
        for row in self.df_flights.iterrows():
            FltNum = row[1][0]
            DptrDate= int(row[1][1].split('/')[1])
            DptrTime = 60*int(row[1][2].split(':')[0])+int(row[1][2].split(':')[1])
            DptrStn = row[1][3]
            ArrvDate = int(row[1][4].split('/')[1])
            ArrvTime = 60*int(row[1][5].split(':')[0])+int(row[1][5].split(':')[1])
            ArrvStn = row[1][6]
            flights.append(Flight(FltNum, 
                                  DptrDate, DptrTime, DptrStn,
                                  ArrvDate, ArrvTime, ArrvStn))
        return employees, flights

    # get different crew
    def get_C(self):
        C = list(self.df_employees['EmpNo']) # all crew
        C1 = [] # crew only with caption
        for row in self.df_employees.iterrows():
            if row[1][1] == 'Y' and row[1][2] == 0:
                C1.append(row[1][0])
        C2 = [] # crew with caption and first officer
        for row in self.df_employees.iterrows():
            if row[1][2] == 'Y' and row[1][1] == 'Y':
                C2.append(row[1][0])
        C3 = [] # crew only with first officer
        for row in self.df_employees.iterrows():
            if row[1][2] == 'Y' and row[1][1] == 0:
                C3.append(row[1][0])
        return C, C1, C2, C3

    # get airport
    def get_AP(self):
        AP = [] # all airports
        for row in self.df_flights.iterrows():
            if row[1][3] not in AP:
                AP.append(row[1][3])
            if row[1][6] not in AP:
                AP.append(row[1][6])
        return AP

    # get base
    def get_Base(self):
        Base = [] # all bases
        for row in self.df_employees.iterrows():
            if row[1][4] not in Base:
                Base.append(row[1][4])
        return Base
    
    # get flight
    def get_F(self):
        Base = self.get_Base()
        F = [] # all flights
        F_leave_base = [] # all leave base flights
        F_arrive_base = [] # all arrive base flights
        for i in range(len(Base)):
            temp_a = []
            temp_b = []
            F_leave_base.append(temp_a)
            F_arrive_base.append(temp_b)

        for row in self.df_flights.iterrows():
            F.append(row[1][0]+'/'+str(row[1][1]).split('/')[1])
            for i in range(len(Base)):
                if (row[1][3] == Base[i]):
                    F_leave_base[i].append(row[1][0]+'/'+str(row[1][1]).split('/')[1])
                if (row[1][6] == Base[i]):
                    F_arrive_base[i].append(row[1][0]+'/'+str(row[1][1]).split('/')[1])

        return F, F_leave_base, F_arrive_base

    # get the minimize day in dataset.
    def get_min_day(self):
        day_min = 1000
        for row in self.df_flights.iterrows():
            this_day = int(row[1][1].split('/')[1])
            if this_day < day_min:
                day_min = this_day
        return day_min

    # get False Flights
    def get_FF(self, minCT=40):
        FF = []
        _, flights = self.dump_data()
        for flight_a in flights:
            for flight_b in flights:
                if flight_a.arr_stn is not flight_b.dpt_stn:
                    FF.append((flight_a.number+'/'+str(flight_a.dpt_date), flight_b.number+'/'+str(flight_b.dpt_date)))
                    continue
                arrv_time_i = 24*60*flight_a.arr_date + flight_a.arr_time
                dptr_time_j = 24*60*flight_b.dpt_date + flight_b.dpt_time
                if dptr_time_j - arrv_time_i < minCT:
                    FF.append((flight_a.number+'/'+str(flight_a.dpt_date), flight_b.number+'/'+str(flight_b.dpt_date)))
        # df_flights_temp = []
        # for row_i in self.df_flights.iterrows():
        #     df_flights_temp.append([row_i[1][0],row_i[1][1],row_i[1][2],row_i[1][3],
        #                             row_i[1][4],row_i[1][5],row_i[1][6]])
        # for row_i in self.df_flights.iterrows():
        #     for row_j in df_flights_temp:
        #         if (row_i[1][3] is not row_j[6]):
        #             FF.append((row_i[1][0]+'/'+str(row_i[1][1]).split('/')[1],
        #                       (row_j[0]+'/'+str(row_j[1]).split('/')[1])))
        #         # dptr_time_i = 24*60*(int(row_i[1][1].split('/')[1])-self.get_min_day())\
        #         #                 + 60*int(row_i[1][2].split(':')[0])\
        #         #                 + int(row_i[1][2].split(':')[1])
        #         arrv_time_i = 24*60*(int(row_i[1][4].split('/')[1])-self.get_min_day())\
        #                         + 60*int(row_i[1][5].split(':')[0])\
        #                         + int(row_i[1][5].split(':')[1])
        #         dptr_time_j = 24*60*(int(row_j[1].split('/')[1])-self.get_min_day())\
        #                         + 60*int(row_j[2].split(':')[0])\
        #                         + int(row_j[2].split(':')[1])
        #         # arrv_time_j = 24*60*(int(row_i[1][4].split('/')[1])-self.get_min_day())\
        #         #                 + 60*int(row_i[1][5].split(':')[0])\
        #         #                 + int(row_i[1][5].split(':')[1])

        #         if dptr_time_j - arrv_time_i < minCT:
        #             FF.append((row_i[1][0]+'/'+str(row_i[1][1]).split('/')[1],
        #                       (row_j[0]+'/'+str(row_j[1]).split('/')[1])))
        return FF



if __name__=="__main__":
    data_loader = DataLoader('data/Data A-Crew.csv', 'data/Data A-Flight.csv')
    print(data_loader.get_min_day())