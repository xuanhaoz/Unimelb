#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import random
import os
from itertools import combinations
from copy import copy, deepcopy
from types import MethodType

import pyframe
import ROOT

from units import GeV

import logging
log = logging.getLogger(__name__)

def fatal(message):
    sys.exit("Fatal error in %s: %s" % (__file__, message))

#------------------------------------------------------------------------------
class BuildTrigConfig(pyframe.core.Algorithm):
    """
    Algorithm to configure the trigger chain
    """
    #__________________________________________________________________________
    def __init__(self, 
          cutflow           = None,
          required_triggers = None,
          key               = None):
        pyframe.core.Algorithm.__init__(self, name="TrigConfig", isfilter=True)
        self.cutflow           = cutflow
        self.required_triggers = required_triggers
        self.key               = key
    
    #__________________________________________________________________________
    def initialize(self):
        log.info('initialize trigger config for %s...' % self.key)

    #__________________________________________________________________________
    def execute(self, weight):
        
      #assert len(self.chain.passedTriggers) == len(self.chain.triggerPrescales), "ERROR: # passed triggers != # trigger prescales !!!"
     
      nolim = 1000. 

      # slices for jet triggers
      # -----------------------
      jet_trigger_slice = {}
      jet_trigger_slice["HLT_j15"]  = (17.  * GeV, nolim * GeV)
      jet_trigger_slice["HLT_j25"]  = (30.  * GeV, nolim * GeV)
      jet_trigger_slice["HLT_j35"]  = (40.  * GeV, nolim * GeV)
      jet_trigger_slice["HLT_j55"]  = (60.  * GeV, nolim * GeV)
      jet_trigger_slice["HLT_j60"]  = (66.  * GeV, nolim * GeV)
      jet_trigger_slice["HLT_j85"]  = (94.  * GeV, nolim * GeV)
      jet_trigger_slice["HLT_j110"] = (120. * GeV, nolim * GeV)
      jet_trigger_slice["HLT_j150"] = (165. * GeV, nolim * GeV)
      jet_trigger_slice["HLT_j175"] = (195. * GeV, nolim * GeV)
      jet_trigger_slice["HLT_j260"] = (285. * GeV, nolim * GeV)
      jet_trigger_slice["HLT_j320"] = (350. * GeV, nolim * GeV)
      jet_trigger_slice["HLT_j360"] = (395. * GeV, nolim * GeV)
      jet_trigger_slice["HLT_j380"] = (420. * GeV, nolim * GeV)
      jet_trigger_slice["HLT_j400"] = (440. * GeV, nolim * GeV)
      jet_trigger_slice["HLT_j420"] = (465. * GeV, nolim * GeV)
      jet_trigger_slice["HLT_j440"] = (485. * GeV, nolim * GeV)
      jet_trigger_slice["HLT_j460"] = (505. * GeV, nolim * GeV)


      # slices for muon triggers
      # ------------------------
      mu_trigger_slice = {}
      mu_trigger_slice["HLT_mu24"]  = (26. * GeV,  nolim * GeV)
      mu_trigger_slice["HLT_mu50"]  = (43. * GeV,  nolim * GeV)


      # initialise the different slices
      pt_slice = {}
      if self.key == "jets": pt_slice = jet_trigger_slice
      if self.key == "muons": pt_slice = mu_trigger_slice

      if not "reqTrig" in self.store.keys():
        self.store["reqTrig"] = self.required_triggers

      """
      if not "passTrig" in self.store.keys():
        self.store["passTrig"] = {}
        for trig,presc in zip(self.chain.passedTriggers,self.chain.triggerPrescales):
          if trig in pt_slice.keys():
            self.store["passTrig"][trig] = {"prescale":presc, "pt_slice":pt_slice[trig]}
      """
      
      # bogus crap that we need until 
      # the prescales will be back on
      if not "passTrig" in self.store.keys():
        self.store["passTrig"] = {}
        for trig,presc in zip(self.chain.passedTriggers,self.chain.passedTriggers):
          if trig in pt_slice.keys():
            self.store["passTrig"][trig] = {"prescale":1, "pt_slice":pt_slice[trig]}


      return True

