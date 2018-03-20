#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
j.postprocessor.py
"""

## std modules
import os,re

## ROOT
import ROOT
ROOT.gROOT.SetBatch(True)

## my modules
import pyframe

## local modules
import ssdilep

GeV = 1000.0


#_____________________________________________________________________________
def analyze(config):
  
    ##-------------------------------------------------------------------------
    ## setup
    ##-------------------------------------------------------------------------
    config['tree']       = 'physics/nominal'
    config['do_var_log'] = True
    main_path = os.getenv('MAIN')
    
    ## build chain
    chain = ROOT.TChain(config['tree'])
    for fn in config['input']: chain.Add(fn)

    ##-------------------------------------------------------------------------
    ## systematics 
    ##-------------------------------------------------------------------------
    """
    pass systematics on the command line like this:
    python j.plotter.py --config="sys:SYS_UP"
    """
    config.setdefault('sys',None)
    systematic = config['sys']

    sys_ff    = None

    if   systematic == None: pass
    elif systematic == 'FF_UP':      sys_ff    = 'up'
    elif systematic == 'FF_DN':      sys_ff    = 'dn'
    else: 
        assert False, "Invalid systematic %s!"%(systematic)


    ##-------------------------------------------------------------------------
    ## event loop
    ##-------------------------------------------------------------------------
    loop = pyframe.core.EventLoop(name='ssdilep',
                                  sampletype=config['sampletype'],
                                  samplename=config['samplename'],
                                  outfile=config['samplename']+".root",
                                  quiet=False,
                                  )
    
    ## configure the list of triggers 
    ## with eventual prescales and puts a
    ## trig list to the store for later cutflow
    ## ---------------------------------------
    loop += ssdilep.algs.vars.BuildTrigConfig(
        required_triggers = ["HLT_mu26_imedium", "HLT_mu50"],
        key               = 'muons',
        )
    
    ## build and pt-sort objects
    ## ---------------------------------------
    loop += pyframe.algs.ListBuilder(
        prefixes = ['muon_','el_','jet_'],
        keys = ['muons','electrons','jets'],
        )
    loop += pyframe.algs.AttachTLVs(
        keys = ['muons','electrons','jets'],
        )
    # just a decoration of particles ...
    loop += ssdilep.algs.vars.ParticlesBuilder(
        key='muons',
        )

    ## build MET
    ## ---------------------------------------
    loop += ssdilep.algs.met.METCLUS(
        prefix='metFinalClus',
        key = 'met_clus',
        )
    loop += ssdilep.algs.met.METTRK(
        prefix='metFinalTrk',
        key = 'met_trk',
        )
   
    ## start preselection cutflow 
    ## ---------------------------------------
    loop += pyframe.algs.CutFlowAlg(key='presel')
    
    ## weights
    ## +++++++++++++++++++++++++++++++++++++++
    loop += ssdilep.algs.EvWeights.MCEventWeight(cutflow='presel',key='weight_mc_event')
    loop += ssdilep.algs.EvWeights.LPXKfactor(cutflow='presel',key='weight_kfactor')
    loop += ssdilep.algs.EvWeights.Pileup(cutflow='presel',key='weight_pileup')
    
    ## initialize and/or decorate objects
    ## ---------------------------------------
    loop += ssdilep.algs.vars.TagAndProbeVars(key_muons='muons')   
    loop += ssdilep.algs.vars.DiMuVars(key_muons='muons')   

    ## cuts
    ## +++++++++++++++++++++++++++++++++++++++
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='TwoMuons') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='TagAndProbeExist') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='AllMuPt25') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='AllMuLoose') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='AllMuEta247') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='AllMuZ0SinTheta05') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='AllMuIsoBound08') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='AllPairsM20') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='Mlow200') 

    
    loop += ssdilep.algs.vars.ProbeVars(key_tag='tag',key_probe='probe')   

    ## weights configuration
    ## ---------------------------------------
    ## event
    ## +++++++++++++++++++++++++++++++++++++++
    loop += ssdilep.algs.EvWeights.MuTrigSF(
            trig_list     = ["HLT_mu26_imedium_OR_HLT_mu50"],
            mu_reco       = "Loose",
            mu_iso        = "FixedCutTightTrackOnly",
            key           = "MuTrigSFRecoLoose",
            scale         = None,
            )
    
    ## objects
    ## +++++++++++++++++++++++++++++++++++++++
    loop += ssdilep.algs.ObjWeights.MuAllSF(
            mu_index      = 'tag',
            mu_iso        = "NotFixedCutTightTrackOnly",
            mu_reco       = "Loose",
            key           = "TagRecoSF",
            scale         = None,
            )
    loop += ssdilep.algs.ObjWeights.MuAllSF(
            mu_index      = 'tag',
            mu_iso        = "FixedCutTightTrackOnly",
            mu_reco       = "Loose",
            key           = "TagAllSF",
            scale         = None,
            )
    loop += ssdilep.algs.ObjWeights.MuAllSF(
            mu_index      = 'probe',
            mu_iso        = "NotFixedCutTightTrackOnly",
            mu_reco       = "Loose",
            key           = "ProbeRecoSF",
            scale         = None,
            )
    loop += ssdilep.algs.ObjWeights.MuAllSF(
            mu_index      = 'probe',
            mu_iso        = "FixedCutTightTrackOnly",
            mu_reco       = "Loose",
            key           = "ProbeAllSF",
            scale         = None,
            )
    
    ## configure histograms
    ## ---------------------------------------
    hist_list = []
    #hist_list += ssdilep.hists.Main_hists.hist_list
    hist_list += ssdilep.hists.TAndP_hists.hist_list
    
    
    ##-------------------------------------------------------------------------
    ## make plots
    ##-------------------------------------------------------------------------
    """    
    # F1
    # -------------------------------
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'ProbeTight_F1',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow  = [
              ['TwoSSMuons',None],
              ['TagIsMatched',['MuTrigSFRecoLoose']],
              ['TagisTight',['TagAllSF']],
              ['ProbeisTight',None],
              ['ProbeTruthFilter',None],
              ],
            )
    """ 
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'ProbeLoose_F1',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow  = [
              ['TwoSSMuons',None],
              ['TagIsMatched',['MuTrigSFRecoLoose']],
              ['TagPt28',None],
              ['TagisTight',['TagAllSF']],
              ['ProbeisLoose',None],
              ['ProbeTruthFilter',None],
              ],
            )
    """
    # F2
    # -------------------------------
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'ProbeTight_F2',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow  = [
              ['TwoOSMuons',None],
              ['TagIsMatched',['MuTrigSFRecoLoose']],
              ['TagisTight',['TagAllSF']],
              ['ProbeisTight',None],
              ['ProbeTruthFilter',None],
              ],
            )
    
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'ProbeLoose_F2',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow  = [
              ['TwoOSMuons',None],
              ['TagIsMatched',['MuTrigSFRecoLoose']],
              ['TagisTight',['TagAllSF']],
              ['ProbeisLoose',None],
              ['ProbeTruthFilter',None],
              ],
            )
   
    # R1
    # -------------------------------
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'ProbeTight_R1',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow  = [
              ['TwoSSMuons',None],
              ['TagIsMatched',['MuTrigSFRecoLoose']],
              ['TagisTight',['TagAllSF']],
              ['ProbeisTight',None],
              ['ProbeMuFakeFilter',None],
              ],
            )
    
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'ProbeLoose_R1',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow  = [
              ['TwoSSMuons',None],
              ['TagIsMatched',['MuTrigSFRecoLoose']],
              ['TagisTight',['TagAllSF']],
              ['ProbeisLoose',None],
              ['ProbeMuFakeFilter',None],
              ],
            )
    
    # R2
    # -------------------------------
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'ProbeTight_R2',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow  = [
              ['TwoSSMuons',None],
              ['TagIsMatched',['MuTrigSFRecoLoose']],
              ['TagisTight',['TagAllSF']],
              ['ProbeisTight',None],
              ['ProbeMuFailTruthFilter',None],
              ],
            )
    
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'ProbeLoose_R2',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow  = [
              ['TwoSSMuons',None],
              ['TagIsMatched',['MuTrigSFRecoLoose']],
              ['TagisTight',['TagAllSF']],
              ['ProbeisLoose',None],
              ['ProbeMuFailTruthFilter',None],
              ],
            )
    
    # R3
    # -------------------------------
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'ProbeTight_R3',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow  = [
              ['TwoOSMuons',None],
              ['TagIsMatched',['MuTrigSFRecoLoose']],
              ['TagisTight',['TagAllSF']],
              ['ProbeisTight',None],
              ['ProbeMuFakeFilter',None],
              ],
            )
    
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'ProbeLoose_R3',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow  = [
              ['TwoOSMuons',None],
              ['TagIsMatched',['MuTrigSFRecoLoose']],
              ['TagisTight',['TagAllSF']],
              ['ProbeisLoose',None],
              ['ProbeMuFakeFilter',None],
              ],
            )
    
    # R4
    # -------------------------------
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'ProbeTight_R4',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow  = [
              ['TwoOSMuons',None],
              ['TagIsMatched',['MuTrigSFRecoLoose']],
              ['TagisTight',['TagAllSF']],
              ['ProbeisTight',None],
              ['ProbeMuFailTruthFilter',None],
              ],
            )
    
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'ProbeLoose_R4',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow  = [
              ['TwoOSMuons',None],
              ['TagIsMatched',['MuTrigSFRecoLoose']],
              ['TagisTight',['TagAllSF']],
              ['ProbeisLoose',None],
              ['ProbeMuFailTruthFilter',None],
              ],
            )
    """
    loop += pyframe.algs.HistCopyAlg()

    ##-------------------------------------------------------------------------
    ## run the job
    ##-------------------------------------------------------------------------
    loop.run(chain, 0, config['events'],
            branches_on_file = config.get('branches_on_file'),
            do_var_log = config.get('do_var_log'),
            )
#______________________________________________________________________________
if __name__ == '__main__':
    pyframe.config.main(analyze)



