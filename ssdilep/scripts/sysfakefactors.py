import os
import ROOT
from array import array

ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0000)

# -------------------------------------------------------------------------------------
# config
# -------------------------------------------------------------------------------------
RUN = "VeryLoose"
#RUN = "AtLeastLoose"
#RUN = "ptRatio"
#RUN = "TwoSS"
#RUN = "TwoOS"

#RUN = "NotTight"
#RUN = "NotTightAtLeastLoose"
#RUN = "LeadTauPt65AtLeastLoose"
#RUN = "LeadTauPt65NotTight"

#indir   = "/coepp/cephfs/mel/fscutti/Analysis/ssdilep/scripts/Fakes23Jan"
#indir   = "/coepp/cephfs/mel/fscutti/Analysis/ssdilep/scripts/FakesLTT"
#indir	= "/coepp/cephfs/mel/xuanhaoz/SSDiLep/SUSY11TauPlots/FF/%s"%(RUN)
indir	= "/coepp/cephfs/mel/xuanhaoz/SSDiLep/jobs/SUSY11Data.v3.r1/FF/%s"%(RUN)

tag     = "r1"
name    = "r1"


#--------------
# taulead_pt
#--------------
# pt
var     = "taulead_pt"
axislab = "p_{T}(#tau_{lead}) [GeV]"
new_bins = array('d', [0.,25.,50.,75.,100.,125.,150.,200.,300.,600.])

#--------------
# tausublead_pt
#--------------
# pt
#var     = "tausublead_pt"
#axislab = "p_{T}(#tau_{sublead}) [GeV]"
#new_bins = array('d', [0.,25.,50.,75.,100.,150.,200.,250.,300.,600.])

#new_bins = array('d', [0.,25.,28.,32.,36.,40.,45.,60.,80.,300.])
#new_bins = array('d', [0.,25.,28.,32.,36.,40.,45.,300.])
#new_bins = array('d', [0.,25.,28.,32.,36.,40.,300.])
#new_bins = array('d', [0.,22.,40.,60.,90.,300.])

'''
# eta
var     = "mulead_eta"
axislab = "#eta(#mu_{lead})"
new_bins = array('d', [-2.5, -2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0, 2.5,])
'''


infile  = "merged_ff_"+var+"_"+name+"_"+tag+".root"
outfile = "sys_ff_"+var+"_"+name+"_"+tag+".root"
inf     = ROOT.TFile.Open(os.path.join(indir,infile),"READ")


# -------------------------------------------------------------------------------------

hdict = {}

hdict["NOM"] = inf.Get("h_ff_F1").Clone()
#hdict["NOM"] = inf.Get("h_ff_F2").Clone()
n_bins = hdict["NOM"].GetNbinsX()
#for i in [2,3,4,5,6,7,8,9,10,11,12,13,14,15]:
for i in [1,2,3,4,5,6,7,8]:#9,10]:
#for i in [2]:
  hdict["SYS%s"%str(i)] = inf.Get("h_ff_F%s"%str(i)).Clone()

slabel = {}
#slabel["NOM"]  = "nominal"
slabel["SYS1"] = "p_{T}(#tau_{lead}) > 30 GeV"

slabel["SYS2"] = "p_{T}(jet) > 170 GeV"
slabel["SYS3"] = "p_{T}(jet) > 130 GeV"
slabel["SYS4"] = "#Delta#phi(#tau,jet) > 2.9"
slabel["SYS5"] = "#Delta#phi(#tau,jet) < 2.5"
slabel["SYS6"] = "N(jets) > 1"
slabel["SYS7"] = "N(jets) > 2"
slabel["SYS8"] = "0.95 < p_{T}(#tau_lead)/p_{T}(jetlead) < 1.05"
#slabel["SYS8"] = "p_{T}(jet) > 40 GeV"
#slabel["SYS9"] = "MC + 5%"
#slabel["SYS10"] = "MC - 5%"

#slabel["NOM"]  = "one jet"
#slabel["SYS2"] = "one jet, den fails iso or d0"
#slabel["SYS3"] = "al one jet"
#slabel["SYS4"] = "al one jet, gradient"
#slabel["SYS5"] = "al one jet, gradient, nom med"
#slabel["SYS6"] = "al one jet, gradient, nom med, den d015"
#slabel["SYS7"] = "al one jet, fixedcut, den fails iso or d0"

g_sys_ff = ROOT.TGraphAsymmErrors(n_bins)
g_nom_ff = ROOT.TGraphAsymmErrors(n_bins)


for ibin in xrange(1,n_bins+1):
    g_sys_ff.SetPoint(ibin,hdict["NOM"].GetBinCenter(ibin),hdict["NOM"].GetBinContent(ibin))  
    g_nom_ff.SetPoint(ibin,hdict["NOM"].GetBinCenter(ibin),hdict["NOM"].GetBinContent(ibin))  

    g_sys_ff.SetPointEYlow(ibin, hdict["NOM"].GetBinErrorLow(ibin))
    g_sys_ff.SetPointEYhigh(ibin, hdict["NOM"].GetBinErrorUp(ibin))
    
    g_nom_ff.SetPointEYlow(ibin, hdict["NOM"].GetBinErrorLow(ibin))
    g_nom_ff.SetPointEYhigh(ibin, hdict["NOM"].GetBinErrorUp(ibin))

    g_sys_ff.SetPointEXlow(ibin, hdict["NOM"].GetBinWidth(ibin)/2.)
    g_sys_ff.SetPointEXhigh(ibin, hdict["NOM"].GetBinWidth(ibin)/2.)
    
    g_nom_ff.SetPointEXlow(ibin, hdict["NOM"].GetBinWidth(ibin)/2.)
    g_nom_ff.SetPointEXhigh(ibin, hdict["NOM"].GetBinWidth(ibin)/2.)

