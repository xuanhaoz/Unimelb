# encoding: utf-8
'''
samples.py

description:
 samples for HIGG3D3 derivations
'''

#------------------------------------------------------------------------------
# All MC xsections can be found here:
# https://twiki.cern.ch/twiki/bin/viewauth/AtlasProtected/CentralMC15ProductionList
#------------------------------------------------------------------------------

## modules
from sample import Sample
import ROOT


## colors
black = ROOT.kBlack
white = ROOT.kWhite
red   = ROOT.kRed
green = ROOT.kGreen+1



#-------------------------------------------------------------------------------
# data
#-------------------------------------------------------------------------------
periods = []

periods += [
         # 2015
         "data15_13TeV_periodD",
         "data15_13TeV_periodE",
         "data15_13TeV_periodF",
         "data15_13TeV_periodG",
         "data15_13TeV_periodH",
         "data15_13TeV_periodJ",
         # 2016
         "data16_13TeV_periodA",
         "data16_13TeV_periodB",
         "data16_13TeV_periodC",
         "data16_13TeV_periodD",
         "data16_13TeV_periodE",
         "data16_13TeV_periodF",
         "data16_13TeV_periodG",
         "data16_13TeV_periodI",
         "data16_13TeV_periodK",
         "data16_13TeV_periodL",
         # 2017
         "data17_13TeV_periodB",
         "data17_13TeV_periodC",
         "data17_13TeV_periodD",
         "data17_13TeV_periodE",
         "data17_13TeV_periodF",
         "data17_13TeV_periodH",
         "data17_13TeV_periodI",
         "data17_13TeV_periodK",
        ]


for name in periods:
    globals()[name] = Sample(
            name = name,
            type = "data"
            )

list_runs =[globals()[name] for name in periods]

data = Sample(name         = "data",
              tlatex       = "Data 2015+2016+2017",
              fill_color   = white,
              fill_style   = 0,
              line_color   = black,
              line_style   = 1,
              marker_color = black,
              marker_style = 20,
              daughters    = list_runs,
              )


#-------------------------------------------------------------------------------
# data-driven background
#-------------------------------------------------------------------------------
fakes    = Sample( name         = "fakes",
                   tlatex       = "Fakes",
                   fill_color   = ROOT.kGray,
                   line_color   = ROOT.kGray+1,
                   line_style   = 1,
                   marker_color = ROOT.kGray+1,
                   marker_style = 20,
                   daughters    = list_runs,
                   type         = "datadriven",
                   )



#-------------------------------------------------------------------------------
# Collections 
#-------------------------------------------------------------------------------

# Samples loaded for SubmitHist.py
#---------------------------------

all_data = data.daughters

all_mc = []
mc_bkg = []
#all_mc += ttbar.daughters
#all_mc += singletop.daughters

#all_mc += Wenu.daughters
#all_mc += Wmunu.daughters
#all_mc += Wtaunu.daughters

#all_mc += Zee.daughters
#all_mc += Zmumu.daughters
#all_mc += Ztautau.daughters



# Samples loaded for SubmitPlot.py
#---------------------------------
"""
mc_bkg = []

#mc_bkg.append( Wenu )
mc_bkg.append( Wmunu )
mc_bkg.append( Wtaunu )

#mc_bkg.append( Zee ) 
mc_bkg.append( Zmumu )
mc_bkg.append( Ztautau )

mc_bkg.append( singletop )
mc_bkg.append( ttbar )
"""
## EOF
