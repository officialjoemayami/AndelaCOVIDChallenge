from res import converter as conv

def convertUSD(usd, tte, pt):
  if pt == 'days':
    # find the powered factor in days
    d = usd * tte
    print('DOLLAR IS ' + str(d))
    d_w = conv.dw(d) # convert days powered factor to week
    d_m = conv.dm(d) # convert days powered factor to month
    f = (d, d_w, d_m)
  
  elif pt == 'weeks':
    # find the powered factor in weeks
    w_d = conv.wd(tte) # convert to days
    d = usd * w_d
    d_w = conv.dw(d)
    d_m = conv.dm(d)
    f = (d, d_w, d_m)

  elif pt == 'months':
    # find the powered factor in months
    m_d = conv.md(tte) # conver to days
    d = usd * m_d
    d_w = conv.dw(d)
    d_m = conv.dm(d)
    f = (d, d_w, d_m)

  return f