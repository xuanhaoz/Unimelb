# encoding: utf-8
'''
samples.py

description:
 signal samples (EXOT12)
'''

#------------------------------------------------------------------------------
# All MC xsections can be found here:
# https://twiki.cern.ch/twiki/bin/viewauth/AtlasProtected/CentralMC15ProductionList
#------------------------------------------------------------------------------

## modules
from sample import Sample
from copy import copy

import ROOT

#------------------------------------------------------------------------------------------------------
# Doubly charged Higss 
# Notes:
#       * cross sections: https://twiki.cern.ch/twiki/bin/view/AtlasProtected/XsecSummaryHiggsBSMOthers 
#------------------------------------------------------------------------------------------------------

DCH300 = Sample(name = "DCH300", 
                tlatex = 'm_{H^{\pm\pm}}=300 GeV',         
                line_color   = ROOT.kRed+1,
                marker_color = ROOT.kRed+1,
                fill_color   = ROOT.kRed+1,
                line_width   = 3,
                line_style   = 1,
                fill_style   = 3004,
                xsec         = 0.020179, 
                feff         = 1.0,  
                )

DCH400 = Sample(name = "DCH400", 
                tlatex = 'm_{H^{\pm\pm}}=400 GeV',         
                line_color   = ROOT.kOrange-3,
                marker_color = ROOT.kOrange-3,
                fill_color   = ROOT.kOrange-3,
                line_width   = 3,
                line_style   = 1,
                fill_style   = 3004,
                xsec         = 0.0059727, 
                feff         = 1.0,  
                )

DCH500 = Sample(name = "DCH500", 
                tlatex = 'm_{H^{\pm\pm}}=500 GeV',         
                line_color   = ROOT.kOrange-3,
                marker_color = ROOT.kOrange-3,
                fill_color   = ROOT.kOrange-3,
                line_width   = 3,
                line_style   = 1,
                fill_style   = 3004,
                xsec         = 0.0021733, 
                feff         = 1.0,  
                )

DCH600 = Sample(name = "DCH600", 
                tlatex = 'm_{H^{\pm\pm}}=600 GeV',         
                line_color   = ROOT.kOrange-3,
                marker_color = ROOT.kOrange-3,
                fill_color   = ROOT.kOrange-3,
                line_width   = 3,
                line_style   = 1,
                fill_style   = 3004,
                xsec         = 0.00089447, 
                feff         = 1.0,  
                )

DCH700 = Sample(name = "DCH700", 
                tlatex = 'm_{H^{\pm\pm}}=700 GeV',         
                line_color   = ROOT.kOrange-3,
                marker_color = ROOT.kOrange-3,
                fill_color   = ROOT.kOrange-3,
                line_width   = 3,
                line_style   = 1,
                fill_style   = 3004,
                xsec         = 0.00040462, 
                feff         = 1.0,  
                )

DCH800 = Sample(name = "DCH800", 
                tlatex = 'm_{H^{\pm\pm}}=800 GeV',         
                line_color   = ROOT.kBlue+1,
                marker_color = ROOT.kBlue+1,
                fill_color   = ROOT.kBlue+1,
                line_width   = 3,
                line_style   = 1,
                fill_style   = 3004,
                xsec         = 0.00019397, 
                feff         = 1.0,  
                )

DCH900 = Sample(name = "DCH900", 
                tlatex = 'm_{H^{\pm\pm}}=900 GeV',         
                line_color   = ROOT.kOrange-3,
                marker_color = ROOT.kOrange-3,
                fill_color   = ROOT.kOrange-3,
                line_width   = 3,
                line_style   = 1,
                fill_style   = 3004,
                xsec         = 9.8716e-05, 
                feff         = 1.0,  
                )

DCH1000 = Sample(name = "DCH1000", 
                tlatex = 'm_{H^{\pm\pm}}=1000 GeV',         
                line_color   = ROOT.kOrange-3,
                marker_color = ROOT.kOrange-3,
                fill_color   = ROOT.kOrange-3,
                line_width   = 3,
                line_style   = 1,
                fill_style   = 3004,
                xsec         = 5.2052e-05, 
                feff         = 1.0,  
                )

