from res import converter as conv

def factor(pt, tte, e, ep):
  if pt == 'days':
    # find the powered factor in days
    d = int(tte / e)
    d = int(ep**d)
    d_w = int(conv.dw(d)) # convert days powered factor to week
    d_m = int(conv.dm(d)) # convert days powered factor to month
    f = (d, d_w, d_m)
  
  elif pt == 'weeks':
    # find the powered factor in weeks
    w_d = int(conv.wd(tte)) # convert to days
    d = int(ep**(w_d / e))
    d_w = int(conv.dw(d))
    d_m = int(conv.dm(d))
    f = (d, d_w, d_m)

  elif pt == 'months':
    # find the powered factor in months
    m_d = int(conv.md(tte)) # conver to days
    d = int(ep**(m_d / e))
    d_w = int(conv.dw(d))
    d_m = int(conv.dm(d))
    f = (d, d_w, d_m)

  return f