#-------------------------------------------------------------------------------
class Particle(pyframe.core.ParticleProxy):
    """
    Variables added to the particle
    """
    #__________________________________________________________________________
    def __init__(self, particle, **kwargs):
        pyframe.core.ParticleProxy.__init__(self, 
             tree_proxy = particle.tree_proxy,
             index      = particle.index,
             prefix     = particle.prefix)   
        self.particle = particle
        self.__dict__ = particle.__dict__.copy() 
    
    #__________________________________________________________________________
    def isMatchedToTrigChain(self):
      return self.isTrigMatched

    # https://svnweb.cern.ch/trac/atlasoff/browser/PhysicsAnalysis/MCTruthClassifier/tags/MCTruthClassifier-00-00-26/MCTruthClassifier/MCTruthClassifierDefs.h
    # https://twiki.cern.ch/twiki/bin/view/AtlasProtected/MCTruthClassifier 
    #__________________________________________________________________________
    def isTrueNonIsoMuon(self):
      matchtype = self.truthType in [5,7,8]
      #return self.isTruthMatchedToMuon and matchtype
      return matchtype
    #__________________________________________________________________________
    def isTrueIsoMuon(self):
      matchtype = self.truthType in [6]
      #return self.isTruthMatchedToMuon and matchtype
      return matchtype


class ParticlesBuilder(pyframe.core.Algorithm):
    #__________________________________________________________________________
    def __init__(self, name="ParticlesBuilder", key=""):
        pyframe.core.Algorithm.__init__(self, name=name)
        self.key  = key
    #__________________________________________________________________________
    def initialize(self):
        log.info('initialize single particles for %s ...' % self.key)
    #__________________________________________________________________________
    def execute(self,weight):
        self.store[self.key] = [Particle(copy(l)) for l in self.store[self.key]]


#------------------------------------------------------------------------------
class TagAndProbeVars(pyframe.core.Algorithm):
    """
    computes variables for the tag-and-probe selection
    in the di-muon channel
    """
    #__________________________________________________________________________
    def __init__(self, 
                 name      = 'TagAndProbeVars',
                 key_muons = 'muons',
                 key_met   = 'met_trk',
                 ):
        pyframe.core.Algorithm.__init__(self, name)
        self.key_muons = key_muons
        self.key_met = key_met

    #__________________________________________________________________________
    def execute(self, weight):
        pyframe.core.Algorithm.execute(self, weight)
        """
        computes variables and puts them in the store
        """

        ## get objects from event candidate
        ## --------------------------------------------------
        assert self.store.has_key(self.key_muons), "muons key: %s not found in store!" % (self.key_muons)
        muons = self.store[self.key_muons]
        
        if len(muons)<2: 
          return True
        
        met = self.store[self.key_met]
        muon1 = muons[0] 
        muon2 = muons[1] 

        # ------------------
        # at least two muons
        # ------------------
          
        # definition of tag and probe 
        lead_mu_is_tight = bool(muon1.isIsolated_FixedCutTightTrackOnly and muon1.trkd0sig<3.)
        lead_mu_is_loose = bool(not muon1.isIsolated_FixedCutTightTrackOnly and muon1.trkd0sig<10.)

        sublead_mu_is_tight = bool(muon2.isIsolated_FixedCutTightTrackOnly and muon2.trkd0sig<3.)
        sublead_mu_is_loose = bool(not muon2.isIsolated_FixedCutTightTrackOnly and muon2.trkd0sig<10.)
       
        if lead_mu_is_tight and sublead_mu_is_tight:
          if random.randint(0,9) > 4:
            self.store['tag'] = muon1
            self.store['probe'] = muon2 
          else:
            self.store['tag'] = muon2
            self.store['probe'] = muon1 
        elif lead_mu_is_loose or sublead_mu_is_tight:
          self.store['tag'] = muon2
          self.store['probe'] = muon1
        elif sublead_mu_is_loose or lead_mu_is_tight:
          self.store['tag'] = muon1
          self.store['probe'] = muon2


        return True


