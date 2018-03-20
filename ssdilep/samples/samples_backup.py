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
GRL = []

GRL += [
        # 2015
        # data15_13TeV.periodAllYear_DetStatus-v79-repro20-02_DQDefects-00-02-02_PHYS_StandardGRL_All_Good_25ns.xml
        "276262","276329","276336","276416","276511","276689","276778","276790",
        "276952","276954","278880","278912","278968","279169","279259","279279",
        "279284","279345","279515","279598","279685","279813","279867","279928",
        "279932","279984","280231","280273","280319","280368","280423","280464",
        "280500","280520","280614","280673","280753","280853","280862","280950",
        "280977","281070","281074","281075","281317","281385","281411","282625",
        "282631","282712","282784","282992","283074","283155","283270","283429",
        "283608","283780","284006","284154","284213","284285","284420","284427",
        "284484",
       
        
        # 2016
        # data16_13TeV.periodAllYear_DetStatus-v88-pro20-21_DQDefects-00-02-04_PHYS_StandardGRL_All_Good_25ns.xml
        "297730","298595","298609","298633","298687","298690","298771","298773",
        "298862","298967","299055","299144","299147","299184","299243","299584",
        "300279","300345","300415","300418","300487","300540","300571","300600",
        "300655","300687","300784","300800","300863","300908","301912","301918",
        "301932","301973","302053","302137","302265","302269","302300","302347",
        "302380","302391","302393","302737","302831","302872","302919","302925",
        "302956","303007","303079","303201","303208","303264","303266","303291",
        "303304","303338","303421","303499","303560","303638","303832","303846",
        "303892","303943","304006","304008","304128","304178","304198","304211",
        "304243","304308","304337","304409","304431","304494","305380","305543",
        "305571","305618","305671","305674","305723","305727","305735","305777",
        "305811","305920","306269","306278","306310","306384","306419","306442",
        "306448","306451","307126","307195","307259","307306","307354","307358",
        "307394","307454","307514","307539","307569","307601","307619","307656",
        "307710","307716","307732","307861","307935","308047","308084","309375",
        "309390","309440","309516","309640","309674","309759","310015","310247",
        "310249","310341","310370","310405","310468","310473","310634","310691",
        "310738","310809","310863","310872","310969","311071","311170","311244",
        "311287","311321","311365","311402","311473","311481"
        ]


ds_name = 'physics_Main_00%s'

for run in GRL:
    name = ds_name % run
    globals()[name] = Sample(
            name = name,
            type = "data"
            )

list_runs =[globals()[ds_name%(run)] for run in GRL]

