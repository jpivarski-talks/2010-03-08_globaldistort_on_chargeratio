import ROOT
execfile("/home/jpivarski/bin/tdrstyle.py")

f = ROOT.TF2("f", "0.0005 * (exp(-(1./y)**2/2./0.01**2) - exp(-(1./x)**2/2./0.01**2))", 0, 200., 0, 200.)
f.GetXaxis().SetTitle("p_{T} of bottom track (GeV/c)")
f.GetYaxis().SetTitle("p_{T} of top track (GeV/c)")
f.GetXaxis().CenterTitle()
f.GetYaxis().CenterTitle()
f.GetXaxis().SetTitleOffset(1.1)
f.GetYaxis().SetTitleOffset(1)

f.Draw("colz")
ROOT.gPad.SaveAs("plot2d.png")


