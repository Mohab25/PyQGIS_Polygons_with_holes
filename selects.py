la = iface.activeLayer()
feat = la.getFeatures()
feat = [f for f in feat]
for i in feat:
    g = eval(i.geometry().asJson())['coordinates'][0]
    if len(g)>1:
        la.select(i.id())
