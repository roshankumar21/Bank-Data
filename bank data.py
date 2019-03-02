class BankData:
    def __str__(self):
        return "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t".format(self.age,
                                                                                             self.job,
                                                                                             self.marital,
                                                                                             self.education,
                                                                                             self.default,
                                                                                             self.balance,
                                                                                             self.housing,
                                                                                             self.loan,
                                                                                             self.contact,
                                                                                             self.day,
                                                                                             self.month,
                                                                                             self.duration,
                                                                                             self.campaign,
                                                                                             self.pdays,
                                                                                             self.previous,
                                                                                             self.poutcome,
                                                                                             self.y
                                                                                             )

    def __init__(self, age, job, marital, education, default, balance, housing, loan, contact, day, month, duration,
                 campaign, pdays, previous, poutcome, y):
        self.age = age
        self.job = job
        self.marital = marital
        self.education = education
        self.default = default
        self.balance = balance
        self.housing = housing
        self.loan = loan

        self.contact = contact
        self.day = day
        self.month = month
        self.duration = duration
        self.campaign = campaign
        self.pdays = pdays
        self.previous = previous
        self.poutcome = poutcome
        self.y = y


def getAllJobs(bData):
    s = set()
    for _ in bData:
        s.add(_.job)
    return s


if __name__ == '__main__':
    data = None
    d = []
    with open('d:\\bank.csv', 'r') as f:
        cols = []
        rows = f.readlines()
        for row in rows:
            cols = row.split(';')
            data = BankData(age=cols[0].replace('"', ''),
                            job=cols[1].replace('"', ''),
                            marital=cols[2].replace('"', ''),
                            education=cols[3].replace('"', ''),
                            default=cols[4].replace('"', ''),
                            balance=cols[5].replace('"', ''),
                            housing=cols[6].replace('"', ''),
                            loan=cols[7].replace('"', ''),
                            contact=cols[8].replace('"', ''),
                            day=cols[9].replace('"', ''),
                            month=cols[10].replace('"', ''),
                            duration=cols[11].replace('"', ''),
                            campaign=cols[12].replace('"', ''),
                            pdays=cols[13].replace('"', ''),
                            previous=cols[14].replace('"', ''),
                            poutcome=cols[15].replace('"', ''),
                            y=cols[16].replace('"', ''))
            d.append(data)
print(data)

