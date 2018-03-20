#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
EvWeights.py:
weights applied
to the event
"""

from math import sqrt
from array import array
from copy import copy
# logging
import logging
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

# ROOT
import ROOT
import metaroot

# pyframe
import pyframe

# pyutils
import rootutils

from units import GeV

#------------------------------------------------------------------------------
class TrigPresc(pyframe.core.Algorithm):
    """
    Algorithm to unprescale data
    Applies the prescale according to a specific list of triggers
    """
    #__________________________________________________________________________
    def __init__(self, 
          cutflow     = None,
          #use_avg     = None,
          particles   = None,
          key         = None):
        pyframe.core.Algorithm.__init__(self, name="TrigPresc", isfilter=True)
        self.cutflow     = cutflow
        #self.use_avg     = use_avg
        self.particles   = particles
        self.key         = key
    #__________________________________________________________________________
    def execute(self, weight):
        trigpresc = 1.0
        
        # luminosity weighted prescales
        #presc_dict = {
        #    "HLT_mu20_L1MU15"     : 354.153, 
        #    "HLT_mu24"            : 47.64, 
        #    "HLT_mu50"            : 1.0,
        #    #"HLT_mu26_imedium"    : 1.943,
        #    "HLT_mu26_ivarmedium" : 1.098,
        #    }

        if "data" in self.sampletype:
          ineff_list = []
          for trig in self.store["reqTrig"]: 
            
            # used for main analysis
            # ----------------------
            #for mu in self.store["muons"]:
            #  if mu.tlv.Pt()>=self.store["singleMuTrigSlice"][trig][0] and mu.tlv.Pt()<self.store["singleMuTrigSlice"][trig][1]:
            #    ineff_list.append(1. - 1. / presc_dict[trig])
            
            # used for fake-factors
            # ----------------------
            #if trig in self.store["passTrig"].keys(): 
            #  for mu in self.store["muons"]:
            #    ineff_list.append(1. - 1. / presc_dict[trig])


            # used for new fake-factors
            # ----------------------
            if trig in self.store["passTrig"].keys(): 
              for p in self.store[self.particles]:
                if self.store["passTrig"][trig]["prescale"] == 0.: continue
                ineff_list.append(1. - 1. / self.store["passTrig"][trig]["prescale"])

          if ineff_list:
            tot_ineff = 1.0
            for ineff in ineff_list: tot_ineff *= ineff
            trigpresc -= tot_ineff
        
        trigpresc = 1. / trigpresc

        if self.key:
          self.store[self.key] = trigpresc
        self.set_weight(trigpresc*weight)
        return True

#------------------------------------------------------------------------------
class Pileup(pyframe.core.Algorithm):
    """
    multiply event weight by pileup weight

    if 'key' is specified the pileup weight will be put in the store
    """
    #__________________________________________________________________________
    def __init__(self, cutflow=None,key=None):
        pyframe.core.Algorithm.__init__(self, name="Pileup", isfilter=True)
        self.cutflow = cutflow
        self.key = key
    #__________________________________________________________________________
    def execute(self, weight):
        if "mc" in self.sampletype: 
            wpileup = self.chain.weight_pileup
            if self.key: self.store[self.key] = wpileup
            self.set_weight(wpileup*weight)
        return True


#------------------------------------------------------------------------------
class MCEventWeight(pyframe.core.Algorithm):
    """
    multiply event weight by MC weight

    if 'key' is specified the MC weight will be put in the store
    """
    #__________________________________________________________________________
    def __init__(self, cutflow=None,key=None):
        pyframe.core.Algorithm.__init__(self, name="MCEventWeight", isfilter=True)
        self.cutflow = cutflow
        self.key = key
    #__________________________________________________________________________
    def execute(self, weight):
        if "mc" in self.sampletype: 
            wmc = self.chain.mcEventWeight
            if self.key: self.store[self.key] = wmc
            self.set_weight(wmc*weight)
        return True


#------------------------------------------------------------------------------
class LPXKfactor(pyframe.core.Algorithm):
    """
    multiply event weight by Kfactor from LPX tool

    """
    #__________________________________________________________________________
    def __init__(self, cutflow=None,key=None):
        pyframe.core.Algorithm.__init__(self, name="LPXKfactor", isfilter=True)
        self.cutflow = cutflow
        self.key = key
    #__________________________________________________________________________
    def execute(self, weight):
        if "mc" in self.sampletype: 
            wkf = self.chain.LPXKfactorVec.at(0)
            if self.key: self.store[self.key] = wkf
            self.set_weight(wkf*weight)
        return True


#------------------------------------------------------------------------------
class MuTrigSF(pyframe.core.Algorithm):
    """
    Muon trigger scale factor (OR of signle muon triggers)
    """
    #__________________________________________________________________________
    def __init__(self, name="MuTrigSF",
            trig_list   = None,
            match_all   = False,
            mu_iso      = None,
            mu_reco     = None,
            key         = None,
            scale       = None,
            ):
        pyframe.core.Algorithm.__init__(self, name=name)
        self.trig_list   = trig_list # if for some reason a different list is needed
        self.match_all   = match_all
        self.mu_iso      = mu_iso
        self.mu_reco     = mu_reco
        self.key         = key
        self.scale       = scale

        assert key, "Must provide key for storing mu reco sf"
    #_________________________________________________________________________
    def initialize(self):
      
      if not self.mu_reco:      self.mu_reco = "Medium"
      if not self.mu_iso:       self.mu_iso  = "FixedCutTightTrackOnly"
      
      if "Not" in self.mu_iso:  self.mu_iso  = "FixedCutTightTrackOnly"
      if "Not" in self.mu_reco: self.mu_reco = "Medium"

      if not self.trig_list: self.trig_list = self.store["reqTrig"]

    #_________________________________________________________________________
    def execute(self, weight):
        trig_sf=1.0
        if "mc" in self.sampletype: 
          muons = self.store['muons']
          
          eff_data_chain = 1.0 
          eff_mc_chain   = 1.0
          
          for i,m in enumerate(muons):
          
            eff_data_muon = 1.0 
            eff_mc_muon   = 1.0

            #if m.isTruthMatchedToMuon: 
            if m.isTrueIsoMuon(): 
              for trig in self.trig_list:
                
                sf_muon  = getattr(m,"_".join(["TrigEff","SF",trig,"Reco"+self.mu_reco,"Iso"+self.mu_iso])).at(0)
                eff_muon = getattr(m,"_".join(["TrigMCEff",trig,"Reco"+self.mu_reco,"Iso"+self.mu_iso])).at(0)
                
                # EXOT12 for v1 ntuples
                #sf_muon  = getattr(m,"_".join(["TrigEff","SF",self.mu_reco,self.mu_iso])).at(0)
                #eff_muon = getattr(m,"_".join(["TrigMCEff",self.mu_reco,self.mu_iso])).at(0)
                
                eff_data_muon *= 1 - sf_muon * eff_muon
                eff_mc_muon   *= 1 - eff_muon
              
              eff_data_muon = ( 1 - eff_data_muon )
              eff_mc_muon   = ( 1 - eff_mc_muon )
              
              if self.match_all:
                eff_data_chain *= eff_data_muon
                eff_mc_chain   *= eff_mc_muon
              else:
                eff_data_chain *= 1. - eff_data_muon
                eff_mc_chain   *= 1. - eff_mc_muon
          
          if not self.match_all: 
            eff_data_chain = ( 1 - eff_data_chain )
            eff_mc_chain   = ( 1 - eff_mc_chain )
          
          if eff_mc_chain > 0:
            trig_sf = eff_data_chain / eff_mc_chain
          
          #if self.scale: pass
       
        if self.key: 
          self.store[self.key] = trig_sf
        return True

#------------------------------------------------------------------------------
class GlobalBjet(pyframe.core.Algorithm):
    """
    GlobalBjet
    """
    #__________________________________________________________________________
    def __init__(self, name="GlobalBjet",
            key            = None,
            ):

        pyframe.core.Algorithm.__init__(self, name=name)
        self.key               = key

        assert key, "Must provide key for storing ele reco sf"
    #_________________________________________________________________________
    def initialize(self):
      pass
    #_________________________________________________________________________
    def execute(self, weight):
      sf=1.0
      if "mc" in self.sampletype: 
        jets = self.store['jets_tight']
        for jet in jets:
          if jet.is_MV2c10_FixedCutBEff_77: 
            sf *= getattr(jet,"SF_MV2c10_FixedCutBEff_77").at(0)

      if self.key: 
        self.store[self.key] = sf
      return True


#------------------------------------------------------------------------------
class GlobalJVT(pyframe.core.Algorithm):
    """
    GlobalJVT
    """
    #__________________________________________________________________________
    def __init__(self, name="GlobalJVT",
            key            = None,
            ):

        pyframe.core.Algorithm.__init__(self, name=name)
        self.key               = key

        assert key, "Must provide key for storing ele reco sf"
    #_________________________________________________________________________
    def initialize(self):
      pass
    #_________________________________________________________________________
    def execute(self, weight):
      sf=1.0
      if "mc" in self.sampletype: 
        jets = self.store['jets']
        for jet in jets:
          sf *= getattr(jet,"JvtEff_SF_Medium").at(0)
          sf *= getattr(jet,"fJvtEff_SF_Medium").at(0)

      if self.key: 
        self.store[self.key] = sf
      return True


#------------------------------------------------------------------------------
class EffCorrPair(pyframe.core.Algorithm):
    """
    Applies trigger efficiency correction for muon pairs
    """
    #__________________________________________________________________________
    def __init__(self, name="EffCorrector",
            config_file     = None,
            mu_lead_type    = None,
            mu_sublead_type = None,
            key             = None,
            scale           = None
            ):
        pyframe.core.Algorithm.__init__(self,name=name)
        self.config_file     = config_file
        self.mu_lead_type    = mu_lead_type
        self.mu_sublead_type = mu_sublead_type
        self.key             = key
        self.scale           = scale
        
        assert config_file, "Must provide config file!"
        assert key, "Must provide key for storing fakefactor"
    #_________________________________________________________________________
    def initialize(self):
        f = ROOT.TFile.Open(self.config_file)
        assert f, "Failed to open config file for efficiency correction: %s"%(self.config_file)

        g_loose_eff = f.Get("g_loose_eff")
        g_tight_eff = f.Get("g_tight_eff")
        
        assert self.mu_lead_type in ["Loose","Tight"], "mu_lead_type not Loose or Tight"
        assert self.mu_sublead_type in ["Loose","Tight"], "mu_sublead_type not Loose or Tight"
        
        assert g_loose_eff, "Failed to get 'g_loose_eff' from %s"%(self.config_file)
        assert g_tight_eff, "Failed to get 'g_tight_eff' from %s"%(self.config_file)
        
        self.g_loose_eff = g_loose_eff.Clone()
        self.g_tight_eff = g_tight_eff.Clone()
        f.Close()
    #_________________________________________________________________________
    def execute(self, weight):
        #muons = self.store['muons']

        # check particular quality 
        # of muons in the SS pair
        muons = [self.store['muon1'],self.store['muon2']]
         
        if len(self.store['muons'])>2:
          for i in xrange(3,len(self.store['muons'])+1):
            muons.append(self.store['muon%d'%i])

        mu_lead    = muons[0]
        mu_sublead = muons[1]
        
        pt_lead    = mu_lead.tlv.Pt()/GeV  
        pt_sublead = mu_sublead.tlv.Pt()/GeV  
       
        g_lead_eff    = None
        g_sublead_eff = None

        if self.mu_lead_type == "Loose":      g_lead_eff = self.g_loose_eff
        elif self.mu_lead_type == "Tight":    g_lead_eff = self.g_tight_eff
        
        if self.mu_sublead_type == "Loose":   g_sublead_eff = self.g_loose_eff
        elif self.mu_sublead_type == "Tight": g_sublead_eff = self.g_tight_eff

        eff_lead = 0.0
        eff_sublead = 0.0
        eff_lead_tight = 0.0
        eff_sublead_tight = 0.0

        for ibin_lead in xrange(1,g_lead_eff.GetN()):
          for ibin_sublead in xrange(1,g_sublead_eff.GetN()):
          
            edlow_lead = g_lead_eff.GetX()[ibin_lead] - g_lead_eff.GetEXlow()[ibin_lead]
            edhi_lead  = g_lead_eff.GetX()[ibin_lead] + g_lead_eff.GetEXhigh()[ibin_lead]
            if pt_lead>=edlow_lead and pt_lead<edhi_lead: 
              eff_lead = g_lead_eff.GetY()[ibin_lead]
              eff_lead_tight = self.g_tight_eff.GetY()[ibin_lead]
              
            edlow_sublead = g_sublead_eff.GetX()[ibin_sublead] - g_sublead_eff.GetEXlow()[ibin_sublead]
            edhi_sublead  = g_sublead_eff.GetX()[ibin_sublead] + g_sublead_eff.GetEXhigh()[ibin_sublead]
            if pt_sublead>=edlow_sublead and pt_sublead<edhi_sublead: 
              eff_sublead = g_sublead_eff.GetY()[ibin_sublead]
              eff_sublead_tight = self.g_tight_eff.GetY()[ibin_sublead]
         
         
        ineff_others = 1.0 

        for m in muons[2:]:
          muon_is_loose    = bool(not m.isIsolated_FixedCutTightTrackOnly and m.trkd0sig<10.)
          muon_is_tight    = bool(m.isIsolated_FixedCutTightTrackOnly and m.trkd0sig<3.)
          
          pt_other    = m.tlv.Pt()/GeV  
          eff_other   = 0.0
          g_other_eff = None
          
          if muon_is_loose:
            g_other_eff = self.g_loose_eff
          elif muon_is_tight:
            g_other_eff = self.g_tight_eff
          else: continue
         
          for ibin_other in xrange(1,g_other_eff.GetN()):
            
              edlow_other = g_other_eff.GetX()[ibin_other] - g_other_eff.GetEXlow()[ibin_other]
              edhi_other  = g_other_eff.GetX()[ibin_other] + g_other_eff.GetEXhigh()[ibin_other]
              if pt_other>=edlow_other and pt_other<edhi_other: 
                eff_other = g_other_eff.GetY()[ibin_other]
                
              ineff_others *= (1 - eff_other)
        
        num_pair_eff = 1 - ( 1 - eff_lead_tight ) * ( 1 - eff_sublead_tight ) * ineff_others
        den_pair_eff = 1 - ( 1 - eff_lead ) * ( 1 - eff_sublead ) * ineff_others
       
       
        corr_eff = 1.0
        if den_pair_eff != 0:
          corr_eff =  num_pair_eff / den_pair_eff

        # error bars are asymmetric
        #eff_up_mu = self.g_ff.GetEYhigh()[ibin_mu]
        #eff_dn_mu = self.g_ff.GetEYlow()[ibin_mu]
        
        if self.scale == 'up': pass
        if self.scale == 'dn': pass
       
        if self.key: 
          self.store[self.key] = corr_eff

        return True


# EOF