#------------------------------------------------------------------------------
class ProbeVars(pyframe.core.Algorithm):
    """
    computes variables for the tag-and-probe selection
    in the di-muon channel
    """
    #__________________________________________________________________________
    def __init__(self, 
                 name      = 'ProbeVars',
                 key_tag   = 'tag',
                 key_probe = 'probe',
                 ):
        pyframe.core.Algorithm.__init__(self, name)
        
        self.key_tag   = key_tag
        self.key_probe = key_probe
    #__________________________________________________________________________
    def execute(self, weight):
        pyframe.core.Algorithm.execute(self, weight)
        """
        computes variables and puts them in the store
        """

        ## get objects from event candidate
        ## --------------------------------------------------
        assert self.store.has_key(self.key_tag), "tag key: %s not found in store!" % (self.key_tag)
        assert self.store.has_key(self.key_probe), "probe key: %s not found in store!" % (self.key_probe)
        tag   = self.store[self.key_tag]
        probe = self.store[self.key_probe]
       
        """
        iso/pt<0.8
        ----------
        p0  = 5.66581   +/-   6.81268
        p1  = 1.25722   +/-   0.0603463 
        """
        
        p0  = 5.66581
        p1  = 1.25722

        # RMS is in GeV
        RMS = {}

        RMS["ptiso_20_25"]   = 0.0
        RMS["ptiso_25_30"]   = 12.4064460713
        RMS["ptiso_30_35"]   = 13.2433526355
        RMS["ptiso_35_40"]   = 14.4159208352
        RMS["ptiso_40_45"]   = 16.2752782594
        RMS["ptiso_45_50"]   = 18.2407633765
        RMS["ptiso_50_55"]   = 19.5622710782
        RMS["ptiso_55_60"]   = 20.7644848946
        RMS["ptiso_60_65"]   = 22.4369845476
        RMS["ptiso_65_70"]   = 24.2929719957
        RMS["ptiso_70_75"]   = 26.7638147383
        RMS["ptiso_75_80"]   = 27.4958307282
        RMS["ptiso_80_85"]   = 28.6467918032
        RMS["ptiso_85_90"]   = 30.3006145851
        RMS["ptiso_90_95"]   = 31.4212980513
        RMS["ptiso_95_100"]  = 32.3088211841
        RMS["ptiso_100_105"] = 33.1844260853
        RMS["ptiso_105_110"] = 34.7326856135
        RMS["ptiso_110_115"] = 35.2736180541
        RMS["ptiso_115_120"] = 36.4129657978
        RMS["ptiso_120_125"] = 37.4741421704
        RMS["ptiso_125_130"] = 37.7874721485
        RMS["ptiso_130_135"] = 38.557678202
        RMS["ptiso_135_140"] = 40.4975404537
        RMS["ptiso_140_145"] = 40.998314068
        RMS["ptiso_145_150"] = 42.8896945092
        RMS["ptiso_150_155"] = 43.5952011684
        RMS["ptiso_155_160"] = 44.1735072515
        RMS["ptiso_160_165"] = 45.5866562887
        RMS["ptiso_165_170"] = 47.524117093
        RMS["ptiso_170_175"] = 44.5405330826
        RMS["ptiso_175_180"] = 48.3866372102
        RMS["ptiso_180_185"] = 52.0070717859
        RMS["ptiso_185_190"] = 47.744819892
        RMS["ptiso_190_195"] = 50.5839599775
        RMS["ptiso_195_200"] = 54.7332840655
        RMS["ptiso_200_205"] = 53.1491008055
        RMS["ptiso_205_210"] = 52.2524439685
        RMS["ptiso_210_215"] = 54.2499328095
        RMS["ptiso_215_220"] = 55.2824187879
        RMS["ptiso_220_225"] = 57.1261788076
        RMS["ptiso_225_230"] = 53.3562019687
        RMS["ptiso_230_235"] = 63.8959744557
        RMS["ptiso_235_240"] = 58.3227138415
        RMS["ptiso_240_245"] = 62.1696165824
        RMS["ptiso_245_250"] = 60.1443277898
        RMS["ptiso_250_255"] = 43.3303155178
        RMS["ptiso_255_260"] = 49.5807605407
        RMS["ptiso_260_265"] = 63.1491729748
        RMS["ptiso_265_270"] = 66.1689375705
        RMS["ptiso_270_275"] = 81.6534137744
        RMS["ptiso_275_280"] = 83.7920957755
        RMS["ptiso_280_285"] = 45.3639772014
        RMS["ptiso_285_290"] = 74.506656773
        RMS["ptiso_290_295"] = 69.0819259747
        RMS["ptiso_295_300"] = 56.9806508594
        RMS["ptiso_300_305"] = 50.6671197602
        RMS["ptiso_305_310"] = 71.6676212378
        RMS["ptiso_310_315"] = 62.3832400493
        RMS["ptiso_315_320"] = 94.7307677967
        
        probe_ptiso = ( probe.tlv.Pt() + probe.ptvarcone30 ) / GeV

        probe_RMS = 94.7307677967 # last bin!
        
        for k,v in RMS.iteritems():
          if probe_ptiso >= float(k.split("_")[1]) and probe_ptiso < float(k.split("_")[2]):
            probe_RMS = v

        self.store["probe_ujet_pt"] =  p1 * probe_ptiso + p0 + random.gauss(0.,probe_RMS)

        return True



