import os
import ROOT
from array import array


# -------------------------------------------------------------------------------------
# config
# -------------------------------------------------------------------------------------
RUN = "VeryLoose"
#RUN = "AtLeastLoose"
#RUN = "noUnpresc"
#RUN = "TwoSS"
#RUN = "TwoOS"

#RUN = "NotMedium"
#RUN = "NotMediumAtLeastLoose"
#RUN = "oneTrack"
#RUN = "threeTrack"

#indir     = "/coepp/cephfs/mel/fscutti/Analysis/ssdilep/scripts/FakesLTT"
#indir     = "/coepp/cephfs/mel/fscutti/Analysis/ssdilep/scripts/FakesSteve"
indir	  = "/coepp/cephfs/mel/xuanhaoz/SSDiLep/jobs/SUSY11Data.v3.r1/FF/%s"%(RUN)

tag       = "r1"
name      = "r1"

# pt 
var       = "taulead_pt"


#--------------
# taulead_pt
#--------------
new_bins = array('d', [0.,25.,50.,75.,100.,125.,150.,200.,300.,600.])

#--------------
# tausublead_pt
#--------------
#new_bins = array('d', [0.,25.,50.,75.,100.,150.,200.,250.,300.,600.])

#new_bins = array('d', [0.,25.,28.,32.,36.,40.,45.,300.])
#new_bins = array('d', [0.,25.,28.,32.,36.,40.,300.])
#new_bins = array('d', [0.,25.,40.,60.,90.,300.])

'''
# eta
new_bins = array('d', [-2.5, -2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0, 2.5,])
var       = "mulead_eta"
'''

infile    = "hists_"+var+"_FAKES_%s_F%s_"+tag+".root"
outfile   = "ff_"+var+"_"+name+"_"+tag+"_F%s.root"
outmerged = "merged_ff_"+var+"_"+name+"_"+tag+".root"

# -------------------------------------------------------------------------------------


ROOT.gROOT.SetBatch(True)
rcol = [
   ROOT.kBlack,
   #ROOT.kBlue+1,
   ROOT.kRed,
   #ROOT.kRed+1, 
   #ROOT.kRed+2,
   #ROOT.kRed+3,
   #ROOT.kGreen,
   #ROOT.kGreen+1,
   ROOT.kGreen+2,
   #ROOT.kGreen+3,
   ROOT.kBlue,
   #ROOT.kBlue+1,
   #ROOT.kBlue+2,
   #ROOT.kBlue+3,
   #ROOT.kMagenta, 
   #ROOT.kMagenta+1,
   ROOT.kMagenta+2,
   #ROOT.kMagenta+3,
   ROOT.kYellow,
   ROOT.kYellow+1,
   #ROOT.kYellow+2,
   #ROOT.kYellow+3,
   ROOT.kOrange+7,
   ROOT.kCyan+1,
   ROOT.kBlue+3,
   ]

"""
c_all = ROOT.TCanvas("c_all_ff","c_all_ff",650,600)
c_all.SetTopMargin(0.05)
c_all.SetBottomMargin(0.13)
c_all.SetLeftMargin(0.13)
c_all.SetRightMargin(0.05)
c_all.SetTickx()
c_all.SetTicky()
"""

merged_ff_file = ROOT.TFile.Open(os.path.join(indir,outmerged),"UPDATE")

for i in xrange(1,9):
  num_file = ROOT.TFile.Open(os.path.join(indir,infile%("NUM",i)),"READ")
  den_file = ROOT.TFile.Open(os.path.join(indir,infile%("DEN",i)),"READ")

  h_num = num_file.Get("h_FAKES_NUM_F%s_nominal_fakes"%i).Clone()
  h_num.SetNameTitle("h_num","h_num")
  h_den = den_file.Get("h_FAKES_DEN_F%s_nominal_fakes"%i).Clone()
  h_den.SetNameTitle("h_den","h_den")

 
  h_new_num = h_num.Rebin(len(new_bins)-1,"h_new_num",new_bins)
  h_new_den = h_den.Rebin(len(new_bins)-1,"h_new_den",new_bins)
 
  h_ff = h_new_num.Clone()
  h_ff.Divide(h_new_den)
 
  h_ff.SetNameTitle("h_ff_F%s"%i,"")
  h_ff.GetYaxis().SetTitle("Fake-factor")
  
  h_ff.GetYaxis().SetTitleSize(0.045)
  h_ff.GetXaxis().SetTitleSize(0.045)
  h_ff.GetYaxis().SetLabelSize(0.045)
  h_ff.GetXaxis().SetLabelSize(0.045)
  h_ff.GetYaxis().SetTitleOffset(1.2)
  h_ff.GetXaxis().SetTitleOffset(1.2)
  
  h_ff.GetXaxis().SetRangeUser(min(new_bins),max(new_bins))
  h_ff.SetLineColor(rcol[i-1])
  h_ff.SetMarkerColor(rcol[i-1])
  h_ff.SetMarkerSize(0.01)
  h_ff.SetMaximum(0.2)
  h_ff.SetMinimum(0)
  
  #c_all.cd()
  #if i==1: h_ff.Draw("E1 SAME")
  #else: h_ff.Draw("E1 SAME")
  
  c = ROOT.TCanvas("c_ff_F%s"%i,"c_ff_F%s"%i,650,600)
  c.SetTopMargin(0.05)
  c.SetBottomMargin(0.13)
  c.SetLeftMargin(0.13)
  c.SetRightMargin(0.05)
  c.SetTickx()
  c.SetTicky()
  c.cd() 
  
  h_ff.SetStats(0)
  h_ff.Draw("E1")
  
  merged_ff_file.WriteTObject(h_ff.Clone())
  merged_ff_file.WriteTObject(c.Clone())
  
  ff_file = ROOT.TFile.Open(os.path.join(indir,outfile%i),"RECREATE")
  ff_file.WriteTObject(h_ff.Clone())
  ff_file.WriteTObject(c.Clone())
 
# EOF

