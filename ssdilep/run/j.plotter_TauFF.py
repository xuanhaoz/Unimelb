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

    sys_somesys    = None

    if   systematic == None: pass
    elif systematic == 'SOMESYS_UP':      sys_somesys    = 'up'
    elif systematic == 'SOMESYS_DN':      sys_somesys    = 'dn'
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
        required_triggers = [
                             'HLT_j15', 
                             'HLT_j25', 
                             'HLT_j35', 
                             'HLT_j55', 
                             'HLT_j60', 
                             'HLT_j85', 
                             'HLT_j110',
                             'HLT_j150',
                             'HLT_j175',
                             'HLT_j260',
                             'HLT_j320',
                             'HLT_j360',
                             'HLT_j380',
                             'HLT_j400',
                             'HLT_j420',
                             'HLT_j440',
                             'HLT_j460',
                             ],
        key               = 'jets',
        )

    ## build and pt-sort objects
    ## ---------------------------------------
    loop += pyframe.algs.ListBuilder(
        prefixes = ['tau_','jet_'],
        keys = ['taus','jets'],
        )
    loop += pyframe.algs.AttachTLVs(
        keys = ['taus','jets'],
        )
    # just a decoration of particles ...
    loop += ssdilep.algs.vars.ParticlesBuilder(
        key='taus',
        )

    ## build MET
    ## ---------------------------------------
    #loop += ssdilep.algs.met.METCLUS(
    #    prefix='metFinalClus',
    #    key = 'met_clus',
    #    )
    loop += ssdilep.algs.met.METTRK(
        prefix='metFinalTrk',
        key = 'met_trk',
        )

    ## start preselection cutflow 
    ## ---------------------------------------
    loop += pyframe.algs.CutFlowAlg(key='presel')
    
    ## filter weights
    ## +++++++++++++++++++++++++++++++++++++++
    loop += ssdilep.algs.EvWeights.MCEventWeight(cutflow='presel',key='weight_mc_event')
    loop += ssdilep.algs.EvWeights.Pileup(cutflow='presel',key='weight_pileup')
    #loop += ssdilep.algs.EvWeights.TrigPresc(cutflow='presel',particles="jets",key="weight_data_unpresc")
   
    ## initialize and/or decorate objects
    ## ---------------------------------------
    loop += ssdilep.algs.vars.DiJetVars(key_leptons='taus',key_jets='jets')   
    
    ## cuts
    ## +++++++++++++++++++++++++++++++++++++++
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='OneTau') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='EleVeto') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='MuVeto')
    #loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='TwoSSTaus')
    #loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='TwoOSTaus')
    #loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='TauJetPtRatio')

    #loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='LeadTauOneTrack')
    #loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='LeadTauThreeTrack')

    ## weights configuration
    ## ---------------------------------------
    ## event
    ## +++++++++++++++++++++++++++++++++++++++
    
    # WARNING: no trigger correction available for HLT_mu20_L1MU15 
    """
    """
    ## objects
    ## +++++++++++++++++++++++++++++++++++++++
    """
    """ 
    ## configure histograms
    ## ---------------------------------------
    hist_list = []
    hist_list += ssdilep.hists.TauFF_hists.hist_list
    #hist_list += ssdilep.hists.H2D_hists.hist_list
    #hist_list += ssdilep.hists.PtOnly_hists.hist_list
    
    
    ##-------------------------------------------------------------------------
    ## make plots
    ##-------------------------------------------------------------------------
    ## before any selection
    ## ---------------------------------------
    

    ##-------------------------------------------------------------------------
    ## F1 LeadTauPt > 30
    ##-------------------------------------------------------------------------

    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_NUM_F1',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['SingleJetTrigger', None],
	      ['LeadTauPt30', None],
              ['LeadJetPt150', None],
              ['TauJetDphi282', None],
              ['LeadTauIsMedium', None],
	      ],
            )
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_DEN_F1',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['SingleJetTrigger', None],
	      ['LeadTauPt30', None],
              ['LeadJetPt150', None],
              ['TauJetDphi282', None],
	      ['LeadTauNotMediumAtLeastLoose', None],
              ],
            )

    ##-------------------------------------------------------------------------
    ## F2  LeadJetPt > 170
    ##-------------------------------------------------------------------------

    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_NUM_F2',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['SingleJetTrigger', None],
              #['LeadTauPt65', None],
              ['LeadTauPt65', None],
              ['LeadJetPt170', None],
              ['TauJetDphi282', None],
              ['LeadTauIsMedium', None],
              ],
            )
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_DEN_F2',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['SingleJetTrigger', None],
              #['LeadTauPt65', None],
              ['LeadTauPt65', None],
              ['LeadJetPt170', None],
              ['TauJetDphi282', None],
              ['LeadTauNotMediumAtLeastLoose', None],
              ],
            )
  
    ##-------------------------------------------------------------------------
    ## F3  LeadJetPt > 130
    ##-------------------------------------------------------------------------

    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_NUM_F3',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['SingleJetTrigger', None],
              #['LeadTauPt65', None],
              ['LeadTauPt65', None],
              ['LeadJetPt130', None],
              ['TauJetDphi282', None],
              ['LeadTauIsMedium', None],
              ],
            )
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_DEN_F3',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['SingleJetTrigger', None],
              #['LeadTauPt65', None],
              ['LeadTauPt65', None],
              ['LeadJetPt130', None],
              ['TauJetDphi282', None],
              ['LeadTauNotMediumAtLeastLoose', None],
              ],
            ) 

    ##-------------------------------------------------------------------------
    ## F4  TauJetDphi > 2.90
    ##-------------------------------------------------------------------------

    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_NUM_F4',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['SingleJetTrigger', None],
              #['LeadTauPt65', None],
              ['LeadTauPt65', None],
              ['LeadJetPt130', None],
              ['TauJetDphi290', None],
              ['LeadTauIsMedium', None],
              ],
            )
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_DEN_F4',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['SingleJetTrigger', None],
              #['LeadTauPt65', None],
              ['LeadTauPt65', None],
              ['LeadJetPt130', None],
              ['TauJetDphi290', None],
              ['LeadTauNotMediumAtLeastLoose', None],
              ],
            )
 
    ##-------------------------------------------------------------------------
    ## F5  TauJetDphi > 2.50
    ##-------------------------------------------------------------------------

    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_NUM_F5',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['SingleJetTrigger', None],
              #['LeadTauPt65', None],
              ['LeadTauPt65', None],
              ['LeadJetPt130', None],
              ['TauJetDphi250', None],
              ['LeadTauIsMedium', None],
              ],
            )
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_DEN_F5',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['SingleJetTrigger', None],
              #['LeadTauPt65', None],
              ['LeadTauPt65', None],
              ['LeadJetPt130', None],
              ['TauJetDphi250', None],
              ['LeadTauNotMediumAtLeastLoose', None],
              ],
            )

    ##-------------------------------------------------------------------------
    ## F6  AtLeastTwoJet
    ##-------------------------------------------------------------------------

    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_NUM_F6',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['SingleJetTrigger', None],
              #['LeadTauPt65', None],
              ['LeadTauPt65', None],
              ['LeadJetPt130', None],
              ['TauJetDphi282', None],
	      ['AtLeastTwoJet', None],
              ['LeadTauIsMedium', None],
              ],
            )
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_DEN_F6',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['SingleJetTrigger', None],
              #['LeadTauPt65', None],
              ['LeadTauPt65', None],
              ['LeadJetPt130', None],
              ['TauJetDphi282', None],
	      ['AtLeastTwoJet', None],
              ['LeadTauNotMediumAtLeastLoose', None],
              ],
            )

    ##-------------------------------------------------------------------------
    ## F7  AtLeastThreeJet
    ##-------------------------------------------------------------------------

    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_NUM_F7',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['SingleJetTrigger', None],
              #['LeadTauPt65', None],
              ['LeadTauPt65', None],
              ['LeadJetPt130', None],
              ['TauJetDphi282', None],
              ['AtLeastThreeJet', None],
              ['LeadTauIsMedium', None],
              ],
            )
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_DEN_F7',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['SingleJetTrigger', None],
              #['LeadTauPt65', None],
              ['LeadTauPt65', None],
              ['LeadJetPt130', None],
              ['TauJetDphi282', None],
              ['AtLeastThreeJet', None],
              ['LeadTauNotMediumAtLeastLoose', None],
              ],
            )

    ##-------------------------------------------------------------------------
    ## F8  TauJetPtRatio
    ##-------------------------------------------------------------------------
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_NUM_F8',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['SingleJetTrigger', None],
              #['LeadTauPt65', None],
              ['LeadTauPt65', None],
              ['LeadJetPt130', None],
              ['TauJetDphi282', None],
              ['AtLeastThreeJet', None],
              ['LeadTauIsMedium', None],
              ['TauJetPtRatio', None],
              ],
            )
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_DEN_F8',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['SingleJetTrigger', None],
              #['LeadTauPt65', None],
              ['LeadTauPt65', None],
              ['LeadJetPt130', None],
              ['TauJetDphi282', None],
              ['AtLeastThreeJet', None],
              ['LeadTauNotMediumAtLeastLoose', None],
              ['TauJetPtRatio', None],
              ],
            )

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



