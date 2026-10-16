"""Sun position for Manchester (NOAA solar-position algorithm) — sunrise, sunset, civil dusk and low-sun glare windows.
Used by the SQ Driving Data Lab daylight study. Pure Python, deterministic."""
import math, json, datetime as dt
LAT, LON = 53.4808, -2.2426   # Manchester city centre
def bst(d):  # UK clock offset (hours) for a date: last Sunday of March -> last Sunday of October
    y=d.year
    def lastsun(m):
        x=dt.date(y,m,31)
        while x.weekday()!=6: x-=dt.timedelta(days=1)
        return x
    return 1 if lastsun(3)<=d<lastsun(10) else 0
def solar(ts):  # ts = UTC datetime -> (elevation deg, azimuth deg)  NOAA algorithm
    jd = ts.timestamp()/86400.0 + 2440587.5
    T=(jd-2451545.0)/36525.0
    L0=(280.46646+T*(36000.76983+T*0.0003032))%360
    M=357.52911+T*(35999.05029-0.0001537*T)
    e=0.016708634-T*(0.000042037+0.0000001267*T)
    C=math.sin(math.radians(M))*(1.914602-T*(0.004817+0.000014*T))+math.sin(math.radians(2*M))*(0.019993-0.000101*T)+math.sin(math.radians(3*M))*0.000289
    tl=L0+C; om=125.04-1934.136*T; lam=tl-0.00569-0.00478*math.sin(math.radians(om))
    eps0=23+(26+((21.448-T*(46.815+T*(0.00059-T*0.001813))))/60)/60; eps=eps0+0.00256*math.cos(math.radians(om))
    dec=math.degrees(math.asin(math.sin(math.radians(eps))*math.sin(math.radians(lam))))
    y=math.tan(math.radians(eps/2))**2
    eq=4*math.degrees(y*math.sin(2*math.radians(L0))-2*e*math.sin(math.radians(M))+4*e*y*math.sin(math.radians(M))*math.cos(2*math.radians(L0))-0.5*y*y*math.sin(4*math.radians(L0))-1.25*e*e*math.sin(2*math.radians(M)))
    mins=ts.hour*60+ts.minute+ts.second/60
    tst=(mins+eq+4*LON)%1440
    ha=tst/4-180 if tst/4>=0 else tst/4+180
    lat=math.radians(LAT); d=math.radians(dec); h=math.radians(ha)
    cz=math.sin(lat)*math.sin(d)+math.cos(lat)*math.cos(d)*math.cos(h); cz=max(-1,min(1,cz))
    zen=math.degrees(math.acos(cz)); el=90-zen
    # refraction (approx)
    if el>-0.575:
        te=math.tan(math.radians(el))
        if el>5: r=58.1/te-0.07/te**3+0.000086/te**5
        elif el>-0.575: r=1735+el*(-518.2+el*(103.4+el*(-12.79+el*0.711)))
        el+=r/3600
    az=(math.degrees(math.atan2(math.sin(h), math.cos(h)*math.sin(lat)-math.tan(d)*math.cos(lat)))+180)%360
    return el, az
def day(d):
    off=bst(d); rows=[]
    for m in range(0,24*60):
        lt=dt.datetime(d.year,d.month,d.day,0,0)+dt.timedelta(minutes=m)
        ut=(lt-dt.timedelta(hours=off)).replace(tzinfo=dt.timezone.utc)
        rows.append((m,)+solar(ut))
    def first(cond, rng):
        for m,el,az in rng:
            if cond(el): return m
    up=[r for r in rows]
    sunrise=next(m for m,el,az in rows if el>-0.833)
    sunset=next(m for m,el,az in reversed(rows) if el>-0.833)+1
    dawn=next(m for m,el,az in rows if el>-6)
    dusk=next(m for m,el,az in reversed(rows) if el>-6)+1
    noon=max(rows,key=lambda r:r[1])
    glare_am=[m for m,el,az in rows if 0.5<el<15 and 7*60<=m<10*60]
    glare_pm=[m for m,el,az in rows if 0.5<el<15 and 15*60<=m<19*60]
    span=lambda L:(f"{L[0]//60:02d}:{L[0]%60:02d}–{(L[-1]+1)//60:02d}:{(L[-1]+1)%60:02d}" if L else "")
    az_at=lambda mm: round(rows[mm][2])
    f=lambda m:f"{m//60:02d}:{m%60:02d}"
    return {"date":d.isoformat(),"clock":"BST" if off else "GMT","sunrise":f(sunrise),"sunset":f(sunset),"dawn":f(dawn),"dusk":f(dusk),
            "daylight_min":sunset-sunrise,"noon_elev":round(noon[1],1),"glare_am":span(glare_am),"glare_am_min":len(glare_am),"glare_pm":span(glare_pm),"glare_pm_min":len(glare_pm),
            "rise_az":az_at(sunrise),"set_az":az_at(min(sunset,1439)),"dark_1630":rows[16*60+30][1]<-6,"dark_1730":rows[17*60+30][1]<-6,"dark_0745":rows[7*60+45][1]<-6}


def months(year=2027):
    return [day(dt.date(year, m, 15)) for m in range(1, 13)]


def extra():
    return {"shortest": day(dt.date(2026, 12, 21)), "longest": day(dt.date(2027, 6, 21)),
            "before_change": day(dt.date(2026, 10, 24)), "after_change": day(dt.date(2026, 10, 26))}
