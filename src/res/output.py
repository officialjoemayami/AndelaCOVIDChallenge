
class OUTPUT():
    def __init__(self, dif_min_days, dif_max_days, dif_min_weeks, dif_max_weeks, dif_min_months, dif_max_months, ci_min, ibrt_min_days, ibrt_min_weeks, ibrt_min_months, ci_max, ibrt_max_days, ibrt_max_weeks, ibrt_max_months, scbrt_min_days, scbrt_max_days, scbrt_min_weeks, scbrt_max_weeks, scbrt_min_months, scbrt_max_months, hbbrt_min_days, hbbrt_max_days, hbbrt_min_weeks, hbbrt_max_weeks, hbbrt_min_months, hbbrt_max_months, cfibrt_min_days, cfibrt_max_days, cfibrt_min_weeks, cfibrt_max_weeks, cfibrt_min_months, cfibrt_max_months, cfvbrt_min_days, cfvbrt_max_days, cfvbrt_min_weeks, cfvbrt_max_weeks, cfvbrt_min_months, cfvbrt_max_months):
        self.output = {}
        self.dif_min_days = int(dif_min_days)
        self.dif_min_weeks = int(dif_min_weeks)
        self.dif_min_months = int(dif_min_months)
        self.dif_max_days = int(dif_max_days)
        self.dif_max_weeks = int(dif_max_weeks)
        self.dif_max_months = int(dif_max_months)
        self.ci_min = int(ci_min)
        self.ibrt_min_days = int(ibrt_min_days)
        self.ibrt_min_weeks = int(ibrt_min_weeks)
        self.ibrt_min_months = int(ibrt_min_months)
        self.ci_max = int(ci_max)
        self.ibrt_max_days = int(ibrt_max_days)
        self.ibrt_max_weeks = int(ibrt_max_weeks)
        self.ibrt_max_months = int(ibrt_max_months)
        self.scbrt_min_days = int(scbrt_min_days)
        self.scbrt_min_weeks = int(scbrt_min_weeks)
        self.scbrt_min_months = int(scbrt_min_months)
        self.scbrt_max_days = int(scbrt_max_days)
        self.scbrt_max_weeks = int(scbrt_max_weeks)
        self.scbrt_max_months = int(scbrt_max_months)
        self.hbbrt_min_days = int(hbbrt_min_days)
        self.hbbrt_min_weeks = int(hbbrt_min_weeks)
        self.hbbrt_min_months = int(hbbrt_min_months)
        self.hbbrt_max_days = int(hbbrt_max_days)
        self.hbbrt_max_weeks = int(hbbrt_max_weeks)
        self.hbbrt_max_months = int(hbbrt_max_months)
        self.cfibrt_min_days = int(cfibrt_min_days)
        self.cfibrt_min_weeks = int(cfibrt_min_weeks)
        self.cfibrt_min_months = int(cfibrt_min_months)
        self.cfibrt_max_days = int(cfibrt_max_days)
        self.cfibrt_max_weeks = int(cfibrt_max_weeks)
        self.cfibrt_max_months = int(cfibrt_max_months)
        self.cfvbrt_min_days = int(cfvbrt_min_days)
        self.cfvbrt_min_weeks = int(cfvbrt_min_weeks)
        self.cfvbrt_min_months = int(cfvbrt_min_months)
        self.cfvbrt_max_days = int(cfvbrt_max_days)
        self.cfvbrt_max_weeks = int(cfvbrt_max_weeks)
        self.cfvbrt_max_months = int(cfvbrt_max_months)

    def result(self):
        # output
        output = {
        # the input data i got
        'data' : { },
        # the base case estimation
        'impact' : {
            'currentlyInfected' : self.ci_min,
            'infectionsByRequestedTime' : {
            'days' : self.ibrt_min_days,
            'weeks' : self.ibrt_min_weeks,
            'months' : self.ibrt_min_months
            },
            'severeCasesByRequestedTime' : {
            'days' : self.scbrt_min_days,
            'weeks' : self.scbrt_min_weeks,
            'months' : self.scbrt_min_months
            },
            'hospitalBedsByRequestedTime' : {
            'days' : self.hbbrt_min_days,
            'weeks' : self.hbbrt_min_weeks,
            'months' : self.hbbrt_min_months
            },
            'casesForICUByRequestedTime' : {
            'days' : self.cfibrt_min_days,
            'weeks' : self.cfibrt_min_weeks,
            'months' : self.cfibrt_min_months
            },
            'casesForVentilatorsByRequestedTime' : {
            'days' : self.cfvbrt_min_days,
            'weeks' : self.cfvbrt_min_weeks,
            'months' : self.cfvbrt_min_months
            },
            'dollarsInFlight' : {
            'days' : self.dif_min_days,
            'weeks' : self.dif_min_weeks,
            'months' : self.dif_min_months
            }
        },
        # the server case estimation
        'severImpact' : {
            'currentlyInfected' : self.ci_max,
            'infectionsByRequestedTime' : {
            'days' : self.ibrt_max_days,
            'weeks' : self.ibrt_max_weeks,
            'months' : self.ibrt_max_months
            },
            'severeCasesByRequestedTime' : {
            'days' : self.scbrt_max_days,
            'weeks' : self.scbrt_max_weeks,
            'months' : self.scbrt_max_months
            },
            'hospitalBedsByRequestedTime' : {
            'days' : self.hbbrt_max_days,
            'weeks' : self.hbbrt_max_weeks,
            'months' : self.hbbrt_max_months
            },
            'casesForICUByRequestedTime' : {
            'days' : self.cfibrt_max_days,
            'weeks' : self.cfibrt_max_weeks,
            'months' : self.cfibrt_max_months
            },
            'casesForVentilatorsByRequestedTime' : {
            'days' : self.cfvbrt_max_days,
            'weeks' : self.cfvbrt_max_weeks,
            'months' : self.cfvbrt_max_months
            },
            'dollarsInFlight' : {
            'days' : self.dif_max_days,
            'weeks' : self.dif_max_weeks,
            'months' : self.dif_max_months
            },
        }
        }
        return output

    