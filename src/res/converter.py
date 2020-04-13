d_m = 0.0328767 # one day equals 0.0328767 months (using google standard converter)
w_d = 7 # one week equals to 7 days (using google standard converter)
w_m = 0.230137 # one week equals to 0.230137 months (using google standard converter)
m_d = 30.4167 # one month equals to 30.4167 days (using google standard converter)
m_w = 4.34524 # one month equals to 4.34524 weeks (using google standard converter)
d_w = 0.142857 # one day equals 0.142857 weeks (using google standard converter)
    
def dm(days):
    # convert days to months
    f = days * d_m
    return f
def wd(weeks):
    # convert weeks to days
    f = weeks * w_d
    return f
def wm(weeks):
    # convert weeks to months
    f = weeks * w_m
    return f
def md(months):
    # convert months to days
    f = months * m_d
    return f
def mw(months):
    # convert months to weeks
    f = months * m_w
    return f
def dw(days):
    # convert days to weeks
    f = days * d_w
    return f

