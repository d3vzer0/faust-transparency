import faust

app = faust.App('faust-transparancy', 
    broker='kafka://localhost:29092',
    origin='proj',
    autodiscover=['proj.transparency'] )