#------------------------------------------------------------------------------
class DiJetVars(pyframe.core.Algorithm):
          
    """
    computes variables for the di-jet selection used for
    muon fake-factor measurement
    """
    #__________________________________________________________________________
    def __init__(self, 
                 name        = 'VarsAlg',
                 key_leptons = 'taus',
                 key_jets    = 'jets',
                 key_met     = 'met_trk',
                 build_tight_jets = False,
                 ):
        pyframe.core.Algorithm.__init__(self, name)
        self.key_leptons = key_leptons
        self.key_jets = key_jets
        self.key_met = key_met
        self.build_tight_jets = build_tight_jets

    #__________________________________________________________________________
    def execute(self, weight):
        pyframe.core.Algorithm.execute(self, weight)
        """
        computes variables and puts them in the store
        """

        ## get objects from event candidate
        ## --------------------------------------------------
        assert self.store.has_key(self.key_leptons), "leptons key: %s not found in store!" % (self.key_leptons)
        leptons = self.store[self.key_leptons]
        met = self.store[self.key_met]
        jets = self.store[self.key_jets]
       
        prefix = ""
        if self.key_leptons == "muons": prefix = "mu"
        if self.key_leptons == "taus": prefix = "tau"

        # ---------------------------
        # at least a lepton and a jet
        # ---------------------------
        
        if bool(len(jets)) and bool(len(leptons)):
          self.store['%sjet_dphi'%prefix] = leptons[0].tlv.DeltaPhi(jets[0].tlv)
          scdphi = 0.0
          scdphi += ROOT.TMath.Cos(met.tlv.Phi() - leptons[0].tlv.Phi())
          scdphi += ROOT.TMath.Cos(met.tlv.Phi() - jets[0].tlv.Phi())
          self.store['%sjet_scdphi'%prefix] = scdphi
       
          self.store['%sjet_ptratio'%prefix] = leptons[0].tlv.Pt() / jets[0].tlv.Pt()
        
        # -------------------------
        # build tight jets
        # -------------------------
        if self.build_tight_jets:
           jets_tight = []
           jets_nontight = []
           for jet in jets:
             if jet.JvtPass_Medium and jet.fJvtPass_Medium and abs(jet.eta) <= 2.8:
               jets_tight += [jet]
             else:
               jets_nontight += [jet]
           
           jets_tight.sort(key=lambda x: x.tlv.Pt(), reverse=True )
           jets_nontight.sort(key=lambda x: x.tlv.Pt(), reverse=True )
           
           if len(jets_tight) > 1:
             assert jets_tight[0].tlv.Pt() >= jets_tight[1].tlv.Pt(), "jets_tight not sorted.."
           if len(jets_nontight) > 1:
             assert jets_nontight[0].tlv.Pt() >= jets_nontight[1].tlv.Pt(), "jets_nontight not sorted.."
           self.store['jets_tight'] = jets_tight        
           self.store['jets_nontight'] = jets_nontight        
        return True