DCH1100 = Sample(name = "DCH1100", 
                tlatex = 'm_{H^{\pm\pm}}=1100 GeV',         
                line_color   = ROOT.kOrange-3,
                marker_color = ROOT.kOrange-3,
                fill_color   = ROOT.kOrange-3,
                line_width   = 3,
                line_style   = 1,
                fill_style   = 3004,
                xsec         = 2.8246e-05, 
                feff         = 1.0,  
                )

DCH1200 = Sample(name = "DCH1200", 
                tlatex = 'm_{H^{\pm\pm}}=1200 GeV',         
                line_color   = ROOT.kOrange-3,
                marker_color = ROOT.kOrange-3,
                fill_color   = ROOT.kOrange-3,
                line_width   = 3,
                line_style   = 1,
                fill_style   = 3004,
                xsec         = 1.5651e-05, 
                feff         = 1.0,  
                )

DCH1300 = Sample(name = "DCH1300", 
                tlatex = 'm_{H^{\pm\pm}}=1300 GeV',         
                line_color   = ROOT.kGreen+1,
                marker_color = ROOT.kGreen+1,
                fill_color   = ROOT.kGreen+1,
                line_width   = 3,
                line_style   = 1,
                fill_style   = 3004,
                xsec         = 8.877e-06, 
                feff         = 1.0,  
                )

root_DCH = []
root_DCH.append(DCH300)
root_DCH.append(DCH400)
root_DCH.append(DCH500)
root_DCH.append(DCH600)
root_DCH.append(DCH700)
root_DCH.append(DCH800)
root_DCH.append(DCH900)
root_DCH.append(DCH1000)
root_DCH.append(DCH1100)
root_DCH.append(DCH1200)
root_DCH.append(DCH1300)


# -----------------
# build decay modes
# -----------------

parent = {}
parent["HR"] = {"feff":1.0, "tlatex": "H^{\pm\pm}_{R}(%s)"}
parent["HL"] = {"feff":1.0, "tlatex": "H^{\pm\pm}_{L}(%s)"}

pos_decay = {}
pos_decay["MpMp"] = {"feff": 1. / 0.25, "tlatex": " #mu^{+} #mu^{+}"}
pos_decay["EpMp"] = {"feff": 1. / 0.50, "tlatex": " e^{+} #mu^{+}"}
pos_decay["EpEp"] = {"feff": 1. / 0.25, "tlatex": " #mu^{+} #mu^{+}"}

neg_decay = {}
neg_decay["MmMm"] = {"feff": 1. / 0.25, "tlatex": " #mu^{-} #mu^{-}"}
neg_decay["EmMm"] = {"feff": 1. / 0.50, "tlatex": " e^{-} #mu^{-}"}
neg_decay["EmEm"] = {"feff": 1. / 0.25, "tlatex": " #mu^{-} #mu^{-}"}

# loops over the list of original samples
# and appends the decay modes taking into
# account the different efficiencies

full_DCH = []
for boson in parent.keys():
  for pos_mode in pos_decay.keys():
    for neg_mode in neg_decay.keys():
      sname = "%s%s_%s%s"%(boson,pos_mode,boson,neg_mode)
      for sroot in root_DCH:
        if "HL" in sname:
          globals()[full_sname].line_color   += 2
          globals()[full_sname].marker_color += 2
          globals()[full_sname].fill_color   += 2
        full_sname = "%s_%s"%(sroot.name,sname) 
        globals()[full_sname]         = copy(sroot)
        globals()[full_sname].infile  = sroot.name
        globals()[full_sname].name    = full_sname
        globals()[full_sname].tlatex  = parent[boson]["tlatex"]%(sroot.name.replace("DCH",""))+" #rightarrow" + pos_decay[pos_mode]["tlatex"] + neg_decay[neg_mode]["tlatex"]
        globals()[full_sname].feff    = parent[boson]["feff"] * pos_decay[pos_mode]["feff"] * neg_decay[neg_mode]["feff"]
        full_DCH.append(globals()[full_sname])


# EOF