g_nom_ff.SetNameTitle("g_ff_stat","")
g_sys_ff.SetNameTitle("g_ff_stat_sys","")

for sys,hist in hdict.iteritems():
  if sys == "NOM": continue
  for ibin in xrange(1,n_bins+1):
    
    nom_minus_sys = hdict["NOM"].GetBinContent(ibin)-hdict[sys].GetBinContent(ibin)
    
    if nom_minus_sys>0. and nom_minus_sys > hdict[sys].GetBinErrorUp(ibin):
     g_sys_ff.SetPointEYlow(ibin, max(g_sys_ff.GetErrorYlow(ibin),abs(nom_minus_sys)))

    if nom_minus_sys<0. and abs(nom_minus_sys) > hdict[sys].GetBinErrorLow(ibin):
     g_sys_ff.SetPointEYhigh(ibin, max(g_sys_ff.GetErrorYhigh(ibin),abs(nom_minus_sys)))
    
c = ROOT.TCanvas("c_ff","c_ff",650,600)
c.SetTopMargin(0.05)
c.SetBottomMargin(0.13)
c.SetLeftMargin(0.13)
c.SetRightMargin(0.05)
c.SetTickx()
c.SetTicky()

#l = ROOT.TLegend(0.15,0.65,0.55,0.9)
l = ROOT.TLegend(0.60,0.5,0.9,0.9)
l.SetBorderSize(0)
l.SetFillColor(0)
l.SetFillStyle(0)


g_sys_ff.GetYaxis().SetTitle("Fake-factor")
g_sys_ff.GetXaxis().SetTitle(axislab)
g_sys_ff.GetYaxis().SetTitleSize(0.045)
g_sys_ff.GetXaxis().SetTitleSize(0.045)
g_sys_ff.GetYaxis().SetLabelSize(0.045)
g_sys_ff.GetXaxis().SetLabelSize(0.045)
g_sys_ff.GetYaxis().SetTitleOffset(1.2)
g_sys_ff.GetXaxis().SetTitleOffset(1.2)
g_sys_ff.GetXaxis().SetRangeUser(min(new_bins),max(new_bins))
g_sys_ff.SetLineColor(ROOT.kYellow)
g_sys_ff.SetMarkerColor(ROOT.kBlack)
g_sys_ff.SetFillColor(ROOT.kYellow)
g_sys_ff.SetMarkerSize(1.3)
g_sys_ff.SetMaximum(0.20)
g_sys_ff.SetMinimum(0.0)

g_nom_ff.GetYaxis().SetTitle("Fake-factor")
g_nom_ff.GetXaxis().SetTitle(axislab)
g_nom_ff.GetYaxis().SetTitleSize(0.045)
g_nom_ff.GetXaxis().SetTitleSize(0.045)
g_nom_ff.GetYaxis().SetLabelSize(0.045)
g_nom_ff.GetXaxis().SetLabelSize(0.045)
g_nom_ff.GetYaxis().SetTitleOffset(1.2)
g_nom_ff.GetXaxis().SetTitleOffset(1.2)
g_nom_ff.GetXaxis().SetRangeUser(min(new_bins),max(new_bins))
g_nom_ff.SetLineColor(ROOT.kBlack)
g_nom_ff.SetLineWidth(2)
g_nom_ff.SetMarkerColor(ROOT.kBlack)
g_nom_ff.SetMarkerStyle(20)
g_nom_ff.SetMarkerSize(0.9)
g_nom_ff.SetMaximum(0.20)
g_nom_ff.SetMinimum(0.0)

c.cd() 

g_sys_ff.Draw("APE2")
g_nom_ff.Draw("SAME,P")
l.SetHeader("Nominal Fake-factor")
l.AddEntry(g_sys_ff,"stat.+sys.","F")
l.AddEntry(g_nom_ff,"stat.","PL")
l.Draw()
c.RedrawAxis()

c2 = ROOT.TCanvas("c_sys","c_sys",650,600)
c2.SetTopMargin(0.05)
c2.SetBottomMargin(0.13)
c2.SetLeftMargin(0.13)
c2.SetRightMargin(0.05)
c2.SetTickx()
c2.SetTicky()

#l2 = ROOT.TLegend(0.15,0.5,0.45,0.9)
l2 = ROOT.TLegend(0.6,0.5,0.9,0.9)
l2.SetBorderSize(0)
l2.SetFillColor(0)
l2.SetFillStyle(0)

c2.cd()

hdict["NOM"].SetStats(0)
hdict["NOM"].SetLineWidth(2)
hdict["NOM"].Draw()
l2.SetHeader("Systematics")

l2.AddEntry(hdict["NOM"],"nominal","PL")

for sys,hist in hdict.iteritems():
    if sys == "NOM": continue
    hist.Draw("SAME,E1")
    l2.AddEntry(hist,slabel[sys],"PL")

hdict["NOM"].Draw("SAME,PE1")

l2.Draw()

c.SaveAs(os.path.join(indir,c.GetName()+"_%s.eps"%tag))
c2.SaveAs(os.path.join(indir,c2.GetName()+"_%s.eps"%tag))

outfile = ROOT.TFile.Open(os.path.join(indir,outfile),"RECREATE")

outfile.WriteTObject(g_sys_ff)
outfile.WriteTObject(g_nom_ff)
outfile.WriteTObject(c)
outfile.WriteTObject(c2)