#------------------------------------------------------------------------------
class DiMuVars(pyframe.core.Algorithm):
    """
    computes variables for the di-muon selection
    """
    #__________________________________________________________________________
    def __init__(self, 
                 name      = 'DiMuVars',
                 key_muons = 'muons',
                 key_met   = 'met_trk',
                 ):
        pyframe.core.Algorithm.__init__(self, name)
        self.key_muons = key_muons
        self.key_met   = key_met

    #__________________________________________________________________________
    def execute(self, weight):
        pyframe.core.Algorithm.execute(self, weight)
        """
        computes variables and puts them in the store
        """

        ## get objects from event candidate
        ## --------------------------------------------------
        assert self.store.has_key(self.key_muons), "muons key: %s not found in store!" % (self.key_muons)
        muons = self.store[self.key_muons]
        met = self.store[self.key_met]
        
        # ------------------
        # at least two muons
        # ------------------
        
        # dict containing pair 
        # and significance
        ss_pairs = {} 
        if len(muons)>=2:
          
          for p in combinations(muons,2):
            if p[0].trkcharge * p[1].trkcharge > 0.:
              ss_pairs[p] = p[0].trkd0sig + p[1].trkd0sig 
          
          max_sig  = 1000.
          for pair,sig in ss_pairs.iteritems():
            if sig < max_sig: 
              if pair[0].tlv.Pt() > pair[1].tlv.Pt():
                self.store['muon1'] = pair[0]
                self.store['muon2'] = pair[1]
              else: 
                self.store['muon1'] = pair[1]
                self.store['muon2'] = pair[0]
              max_sig = sig 
        
        if ss_pairs:
          muon1 = self.store['muon1'] 
          muon2 = self.store['muon2'] 
          muon1T = ROOT.TLorentzVector()
          muon1T.SetPtEtaPhiM( muon1.tlv.Pt(), 0., muon1.tlv.Phi(), muon1.tlv.M() )
          muon2T = ROOT.TLorentzVector()
          muon2T.SetPtEtaPhiM( muon2.tlv.Pt(), 0., muon2.tlv.Phi(), muon2.tlv.M() )
        
          self.store['charge_product'] = muon2.trkcharge*muon1.trkcharge
          self.store['mVis']           = (muon2.tlv+muon1.tlv).M()
          self.store['mTtot']          = (muon1T + muon2T + met.tlv).M()  
          self.store['muons_dphi']     = muon2.tlv.DeltaPhi(muon1.tlv)
          self.store['muons_deta']     = muon2.tlv.Eta()-muon1.tlv.Eta()
          self.store['muons_pTH']      = (muon2.tlv+muon1.tlv).Pt()
          self.store['muons_dR']       = math.sqrt(self.store['muons_dphi']**2 + self.store['muons_deta']**2)
         
        # puts additional muons in the store
        if ss_pairs and len(muons)>2:
           i = 2
           for m in muons:
             if m==self.store['muon1'] or m==self.store['muon2']: continue
             i = i + 1
             self.store['muon%d'%i] = m

        return True


