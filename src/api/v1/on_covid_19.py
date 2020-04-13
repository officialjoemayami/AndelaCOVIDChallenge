# import from res, custom function used for this project
from res import factors as f
from res import usd
from res.output import OUTPUT



class COVID():
    def __init__(self, data):
        # collecting variable datapoints
        self.rc = data['reportedCases']
        self.pt = data['periodType']
        self.tte = data['timeToElapse']
        self.thb = data['totalHospitalBeds']
        self.usdc = data['region']['avgDailyIncomeInUSD']

        # declare constant points
        self.e = 3 # exponetial increase of currentlyInfected people is set to default 3days.
        self.ep = 2 # exponetial power is set to 2 which means currentlyInfected people doubles every (e)days 
        self.min, self.max = (10, 50) # impact (min) vs server impact (max)
        self.ip = 0.15 # default % of infectionsByRequestedTime
        self.bp = 0.35 # default % of beds available in hospital
        self.icup = 0.5 # default % for icu care
        self.vp = 0.2 # default % for ventilators
        self.r = 0.65 # default % of the region earnings

    def on_convid_19_estimator(self):
        # convert data to days, weeks and months
        fd, fw, fm = f.factor(self.pt, self.tte, self.e, self.ep) # get powered factor in days, weeks, and months
        usd_days, usd_weeks, usd_months = usd.convertUSD(self.usdc, self.tte, self.pt) # get usd value in days, weeks and months

        # begin estimation
        ab = self.thb * self.bp # avialable beds
        ci_min, ci_max = (self.rc * self.min, self.rc * self.max) # get currentlyInfected for both impact (min) and severImpact (max)
        ibrt_min_days, ibrt_min_weeks, ibrt_min_months = (ci_min * fd, ci_min * fw, ci_min * fm) # get infecectionsByRequestedTime in days, weeks, and months for impact
        ibrt_max_days, ibrt_max_weeks, ibrt_max_months = (ci_max * fd, ci_max * fw, ci_max * fm) # get infectionsByRequestedTime in days, weeks, and months for severeImpact
        
        scbrt_min_days, scbrt_min_weeks, scbrt_min_months = (ibrt_min_days * self.ip, ibrt_min_weeks * self.ip, ibrt_min_months * self.ip) # get (p)% of infectionsByRequestedTime for Impact
        scbrt_max_days, scbrt_max_weeks, scbrt_max_months = (ibrt_max_days * self.ip, ibrt_max_weeks * self.ip, ibrt_max_months * self.ip) # get (p)% of infectionsByRequestedTime for severeImpact
        
        hbbrt_min_days, hbbrt_min_weeks, hbbrt_min_months = (ab - scbrt_min_days, ab - scbrt_min_weeks, ab - scbrt_min_months) # get hospitalBedsByRequestedTime in days, weeks, and months Impact
        hbbrt_max_days, hbbrt_max_weeks, hbbrt_max_months = (ab - scbrt_max_days, ab - scbrt_max_weeks, ab - scbrt_max_months) # get hospitalBedsByRequestedTime in days, weeks, and months for severeImpact
        
        cfibrt_min_days, cfibrt_min_weeks, cfibrt_min_months = (ibrt_min_days * self.icup, ibrt_min_weeks * self.icup, ibrt_min_months * self.icup) # get casesForICUByRequestedTime in days, weeks and months for Impact
        cfibrt_max_days, cfibrt_max_weeks, cfibrt_max_months = (ibrt_max_days * self.icup, ibrt_max_weeks * self.icup, ibrt_max_months * self.icup) # get casesForICUByRequestedTime in days, weeks and months for severeImpact
        
        cfvbrt_min_days, cfvbrt_min_weeks, cfvbrt_min_months = (ibrt_min_days * self.vp, ibrt_min_weeks * self.vp, ibrt_min_months * self.vp) # get casesForVentilatorsByRequestedTime in days, weeks and months for Impact
        cfvbrt_max_days, cfvbrt_max_weeks, cfvbrt_max_months = (ibrt_max_days * self.vp, ibrt_max_weeks * self.vp, ibrt_max_months * self.vp) # get casesForVentilatorsByRequestedTime in days, weeks and months for severeImpact
        
        dif_min_days, dif_min_weeks, dif_min_months = ((ibrt_min_days * self.r) * usd_days, (ibrt_min_weeks * self.r) * usd_weeks, (ibrt_min_months * self.r) * usd_months) # get dollarsInFlight in days, weeks, and months Impact
        dif_max_days, dif_max_weeks, dif_max_months = ((ibrt_max_days * self.r) * usd_days, (ibrt_max_weeks * self.r) * usd_weeks, (ibrt_max_months * self.r) * usd_months) # get dollarsInflight in days, weeks, and months for severImpact

        # get result
        result = OUTPUT(dif_min_days, dif_max_days, dif_min_weeks, dif_max_weeks, dif_min_months, dif_max_months, ci_min, ibrt_min_days, ibrt_min_weeks, ibrt_min_months, ci_max, ibrt_max_days, ibrt_max_weeks, ibrt_max_months, scbrt_min_days, scbrt_max_days, scbrt_min_weeks, scbrt_max_weeks, scbrt_min_months, scbrt_max_months, hbbrt_min_days, hbbrt_max_days, hbbrt_min_weeks, hbbrt_max_weeks, hbbrt_min_months, hbbrt_max_months, cfibrt_min_days, cfibrt_max_days, cfibrt_min_weeks, cfibrt_max_weeks, cfibrt_min_months, cfibrt_max_months, cfvbrt_min_days, cfvbrt_max_days, cfvbrt_min_weeks, cfvbrt_max_weeks, cfvbrt_min_months, cfvbrt_max_months)
        

        return result