data = Sample(name         = "data",
              tlatex       = "Data 2015+2016",
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


#-------------------------------------------------------------------------------------------------------------------------
# W + jets (Sherpa 2.2)
# Notes:
#       * cross sections: https://twiki.cern.ch/twiki/bin/view/AtlasProtected/XsecSummaryWjetsSherpa22Light (light filter)
#                         https://twiki.cern.ch/twiki/bin/view/AtlasProtected/XsecSummaryWjetsSherpa22C     (C filter) 
#                         https://twiki.cern.ch/twiki/bin/view/AtlasProtected/XsecSummaryWjetsSherpa22B     (B filter) 
#-------------------------------------------------------------------------------------------------------------------------

#-----
# Wenu
#-----

Sherpa_NNPDF30NNLO_Wenu_Pt0_70_CVetoBVeto         = Sample( name =  "Sherpa_NNPDF30NNLO_Wenu_Pt0_70_CVetoBVeto",         xsec = 20029.0    , feff = 9.0 * 0.81379 , kfactor = 0.9702 ) 
Sherpa_NNPDF30NNLO_Wenu_Pt70_140_CVetoBVeto       = Sample( name =  "Sherpa_NNPDF30NNLO_Wenu_Pt70_140_CVetoBVeto",       xsec = 588.04     , feff = 9.0 * 0.65978 , kfactor = 0.9702 )
Sherpa_NNPDF30NNLO_Wenu_Pt140_280_CVetoBVeto      = Sample( name =  "Sherpa_NNPDF30NNLO_Wenu_Pt140_280_CVetoBVeto",      xsec = 84.141     , feff = 9.0 * 0.61484 , kfactor = 0.9702 )
Sherpa_NNPDF30NNLO_Wenu_Pt280_500_CVetoBVeto      = Sample( name =  "Sherpa_NNPDF30NNLO_Wenu_Pt280_500_CVetoBVeto",      xsec = 6.091      , feff = 9.0 * 0.58138 , kfactor = 0.9702 )
Sherpa_NNPDF30NNLO_Wenu_Pt500_700_CVetoBVeto      = Sample( name =  "Sherpa_NNPDF30NNLO_Wenu_Pt500_700_CVetoBVeto",      xsec = 0.38167    , feff = 9.0 * 0.57124 , kfactor = 0.9702 )
Sherpa_NNPDF30NNLO_Wenu_Pt700_1000_CVetoBVeto     = Sample( name =  "Sherpa_NNPDF30NNLO_Wenu_Pt700_1000_CVetoBVeto",     xsec = 0.068378   , feff = 9.0 * 0.55719 , kfactor = 0.9702 )
Sherpa_NNPDF30NNLO_Wenu_Pt1000_2000_CVetoBVeto    = Sample( name =  "Sherpa_NNPDF30NNLO_Wenu_Pt1000_2000_CVetoBVeto",    xsec = 0.0087439  , feff = 9.0 * 0.54755 , kfactor = 0.9702 )
Sherpa_NNPDF30NNLO_Wenu_Pt2000_E_CMS_CVetoBVeto   = Sample( name =  "Sherpa_NNPDF30NNLO_Wenu_Pt2000_E_CMS_CVetoBVeto",   xsec = 3.1287e-05 , feff = 9.0 * 0.42738 , kfactor = 0.9702 )
                                                                                                                                             
Sherpa_NNPDF30NNLO_Wenu_Pt0_70_CFilterBVeto       = Sample( name =  "Sherpa_NNPDF30NNLO_Wenu_Pt0_70_CFilterBVeto",       xsec = 20015.0    , feff = 9.0 * 0.13825 , kfactor = 0.9702  )
Sherpa_NNPDF30NNLO_Wenu_Pt70_140_CFilterBVeto     = Sample( name =  "Sherpa_NNPDF30NNLO_Wenu_Pt70_140_CFilterBVeto",     xsec = 589.12     , feff = 9.0 * 0.25614 , kfactor = 0.9702  )
Sherpa_NNPDF30NNLO_Wenu_Pt140_280_CFilterBVeto    = Sample( name =  "Sherpa_NNPDF30NNLO_Wenu_Pt140_280_CFilterBVeto",    xsec = 84.155     , feff = 9.0 * 0.27679 , kfactor = 0.9702  )
Sherpa_NNPDF30NNLO_Wenu_Pt280_500_CFilterBVeto    = Sample( name =  "Sherpa_NNPDF30NNLO_Wenu_Pt280_500_CFilterBVeto",    xsec = 6.0816     , feff = 9.0 * 0.28485 , kfactor = 0.9702  )
Sherpa_NNPDF30NNLO_Wenu_Pt500_700_CFilterBVeto    = Sample( name =  "Sherpa_NNPDF30NNLO_Wenu_Pt500_700_CFilterBVeto",    xsec = 0.38112    , feff = 9.0 * 0.29004 , kfactor = 0.9702  )
Sherpa_NNPDF30NNLO_Wenu_Pt700_1000_CFilterBVeto   = Sample( name =  "Sherpa_NNPDF30NNLO_Wenu_Pt700_1000_CFilterBVeto",   xsec = 0.067651   , feff = 9.0 * 0.28984 , kfactor = 0.9702  )
Sherpa_NNPDF30NNLO_Wenu_Pt1000_2000_CFilterBVeto  = Sample( name =  "Sherpa_NNPDF30NNLO_Wenu_Pt1000_2000_CFilterBVeto",  xsec = 0.0088697  , feff = 9.0 * 0.28403 , kfactor = 0.9702  )
Sherpa_NNPDF30NNLO_Wenu_Pt2000_E_CMS_CFilterBVeto = Sample( name =  "Sherpa_NNPDF30NNLO_Wenu_Pt2000_E_CMS_CFilterBVeto", xsec = 2.5889e-05 , feff = 9.0 * 0.094117 , kfactor = 0.9702 )
                                                                                                                                                            
Sherpa_NNPDF30NNLO_Wenu_Pt0_70_BFilter            = Sample( name =  "Sherpa_NNPDF30NNLO_Wenu_Pt0_70_BFilter",            xsec = 20004.0    , feff = 9.0 * 0.046999 , kfactor = 0.9702 )
Sherpa_NNPDF30NNLO_Wenu_Pt70_140_BFilter          = Sample( name =  "Sherpa_NNPDF30NNLO_Wenu_Pt70_140_BFilter",          xsec = 589.57     , feff = 9.0 * 0.086323 , kfactor = 0.9702 )
Sherpa_NNPDF30NNLO_Wenu_Pt140_280_BFilter         = Sample( name =  "Sherpa_NNPDF30NNLO_Wenu_Pt140_280_BFilter",         xsec = 84.144     , feff = 9.0 * 0.10578  , kfactor = 0.9702 )
Sherpa_NNPDF30NNLO_Wenu_Pt280_500_BFilter         = Sample( name =  "Sherpa_NNPDF30NNLO_Wenu_Pt280_500_BFilter",         xsec = 6.021      , feff = 9.0 * 0.12485  , kfactor = 0.9702 )
Sherpa_NNPDF30NNLO_Wenu_Pt500_700_BFilter         = Sample( name =  "Sherpa_NNPDF30NNLO_Wenu_Pt500_700_BFilter",         xsec = 0.38452    , feff = 9.0 * 0.13681  , kfactor = 0.9702 )
Sherpa_NNPDF30NNLO_Wenu_Pt700_1000_BFilter        = Sample( name =  "Sherpa_NNPDF30NNLO_Wenu_Pt700_1000_BFilter",        xsec = 0.072063   , feff = 9.0 * 0.13566  , kfactor = 0.9702 )
Sherpa_NNPDF30NNLO_Wenu_Pt1000_2000_BFilter       = Sample( name =  "Sherpa_NNPDF30NNLO_Wenu_Pt1000_2000_BFilter",       xsec = 0.0088869  , feff = 9.0 * 0.15161  , kfactor = 0.9702 )
Sherpa_NNPDF30NNLO_Wenu_Pt2000_E_CMS_BFilter      = Sample( name =  "Sherpa_NNPDF30NNLO_Wenu_Pt2000_E_CMS_BFilter",      xsec = 2.9071e-05 , feff = 9.0 * 0.13137  , kfactor = 0.9702 )


WenuSherpa22 = Sample( name =   'WenuSherpa22',
                  tlatex = 'W #rightarrow e#nu+jets',
                  fill_color = ROOT.kRed+1,
                  line_color =  ROOT.kRed+2,
                  marker_color =  ROOT.kRed+2,
                  daughters = [
                               Sherpa_NNPDF30NNLO_Wenu_Pt0_70_CVetoBVeto,        
                               Sherpa_NNPDF30NNLO_Wenu_Pt70_140_CVetoBVeto,                                    
                               Sherpa_NNPDF30NNLO_Wenu_Pt140_280_CVetoBVeto,     
                               Sherpa_NNPDF30NNLO_Wenu_Pt280_500_CVetoBVeto,     
                               Sherpa_NNPDF30NNLO_Wenu_Pt500_700_CVetoBVeto,     
                               Sherpa_NNPDF30NNLO_Wenu_Pt700_1000_CVetoBVeto,    
                               Sherpa_NNPDF30NNLO_Wenu_Pt1000_2000_CVetoBVeto,   
                               Sherpa_NNPDF30NNLO_Wenu_Pt2000_E_CMS_CVetoBVeto,  
                               Sherpa_NNPDF30NNLO_Wenu_Pt0_70_CFilterBVeto,      
                               Sherpa_NNPDF30NNLO_Wenu_Pt70_140_CFilterBVeto,    
                               Sherpa_NNPDF30NNLO_Wenu_Pt140_280_CFilterBVeto,   
                               Sherpa_NNPDF30NNLO_Wenu_Pt280_500_CFilterBVeto,   
                               Sherpa_NNPDF30NNLO_Wenu_Pt500_700_CFilterBVeto,   
                               Sherpa_NNPDF30NNLO_Wenu_Pt700_1000_CFilterBVeto,  
                               Sherpa_NNPDF30NNLO_Wenu_Pt1000_2000_CFilterBVeto, 
                               Sherpa_NNPDF30NNLO_Wenu_Pt2000_E_CMS_CFilterBVeto,
                               Sherpa_NNPDF30NNLO_Wenu_Pt0_70_BFilter,           
                               Sherpa_NNPDF30NNLO_Wenu_Pt70_140_BFilter,         
                               Sherpa_NNPDF30NNLO_Wenu_Pt140_280_BFilter,        
                               Sherpa_NNPDF30NNLO_Wenu_Pt280_500_BFilter,        
                               Sherpa_NNPDF30NNLO_Wenu_Pt500_700_BFilter,        
                               Sherpa_NNPDF30NNLO_Wenu_Pt700_1000_BFilter,       
                               Sherpa_NNPDF30NNLO_Wenu_Pt1000_2000_BFilter,      
                               Sherpa_NNPDF30NNLO_Wenu_Pt2000_E_CMS_BFilter,     
                              ],
                ) 


#------
# Wmunu
#------

Sherpa_NNPDF30NNLO_Wmunu_Pt0_70_CVetoBVeto         = Sample( name =  "Sherpa_NNPDF30NNLO_Wmunu_Pt0_70_CVetoBVeto",         xsec = 20011.0   , feff = 9.0 * 0.81357 , kfactor = 0.9702 )
Sherpa_NNPDF30NNLO_Wmunu_Pt70_140_CVetoBVeto       = Sample( name =  "Sherpa_NNPDF30NNLO_Wmunu_Pt70_140_CVetoBVeto",       xsec = 589.74    , feff = 9.0 * 0.66021 , kfactor = 0.9702 ) 
Sherpa_NNPDF30NNLO_Wmunu_Pt140_280_CVetoBVeto      = Sample( name =  "Sherpa_NNPDF30NNLO_Wmunu_Pt140_280_CVetoBVeto",      xsec = 84.068    , feff = 9.0 * 0.61464 , kfactor = 0.9702 )
Sherpa_NNPDF30NNLO_Wmunu_Pt280_500_CVetoBVeto      = Sample( name =  "Sherpa_NNPDF30NNLO_Wmunu_Pt280_500_CVetoBVeto",      xsec = 6.5041    , feff = 9.0 * 0.58443 , kfactor = 0.9702 )
Sherpa_NNPDF30NNLO_Wmunu_Pt500_700_CVetoBVeto      = Sample( name =  "Sherpa_NNPDF30NNLO_Wmunu_Pt500_700_CVetoBVeto",      xsec = 0.38798   , feff = 9.0 * 0.56674 , kfactor = 0.9702 )
Sherpa_NNPDF30NNLO_Wmunu_Pt700_1000_CVetoBVeto     = Sample( name =  "Sherpa_NNPDF30NNLO_Wmunu_Pt700_1000_CVetoBVeto",     xsec = 0.068303  , feff = 9.0 * 0.56002 , kfactor = 0.9702 )
Sherpa_NNPDF30NNLO_Wmunu_Pt1000_2000_CVetoBVeto    = Sample( name =  "Sherpa_NNPDF30NNLO_Wmunu_Pt1000_2000_CVetoBVeto",    xsec = 0.0089461 , feff = 9.0 * 0.55171 , kfactor = 0.9702 )
Sherpa_NNPDF30NNLO_Wmunu_Pt2000_E_CMS_CVetoBVeto   = Sample( name =  "Sherpa_NNPDF30NNLO_Wmunu_Pt2000_E_CMS_CVetoBVeto",   xsec = 2.6342e-05, feff = 9.0 * 0.48317 , kfactor = 0.9702 )
                                                                                                                                              
Sherpa_NNPDF30NNLO_Wmunu_Pt0_70_CFilterBVeto       = Sample( name =  "Sherpa_NNPDF30NNLO_Wmunu_Pt0_70_CFilterBVeto",       xsec = 20033.0   , feff = 9.0 * 0.13764 , kfactor = 0.9702 )
Sherpa_NNPDF30NNLO_Wmunu_Pt70_140_CFilterBVeto     = Sample( name =  "Sherpa_NNPDF30NNLO_Wmunu_Pt70_140_CFilterBVeto",     xsec = 590.75    , feff = 9.0 * 0.25322 , kfactor = 0.9702 )
Sherpa_NNPDF30NNLO_Wmunu_Pt140_280_CFilterBVeto    = Sample( name =  "Sherpa_NNPDF30NNLO_Wmunu_Pt140_280_CFilterBVeto",    xsec = 84.296    , feff = 9.0 * 0.27632 , kfactor = 0.9702 )
Sherpa_NNPDF30NNLO_Wmunu_Pt280_500_CFilterBVeto    = Sample( name =  "Sherpa_NNPDF30NNLO_Wmunu_Pt280_500_CFilterBVeto",    xsec = 6.0684    , feff = 9.0 * 0.28826 , kfactor = 0.9702 )
Sherpa_NNPDF30NNLO_Wmunu_Pt500_700_CFilterBVeto    = Sample( name =  "Sherpa_NNPDF30NNLO_Wmunu_Pt500_700_CFilterBVeto",    xsec = 0.37959   , feff = 9.0 * 0.2909  , kfactor = 0.9702 )
Sherpa_NNPDF30NNLO_Wmunu_Pt700_1000_CFilterBVeto   = Sample( name =  "Sherpa_NNPDF30NNLO_Wmunu_Pt700_1000_CFilterBVeto",   xsec = 0.068517  , feff = 9.0 * 0.27373 , kfactor = 0.9702 )
Sherpa_NNPDF30NNLO_Wmunu_Pt1000_2000_CFilterBVeto  = Sample( name =  "Sherpa_NNPDF30NNLO_Wmunu_Pt1000_2000_CFilterBVeto",  xsec = 0.0088991 , feff = 9.0 * 0.28896 , kfactor = 0.9702 )
Sherpa_NNPDF30NNLO_Wmunu_Pt2000_E_CMS_CFilterBVeto = Sample( name =  "Sherpa_NNPDF30NNLO_Wmunu_Pt2000_E_CMS_CFilterBVeto", xsec = 3.2907e-05, feff = 9.0 * 0.30733 , kfactor = 0.9702 )
                                                                                                                                                              
Sherpa_NNPDF30NNLO_Wmunu_Pt0_70_BFilter            = Sample( name =  "Sherpa_NNPDF30NNLO_Wmunu_Pt0_70_BFilter",            xsec = 20020.0   , feff = 9.0 * 0.046728 , kfactor = 0.9702 )
Sherpa_NNPDF30NNLO_Wmunu_Pt70_140_BFilter          = Sample( name =  "Sherpa_NNPDF30NNLO_Wmunu_Pt70_140_BFilter",          xsec = 589.48    , feff = 9.0 * 0.086333 , kfactor = 0.9702 )
Sherpa_NNPDF30NNLO_Wmunu_Pt140_280_BFilter         = Sample( name =  "Sherpa_NNPDF30NNLO_Wmunu_Pt140_280_BFilter",         xsec = 83.964    , feff = 9.0 * 0.10602  , kfactor = 0.9702 )
Sherpa_NNPDF30NNLO_Wmunu_Pt280_500_BFilter         = Sample( name =  "Sherpa_NNPDF30NNLO_Wmunu_Pt280_500_BFilter",         xsec = 6.1503    , feff = 9.0 * 0.12376  , kfactor = 0.9702 )
Sherpa_NNPDF30NNLO_Wmunu_Pt500_700_BFilter         = Sample( name =  "Sherpa_NNPDF30NNLO_Wmunu_Pt500_700_BFilter",         xsec = 0.3807    , feff = 9.0 * 0.13669  , kfactor = 0.9702 )
Sherpa_NNPDF30NNLO_Wmunu_Pt700_1000_BFilter        = Sample( name =  "Sherpa_NNPDF30NNLO_Wmunu_Pt700_1000_BFilter",        xsec = 0.068219  , feff = 9.0 * 0.14245  , kfactor = 0.9702 )
Sherpa_NNPDF30NNLO_Wmunu_Pt1000_2000_BFilter       = Sample( name =  "Sherpa_NNPDF30NNLO_Wmunu_Pt1000_2000_BFilter",       xsec = 0.0088975 , feff = 9.0 * 0.14879  , kfactor = 0.9702 )
Sherpa_NNPDF30NNLO_Wmunu_Pt2000_E_CMS_BFilter      = Sample( name =  "Sherpa_NNPDF30NNLO_Wmunu_Pt2000_E_CMS_BFilter",      xsec = 2.7767e-05, feff = 9.0 * 0.19726  , kfactor = 0.9702 )

WmunuSherpa22 = Sample( name =   'WmunuSherpa22',
                  tlatex = 'W #rightarrow #mu#nu+jets',
                  fill_color = ROOT.kGreen+1,
                  line_color =  ROOT.kGreen+2,
                  marker_color =  ROOT.kGreen+2,
                  daughters = [
                               Sherpa_NNPDF30NNLO_Wmunu_Pt0_70_CVetoBVeto,        
                               Sherpa_NNPDF30NNLO_Wmunu_Pt70_140_CVetoBVeto,                                    
                               Sherpa_NNPDF30NNLO_Wmunu_Pt140_280_CVetoBVeto,     
                               Sherpa_NNPDF30NNLO_Wmunu_Pt280_500_CVetoBVeto,     
                               Sherpa_NNPDF30NNLO_Wmunu_Pt500_700_CVetoBVeto,     
                               Sherpa_NNPDF30NNLO_Wmunu_Pt700_1000_CVetoBVeto,    
                               Sherpa_NNPDF30NNLO_Wmunu_Pt1000_2000_CVetoBVeto,   
                               Sherpa_NNPDF30NNLO_Wmunu_Pt2000_E_CMS_CVetoBVeto,  
                               Sherpa_NNPDF30NNLO_Wmunu_Pt0_70_CFilterBVeto,      
                               Sherpa_NNPDF30NNLO_Wmunu_Pt70_140_CFilterBVeto,    
                               Sherpa_NNPDF30NNLO_Wmunu_Pt140_280_CFilterBVeto,   
                               Sherpa_NNPDF30NNLO_Wmunu_Pt280_500_CFilterBVeto,   
                               Sherpa_NNPDF30NNLO_Wmunu_Pt500_700_CFilterBVeto,   
                               Sherpa_NNPDF30NNLO_Wmunu_Pt700_1000_CFilterBVeto,  
                               Sherpa_NNPDF30NNLO_Wmunu_Pt1000_2000_CFilterBVeto, 
                               Sherpa_NNPDF30NNLO_Wmunu_Pt2000_E_CMS_CFilterBVeto,
                               Sherpa_NNPDF30NNLO_Wmunu_Pt0_70_BFilter,           
                               Sherpa_NNPDF30NNLO_Wmunu_Pt70_140_BFilter,         
                               Sherpa_NNPDF30NNLO_Wmunu_Pt140_280_BFilter,        
                               Sherpa_NNPDF30NNLO_Wmunu_Pt280_500_BFilter,        
                               Sherpa_NNPDF30NNLO_Wmunu_Pt500_700_BFilter,        
                               Sherpa_NNPDF30NNLO_Wmunu_Pt700_1000_BFilter,       
                               Sherpa_NNPDF30NNLO_Wmunu_Pt1000_2000_BFilter,      
                               Sherpa_NNPDF30NNLO_Wmunu_Pt2000_E_CMS_BFilter,     
                              ],
                ) 

#-------
# Wtaunu
#-------
Sherpa_NNPDF30NNLO_Wtaunu_Pt0_70_CVetoBVeto         = Sample( name =  "Sherpa_NNPDF30NNLO_Wtaunu_Pt0_70_CVetoBVeto",         xsec = 20024.0    , feff = 9.0 * 0.81442 , kfactor = 0.9702 )
Sherpa_NNPDF30NNLO_Wtaunu_Pt70_140_CVetoBVeto       = Sample( name =  "Sherpa_NNPDF30NNLO_Wtaunu_Pt70_140_CVetoBVeto",       xsec = 589.14     , feff = 9.0 * 0.6574  , kfactor = 0.9702 ) 
Sherpa_NNPDF30NNLO_Wtaunu_Pt140_280_CVetoBVeto      = Sample( name =  "Sherpa_NNPDF30NNLO_Wtaunu_Pt140_280_CVetoBVeto",      xsec = 84.22      , feff = 9.0 * 0.61404 , kfactor = 0.9702 )
Sherpa_NNPDF30NNLO_Wtaunu_Pt280_500_CVetoBVeto      = Sample( name =  "Sherpa_NNPDF30NNLO_Wtaunu_Pt280_500_CVetoBVeto",      xsec = 6.0858     , feff = 9.0 * 0.58438 , kfactor = 0.9702 )
Sherpa_NNPDF30NNLO_Wtaunu_Pt500_700_CVetoBVeto      = Sample( name =  "Sherpa_NNPDF30NNLO_Wtaunu_Pt500_700_CVetoBVeto",      xsec = 0.38105    , feff = 9.0 * 0.56773 , kfactor = 0.9702 )
Sherpa_NNPDF30NNLO_Wtaunu_Pt700_1000_CVetoBVeto     = Sample( name =  "Sherpa_NNPDF30NNLO_Wtaunu_Pt700_1000_CVetoBVeto",     xsec = 0.073222   , feff = 9.0 * 0.56144 , kfactor = 0.9702 )
Sherpa_NNPDF30NNLO_Wtaunu_Pt1000_2000_CVetoBVeto    = Sample( name =  "Sherpa_NNPDF30NNLO_Wtaunu_Pt1000_2000_CVetoBVeto",    xsec = 0.0090285  , feff = 9.0 * 0.55575 , kfactor = 0.9702 )
Sherpa_NNPDF30NNLO_Wtaunu_Pt2000_E_CMS_CVetoBVeto   = Sample( name =  "Sherpa_NNPDF30NNLO_Wtaunu_Pt2000_E_CMS_CVetoBVeto",   xsec = 2.6193e-05 , feff = 9.0 * 0.56055 , kfactor = 0.9702 )
                                                                                                                                                 
Sherpa_NNPDF30NNLO_Wtaunu_Pt0_70_CFilterBVeto       = Sample( name =  "Sherpa_NNPDF30NNLO_Wtaunu_Pt0_70_CFilterBVeto",       xsec = 20015.0    , feff = 9.0 * 0.04684  , kfactor = 0.9702 )
Sherpa_NNPDF30NNLO_Wtaunu_Pt70_140_CFilterBVeto     = Sample( name =  "Sherpa_NNPDF30NNLO_Wtaunu_Pt70_140_CFilterBVeto",     xsec = 589.83     , feff = 9.0 * 0.085814 , kfactor = 0.9702 )
Sherpa_NNPDF30NNLO_Wtaunu_Pt140_280_CFilterBVeto    = Sample( name =  "Sherpa_NNPDF30NNLO_Wtaunu_Pt140_280_CFilterBVeto",    xsec = 84.177     , feff = 9.0 * 0.10544  , kfactor = 0.9702 )
Sherpa_NNPDF30NNLO_Wtaunu_Pt280_500_CFilterBVeto    = Sample( name =  "Sherpa_NNPDF30NNLO_Wtaunu_Pt280_500_CFilterBVeto",    xsec = 6.0788     , feff = 9.0 * 0.12063  , kfactor = 0.9702 )
Sherpa_NNPDF30NNLO_Wtaunu_Pt500_700_CFilterBVeto    = Sample( name =  "Sherpa_NNPDF30NNLO_Wtaunu_Pt500_700_CFilterBVeto",    xsec = 0.37627    , feff = 9.0 * 0.13149  , kfactor = 0.9702 )
Sherpa_NNPDF30NNLO_Wtaunu_Pt700_1000_CFilterBVeto   = Sample( name =  "Sherpa_NNPDF30NNLO_Wtaunu_Pt700_1000_CFilterBVeto",   xsec = 0.067277   , feff = 9.0 * 0.14487  , kfactor = 0.9702 )
Sherpa_NNPDF30NNLO_Wtaunu_Pt1000_2000_CFilterBVeto  = Sample( name =  "Sherpa_NNPDF30NNLO_Wtaunu_Pt1000_2000_CFilterBVeto",  xsec = 0.00902    , feff = 9.0 * 0.14126  , kfactor = 0.9702 )
Sherpa_NNPDF30NNLO_Wtaunu_Pt2000_E_CMS_CFilterBVeto = Sample( name =  "Sherpa_NNPDF30NNLO_Wtaunu_Pt2000_E_CMS_CFilterBVeto", xsec = 2.9392e-05 , feff = 9.0 * 0.18036  , kfactor = 0.9702 )
                                                                                                                                                                 
Sherpa_NNPDF30NNLO_Wtaunu_Pt0_70_BFilter            = Sample( name =  "Sherpa_NNPDF30NNLO_Wtaunu_Pt0_70_BFilter",            xsec = 20028.0    , feff = 9.0 * 0.13812  , kfactor = 0.9702 )
Sherpa_NNPDF30NNLO_Wtaunu_Pt70_140_BFilter          = Sample( name =  "Sherpa_NNPDF30NNLO_Wtaunu_Pt70_140_BFilter",          xsec = 590.11     , feff = 9.0 * 0.25246  , kfactor = 0.9702 )
Sherpa_NNPDF30NNLO_Wtaunu_Pt140_280_BFilter         = Sample( name =  "Sherpa_NNPDF30NNLO_Wtaunu_Pt140_280_BFilter",         xsec = 84.282     , feff = 9.0 * 0.27588  , kfactor = 0.9702 )
Sherpa_NNPDF30NNLO_Wtaunu_Pt280_500_BFilter         = Sample( name =  "Sherpa_NNPDF30NNLO_Wtaunu_Pt280_500_BFilter",         xsec = 6.0652     , feff = 9.0 * 0.28685  , kfactor = 0.9702 )
Sherpa_NNPDF30NNLO_Wtaunu_Pt500_700_BFilter         = Sample( name =  "Sherpa_NNPDF30NNLO_Wtaunu_Pt500_700_BFilter",         xsec = 0.37794    , feff = 9.0 * 0.29673  , kfactor = 0.9702 )
Sherpa_NNPDF30NNLO_Wtaunu_Pt700_1000_BFilter        = Sample( name =  "Sherpa_NNPDF30NNLO_Wtaunu_Pt700_1000_BFilter",        xsec = 0.067963   , feff = 9.0 * 0.29231  , kfactor = 0.9702 )
Sherpa_NNPDF30NNLO_Wtaunu_Pt1000_2000_BFilter       = Sample( name =  "Sherpa_NNPDF30NNLO_Wtaunu_Pt1000_2000_BFilter",       xsec = 0.0089116  , feff = 9.0 * 0.29034  , kfactor = 0.9702 )
Sherpa_NNPDF30NNLO_Wtaunu_Pt2000_E_CMS_BFilter      = Sample( name =  "Sherpa_NNPDF30NNLO_Wtaunu_Pt2000_E_CMS_BFilter",      xsec = 3.0985e-05 , feff = 9.0 * 0.28965  , kfactor = 0.9702 )

WtaunuSherpa22 = Sample( name =   'WtaunuSherpa22',
                  tlatex = 'W #rightarrow #tau#nu+jets',
                  fill_color = ROOT.kBlue+1,
                  line_color =  ROOT.kBlue+2,
                  marker_color =  ROOT.kBlue+2,
                  daughters = [
                               Sherpa_NNPDF30NNLO_Wtaunu_Pt0_70_CVetoBVeto,        
                               Sherpa_NNPDF30NNLO_Wtaunu_Pt70_140_CVetoBVeto,                                    
                               Sherpa_NNPDF30NNLO_Wtaunu_Pt140_280_CVetoBVeto,     
                               Sherpa_NNPDF30NNLO_Wtaunu_Pt280_500_CVetoBVeto,     
                               Sherpa_NNPDF30NNLO_Wtaunu_Pt500_700_CVetoBVeto,     
                               Sherpa_NNPDF30NNLO_Wtaunu_Pt700_1000_CVetoBVeto,    
                               Sherpa_NNPDF30NNLO_Wtaunu_Pt1000_2000_CVetoBVeto,   
                               Sherpa_NNPDF30NNLO_Wtaunu_Pt2000_E_CMS_CVetoBVeto,  
                               Sherpa_NNPDF30NNLO_Wtaunu_Pt0_70_CFilterBVeto,      
                               Sherpa_NNPDF30NNLO_Wtaunu_Pt70_140_CFilterBVeto,    
                               Sherpa_NNPDF30NNLO_Wtaunu_Pt140_280_CFilterBVeto,   
                               Sherpa_NNPDF30NNLO_Wtaunu_Pt280_500_CFilterBVeto,   
                               Sherpa_NNPDF30NNLO_Wtaunu_Pt500_700_CFilterBVeto,   
                               Sherpa_NNPDF30NNLO_Wtaunu_Pt700_1000_CFilterBVeto,  
                               Sherpa_NNPDF30NNLO_Wtaunu_Pt1000_2000_CFilterBVeto, 
                               Sherpa_NNPDF30NNLO_Wtaunu_Pt2000_E_CMS_CFilterBVeto,
                               Sherpa_NNPDF30NNLO_Wtaunu_Pt0_70_BFilter,           
                               Sherpa_NNPDF30NNLO_Wtaunu_Pt70_140_BFilter,         
                               Sherpa_NNPDF30NNLO_Wtaunu_Pt140_280_BFilter,        
                               Sherpa_NNPDF30NNLO_Wtaunu_Pt280_500_BFilter,        
                               Sherpa_NNPDF30NNLO_Wtaunu_Pt500_700_BFilter,        
                               Sherpa_NNPDF30NNLO_Wtaunu_Pt700_1000_BFilter,       
                               Sherpa_NNPDF30NNLO_Wtaunu_Pt1000_2000_BFilter,      
                               Sherpa_NNPDF30NNLO_Wtaunu_Pt2000_E_CMS_BFilter,     
                              ],
                ) 

#--------------------------------------------------------------------------------------------------------------------------
# Z + jets (Sherpa 2.2)
# Notes:
#       * cross sections:  https://twiki.cern.ch/twiki/bin/view/AtlasProtected/XsecSummaryZjetsSherpa22Light (light filter)
#                          https://twiki.cern.ch/twiki/bin/view/AtlasProtected/XsecSummaryZjetsSherpa22C     (C filter) 
#                          https://twiki.cern.ch/twiki/bin/view/AtlasProtected/XsecSummaryZjetsSherpa22B     (B filter) 
# for my tags!!!
# https://twiki.cern.ch/twiki/pub/AtlasProtected/CentralMC15ProductionList/XSections_13TeV_e3651_e4133.txt
#--------------------------------------------------------------------------------------------------------------------------

#-----
# Zee
#-----
Sherpa_NNPDF30NNLO_Zee_Pt0_70_CVetoBVeto         = Sample( name =  "Sherpa_NNPDF30NNLO_Zee_Pt0_70_CVetoBVeto",                xsec = 2076.4     , feff = 9.0 * 0.81072 , kfactor = 0.9751 ) 
Sherpa_NNPDF30NNLO_Zee_Pt70_140_CVetoBVeto       = Sample( name =  "Sherpa_NNPDF30NNLO_Zee_Pt70_140_CVetoBVeto",              xsec = 71.681     , feff = 9.0 * 0.66943 , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Zee_Pt140_280_CVetoBVeto      = Sample( name =  "Sherpa_NNPDF30NNLO_Zee_Pt140_280_CVetoBVeto",             xsec = 11.095     , feff = 9.0 * 0.6276  , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Zee_Pt280_500_CVetoBVeto      = Sample( name =  "Sherpa_NNPDF30NNLO_Zee_Pt280_500_CVetoBVeto",             xsec = 0.83477    , feff = 9.0 * 0.59849 , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Zee_Pt500_700_CVetoBVeto      = Sample( name =  "Sherpa_NNPDF30NNLO_Zee_Pt500_700_CVetoBVeto",             xsec = 0.053181   , feff = 9.0 * 0.55451 , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Zee_Pt700_1000_CVetoBVeto     = Sample( name =  "Sherpa_NNPDF30NNLO_Zee_Pt700_1000_CVetoBVeto",            xsec = 0.0096374  , feff = 9.0 * 0.57617 , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Zee_Pt1000_2000_CVetoBVeto    = Sample( name =  "Sherpa_NNPDF30NNLO_Zee_Pt1000_2000_CVetoBVeto",           xsec = 0.0012529  , feff = 9.0 * 0.57115 , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Zee_Pt2000_E_CMS_CVetoBVeto   = Sample( name =  "Sherpa_NNPDF30NNLO_Zee_Pt2000_E_CMS_CVetoBVeto",          xsec = 4.9183e-06 , feff = 9.0 * 0.52636 , kfactor = 0.9751 ) 
                                                                                                                                                                 
Sherpa_NNPDF30NNLO_Zee_Pt0_70_CFilterBVeto       = Sample( name =  "Sherpa_NNPDF30NNLO_Zee_Pt0_70_CFilterBVeto",              xsec = 2078.5     , feff = 9.0 * 0.11914 , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Zee_Pt70_140_CFilterBVeto     = Sample( name =  "Sherpa_NNPDF30NNLO_Zee_Pt70_140_CFilterBVeto",            xsec = 71.341     , feff = 9.0 * 0.20196 , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Zee_Pt140_280_CFilterBVeto    = Sample( name =  "Sherpa_NNPDF30NNLO_Zee_Pt140_280_CFilterBVeto",           xsec = 11.051     , feff = 9.0 * 0.22519 , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Zee_Pt280_500_CFilterBVeto    = Sample( name =  "Sherpa_NNPDF30NNLO_Zee_Pt280_500_CFilterBVeto",           xsec = 0.8291     , feff = 9.0 * 0.2453  , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Zee_Pt500_700_CFilterBVeto    = Sample( name =  "Sherpa_NNPDF30NNLO_Zee_Pt500_700_CFilterBVeto",           xsec = 0.052912   , feff = 9.0 * 0.25074 , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Zee_Pt700_1000_CFilterBVeto   = Sample( name =  "Sherpa_NNPDF30NNLO_Zee_Pt700_1000_CFilterBVeto",          xsec = 0.009431   , feff = 9.0 * 0.26107 , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Zee_Pt1000_2000_CFilterBVeto  = Sample( name =  "Sherpa_NNPDF30NNLO_Zee_Pt1000_2000_CFilterBVeto",         xsec = 0.0012711  , feff = 9.0 * 0.26849 , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Zee_Pt2000_E_CMS_CFilterBVeto = Sample( name =  "Sherpa_NNPDF30NNLO_Zee_Pt2000_E_CMS_CFilterBVeto",        xsec = 4.7405e-06 , feff = 9.0 * 0.26346 , kfactor = 0.9751 )
                                                                                                                                                                 
Sherpa_NNPDF30NNLO_Zee_Pt0_70_BFilter            = Sample( name =  "Sherpa_NNPDF30NNLO_Zee_Pt0_70_BFilter",                   xsec = 2074.0     , feff = 9.0 * 0.06948 , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Zee_Pt70_140_BFilter          = Sample( name =  "Sherpa_NNPDF30NNLO_Zee_Pt70_140_BFilter",                 xsec = 71.777     , feff = 9.0 * 0.12645 , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Zee_Pt140_280_BFilter         = Sample( name =  "Sherpa_NNPDF30NNLO_Zee_Pt140_280_BFilter",                xsec = 11.035     , feff = 9.0 * 0.1448  , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Zee_Pt280_500_BFilter         = Sample( name =  "Sherpa_NNPDF30NNLO_Zee_Pt280_500_BFilter",                xsec = 0.83251    , feff = 9.0 * 0.15152 , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Zee_Pt500_700_BFilter         = Sample( name =  "Sherpa_NNPDF30NNLO_Zee_Pt500_700_BFilter",                xsec = 0.052964   , feff = 9.0 * 0.1543  , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Zee_Pt700_1000_BFilter        = Sample( name =  "Sherpa_NNPDF30NNLO_Zee_Pt700_1000_BFilter",               xsec = 0.0096257  , feff = 9.0 * 0.15925 , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Zee_Pt1000_2000_BFilter       = Sample( name =  "Sherpa_NNPDF30NNLO_Zee_Pt1000_2000_BFilter",              xsec = 0.0012502  , feff = 9.0 * 0.15536 , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Zee_Pt2000_E_CMS_BFilter      = Sample( name =  "Sherpa_NNPDF30NNLO_Zee_Pt2000_E_CMS_BFilter",             xsec = 4.6041e-06 , feff = 9.0 * 0.15562 , kfactor = 0.9751 )

ZeeSherpa22 = Sample( name =   'ZeeSherpa22',
                  tlatex = 'Z #rightarrow ee+jets',
                  fill_color = ROOT.kOrange+1,
                  line_color =  ROOT.kOrange+2,
                  marker_color =  ROOT.kOrange+2,
                  daughters = [
                               Sherpa_NNPDF30NNLO_Zee_Pt0_70_CVetoBVeto,        
                               Sherpa_NNPDF30NNLO_Zee_Pt70_140_CVetoBVeto,                                    
                               Sherpa_NNPDF30NNLO_Zee_Pt140_280_CVetoBVeto,     
                               Sherpa_NNPDF30NNLO_Zee_Pt280_500_CVetoBVeto,     
                               Sherpa_NNPDF30NNLO_Zee_Pt500_700_CVetoBVeto,     
                               Sherpa_NNPDF30NNLO_Zee_Pt700_1000_CVetoBVeto,    
                               Sherpa_NNPDF30NNLO_Zee_Pt1000_2000_CVetoBVeto,   
                               Sherpa_NNPDF30NNLO_Zee_Pt2000_E_CMS_CVetoBVeto,  
                               Sherpa_NNPDF30NNLO_Zee_Pt0_70_CFilterBVeto,      
                               Sherpa_NNPDF30NNLO_Zee_Pt70_140_CFilterBVeto,    
                               Sherpa_NNPDF30NNLO_Zee_Pt140_280_CFilterBVeto,   
                               Sherpa_NNPDF30NNLO_Zee_Pt280_500_CFilterBVeto,   
                               Sherpa_NNPDF30NNLO_Zee_Pt500_700_CFilterBVeto,   
                               Sherpa_NNPDF30NNLO_Zee_Pt700_1000_CFilterBVeto,  
                               Sherpa_NNPDF30NNLO_Zee_Pt1000_2000_CFilterBVeto, 
                               Sherpa_NNPDF30NNLO_Zee_Pt2000_E_CMS_CFilterBVeto,
                               Sherpa_NNPDF30NNLO_Zee_Pt0_70_BFilter,           
                               Sherpa_NNPDF30NNLO_Zee_Pt70_140_BFilter,         
                               Sherpa_NNPDF30NNLO_Zee_Pt140_280_BFilter,        
                               Sherpa_NNPDF30NNLO_Zee_Pt280_500_BFilter,        
                               Sherpa_NNPDF30NNLO_Zee_Pt500_700_BFilter,        
                               Sherpa_NNPDF30NNLO_Zee_Pt700_1000_BFilter,       
                               Sherpa_NNPDF30NNLO_Zee_Pt1000_2000_BFilter,      
                               Sherpa_NNPDF30NNLO_Zee_Pt2000_E_CMS_BFilter,     
                              ],
                ) 


#-------
# Zmumu
#-------
                                                                     
Sherpa_NNPDF30NNLO_Zmumu_Pt0_70_CVetoBVeto         = Sample( name =  "Sherpa_NNPDF30NNLO_Zmumu_Pt0_70_CVetoBVeto",              xsec = 2077.0     , feff = 9.0 * 0.81102 , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Zmumu_Pt70_140_CVetoBVeto       = Sample( name =  "Sherpa_NNPDF30NNLO_Zmumu_Pt70_140_CVetoBVeto",            xsec = 71.72      , feff = 9.0 * 0.6669  , kfactor = 0.9751 ) 
Sherpa_NNPDF30NNLO_Zmumu_Pt140_280_CVetoBVeto      = Sample( name =  "Sherpa_NNPDF30NNLO_Zmumu_Pt140_280_CVetoBVeto",           xsec = 11.105     , feff = 9.0 * 0.62584 , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Zmumu_Pt280_500_CVetoBVeto      = Sample( name =  "Sherpa_NNPDF30NNLO_Zmumu_Pt280_500_CVetoBVeto",           xsec = 0.83396    , feff = 9.0 * 0.59232 , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Zmumu_Pt500_700_CVetoBVeto      = Sample( name =  "Sherpa_NNPDF30NNLO_Zmumu_Pt500_700_CVetoBVeto",           xsec = 0.053138   , feff = 9.0 * 0.58356 , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Zmumu_Pt700_1000_CVetoBVeto     = Sample( name =  "Sherpa_NNPDF30NNLO_Zmumu_Pt700_1000_CVetoBVeto",          xsec = 0.0095435  , feff = 9.0 * 0.57641 , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Zmumu_Pt1000_2000_CVetoBVeto    = Sample( name =  "Sherpa_NNPDF30NNLO_Zmumu_Pt1000_2000_CVetoBVeto",         xsec = 0.0012698  , feff = 9.0 * 0.55785 , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Zmumu_Pt2000_E_CMS_CVetoBVeto   = Sample( name =  "Sherpa_NNPDF30NNLO_Zmumu_Pt2000_E_CMS_CVetoBVeto",        xsec = 4.4846e-06 , feff = 9.0 * 0.56059 , kfactor = 0.9751 )
                                                                                                                                                                    
Sherpa_NNPDF30NNLO_Zmumu_Pt0_70_CFilterBVeto       = Sample( name =  "Sherpa_NNPDF30NNLO_Zmumu_Pt0_70_CFilterBVeto",            xsec = 2075.9     , feff = 9.0 * 0.11858 , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Zmumu_Pt70_140_CFilterBVeto     = Sample( name =  "Sherpa_NNPDF30NNLO_Zmumu_Pt70_140_CFilterBVeto",          xsec = 71.743     , feff = 9.0 * 0.20026 , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Zmumu_Pt140_280_CFilterBVeto    = Sample( name =  "Sherpa_NNPDF30NNLO_Zmumu_Pt140_280_CFilterBVeto",         xsec = 11.099     , feff = 9.0 * 0.22245 , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Zmumu_Pt280_500_CFilterBVeto    = Sample( name =  "Sherpa_NNPDF30NNLO_Zmumu_Pt280_500_CFilterBVeto",         xsec = 0.83155    , feff = 9.0 * 0.24084 , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Zmumu_Pt500_700_CFilterBVeto    = Sample( name =  "Sherpa_NNPDF30NNLO_Zmumu_Pt500_700_CFilterBVeto",         xsec = 0.052965   , feff = 9.0 * 0.25111 , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Zmumu_Pt700_1000_CFilterBVeto   = Sample( name =  "Sherpa_NNPDF30NNLO_Zmumu_Pt700_1000_CFilterBVeto",        xsec = 0.0095439  , feff = 9.0 * 0.25478 , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Zmumu_Pt1000_2000_CFilterBVeto  = Sample( name =  "Sherpa_NNPDF30NNLO_Zmumu_Pt1000_2000_CFilterBVeto",       xsec = 0.0012528  , feff = 9.0 * 0.26111 , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Zmumu_Pt2000_E_CMS_CFilterBVeto = Sample( name =  "Sherpa_NNPDF30NNLO_Zmumu_Pt2000_E_CMS_CFilterBVeto",      xsec = 5.2027e-06 , feff = 9.0 * 0.27202 , kfactor = 0.9751 )
                                                                                                                                                                    
Sherpa_NNPDF30NNLO_Zmumu_Pt0_70_BFilter            = Sample( name =  "Sherpa_NNPDF30NNLO_Zmumu_Pt0_70_BFilter",                 xsec = 2077.6     , feff = 9.0 * 0.070383, kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Zmumu_Pt70_140_BFilter          = Sample( name =  "Sherpa_NNPDF30NNLO_Zmumu_Pt70_140_BFilter",               xsec = 71.574     , feff = 9.0 * 0.1282  , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Zmumu_Pt140_280_BFilter         = Sample( name =  "Sherpa_NNPDF30NNLO_Zmumu_Pt140_280_BFilter",              xsec = 11.078     , feff = 9.0 * 0.14501 , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Zmumu_Pt280_500_BFilter         = Sample( name =  "Sherpa_NNPDF30NNLO_Zmumu_Pt280_500_BFilter",              xsec = 0.83216    , feff = 9.0 * 0.15228 , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Zmumu_Pt500_700_BFilter         = Sample( name =  "Sherpa_NNPDF30NNLO_Zmumu_Pt500_700_BFilter",              xsec = 0.053414   , feff = 9.0 * 0.14697 , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Zmumu_Pt700_1000_BFilter        = Sample( name =  "Sherpa_NNPDF30NNLO_Zmumu_Pt700_1000_BFilter",             xsec = 0.0095915  , feff = 9.0 * 0.15988 , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Zmumu_Pt1000_2000_BFilter       = Sample( name =  "Sherpa_NNPDF30NNLO_Zmumu_Pt1000_2000_BFilter",            xsec = 0.0012306  , feff = 9.0 * 0.15391 , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Zmumu_Pt2000_E_CMS_BFilter      = Sample( name =  "Sherpa_NNPDF30NNLO_Zmumu_Pt2000_E_CMS_BFilter",           xsec = 4.7171e-06 , feff = 9.0 * 0.14554 , kfactor = 0.9751 )

ZmumuSherpa22 = Sample( name =   'ZmumuSherpa22',
                  tlatex = 'Z #rightarrow #mu#mu+jets',
                  fill_color = ROOT.kSpring+1,
                  line_color =  ROOT.kSpring+2,
                  marker_color =  ROOT.kSpring+2,
                  daughters = [
                               Sherpa_NNPDF30NNLO_Zmumu_Pt0_70_CVetoBVeto,        
                               Sherpa_NNPDF30NNLO_Zmumu_Pt70_140_CVetoBVeto,                                    
                               Sherpa_NNPDF30NNLO_Zmumu_Pt140_280_CVetoBVeto,     
                               Sherpa_NNPDF30NNLO_Zmumu_Pt280_500_CVetoBVeto,     
                               Sherpa_NNPDF30NNLO_Zmumu_Pt500_700_CVetoBVeto,     
                               Sherpa_NNPDF30NNLO_Zmumu_Pt700_1000_CVetoBVeto,    
                               Sherpa_NNPDF30NNLO_Zmumu_Pt1000_2000_CVetoBVeto,   
                               Sherpa_NNPDF30NNLO_Zmumu_Pt2000_E_CMS_CVetoBVeto,  
                               Sherpa_NNPDF30NNLO_Zmumu_Pt0_70_CFilterBVeto,      
                               Sherpa_NNPDF30NNLO_Zmumu_Pt70_140_CFilterBVeto,    
                               Sherpa_NNPDF30NNLO_Zmumu_Pt140_280_CFilterBVeto,   
                               Sherpa_NNPDF30NNLO_Zmumu_Pt280_500_CFilterBVeto,   
                               Sherpa_NNPDF30NNLO_Zmumu_Pt500_700_CFilterBVeto,   
                               Sherpa_NNPDF30NNLO_Zmumu_Pt700_1000_CFilterBVeto,  
                               Sherpa_NNPDF30NNLO_Zmumu_Pt1000_2000_CFilterBVeto, 
                               Sherpa_NNPDF30NNLO_Zmumu_Pt2000_E_CMS_CFilterBVeto,
                               Sherpa_NNPDF30NNLO_Zmumu_Pt0_70_BFilter,           
                               Sherpa_NNPDF30NNLO_Zmumu_Pt70_140_BFilter,         
                               Sherpa_NNPDF30NNLO_Zmumu_Pt140_280_BFilter,        
                               Sherpa_NNPDF30NNLO_Zmumu_Pt280_500_BFilter,        
                               Sherpa_NNPDF30NNLO_Zmumu_Pt500_700_BFilter,        
                               Sherpa_NNPDF30NNLO_Zmumu_Pt700_1000_BFilter,       
                               Sherpa_NNPDF30NNLO_Zmumu_Pt1000_2000_BFilter,      
                               Sherpa_NNPDF30NNLO_Zmumu_Pt2000_E_CMS_BFilter,     
                              ],
                ) 

#---------
# Ztautau
#---------

Sherpa_NNPDF30NNLO_Ztautau_Pt0_70_CVetoBVeto         = Sample( name =  "Sherpa_NNPDF30NNLO_Ztautau_Pt0_70_CVetoBVeto",         xsec = 2076.5     , feff = 9.0 * 0.81186 , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Ztautau_Pt70_140_CVetoBVeto       = Sample( name =  "Sherpa_NNPDF30NNLO_Ztautau_Pt70_140_CVetoBVeto",       xsec = 71.687     , feff = 9.0 * 0.66882 , kfactor = 0.9751 ) 
Sherpa_NNPDF30NNLO_Ztautau_Pt140_280_CVetoBVeto      = Sample( name =  "Sherpa_NNPDF30NNLO_Ztautau_Pt140_280_CVetoBVeto",      xsec = 11.031     , feff = 9.0 * 0.62603 , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Ztautau_Pt280_500_CVetoBVeto      = Sample( name =  "Sherpa_NNPDF30NNLO_Ztautau_Pt280_500_CVetoBVeto",      xsec = 0.83515    , feff = 9.0 * 0.59782 , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Ztautau_Pt500_700_CVetoBVeto      = Sample( name =  "Sherpa_NNPDF30NNLO_Ztautau_Pt500_700_CVetoBVeto",      xsec =  0.053095  , feff = 9.0 * 0.58109 , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Ztautau_Pt700_1000_CVetoBVeto     = Sample( name =  "Sherpa_NNPDF30NNLO_Ztautau_Pt700_1000_CVetoBVeto",     xsec = 0.0097332  , feff = 9.0 * 0.56759 , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Ztautau_Pt1000_2000_CVetoBVeto    = Sample( name =  "Sherpa_NNPDF30NNLO_Ztautau_Pt1000_2000_CVetoBVeto",    xsec = 0.0012574  , feff = 9.0 * 0.56725 , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Ztautau_Pt2000_E_CMS_CVetoBVeto   = Sample( name =  "Sherpa_NNPDF30NNLO_Ztautau_Pt2000_E_CMS_CVetoBVeto",   xsec = 4.7536e-06 , feff = 9.0 * 0.52119 , kfactor = 0.9751 )
                                                                                                                                                                  
Sherpa_NNPDF30NNLO_Ztautau_Pt0_70_CFilterBVeto       = Sample( name =  "Sherpa_NNPDF30NNLO_Ztautau_Pt0_70_CFilterBVeto",       xsec = 2061.0     , feff = 9.0 * 0.11987 , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Ztautau_Pt70_140_CFilterBVeto     = Sample( name =  "Sherpa_NNPDF30NNLO_Ztautau_Pt70_140_CFilterBVeto",     xsec = 71.653     , feff = 9.0 * 0.20076 , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Ztautau_Pt140_280_CFilterBVeto    = Sample( name =  "Sherpa_NNPDF30NNLO_Ztautau_Pt140_280_CFilterBVeto",    xsec = 11.069     , feff = 9.0 * 0.22357 , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Ztautau_Pt280_500_CFilterBVeto    = Sample( name =  "Sherpa_NNPDF30NNLO_Ztautau_Pt280_500_CFilterBVeto",    xsec = 0.82916    , feff = 9.0 * 0.24345 , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Ztautau_Pt500_700_CFilterBVeto    = Sample( name =  "Sherpa_NNPDF30NNLO_Ztautau_Pt500_700_CFilterBVeto",    xsec = 0.053205   , feff = 9.0 * 0.25463 , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Ztautau_Pt700_1000_CFilterBVeto   = Sample( name =  "Sherpa_NNPDF30NNLO_Ztautau_Pt700_1000_CFilterBVeto",   xsec = 0.0095498  , feff = 9.0 * 0.25722 , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Ztautau_Pt1000_2000_CFilterBVeto  = Sample( name =  "Sherpa_NNPDF30NNLO_Ztautau_Pt1000_2000_CFilterBVeto",  xsec = 0.0012388  , feff = 9.0 * 0.26301 , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Ztautau_Pt2000_E_CMS_CFilterBVeto = Sample( name =  "Sherpa_NNPDF30NNLO_Ztautau_Pt2000_E_CMS_CFilterBVeto", xsec = 4.541e-06  , feff = 9.0 * 0.29017 , kfactor = 0.9751 )
                                                                                                                                                                  
Sherpa_NNPDF30NNLO_Ztautau_Pt0_70_BFilter            = Sample( name =  "Sherpa_NNPDF30NNLO_Ztautau_Pt0_70_BFilter",            xsec = 2079.3     , feff = 9.0 * 0.068943, kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Ztautau_Pt70_140_BFilter          = Sample( name =  "Sherpa_NNPDF30NNLO_Ztautau_Pt70_140_BFilter",          xsec = 71.679     , feff = 9.0 * 0.12637 , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Ztautau_Pt140_280_BFilter         = Sample( name =  "Sherpa_NNPDF30NNLO_Ztautau_Pt140_280_BFilter",         xsec = 11.078     , feff = 9.0 * 0.14399 , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Ztautau_Pt280_500_BFilter         = Sample( name =  "Sherpa_NNPDF30NNLO_Ztautau_Pt280_500_BFilter",         xsec = 0.83458    , feff = 9.0 * 0.15277 , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Ztautau_Pt500_700_BFilter         = Sample( name =  "Sherpa_NNPDF30NNLO_Ztautau_Pt500_700_BFilter",         xsec = 0.052708   , feff = 9.0 * 0.15883 , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Ztautau_Pt700_1000_BFilter        = Sample( name =  "Sherpa_NNPDF30NNLO_Ztautau_Pt700_1000_BFilter",        xsec = 0.0095039  , feff = 9.0 * 0.15905 , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Ztautau_Pt1000_2000_BFilter       = Sample( name =  "Sherpa_NNPDF30NNLO_Ztautau_Pt1000_2000_BFilter",       xsec = 0.0012661  , feff = 9.0 * 0.11731 , kfactor = 0.9751 )
Sherpa_NNPDF30NNLO_Ztautau_Pt2000_E_CMS_BFilter      = Sample( name =  "Sherpa_NNPDF30NNLO_Ztautau_Pt2000_E_CMS_BFilter",      xsec = 4.5616e-06 , feff = 9.0 * 0.188   , kfactor = 0.9751 )


ZtautauSherpa22 = Sample( name =   'ZtautauSherpa22',
                  tlatex = 'Z #rightarrow #tau#tau+jets',
                  fill_color = ROOT.kAzure-4,
                  line_color =  ROOT.kAzure-5,
                  marker_color =  ROOT.kAzure-5,
                  daughters = [
                               Sherpa_NNPDF30NNLO_Ztautau_Pt0_70_CVetoBVeto,        
                               Sherpa_NNPDF30NNLO_Ztautau_Pt70_140_CVetoBVeto,                                    
                               Sherpa_NNPDF30NNLO_Ztautau_Pt140_280_CVetoBVeto,     
                               Sherpa_NNPDF30NNLO_Ztautau_Pt280_500_CVetoBVeto,     
                               Sherpa_NNPDF30NNLO_Ztautau_Pt500_700_CVetoBVeto,     
                               Sherpa_NNPDF30NNLO_Ztautau_Pt700_1000_CVetoBVeto,    
                               Sherpa_NNPDF30NNLO_Ztautau_Pt1000_2000_CVetoBVeto,   
                               Sherpa_NNPDF30NNLO_Ztautau_Pt2000_E_CMS_CVetoBVeto,  
                               Sherpa_NNPDF30NNLO_Ztautau_Pt0_70_CFilterBVeto,      
                               Sherpa_NNPDF30NNLO_Ztautau_Pt70_140_CFilterBVeto,    
                               Sherpa_NNPDF30NNLO_Ztautau_Pt140_280_CFilterBVeto,   
                               Sherpa_NNPDF30NNLO_Ztautau_Pt280_500_CFilterBVeto,   
                               Sherpa_NNPDF30NNLO_Ztautau_Pt500_700_CFilterBVeto,   
                               Sherpa_NNPDF30NNLO_Ztautau_Pt700_1000_CFilterBVeto,  
                               Sherpa_NNPDF30NNLO_Ztautau_Pt1000_2000_CFilterBVeto, 
                               Sherpa_NNPDF30NNLO_Ztautau_Pt2000_E_CMS_CFilterBVeto,
                               Sherpa_NNPDF30NNLO_Ztautau_Pt0_70_BFilter,           
                               Sherpa_NNPDF30NNLO_Ztautau_Pt70_140_BFilter,         
                               Sherpa_NNPDF30NNLO_Ztautau_Pt140_280_BFilter,        
                               Sherpa_NNPDF30NNLO_Ztautau_Pt280_500_BFilter,   
                               Sherpa_NNPDF30NNLO_Ztautau_Pt500_700_BFilter,        
                               Sherpa_NNPDF30NNLO_Ztautau_Pt700_1000_BFilter,       
                               Sherpa_NNPDF30NNLO_Ztautau_Pt1000_2000_BFilter,      
                               Sherpa_NNPDF30NNLO_Ztautau_Pt2000_E_CMS_BFilter,     
                              ],
                ) 



#--------------------------------------------------------------------------------------------------------------------
# W + jets (Sherpa 2.2.1)
# Notes:
#       * cross sections: https://twiki.cern.ch/twiki/bin/view/AtlasProtected/XsecSummaryWjetsSherpa221 (all filters)
#--------------------------------------------------------------------------------------------------------------------

#-----
# Wenu
#-----

Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV0_70_CVetoBVeto         = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV0_70_CVetoBVeto",         xsec = 19127.0 , feff = 9.0 * 0.82447  , kfactor = 0.9702 ) 
Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV70_140_CVetoBVeto       = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV70_140_CVetoBVeto",       xsec = 942.58  , feff = 9.0 * 0.66872  , kfactor = 0.9702 )
Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV140_280_CVetoBVeto      = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV140_280_CVetoBVeto",      xsec = 339.81  , feff = 9.0 * 0.59691  , kfactor = 0.9702 )
Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV280_500_CVetoBVeto      = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV280_500_CVetoBVeto",      xsec = 72.084  , feff = 9.0 * 0.54441  , kfactor = 0.9702 )
                                                                                                                                                                             
Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV0_70_CFilterBVeto       = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV0_70_CFilterBVeto",       xsec = 19130.0 , feff = 9.0 * 0.1303   , kfactor = 0.9702 )
Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV70_140_CFilterBVeto     = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV70_140_CFilterBVeto",     xsec = 945.67  , feff = 9.0 * 0.22787  , kfactor = 0.9702 )
Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV140_280_CFilterBVeto    = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV140_280_CFilterBVeto",    xsec = 339.87  , feff = 9.0 * 0.28965  , kfactor = 0.9702 )
Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV280_500_CFilterBVeto    = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV280_500_CFilterBVeto",    xsec = 72.128  , feff = 9.0 * 0.31675  , kfactor = 0.9702 )
                                                                                                                                                                             
Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV0_70_BFilter            = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV0_70_BFilter",            xsec = 19135.0  , feff = 9.0 * 0.044141, kfactor = 0.9702 )
Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV70_140_BFilter          = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV70_140_BFilter",          xsec = 945.15   , feff = 9.0 * 0.10341 , kfactor = 0.9702 )
Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV140_280_BFilter         = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV140_280_BFilter",         xsec = 339.48   , feff = 9.0 * 0.10898 , kfactor = 0.9702 )
Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV280_500_BFilter         = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV280_500_BFilter",         xsec = 72.113   , feff = 9.0 * 0.13391 , kfactor = 0.9702 )
                                                                                                                                                                             
Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV500_1000                = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV500_1000",                xsec = 15.224   , feff = 9.0 * 1.0     , kfactor = 0.9702 )
Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV1000_E_CMS              = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV1000_E_CMS",              xsec = 1.2334   , feff = 9.0 * 1.0     , kfactor = 0.9702 )


Wenu = Sample( name =   'Wenu',
                  tlatex = 'W #rightarrow e#nu+jets (Sherpa 2.2.1)',
                  fill_color = ROOT.kRed+1,
                  line_color =  ROOT.kRed+2,
                  marker_color =  ROOT.kRed+2,
                  daughters = [
                               Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV0_70_CVetoBVeto,        
                               Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV70_140_CVetoBVeto,                                    
                               Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV140_280_CVetoBVeto,     
                               Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV280_500_CVetoBVeto,     
                               Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV0_70_CFilterBVeto,      
                               Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV70_140_CFilterBVeto,    
                               Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV140_280_CFilterBVeto,   
                               Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV280_500_CFilterBVeto,   
                               Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV0_70_BFilter,           
                               Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV70_140_BFilter,         
                               Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV140_280_BFilter,        
                               Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV280_500_BFilter,        
                               Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV500_1000,        
                               Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV1000_E_CMS,       
                              ],
                ) 

#------
# Wmunu
#------

Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV0_70_CVetoBVeto         = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV0_70_CVetoBVeto",         xsec = 19143.0, feff =  9.0 * 0.8238  , kfactor = 0.9702 )
Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV70_140_CVetoBVeto       = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV70_140_CVetoBVeto",       xsec = 944.85 , feff =  9.0 * 0.67463 , kfactor = 0.9702 ) 
Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV140_280_CVetoBVeto      = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV140_280_CVetoBVeto",      xsec = 339.54 , feff =  9.0 * 0.62601 , kfactor = 0.9702 )
Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV280_500_CVetoBVeto      = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV280_500_CVetoBVeto",      xsec = 72.067 , feff =  9.0 * 0.54647 , kfactor = 0.9702 )
                                                                                                                                                                                                 
Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV0_70_CFilterBVeto       = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV0_70_CFilterBVeto",       xsec = 19121.0, feff =  9.0 * 0.1304  , kfactor = 0.9702 )
Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV70_140_CFilterBVeto     = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV70_140_CFilterBVeto",     xsec = 937.78 , feff =  9.0 * 0.23456 , kfactor = 0.9702 )
Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV140_280_CFilterBVeto    = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV140_280_CFilterBVeto",    xsec = 340.06 , feff =  9.0 * 0.28947 , kfactor = 0.9702 )
Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV280_500_CFilterBVeto    = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV280_500_CFilterBVeto",    xsec = 72.198 , feff =  9.0 * 0.31743 , kfactor = 0.9702 )
                                                                                                                                                                                                 
Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV0_70_BFilter            = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV0_70_BFilter",            xsec = 19135.0, feff =  9.0 * 0.044118, kfactor = 0.9702 )
Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV70_140_BFilter          = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV70_140_BFilter",          xsec = 944.63 , feff =  9.0 * 0.075648, kfactor = 0.9702 )
Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV140_280_BFilter         = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV140_280_BFilter",         xsec = 339.54 , feff =  9.0 * 0.10872 , kfactor = 0.9702 )
Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV280_500_BFilter         = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV280_500_BFilter",         xsec = 72.045 , feff =  9.0 * 0.13337 , kfactor = 0.9702 )
                                                                                                                                                                                                 
Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV500_1000                = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV500_1000",                xsec = 15.01  , feff = 9.0 * 1.0     , kfactor = 0.9702 )
Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV1000_E_CMS              = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV1000_E_CMS",              xsec = 1.2344 , feff = 9.0 * 1.0     , kfactor = 0.9702 )

Wmunu = Sample( name =   'Wmunu',
                  tlatex = 'W #rightarrow #mu#nu+jets (Sherpa 2.2.1)',
                  fill_color = ROOT.kGreen+1,
                  line_color =  ROOT.kGreen+2,
                  marker_color =  ROOT.kGreen+2,
                  daughters = [
                               Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV0_70_CVetoBVeto,        
                               Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV70_140_CVetoBVeto,                                    
                               Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV140_280_CVetoBVeto,     
                               Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV280_500_CVetoBVeto,     
                               Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV0_70_CFilterBVeto,      
                               Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV70_140_CFilterBVeto,    
                               Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV140_280_CFilterBVeto,   
                               Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV280_500_CFilterBVeto,   
                               Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV0_70_BFilter,           
                               Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV70_140_BFilter,         
                               Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV140_280_BFilter,        
                               Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV280_500_BFilter,        
                               Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV500_1000,        
                               Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV1000_E_CMS,       
                              ],
                ) 

#-------
# Wtaunu
#-------
Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV0_70_CVetoBVeto         = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV0_70_CVetoBVeto",         xsec = 19152.0, feff =  9.0 *0.82495 , kfactor = 0.9702 )
Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV70_140_CVetoBVeto       = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV70_140_CVetoBVeto",       xsec = 947.65 , feff =  9.0 *0.67382 , kfactor = 0.9702 ) 
Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV140_280_CVetoBVeto      = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV140_280_CVetoBVeto",      xsec = 339.36 , feff =  9.0 *0.59622 , kfactor = 0.9702 )
Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV280_500_CVetoBVeto      = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV280_500_CVetoBVeto",      xsec = 72.065 , feff =  9.0 *0.54569 , kfactor = 0.9702 )
                                                                                                                                                                                                  
Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV0_70_CFilterBVeto       = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV0_70_CFilterBVeto",       xsec = 19153.0, feff =  9.0 *0.12934 , kfactor = 0.9702 )
Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV70_140_CFilterBVeto     = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV70_140_CFilterBVeto",     xsec = 946.73 , feff =  9.0 *0.22222 , kfactor = 0.9702 )
Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV140_280_CFilterBVeto    = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV140_280_CFilterBVeto",    xsec = 339.63 , feff =  9.0 *0.29025 , kfactor = 0.9702 )
Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV280_500_CFilterBVeto    = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV280_500_CFilterBVeto",    xsec = 71.976 , feff =  9.0 *0.31648 , kfactor = 0.9702 )
                                                                                                                                                                                                  
Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV0_70_BFilter            = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV0_70_BFilter",            xsec = 19163.0, feff =  9.0 *0.044594, kfactor = 0.9702 )
Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV70_140_BFilter          = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV70_140_BFilter",          xsec = 943.3  , feff =  9.0 *0.10391 , kfactor = 0.9702 )
Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV140_280_BFilter         = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV140_280_BFilter",         xsec = 339.54 , feff =  9.0 *0.11799 , kfactor = 0.9702 )
Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV280_500_BFilter         = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV280_500_BFilter",         xsec = 72.026 , feff =  9.0 *0.13426 , kfactor = 0.9702 )
                                                                                                                                                                                                  
Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV500_1000                = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV500_1000",                xsec = 15.046 , feff = 9.0 * 1.0     , kfactor = 0.9702 )
Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV1000_E_CMS              = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV1000_E_CMS",              xsec = 1.2339 , feff = 9.0 * 1.0     , kfactor = 0.9702 )

Wtaunu = Sample( name =   'Wtaunu',
                  tlatex = 'W #rightarrow #tau#nu+jets (Sherpa 2.2.1)',
                  fill_color = ROOT.kBlue+1,
                  line_color =  ROOT.kBlue+2,
                  marker_color =  ROOT.kBlue+2,
                  daughters = [
                               Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV0_70_CVetoBVeto,        
                               Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV70_140_CVetoBVeto,                                    
                               Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV140_280_CVetoBVeto,     
                               Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV280_500_CVetoBVeto,     
                               Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV0_70_CFilterBVeto,      
                               Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV70_140_CFilterBVeto,    
                               Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV140_280_CFilterBVeto,   
                               Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV280_500_CFilterBVeto,   
                               Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV0_70_BFilter,           
                               Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV70_140_BFilter,         
                               Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV140_280_BFilter,        
                               Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV280_500_BFilter,        
                               Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV500_1000,        
                               Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV1000_E_CMS,       
                              ],
                ) 


#---------------------------------------------------------------------------------------------------------------------
# Z + jets (Sherpa 2.2.1)
# Notes:
#       * cross sections:  https://twiki.cern.ch/twiki/bin/view/AtlasProtected/XsecSummaryZjetsSherpa221 (all filters)
#---------------------------------------------------------------------------------------------------------------------

#-----
# Zee
#-----
Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV0_70_CVetoBVeto         = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV0_70_CVetoBVeto",                xsec = 1981.8 , feff = 9.0 *0.82106 , kfactor = 0.9751 ) 
Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV70_140_CVetoBVeto       = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV70_140_CVetoBVeto",              xsec = 110.5  , feff = 9.0 *0.69043 , kfactor = 0.9751 )
Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV140_280_CVetoBVeto      = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV140_280_CVetoBVeto",             xsec = 40.731 , feff = 9.0 *0.61452 , kfactor = 0.9751 )
Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV280_500_CVetoBVeto      = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV280_500_CVetoBVeto",             xsec = 8.6743 , feff = 9.0 *0.56134 , kfactor = 0.9751 )
                                                                                                                                                                                 
Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV0_70_CFilterBVeto       = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV0_70_CFilterBVeto",              xsec = 1980.8 , feff = 9.0 * 0.11295 , kfactor = 0.9751 )
Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV70_140_CFilterBVeto     = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV70_140_CFilterBVeto",            xsec = 110.63 , feff = 9.0 * 0.18382 , kfactor = 0.9751 )
Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV140_280_CFilterBVeto    = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV140_280_CFilterBVeto",           xsec = 40.67  , feff = 9.0 * 0.23044 , kfactor = 0.9751 )
Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV280_500_CFilterBVeto    = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV280_500_CFilterBVeto",           xsec = 8.6711 , feff = 9.0 * 0.26294 , kfactor = 0.9751 )
                                                                                                                                                                                 
Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV0_70_BFilter            = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV0_70_BFilter",                   xsec = 1981.7 , feff = 9.0 * 0.063809, kfactor = 0.9751 )
Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV70_140_BFilter          = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV70_140_BFilter",                 xsec = 110.31 , feff = 9.0 * 0.11443 , kfactor = 0.9751 )
Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV140_280_BFilter         = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV140_280_BFilter",                xsec = 40.643 , feff = 9.0 * 0.14966 , kfactor = 0.9751 )
Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV280_500_BFilter         = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV280_500_BFilter",                xsec = 8.6766 , feff = 9.0 * 0.17223 , kfactor = 0.9751 )
                                                                                                                                                                                 
Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV500_1000                = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV500_1000",                       xsec = 1.8081 , feff = 9.0 * 1.0     , kfactor = 0.9751 )
Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV1000_E_CMS              = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV1000_E_CMS",                     xsec = 0.14857, feff  =9.0 * 1.0     , kfactor = 0.9751 )



Zee = Sample( name =   'Zee',                                                                                                                              
                  tlatex = 'Z #rightarrow ee+jets (Sherpa 2.2.1)',
                  fill_color = ROOT.kOrange+1,
                  line_color =  ROOT.kOrange+2,
                  marker_color =  ROOT.kOrange+2,
                  daughters = [
                               Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV0_70_CVetoBVeto,        
                               Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV70_140_CVetoBVeto,                                    
                               Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV140_280_CVetoBVeto,     
                               Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV280_500_CVetoBVeto,     
                               Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV0_70_CFilterBVeto,      
                               Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV70_140_CFilterBVeto,    
                               Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV140_280_CFilterBVeto,   
                               Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV280_500_CFilterBVeto,   
                               Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV0_70_BFilter,           
                               Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV70_140_BFilter,         
                               Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV140_280_BFilter,        
                               Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV280_500_BFilter,        
                               Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV500_1000,        
                               Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV1000_E_CMS,       
                              ],
                ) 


#-------
# Zmumu
#-------
                                                                     
Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV0_70_CVetoBVeto         = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV0_70_CVetoBVeto",              xsec = 1983.0 , feff = 9.0 * 0.8221  , kfactor = 0.9751 )
Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV70_140_CVetoBVeto       = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV70_140_CVetoBVeto",            xsec = 108.92 , feff = 9.0 * 0.68873 , kfactor = 0.9751 ) 
Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV140_280_CVetoBVeto      = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV140_280_CVetoBVeto",           xsec = 39.878 , feff = 9.0 * 0.60899 , kfactor = 0.9751 )
Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV280_500_CVetoBVeto      = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV280_500_CVetoBVeto",           xsec = 8.5375 , feff = 9.0 * 0.55906 , kfactor = 0.9751 )
                                                                                                                                                                                   
Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV0_70_CFilterBVeto       = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV0_70_CFilterBVeto",            xsec = 1978.4 , feff = 9.0 * 0.11308 , kfactor = 0.9751 )
Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV70_140_CFilterBVeto     = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV70_140_CFilterBVeto",          xsec = 109.42 , feff = 9.0 * 0.18596 , kfactor = 0.9751 )
Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV140_280_CFilterBVeto    = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV140_280_CFilterBVeto",         xsec = 39.795 , feff = 9.0 * 0.23308 , kfactor = 0.9751 )
Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV280_500_CFilterBVeto    = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV280_500_CFilterBVeto",         xsec = 8.5403 , feff = 9.0 * 0.26528 , kfactor = 0.9751 )
                                                                                                                                                                                   
Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV0_70_BFilter            = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV0_70_BFilter",                 xsec = 1982.2 , feff = 9.0 * 0.064161, kfactor = 0.9751 )
Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV70_140_BFilter          = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV70_140_BFilter",               xsec = 108.91 , feff = 9.0 * 0.11375 , kfactor = 0.9751 )
Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV140_280_BFilter         = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV140_280_BFilter",              xsec = 43.675 , feff = 9.0 * 0.13769 , kfactor = 0.9751 )
Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV280_500_BFilter         = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV280_500_BFilter",              xsec = 8.4932 , feff = 9.0 * 0.17559 , kfactor = 0.9751 )
                                                                                                                                                                                   
Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV500_1000                = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV500_1000",                     xsec = 1.7881 , feff = 9.0 * 1.0     , kfactor = 0.9751 )
Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV1000_E_CMS              = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV1000_E_CMS",                   xsec = 0.14769, feff = 9.0 * 1.0     , kfactor = 0.9751 )


Zmumu = Sample( name =   'Zmumu',                                                                                                                         
                  tlatex = 'Z #rightarrow #mu#mu+jets (Sherpa 2.2.1)',
                  fill_color = ROOT.kSpring+1,
                  line_color =  ROOT.kSpring+2,
                  marker_color =  ROOT.kSpring+2,
                  daughters = [
                               Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV0_70_CVetoBVeto,        
                               Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV70_140_CVetoBVeto,                                    
                               Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV140_280_CVetoBVeto,     
                               Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV280_500_CVetoBVeto,     
                               Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV0_70_CFilterBVeto,      
                               Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV70_140_CFilterBVeto,    
                               Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV140_280_CFilterBVeto,   
                               Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV280_500_CFilterBVeto,   
                               Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV0_70_BFilter,           
                               Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV70_140_BFilter,         
                               Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV140_280_BFilter,        
                               Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV280_500_BFilter,        
                               Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV500_1000,        
                               Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV1000_E_CMS,       
                              ],
                ) 



#---------
# Ztautau
#---------

Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV0_70_CVetoBVeto         = Sample( name =  "Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV0_70_CVetoBVeto",         xsec = 1981.6 , feff = 9.0 * 0.82142 , kfactor = 0.9751 )
Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV70_140_CVetoBVeto       = Sample( name =  "Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV70_140_CVetoBVeto",       xsec = 110.37 , feff = 9.0 * 0.68883 , kfactor = 0.9751 ) 
Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV140_280_CVetoBVeto      = Sample( name =  "Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV140_280_CVetoBVeto",      xsec = 40.781 , feff = 9.0 * 0.60821 , kfactor = 0.9751 )
Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV280_500_CVetoBVeto      = Sample( name =  "Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV280_500_CVetoBVeto",      xsec = 8.5502 , feff = 9.0 * 0.56036 , kfactor = 0.9751 )
                                                                                                                                                                                  
Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV0_70_CFilterBVeto       = Sample( name =  "Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV0_70_CFilterBVeto",       xsec = 1978.8 , feff = 9.0 * 0.11314 , kfactor = 0.9751 )
Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV70_140_CFilterBVeto     = Sample( name =  "Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV70_140_CFilterBVeto",     xsec = 110.51 , feff = 9.0 * 0.1829  , kfactor = 0.9751 )
Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV140_280_CFilterBVeto    = Sample( name =  "Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV140_280_CFilterBVeto",    xsec = 40.74  , feff = 9.0 * 0.22897 , kfactor = 0.9751 )
Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV280_500_CFilterBVeto    = Sample( name =  "Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV280_500_CFilterBVeto",    xsec = 8.6707 , feff = 9.0 * 0.26245 , kfactor = 0.9751 )
                                                                                                                                                                                  
Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV0_70_BFilter            = Sample( name =  "Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV0_70_BFilter",            xsec = 1981.8 , feff = 9.0 * 0.064453, kfactor = 0.9751 )
Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV70_140_BFilter          = Sample( name =  "Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV70_140_BFilter",          xsec = 43.675 , feff = 9.0 * 0.13769 , kfactor = 0.9751 ) #missing cross section!!!
Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV140_280_BFilter         = Sample( name =  "Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV140_280_BFilter",         xsec = 40.761 , feff = 9.0 * 0.13442 , kfactor = 0.9751 )
Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV280_500_BFilter         = Sample( name =  "Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV280_500_BFilter",         xsec = 8.6804 , feff = 9.0 * 0.17313 , kfactor = 0.9751 )
                                                                                                                                                                                  
Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV500_1000                = Sample( name =  "Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV500_1000",                xsec = 1.8096,  feff = 9.0 * 1.0     , kfactor = 0.9751 )
Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV1000_E_CMS              = Sample( name =  "Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV1000_E_CMS",              xsec = 0.14834, feff = 9.0 * 1.0     , kfactor = 0.9751 )


Ztautau = Sample( name =   'Ztautau',
                  tlatex = 'Z #rightarrow #tau#tau+jets (Sherpa 2.2.1)',
                  fill_color = ROOT.kAzure-4,
                  line_color =  ROOT.kAzure-5,
                  marker_color =  ROOT.kAzure-5,
                  daughters = [
                               Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV0_70_CVetoBVeto,        
                               Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV70_140_CVetoBVeto,                                    
                               Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV140_280_CVetoBVeto,     
                               Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV280_500_CVetoBVeto,     
                               Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV0_70_CFilterBVeto,      
                               Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV70_140_CFilterBVeto,    
                               Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV140_280_CFilterBVeto,   
                               Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV280_500_CFilterBVeto,   
                               Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV0_70_BFilter,           
                               Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV70_140_BFilter,         
                               Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV140_280_BFilter,        
                               Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV280_500_BFilter,   
                               Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV500_1000,        
                               Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV1000_E_CMS,       
                              ],
                ) 


#-----------------------------------------------------------------------------
# Top 
#-----------------------------------------------------------------------------


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ttbar ( Powheg + Pythia )
# Notes:
#       * cross sections: https://twiki.cern.ch/twiki/bin/view/AtlasProtected/XsecSummaryTTbar 
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
PowhegPythiaEvtGen_P2012_ttbar_hdamp172p5_nonallhad  = Sample( name =  "PowhegPythiaEvtGen_P2012_ttbar_hdamp172p5_nonallhad", xsec = 696.11, feff = 9.0 * 0.543, kfactor = 1.195 )

ttbar = Sample( name =  'ttbar',
                    tlatex = 'ttbar',
                    fill_color = ROOT.kCyan+1,
                    line_color =  ROOT.kCyan+2,
                    marker_color =  ROOT.kCyan+2,
                    daughters = [
                                 PowhegPythiaEvtGen_P2012_ttbar_hdamp172p5_nonallhad,                              
                                ],
                    ) 


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# single-top
# Notes:
#       * cross sections: https://twiki.cern.ch/twiki/bin/view/AtlasProtected/XsecSummarySingleTop
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
PowhegPythiaEvtGen_P2012_singletop_tchan_lept_antitop = Sample( name = "PowhegPythiaEvtGen_P2012_singletop_tchan_lept_antitop",  xsec = 25.778, feff = 9.0 * 1.0,  kfactor = 1.0193 )
PowhegPythiaEvtGen_P2012_singletop_tchan_lept_top     = Sample( name = "PowhegPythiaEvtGen_P2012_singletop_tchan_lept_top",      xsec = 43.739, feff = 9.0 * 1.0,  kfactor = 1.0094 )
PowhegPythiaEvtGen_P2012_Wt_inclusive_antitop         = Sample( name = "PowhegPythiaEvtGen_P2012_Wt_inclusive_antitop",          xsec = 33.989, feff = 9.0 * 1.0,  kfactor = 1.054  )
PowhegPythiaEvtGen_P2012_Wt_inclusive_top             = Sample( name = "PowhegPythiaEvtGen_P2012_Wt_inclusive_top",              xsec = 34.009, feff = 9.0 * 1.0,  kfactor = 1.054  )

singletop = Sample( name =   'singletop',
                    tlatex = 'single-top',
                    fill_color = ROOT.kRed+3,
                    line_color =  ROOT.kRed+4,
                    marker_color =  ROOT.kRed+4,
                    daughters = [
                                 PowhegPythiaEvtGen_P2012_singletop_tchan_lept_antitop,
                                 PowhegPythiaEvtGen_P2012_singletop_tchan_lept_top,    
                                 PowhegPythiaEvtGen_P2012_Wt_inclusive_antitop,        
                                 PowhegPythiaEvtGen_P2012_Wt_inclusive_top,            
                                ],
                ) 


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# di-jet
# Notes:
#       * cross sections: https://twiki.cern.ch/twiki/bin/viewauth/AtlasProtected/XsecSummaryMultijet
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ0W    = Sample( name = "Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ0W",      xsec = 78420000000.0,  feff = 9.0 * 0.98132,  )
Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ1W    = Sample( name = "Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ1W",      xsec = 78420000000.0,  feff = 9.0 * 0.000672, )  
Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ2W    = Sample( name = "Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ2W",      xsec = 2433200000.0,   feff = 9.0 * 0.000333, )  
Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ3W    = Sample( name = "Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ3W",      xsec = 26454000.0,     feff = 9.0 * 0.00032,  ) 
Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ4W    = Sample( name = "Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ4W",      xsec = 254630.0,       feff = 9.0 * 0.00053,  )
Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ5W    = Sample( name = "Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ5W",      xsec = 4553.5,         feff = 9.0 * 0.000922, ) 
Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ6W    = Sample( name = "Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ6W",      xsec = 257.53,         feff = 9.0 * 0.00094,  )
Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ7W    = Sample( name = "Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ7W",      xsec = 16.215,         feff = 9.0 * 0.000392, ) 
Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ8W    = Sample( name = "Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ8W",      xsec = 0.62504,        feff = 9.0 * 0.010167, )
Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ9W    = Sample( name = "Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ9W",      xsec = 0.01964,        feff = 9.0 * 0.012058, )
Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ10W   = Sample( name = "Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ10W",     xsec = 0.0011962,      feff = 9.0 * 0.005897, )
Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ11W   = Sample( name = "Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ11W",     xsec = 4.2258e-05,     feff = 9.0 * 0.002701, )
Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ12W   = Sample( name = "Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ12W",     xsec = 1.0367e-06,     feff = 9.0 * 0.000425, ) 


dijet = Sample( name =   'dijet',
                tlatex = 'di-jets',
                fill_color = ROOT.kBlue+3,
                line_color =  ROOT.kBlue+4,
                marker_color =  ROOT.kBlue+4,
                daughters = [
                             Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ0W, 
                             Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ1W, 
                             Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ2W, 
                             Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ3W, 
                             Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ4W, 
                             Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ5W, 
                             Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ6W, 
                             Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ7W, 
                             Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ8W, 
                             Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ9W, 
                             Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ10W,
                             Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ11W,
                             Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ12W,
                            ],
                ) 


#-------------------------------------------------------------------------------
# Collections 
#-------------------------------------------------------------------------------

# Samples loaded for SubmitHist.py
#---------------------------------

all_data = data.daughters

all_mc = []

all_mc += ttbar.daughters
all_mc += singletop.daughters

all_mc += Wenu.daughters
all_mc += Wmunu.daughters
all_mc += Wtaunu.daughters

all_mc += Zee.daughters
all_mc += Zmumu.daughters
all_mc += Ztautau.daughters

#all_mc += WenuSherpa22.daughters
#all_mc += WmunuSherpa22.daughters
#all_mc += WtaunuSherpa22.daughters

#all_mc += ZeeSherpa22.daughters
#all_mc += ZmumuSherpa22.daughters
#all_mc += ZtautauSherpa22.daughters

#all_mc += dijet.daughters


# Samples loaded for SubmitPlot.py
#---------------------------------

mc_bkg = []

mc_bkg.append( Wenu )
mc_bkg.append( Wmunu )
mc_bkg.append( Wtaunu )

mc_bkg.append( Zee ) 
mc_bkg.append( Zmumu )
mc_bkg.append( Ztautau )

mc_bkg.append( singletop )
mc_bkg.append( ttbar )

## EOF