#------------------------------------------------------------------------------
class MultiMuVars(pyframe.core.Algorithm):
    """
    computes variables for the di-muon selection
    """
    #__________________________________________________________________________
    def __init__(self, 
                 name      = 'MultiMuVars',
                 key_muons = 'muons',
                 key_met   = 'met_trk',
                 ):
        pyframe.core.Algorithm.__init__(self, name)
        self.key_muons = key_muons
        self.key_met   = key_met

    #__________________________________________________________________________
    def execute(self, weight):
        pyframe.core.Algorithm.execute(self, weight)
        """
        computes variables and puts them in the store
        """

        ## get objects from event candidate
        ## --------------------------------------------------
        assert self.store.has_key(self.key_muons), "muons key: %s not found in store!" % (self.key_muons)
        muons = self.store[self.key_muons]

        #--------------------
        # two same-sign pairs
        #--------------------
        two_pairs = {}
        if len(muons)>=4:
          for q in combinations(muons,4):
            if q[0].trkcharge * q[1].trkcharge * q[2].trkcharge * q[3].trkcharge > 0.0:
              two_pairs[q] = q[0].trkd0sig + q[1].trkd0sig + q[2].trkd0sig + q[3].trkd0sig

          max_sig  = 1000.
          for quad,sig in two_pairs.iteritems():

            if sig < max_sig:
              max_sig = sig 

              #Case 1: total charge 0
              if quad[0].trkcharge + quad[1].trkcharge + quad[2].trkcharge + quad[3].trkcharge == 0:
                for p in combinations(quad,2):
                  if (p[0].trkcharge + p[1].trkcharge) == 2:
                    if p[0].tlv.Pt() > p[1].tlv.Pt():
                      self.store['muon1'] = p[0]
                      self.store['muon2'] = p[1]
                    else:
                      self.store['muon1'] = p[1]
                      self.store['muon2'] = p[0]
                  elif (p[0].trkcharge + p[1].trkcharge) == -2:
                    if p[0].tlv.Pt() > p[1].tlv.Pt():
                      self.store['muon3'] = p[0]
                      self.store['muon4'] = p[1]
                    else:
                      self.store['muon3'] = p[1]
                      self.store['muon4'] = p[0]

              #Case 2: Total Charge = +/- 4
              elif abs(quad[0].trkcharge + quad[1].trkcharge + quad[2].trkcharge + quad[3].trkcharge) == 4:
                print("This event has charge 4!\n") #print for debugging purposes 
                self.store['muon1'] = quad[0]
                self.store['muon2'] = quad[1]
                self.store['muon3'] = quad[2]
                self.store['muon4'] = quad[3]

              #Failsafe
              else:
                print("Error: Something has gone horribly wrong with this event!\n")
                self.store['muon1'] = quad[0]
                self.store['muon2'] = quad[1]
                self.store['muon3'] = quad[2]
                self.store['muon4'] = quad[3]

        if two_pairs:
          muon1 = self.store['muon1']
          muon2 = self.store['muon2']
          muon1T = ROOT.TLorentzVector()
          muon1T.SetPtEtaPhiM( muon1.tlv.Pt(), 0., muon1.tlv.Phi(), muon1.tlv.M() )
          muon2T = ROOT.TLorentzVector()
          muon2T.SetPtEtaPhiM( muon2.tlv.Pt(), 0., muon2.tlv.Phi(), muon2.tlv.M() )

          self.store['charge_product1'] = muon2.trkcharge*muon1.trkcharge
          self.store['charge_sum1']     = muon1.trkcharge + muon2.trkcharge
          self.store['mVis1']           = (muon2.tlv+muon1.tlv).M()
          self.store['muons_dphi1']     = muon2.tlv.DeltaPhi(muon1.tlv)
          self.store['muons_deta1']     = muon2.tlv.Eta()-muon1.tlv.Eta()
          self.store['pTH1']            = (muon2.tlv+muon1.tlv).Pt()
          self.store['muons_dR1']       = math.sqrt(self.store['muons_dphi1']**2 + self.store['muons_deta1']**2)

          muon3 = self.store['muon3']
          muon4 = self.store['muon4']
          muon3T = ROOT.TLorentzVector()
          muon3T.SetPtEtaPhiM( muon3.tlv.Pt(), 0., muon3.tlv.Phi(), muon3.tlv.M() )
          muon4T = ROOT.TLorentzVector()
          muon4T.SetPtEtaPhiM( muon4.tlv.Pt(), 0., muon4.tlv.Phi(), muon4.tlv.M() )

          self.store['charge_product2'] = muon4.trkcharge*muon3.trkcharge
          self.store['charge_sum2']     = muon3.trkcharge + muon4.trkcharge
          self.store['mVis2']           = (muon4.tlv+muon3.tlv).M()
          self.store['muons_dphi2']     = muon4.tlv.DeltaPhi(muon3.tlv)
          self.store['muons_deta2']     = muon4.tlv.Eta()-muon3.tlv.Eta()
          self.store['pTH2']            = (muon4.tlv+muon3.tlv).Pt()
          self.store['muons_dR2']       = math.sqrt(self.store['muons_dphi2']**2 + self.store['muons_deta2']**2)

          self.store['charge_product'] = muon4.trkcharge * muon3.trkcharge * muon2.trkcharge * muon1.trkcharge
          self.store['charge_sum']     = muon1.trkcharge + muon2.trkcharge + muon3.trkcharge + muon4.trkcharge
          self.store['mTtot']          = (muon1T + muon2T + muon3T + muon4T + met.tlv).M()
          self.store['mVis']           = (self.store['mVis1']+self.store['mVis2'])/2
          self.store['dmVis']          = self.store['mVis1'] - self.store['mVis2']
          self.store['pairs_dphi']     = (muon3.tlv+muon4.tlv).DeltaPhi(muon1.tlv+muon2.tlv)
          self.store['pairs_deta']     = (muon3.tlv+muon4.tlv).Eta()-(muon1.tlv+muon2.tlv).Eta()
          self.store['pairs_dR']       = math.sqrt(self.store['pairs_dphi']**2 + self.store['pairs_deta']**2)

        return True


# EOF 


