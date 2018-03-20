#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
algs.py

This module contains a set of analysis specific algs 
for calculating variables, applying selection and 
plotting.
"""

## std modules
import itertools
import os
import math
import ROOT

## logging
import logging
log = logging.getLogger(__name__)

## python
from itertools import combinations
import collections
from copy import copy
import sys

## pyframe
import pyframe

from units import GeV

#------------------------------------------------------------------------------
class CutAlg(pyframe.core.Algorithm):
    """
    Filtering alg for applying a single cut.  The predefined cuts must be
    implemeneted as a function with the prefix "cut_". One can then specify the
    cut to be applied by passing the cut=<cut name> in the constructor, which
    will execture the cut_<cut name>() function.
    """
    #__________________________________________________________________________
    def __init__(self,
                 name     = None,
                 cut      = None,
                 cutflow  = None,
                 isfilter = True,
                 ):
        pyframe.core.Algorithm.__init__(self, name if name else cut,isfilter=isfilter)
        self.cutflow = cutflow
         
    #__________________________________________________________________________
    def execute(self, weight):
        pyframe.core.Algorithm.execute(self, weight)

        return self.apply_cut(self.name)

    #__________________________________________________________________________
    def apply_cut(self,cutname):
        if self.store.has_key(cutname): return self.store[cutname]
        cut_function = 'cut_%s'%cutname
        assert hasattr(self,cut_function),"cut %s doesnt exist!'"%(cutname)
        self.store[cutname] = result = getattr(self,cut_function)()
        return result
    
    #__________________________________________________________________________
    def cut_AtLeastTwoMuons(self):
      return self.chain.nmuon > 1
    #__________________________________________________________________________
    def cut_AtLeastTwoSSMuons(self):
      muons = self.store['muons']
      if self.chain.nmuon >= 2:
        for p in combinations(muons,2):
          if p[0].trkcharge * p[1].trkcharge > 0.0: return True
      return False
    #__________________________________________________________________________
    def cut_AtLeastTwoSSMuonPairs(self):
      muons = self.store['muons']
      if self.chain.nmuon >= 4:
        for p in combinations(muons,4):
          if p[0].trkcharge * p[1].trkcharge * p[2].trkcharge * p[3].trkcharge > 0.0: return True
      return False
    #__________________________________________________________________________
    def cut_OddSSMuons(self):
      muons = self.store['muons']
      ss_pairs = []
      if self.chain.nmuon >= 2:
        for p in combinations(muons,2):
          if p[0].trkcharge * p[1].trkcharge > 0.0: ss_pairs.append(p)
      if len(ss_pairs)==1 or len(ss_pairs)==3: return True
      return False
    #__________________________________________________________________________
    def cut_OddOSMuons(self):
      muons = self.store['muons']
      ss_pairs = []
      if self.chain.nmuon >= 2:
        for p in combinations(muons,2):
          if p[0].trkcharge * p[1].trkcharge < 0.0: ss_pairs.append(p)
      if len(ss_pairs)==1 or len(ss_pairs)==3: return True
      return False
    
    #__________________________________________________________________________
    def cut_AtLeastOneMuPt28(self):
        muons = self.store['muons']
        for m in muons:
          if m.tlv.Pt()>28*GeV: return True
        return False
    #__________________________________________________________________________
    def cut_LeadMuPt30(self):
        muons = self.store['muons']
        return muons[0].tlv.Pt()>30*GeV
    #__________________________________________________________________________
    def cut_LeadMuPt28(self):
        muons = self.store['muons']
        return muons[0].tlv.Pt()>28*GeV
    #__________________________________________________________________________
    def cut_SubLeadMuPt28(self):
        muons = self.store['muons']
        return muons[1].tlv.Pt()>28*GeV
    #__________________________________________________________________________
    def cut_TagPt28(self):
        tag = self.store['tag']
        return tag.tlv.Pt()>28*GeV
    
    #__________________________________________________________________________
    def cut_OneTau(self):
        return self.chain.ntau == 1
    #__________________________________________________________________________
    def cut_AtLeastOneJet(self):
        return self.chain.njet > 0
    #__________________________________________________________________________
    def cut_AtLeastTwoJet(self):
        return self.chain.njet > 1
    #__________________________________________________________________________
    def cut_AtLeastThreeJet(self):
        return self.chain.njet > 2

    #__________________________________________________________________________
    def cut_OneMuon(self):
        return self.chain.nmuon == 1
    #__________________________________________________________________________
    def cut_TwoMuons(self):
        return self.chain.nmuon == 2
    #__________________________________________________________________________
    def cut_ThreeMuons(self):
        return self.chain.nmuon == 3
    #__________________________________________________________________________
    def cut_FourMuons(self):
        return self.chain.nmuon == 4
    
    #__________________________________________________________________________
    def cut_TwoSSMuons(self):
      muons  = self.store['muons']
      if len(muons)==2:
        if muons[0].trkcharge * muons[1].trkcharge > 0.0:
          return True
      return False
    
    #__________________________________________________________________________
    def cut_TwoOSMuons(self):
      muons  = self.store['muons']
      if len(muons)==2:
        if muons[0].trkcharge * muons[1].trkcharge < 0.0:
          return True
      return False
    
    #__________________________________________________________________________
    def cut_TwoSSTaus(self):
      taus  = self.store['taus']
      if len(taus)==2:
        if taus[0].charge * taus[1].charge > 0.0:
          return True
      return False

    #__________________________________________________________________________
    def cut_TwoOSTaus(self):
      taus  = self.store['taus']
      if len(taus)==2:
        if taus[0].charge * taus[1].charge < 0.0:
          return True
      return False

    #__________________________________________________________________________
    def cut_OneTightJet(self):
      return len(self.store['jets_tight']) == 1
    
    #__________________________________________________________________________
    def cut_AtLeastTwoTightJets(self):
      return len(self.store['jets_tight']) >=2
    
    #__________________________________________________________________________
    def cut_Two50TightJets(self):
      tight_jets_above_50 = []
      if len(self.store['jets_tight']) >= 2:
        for j in self.store['jets_tight']:
          if j.tlv.Pt() > 50 * GeV: tight_jets_above_50.append(j)
      return len(tight_jets_above_50) == 2


    #__________________________________________________________________________
    def cut_LeadJetPt150(self):
      return self.store['jets'][0].tlv.Pt()>150*GeV
    #__________________________________________________________________________
    def cut_LeadTauPt65(self):
      return self.store['taus'][0].tlv.Pt()>65*GeV
    #__________________________________________________________________________
    def cut_LeadTauPt30(self):
      return self.store['taus'][0].tlv.Pt()>30*GeV
    #__________________________________________________________________________
    def cut_SubleadTauPt30(self):
      return self.store['taus'][1].tlv.Pt()>30*GeV
    #__________________________________________________________________________
    def cut_SubleadTauPt50(self):
      return self.store['taus'][1].tlv.Pt()>50*GeV

    #__________________________________________________________________________
    def cut_LeadJetPt130(self):
      return self.store['jets'][0].tlv.Pt()>130*GeV
    #__________________________________________________________________________
    def cut_LeadJetPt170(self):
      return self.store['jets'][0].tlv.Pt()>170*GeV 


    #__________________________________________________________________________
    def cut_EleVeto(self):
      return self.chain.nel == 0
    
    #__________________________________________________________________________
    def cut_MuVeto(self):
      return self.chain.nmuon == 0

    #__________________________________________________________________________
    def cut_OneOrTwoBjets(self):
        nbjets = 0
        jets = self.store['jets']
        for jet in jets:
          if jet.is_MV2c10_FixedCutBEff_77: nbjets += 1
        return nbjets in [1,2]
    
    #__________________________________________________________________________
    def cut_AtLeastOneBjet(self):
        jets = self.store['jets_tight']
        for jet in jets:
          if jet.is_MV2c10_FixedCutBEff_77: return True
        return False
    
    #__________________________________________________________________________
    def cut_BVeto(self):
        jets = self.store['jets_tight']
        for jet in jets:
          if jet.is_MV2c10_FixedCutBEff_77: return False
        return True
    
    #__________________________________________________________________________
    def cut_JetCleaning(self):
      for j in self.store['jets_tight']:
        if not j.isClean: return False
      return True
    
    #__________________________________________________________________________
    def cut_AllMuPt22(self):
      muons = self.store['muons']
      passed = True
      for m in muons:
        passed = passed and m.tlv.Pt()>=22.0*GeV
      return passed
    
    #__________________________________________________________________________
    def cut_AllMuPt25(self):
      muons = self.store['muons']
      passed = True
      for m in muons:
        passed = passed and m.tlv.Pt()>=25.0*GeV
      return passed
    
    #__________________________________________________________________________
    def cut_AllMuPt28(self):
      muons = self.store['muons']
      passed = True
      for m in muons:
        passed = passed and m.tlv.Pt()>=28.0*GeV
      return passed
    
    #__________________________________________________________________________
    def cut_AllMuPt30(self):
      muons = self.store['muons']
      passed = True
      for m in muons:
        passed = passed and m.tlv.Pt()>=30.0*GeV
      return passed
    
    #__________________________________________________________________________
    def cut_AllMuEta247(self):
      muons = self.store['muons']
      passed = True
      for m in muons:
        passed = passed and abs(m.tlv.Eta())<2.47
      return passed
    #__________________________________________________________________________
    def cut_AllMuZ0SinTheta05(self):
      muons = self.store['muons']
      passed = True
      for m in muons:
        passed = passed and abs(m.trkz0sintheta)<0.5
      return passed
    
    #__________________________________________________________________________
    def cut_DCHFilter(self):
      lep_dict = { "Mm":-13, "Mp":13, "Em":-11, "Ep":11}
      if "DCH" in self.samplename:
        
        pdgId_sampl = []
        for s in self.samplename.split("_"):
          if "HL" in s: pdgId_sampl += [lep_dict[s.replace("HL","")[-2:]],lep_dict[s.replace("HL","")[:2]]]
          if "HR" in s: pdgId_sampl += [lep_dict[s.replace("HR","")[-2:]],lep_dict[s.replace("HR","")[:2]]]
        
        pdgId_branch = []
        if "HL" in self.samplename:
          for pdgId in self.chain.HLpp_Daughters: pdgId_branch += [pdgId]
          for pdgId in self.chain.HLmm_Daughters: pdgId_branch += [pdgId]
        if "HR" in self.samplename:
          for pdgId in self.chain.HRpp_Daughters: pdgId_branch += [pdgId]
          for pdgId in self.chain.HRmm_Daughters: pdgId_branch += [pdgId]
        
        pdgId_branch = filter(lambda pdgId: pdgId != 0, pdgId_branch) 
        
        if not collections.Counter(pdgId_branch) == collections.Counter(pdgId_sampl): return False
      return True

    #__________________________________________________________________________
    def cut_MuNoFilterTT(self):
      muons = self.store['muons']
      lead_is_tight    = bool(muons[0].isIsolated_FixedCutTightTrackOnly and muons[0].trkd0sig<3.)
      sublead_is_tight = bool(muons[1].isIsolated_FixedCutTightTrackOnly and muons[1].trkd0sig<3.)
      
      return lead_is_tight and sublead_is_tight
    #__________________________________________________________________________
    def cut_MuNoFilterTL(self):
      muons = self.store['muons']
      lead_is_tight    = bool(muons[0].isIsolated_FixedCutTightTrackOnly and muons[0].trkd0sig<3.)
      sublead_is_loose = bool(not muons[1].isIsolated_FixedCutTightTrackOnly and muons[1].trkd0sig<10.)

      return lead_is_tight and sublead_is_loose 
    #__________________________________________________________________________
    def cut_MuNoFilterLT(self):
      muons = self.store['muons']
      sublead_is_tight = bool(muons[1].isIsolated_FixedCutTightTrackOnly and muons[1].trkd0sig<3.)
      lead_is_loose = bool(not muons[0].isIsolated_FixedCutTightTrackOnly and muons[0].trkd0sig<10.)

      return lead_is_loose and sublead_is_tight
    #__________________________________________________________________________
    def cut_MuNoFilterLL(self):
      muons = self.store['muons']
      lead_is_loose = bool(not muons[0].isIsolated_FixedCutTightTrackOnly and muons[0].trkd0sig<10.)
      sublead_is_loose = bool(not muons[1].isIsolated_FixedCutTightTrackOnly and muons[1].trkd0sig<10.)

      return lead_is_loose and sublead_is_loose
    
    
    #__________________________________________________________________________
    def cut_MuUniTT(self):
      muons = self.store['muons']
      lead_is_tight    = bool(muons[0].isIsolated_FixedCutTightTrackOnly and muons[0].trkd0sig<3.)
      sublead_is_tight = bool(muons[1].isIsolated_FixedCutTightTrackOnly and muons[1].trkd0sig<3.)
      pass_mc_filter   = True
      
      if self.sampletype=="mc":
        lead_is_real     = muons[0].isTrueIsoMuon()
        sublead_is_real  = muons[1].isTrueIsoMuon()
        pass_mc_filter   = lead_is_real and sublead_is_real     

      return lead_is_tight and sublead_is_tight and pass_mc_filter
    #__________________________________________________________________________
    def cut_MuUniTL(self):
      muons = self.store['muons']
      lead_is_tight    = bool(muons[0].isIsolated_FixedCutTightTrackOnly and muons[0].trkd0sig<3.)
      sublead_is_loose = bool(not muons[1].isIsolated_FixedCutTightTrackOnly and muons[1].trkd0sig<10.)
      pass_mc_filter   = True
      
      if self.sampletype=="mc":
        lead_is_real     = muons[0].isTrueIsoMuon()
        sublead_is_real  = muons[1].isTrueIsoMuon()
        pass_mc_filter   = lead_is_real and sublead_is_real     

      return lead_is_tight and sublead_is_loose and pass_mc_filter
    #__________________________________________________________________________
    def cut_MuUniLT(self):
      muons = self.store['muons']
      sublead_is_tight = bool(muons[1].isIsolated_FixedCutTightTrackOnly and muons[1].trkd0sig<3.)
      lead_is_loose = bool(not muons[0].isIsolated_FixedCutTightTrackOnly and muons[0].trkd0sig<10.)
      pass_mc_filter   = True
      
      if self.sampletype=="mc":
        lead_is_real     = muons[0].isTrueIsoMuon()
        sublead_is_real  = muons[1].isTrueIsoMuon()
        pass_mc_filter   = lead_is_real and sublead_is_real     

      return lead_is_loose and sublead_is_tight and pass_mc_filter
    #__________________________________________________________________________
    def cut_MuUniLL(self):
      muons = self.store['muons']
      lead_is_loose = bool(not muons[0].isIsolated_FixedCutTightTrackOnly and muons[0].trkd0sig<10.)
      sublead_is_loose = bool(not muons[1].isIsolated_FixedCutTightTrackOnly and muons[1].trkd0sig<10.)
      pass_mc_filter   = True

      if self.sampletype=="mc":
        lead_is_real     = muons[0].isTrueIsoMuon()
        sublead_is_real  = muons[1].isTrueIsoMuon()
        pass_mc_filter   = lead_is_real and sublead_is_real     

      return lead_is_loose and sublead_is_loose and pass_mc_filter
    
    
    
    #__________________________________________________________________________
    def cut_MuTT(self):
      muons = self.store['muons']
      lead_is_tight    = bool(muons[0].isIsolated_FixedCutTightTrackOnly and muons[0].trkd0sig<3.)
      sublead_is_tight = bool(muons[1].isIsolated_FixedCutTightTrackOnly and muons[1].trkd0sig<3.)
      pass_mc_filter   = True
      
      if self.sampletype=="mc":
        lead_is_real     = muons[0].isTrueIsoMuon()
        sublead_is_real  = muons[1].isTrueIsoMuon()
        pass_mc_filter   = lead_is_real and sublead_is_real     

      return lead_is_tight and sublead_is_tight and pass_mc_filter
    #__________________________________________________________________________
    def cut_MuTL(self):
      muons = self.store['muons']
      lead_is_tight    = bool(muons[0].isIsolated_FixedCutTightTrackOnly and muons[0].trkd0sig<3.)
      sublead_is_loose = bool(not muons[1].isIsolated_FixedCutTightTrackOnly and muons[1].trkd0sig<10.)
      pass_mc_filter   = True
      
      if self.sampletype=="mc":
        sublead_is_real  = muons[1].isTrueIsoMuon()
        pass_mc_filter   = sublead_is_real   

      return lead_is_tight and sublead_is_loose and pass_mc_filter
    #__________________________________________________________________________
    def cut_MuLT(self):
      muons = self.store['muons']
      sublead_is_tight = bool(muons[1].isIsolated_FixedCutTightTrackOnly and muons[1].trkd0sig<3.)
      lead_is_loose = bool(not muons[0].isIsolated_FixedCutTightTrackOnly and muons[0].trkd0sig<10.)
      pass_mc_filter   = True
      
      if self.sampletype=="mc":
        lead_is_real   = muons[0].isTrueIsoMuon()
        pass_mc_filter = lead_is_real   

      return lead_is_loose and sublead_is_tight and pass_mc_filter
    #__________________________________________________________________________
    def cut_MuLL(self):
      muons = self.store['muons']
      lead_is_loose = bool(not muons[0].isIsolated_FixedCutTightTrackOnly and muons[0].trkd0sig<10.)
      sublead_is_loose = bool(not muons[1].isIsolated_FixedCutTightTrackOnly and muons[1].trkd0sig<10.)
      pass_mc_filter   = True

      if self.sampletype=="mc":
        lead_is_real     = muons[0].isTrueIsoMuon()
        sublead_is_real  = muons[1].isTrueIsoMuon()
        pass_mc_filter   = lead_is_real or sublead_is_real     

      return lead_is_loose and sublead_is_loose and pass_mc_filter
    
    
    #__________________________________________________________________________
    def cut_MuTTT(self):
      muons = self.store['muons']
      if len(muons) < 3: return False
      
      mu0_is_tight     = bool(muons[0].isIsolated_FixedCutTightTrackOnly and muons[0].trkd0sig<3.)
      mu1_is_tight     = bool(muons[1].isIsolated_FixedCutTightTrackOnly and muons[1].trkd0sig<3.)
      mu2_is_tight     = bool(muons[2].isIsolated_FixedCutTightTrackOnly and muons[2].trkd0sig<3.)
      pass_mc_filter   = True
      
      if self.sampletype=="mc":
        mu0_is_real      = muons[0].isTrueIsoMuon()
        mu1_is_real      = muons[1].isTrueIsoMuon()
        mu2_is_real      = muons[2].isTrueIsoMuon()
        pass_mc_filter   = mu0_is_real and mu1_is_real and mu2_is_real   

      return mu0_is_tight and mu1_is_tight and mu2_is_tight and pass_mc_filter
    #__________________________________________________________________________
    def cut_MuTTL(self):
      muons = self.store['muons']
      if len(muons) < 3: return False
      
      mu0_is_tight     = bool(muons[0].isIsolated_FixedCutTightTrackOnly and muons[0].trkd0sig<3.)
      mu1_is_tight     = bool(muons[1].isIsolated_FixedCutTightTrackOnly and muons[1].trkd0sig<3.)
      mu2_is_loose     = bool(not muons[2].isIsolated_FixedCutTightTrackOnly and muons[2].trkd0sig<10.)
      pass_mc_filter   = True
      
      if self.sampletype=="mc":
        mu2_is_real      = muons[2].isTrueIsoMuon()
        pass_mc_filter   = mu2_is_real   

      return mu0_is_tight and mu1_is_tight and mu2_is_loose and pass_mc_filter
    #__________________________________________________________________________
    def cut_MuTLT(self):
      muons = self.store['muons']
      if len(muons) < 3: return False
      
      mu0_is_tight     = bool(muons[0].isIsolated_FixedCutTightTrackOnly and muons[0].trkd0sig<3.)
      mu1_is_loose     = bool(not muons[1].isIsolated_FixedCutTightTrackOnly and muons[1].trkd0sig<10.)
      mu2_is_tight     = bool(muons[2].isIsolated_FixedCutTightTrackOnly and muons[2].trkd0sig<3.)
      pass_mc_filter   = True
      
      if self.sampletype=="mc":
        mu1_is_real      = muons[1].isTrueIsoMuon()
        pass_mc_filter   = mu1_is_real   

      return mu0_is_tight and mu1_is_loose and mu2_is_tight and pass_mc_filter
    #__________________________________________________________________________
    def cut_MuLTT(self):
      muons = self.store['muons']
      if len(muons) < 3: return False
      
      mu0_is_loose     = bool(not muons[0].isIsolated_FixedCutTightTrackOnly and muons[0].trkd0sig<10.)
      mu1_is_tight     = bool(muons[1].isIsolated_FixedCutTightTrackOnly and muons[1].trkd0sig<3.)
      mu2_is_tight     = bool(muons[2].isIsolated_FixedCutTightTrackOnly and muons[2].trkd0sig<3.)
      pass_mc_filter   = True
      
      if self.sampletype=="mc":
        mu0_is_real      = muons[0].isTrueIsoMuon()
        pass_mc_filter   = mu0_is_real   

      return mu0_is_loose and mu1_is_tight and mu2_is_tight and pass_mc_filter
    #__________________________________________________________________________
    def cut_MuLLT(self):
      muons = self.store['muons']
      if len(muons) < 3: return False
      
      mu0_is_loose     = bool(not muons[0].isIsolated_FixedCutTightTrackOnly and muons[0].trkd0sig<10.)
      mu1_is_loose     = bool(not muons[1].isIsolated_FixedCutTightTrackOnly and muons[1].trkd0sig<10.)
      mu2_is_tight     = bool(muons[2].isIsolated_FixedCutTightTrackOnly and muons[2].trkd0sig<3.)
      pass_mc_filter   = True
      
      if self.sampletype=="mc":
        mu0_is_real      = muons[0].isTrueIsoMuon()
        mu1_is_real      = muons[1].isTrueIsoMuon()
        pass_mc_filter   = mu0_is_real or mu1_is_real

      return mu0_is_loose and mu1_is_loose and mu2_is_tight and pass_mc_filter
    #__________________________________________________________________________
    def cut_MuLTL(self):
      muons = self.store['muons']
      if len(muons) < 3: return False
      
      mu0_is_loose     = bool(not muons[0].isIsolated_FixedCutTightTrackOnly and muons[0].trkd0sig<10.)
      mu1_is_tight     = bool(muons[1].isIsolated_FixedCutTightTrackOnly and muons[1].trkd0sig<3.)
      mu2_is_loose     = bool(not muons[2].isIsolated_FixedCutTightTrackOnly and muons[2].trkd0sig<10.)
      pass_mc_filter   = True
      
      if self.sampletype=="mc":
        mu0_is_real      = muons[0].isTrueIsoMuon()
        mu2_is_real      = muons[2].isTrueIsoMuon()
        pass_mc_filter   = mu0_is_real or mu2_is_real

      return mu0_is_loose and mu1_is_tight and mu2_is_loose and pass_mc_filter
    #__________________________________________________________________________
    def cut_MuTLL(self):
      muons = self.store['muons']
      if len(muons) < 3: return False
      
      mu0_is_tight     = bool(muons[0].isIsolated_FixedCutTightTrackOnly and muons[0].trkd0sig<3.)
      mu1_is_loose     = bool(not muons[1].isIsolated_FixedCutTightTrackOnly and muons[1].trkd0sig<10.)
      mu2_is_loose     = bool(not muons[2].isIsolated_FixedCutTightTrackOnly and muons[2].trkd0sig<10.)
      pass_mc_filter   = True
      
      if self.sampletype=="mc":
        mu1_is_real      = muons[1].isTrueIsoMuon()
        mu2_is_real      = muons[2].isTrueIsoMuon()
        pass_mc_filter   = mu1_is_real or mu2_is_real

      return mu0_is_tight and mu1_is_loose and mu2_is_loose and pass_mc_filter
    #__________________________________________________________________________
    def cut_MuLLL(self):
      muons = self.store['muons']
      if len(muons) < 3: return False
      
      mu0_is_loose     = bool(not muons[0].isIsolated_FixedCutTightTrackOnly and muons[0].trkd0sig<10.)
      mu1_is_loose     = bool(not muons[1].isIsolated_FixedCutTightTrackOnly and muons[1].trkd0sig<10.)
      mu2_is_loose     = bool(not muons[2].isIsolated_FixedCutTightTrackOnly and muons[2].trkd0sig<10.)
      pass_mc_filter   = True
      
      if self.sampletype=="mc":
        mu0_is_real      = muons[0].isTrueIsoMuon()
        mu1_is_real      = muons[1].isTrueIsoMuon()
        mu2_is_real      = muons[2].isTrueIsoMuon()
        pass_mc_filter   = mu0_is_real or mu1_is_real or mu2_is_real

      return mu0_is_loose and mu1_is_loose and mu2_is_loose and pass_mc_filter
    
    
    #__________________________________________________________________________
    def cut_MuTTTT(self):
      muons = self.store['muons']
      if len(muons) < 4: return False
      
      mu0_is_tight     = bool(muons[0].isIsolated_FixedCutTightTrackOnly and muons[0].trkd0sig<3.)
      mu1_is_tight     = bool(muons[1].isIsolated_FixedCutTightTrackOnly and muons[1].trkd0sig<3.)
      mu2_is_tight     = bool(muons[2].isIsolated_FixedCutTightTrackOnly and muons[2].trkd0sig<3.)
      mu3_is_tight     = bool(muons[3].isIsolated_FixedCutTightTrackOnly and muons[3].trkd0sig<3.)
      pass_mc_filter   = True
      
      if self.sampletype=="mc":
        mu0_is_real      = muons[0].isTrueIsoMuon()
        mu1_is_real      = muons[1].isTrueIsoMuon()
        mu2_is_real      = muons[2].isTrueIsoMuon()
        mu3_is_real      = muons[3].isTrueIsoMuon()
        pass_mc_filter   = mu0_is_real and mu1_is_real and mu2_is_real and mu3_is_real

      return mu0_is_tight and mu1_is_tight and mu2_is_tight and mu3_is_tight and pass_mc_filter
    
    #__________________________________________________________________________
    def cut_MuTTTL(self):
      muons = self.store['muons']
      if len(muons) < 4: return False
      
      mu0_is_tight     = bool(muons[0].isIsolated_FixedCutTightTrackOnly and muons[0].trkd0sig<3.)
      mu1_is_tight     = bool(muons[1].isIsolated_FixedCutTightTrackOnly and muons[1].trkd0sig<3.)
      mu2_is_tight     = bool(muons[2].isIsolated_FixedCutTightTrackOnly and muons[2].trkd0sig<3.)
      mu3_is_loose     = bool(not muons[3].isIsolated_FixedCutTightTrackOnly and muons[3].trkd0sig<10.)
      pass_mc_filter   = True
      
      if self.sampletype=="mc":
        mu3_is_real      = muons[3].isTrueIsoMuon()
        pass_mc_filter   = mu3_is_real

      return mu0_is_tight and mu1_is_tight and mu2_is_tight and mu3_is_loose and pass_mc_filter
    
    #__________________________________________________________________________
    def cut_MuTTLT(self):
      muons = self.store['muons']
      if len(muons) < 4: return False
      
      mu0_is_tight     = bool(muons[0].isIsolated_FixedCutTightTrackOnly and muons[0].trkd0sig<3.)
      mu1_is_tight     = bool(muons[1].isIsolated_FixedCutTightTrackOnly and muons[1].trkd0sig<3.)
      mu2_is_loose     = bool(not muons[2].isIsolated_FixedCutTightTrackOnly and muons[2].trkd0sig<10.)
      mu3_is_tight     = bool(muons[3].isIsolated_FixedCutTightTrackOnly and muons[3].trkd0sig<3.)
      pass_mc_filter   = True
      
      if self.sampletype=="mc":
        mu2_is_real      = muons[2].isTrueIsoMuon()
        pass_mc_filter   = mu2_is_real

      return mu0_is_tight and mu1_is_tight and mu2_is_loose and mu3_is_tight and pass_mc_filter
    
    #__________________________________________________________________________
    def cut_MuTLTT(self):
      muons = self.store['muons']
      if len(muons) < 4: return False
      
      mu0_is_tight     = bool(muons[0].isIsolated_FixedCutTightTrackOnly and muons[0].trkd0sig<3.)
      mu1_is_loose     = bool(not muons[1].isIsolated_FixedCutTightTrackOnly and muons[1].trkd0sig<10.)
      mu2_is_tight     = bool(muons[2].isIsolated_FixedCutTightTrackOnly and muons[2].trkd0sig<3.)
      mu3_is_tight     = bool(muons[3].isIsolated_FixedCutTightTrackOnly and muons[3].trkd0sig<3.)
      pass_mc_filter   = True
      
      if self.sampletype=="mc":
        mu1_is_real      = muons[1].isTrueIsoMuon()
        pass_mc_filter   = mu1_is_real

      return mu0_is_tight and mu1_is_loose and mu2_is_tight and mu3_is_tight and pass_mc_filter
    
    #__________________________________________________________________________
    def cut_MuLTTT(self):
      muons = self.store['muons']
      if len(muons) < 4: return False
      
      mu0_is_loose     = bool(not muons[0].isIsolated_FixedCutTightTrackOnly and muons[0].trkd0sig<10.)
      mu1_is_tight     = bool(muons[1].isIsolated_FixedCutTightTrackOnly and muons[1].trkd0sig<3.)
      mu2_is_tight     = bool(muons[2].isIsolated_FixedCutTightTrackOnly and muons[2].trkd0sig<3.)
      mu3_is_tight     = bool(muons[3].isIsolated_FixedCutTightTrackOnly and muons[3].trkd0sig<3.)
      pass_mc_filter   = True
      
      if self.sampletype=="mc":
        mu0_is_real      = muons[0].isTrueIsoMuon()
        pass_mc_filter   = mu0_is_real

      return mu0_is_loose and mu1_is_tight and mu2_is_tight and mu3_is_tight and pass_mc_filter
    
    
    #__________________________________________________________________________
    def cut_AllMuMedium(self):
      muons = self.store['muons']
      for m in muons:
        is_medium = bool(m.isMedium) or bool(m.isTight)
        if not is_medium: return False
      return True
    #__________________________________________________________________________
    def cut_AllMuLoose(self):
      muons = self.store['muons']
      for m in muons:
        is_loose = bool(m.isLoose) or bool(m.isMedium) or bool(m.isTight)
        if not is_loose: return False
      return True
    
    #__________________________________________________________________________
    def cut_LeadTauIsTight(self):
      return self.store['taus'][0].isJetBDTSigTight
    #__________________________________________________________________________
    def cut_LeadTauNotTight(self):
      return not self.store['taus'][0].isJetBDTSigTight

    #__________________________________________________________________________
    def cut_LeadTauNotTightAtLeastLoose(self):
        leadtau = self.store['taus'][0]
        if not leadtau.isJetBDTSigTight:
                if leadtau.isJetBDTSigLoose: return True
        return False

    #__________________________________________________________________________
    def cut_LeadTauNotMediumAtLeastLoose(self):
	leadtau = self.store['taus'][0]
	if not leadtau.isJetBDTSigMedium:
		if leadtau.isJetBDTSigLoose: return True
	return False


    #__________________________________________________________________________
    def cut_LeadTauIsMedium(self):
      return self.store['taus'][0].isJetBDTSigMedium
    #__________________________________________________________________________
    def cut_LeadTauNotMedium(self):
      return not self.store['taus'][0].isJetBDTSigMedium 
    
    #__________________________________________________________________________
    def cut_LeadTauIsLoose(self):
      return self.store['taus'][0].isJetBDTSigLoose
    #__________________________________________________________________________
    def cut_LeadTauNotLoose(self):
      return not self.store['taus'][0].isJetBDTSigLoose

    #__________________________________________________________________________
    def cut_SubleadTauIsLoose(self):
      return self.store['taus'][1].isJetBDTSigLoose
    #__________________________________________________________________________
    def cut_SubleadTauNotLoose(self):
      return not self.store['taus'][1].isJetBDTSigLoose

    #__________________________________________________________________________
    def cut_SubleadTauIsMedium(self):
      return self.store['taus'][1].isJetBDTSigMedium
    #__________________________________________________________________________
    def cut_SubleadTauNotMedium(self):
      return not self.store['taus'][1].isJetBDTSigMedium


    #__________________________________________________________________________
    def cut_LeadMuIsLoose(self):
      muons = self.store['muons']
      lead_mu = muons[0]
      is_loose = bool(lead_mu.isLoose) or bool(lead_mu.isMedium) or bool(lead_mu.isTight)
      return is_loose
    #__________________________________________________________________________
    def cut_LeadMuIsMedium(self):
      muons = self.store['muons']
      lead_mu = muons[0]
      is_medium = bool(lead_mu.isMedium) or bool(lead_mu.isTight)
      return is_medium
    #__________________________________________________________________________
    def cut_LeadMuIsTight(self):
      muons = self.store['muons']
      lead_mu = muons[0]
      is_tight = bool(lead_mu.isTight)
      return is_tight
    
    #__________________________________________________________________________
    def cut_LeadMuIsoFixedCutTightTrackOnly(self):
      muons = self.store['muons']
      lead_mu = muons[0]
      return lead_mu.isIsolated_FixedCutTightTrackOnly
    #__________________________________________________________________________
    def cut_LeadMuIsoNotFixedCutTightTrackOnly(self):
      muons = self.store['muons']
      lead_mu = muons[0]
      return not lead_mu.isIsolated_FixedCutTightTrackOnly
    
    #__________________________________________________________________________
    def cut_LeadMuIsoGradient(self):
      muons = self.store['muons']
      lead_mu = muons[0]
      return lead_mu.isIsolated_Gradient
    #__________________________________________________________________________
    def cut_LeadMuIsoNotGradient(self):
      muons = self.store['muons']
      lead_mu = muons[0]
      return not lead_mu.isIsolated_Gradient 
    
    
    #__________________________________________________________________________
    def cut_AllMuIsoBound08(self):
      muons = self.store['muons']
      for m in muons:
        if m.ptvarcone30 / m.tlv.Pt() > 0.8: return False
      return True
    #__________________________________________________________________________
    def cut_AllMuIsoBound15(self):
      muons = self.store['muons']
      for m in muons:
        if m.ptvarcone30 / m.tlv.Pt() > 1.5: return False
      return True
    
    
    #__________________________________________________________________________
    def cut_MZwindow(self):
      mZ = 91.1876*GeV
      muons = self.store['muons']
      mu_lead = muons[0] 
      mu_sublead = muons[1] 
      m_vis = (mu_lead.tlv + mu_sublead.tlv).M()

      return abs(m_vis - mZ) < 10*GeV
    
    #__________________________________________________________________________
    def cut_VetoMZwindow(self):
      mZ = 91.1876*GeV
      muons = self.store['muons']
      mu_lead = muons[0] 
      mu_sublead = muons[1] 
      m_vis = (mu_lead.tlv + mu_sublead.tlv).M()

      return abs(m_vis - mZ) > 20 * GeV
    
    #__________________________________________________________________________
    def cut_AllPairsM20(self):
      muons = self.store['muons']
      if self.chain.nmuon >= 2:
        for p in combinations(muons,2):
          if (p[0].tlv + p[1].tlv).M()<20*GeV: return False
      return True
    
    
    #__________________________________________________________________________
    def cut_M15(self):
      muons = self.store['muons']
      mu_lead = muons[0] 
      mu_sublead = muons[1] 
      m_vis = (mu_lead.tlv + mu_sublead.tlv).M()

      return abs(m_vis)>15*GeV
    
    #__________________________________________________________________________
    def cut_dRhigh35(self):
      return self.store['muons_dR'] > 3.5
    
    #__________________________________________________________________________
    def cut_pTHlow80(self):
      return self.store['muons_pTH'] < 80*GeV
    
    #__________________________________________________________________________
    def cut_Mlow200(self):
      muons = [self.store['muon1'],self.store['muon2']]
      mu_lead = muons[0] 
      mu_sublead = muons[1] 
      m_vis = (mu_lead.tlv + mu_sublead.tlv).M()

      return abs(m_vis)<200*GeV
    
    #__________________________________________________________________________
    def cut_PassAndMatch(self):
      required_triggers = self.store["reqTrig"]
      passed_triggers   = self.store["passTrig"].keys()
   
      for t in required_triggers:
        if t in passed_triggers: return True

      '''
      muons = self.store['muons']
      for m in muons:
        for trig in required_triggers:
          if trig in self.store["singleMuTrigList"].keys():
            muon_is_matched    = bool( m.isTrigMatchedToChain.at(self.store["singleMuTrigList"][trig]) )
            event_is_triggered = bool( trig in passed_triggers )
            if muon_is_matched and event_is_triggered: 
              return True
      '''

      return False
  

    #__________________________________________________________________________
    def cut_SingleJetTrigger(self):
      required_triggers = self.store["reqTrig"]
      passed_triggers   = self.store["passTrig"].keys()
   
      lead_jet = self.store['jets'][0]

      for t in required_triggers:
        if t in passed_triggers: 
          if lead_jet.tlv.Pt() >= self.store["passTrig"][t]["pt_slice"][0] and lead_jet.tlv.Pt() < self.store["passTrig"][t]["pt_slice"][1]:
        	return True
      return False
    
    #__________________________________________________________________________
    def cut_SingleMuTrigger(self):
      required_triggers = self.store["reqTrig"]
      passed_triggers   = self.store["passTrig"].keys()
   
      lead_mu = self.store['muons'][0]

      for t in required_triggers:
        if t in passed_triggers: 
          if lead_mu.tlv.Pt() >= self.store["passTrig"][t]["pt_slice"][0] and lead_mu.tlv.Pt() < self.store["passTrig"][t]["pt_slice"][1]:
            return True
      return False


    #__________________________________________________________________________
    def cut_TagIsMatched(self):
      required_triggers = self.store["reqTrig"]
      passed_triggers   = self.store["passTrig"].keys()
      
      tag = self.store['tag'] 
      for trig in required_triggers:
        if trig in self.store["singleMuTrigList"].keys():
          tag_is_matched     = bool( tag.isTrigMatchedToChain.at(self.store["singleMuTrigList"][trig]) )
          event_is_triggered = bool( trig in passed_triggers )
          if tag_is_matched and event_is_triggered: 
            return True
      return False
    #__________________________________________________________________________
    def cut_LeadIsMatched(self):
      required_triggers = self.store["reqTrig"]
      passed_triggers   = self.store["passTrig"].keys()
      
      lead_mu = self.store['muons'][0]
      for trig in required_triggers:
        if trig in self.store["singleMuTrigList"].keys():
          lead_mu_is_matched = bool( lead_mu.isTrigMatchedToChain.at(self.store["singleMuTrigList"][trig]) )
          event_is_triggered = bool( trig in passed_triggers )
          if lead_mu_is_matched and event_is_triggered: 
            return True
      return False
    #__________________________________________________________________________
    def cut_SubLeadIsMatched(self):
      required_triggers = self.store["reqTrig"]
      passed_triggers   = self.store["passTrig"].keys()
      
      sublead_mu = self.store['muons'][1]
      for trig in required_triggers:
        if trig in self.store["singleMuTrigList"].keys():
          sublead_mu_is_matched = bool( sublead_mu.isTrigMatchedToChain.at(self.store["singleMuTrigList"][trig]) )
          event_is_triggered = bool( trig in passed_triggers )
          if sublead_mu_is_matched and event_is_triggered: 
            return True
      return False


    #__________________________________________________________________________
    def cut_PassAndMatchPresc(self):
      required_triggers = self.store["reqTrig"]
      passed_triggers   = self.store["passTrig"].keys()
 
      muons = self.store['muons']
      
      for m in muons:
        for trig in required_triggers:
          if trig in self.store["singleMuTrigList"].keys():
            muon_is_matched    = bool( m.isTrigMatchedToChain.at(self.store["singleMuTrigList"][trig]) )
            event_is_triggered = bool( trig in passed_triggers )
            if muon_is_matched and event_is_triggered:
              
              if m.tlv.Pt()>=self.store["singleMuTrigSlice"][trig][0] and m.tlv.Pt()<self.store["singleMuTrigSlice"][trig][1]:
                if m.isIsolated_FixedCutTightTrackOnly and m.trkd0sig<3.: # require a tight muon for trigger matching
                  return True
      
      for m in muons:
        for trig in required_triggers:
          if trig in self.store["singleMuTrigList"].keys():
            muon_is_matched    = bool( m.isTrigMatchedToChain.at(self.store["singleMuTrigList"][trig]) )
            event_is_triggered = bool( trig in passed_triggers )
            if muon_is_matched and event_is_triggered:
              
              if m.tlv.Pt()>=self.store["singleMuTrigSlice"][trig][0] and m.tlv.Pt()<self.store["singleMuTrigSlice"][trig][1]:
                  if not m.isIsolated_FixedCutTightTrackOnly and m.trkd0sig<10.: # if no tight is found loop over loose
                    return True

      return False
    
    """ 
    #__________________________________________________________________________
    def cut_LeadIsMatchedPresc(self):
      required_triggers = self.store["reqTrig"]
      passed_triggers   = self.store["passTrig"].keys()
      
      lead_mu = self.store['muons'][0]
      for trig in required_triggers:
        if trig in self.store["singleMuTrigList"].keys():
          lead_mu_is_matched = bool( lead_mu.isTrigMatchedToChain.at(self.store["singleMuTrigList"][trig]) )
          event_is_triggered = bool( trig in passed_triggers )
          if lead_mu_is_matched and event_is_triggered: 
            if lead_mu.tlv.Pt()>=self.store["singleMuTrigSlice"][trig][0] and lead_mu.tlv.Pt()<self.store["singleMuTrigSlice"][trig][1]:
              return True
      return False
    #__________________________________________________________________________
    def cut_SubLeadIsMatchedPresc(self):
      required_triggers = self.store["reqTrig"]
      passed_triggers   = self.store["passTrig"].keys()
      
      sublead_mu = self.store['muons'][1]
      for trig in required_triggers:
        if trig in self.store["singleMuTrigList"].keys():
          sublead_mu_is_matched = bool( sublead_mu.isTrigMatchedToChain.at(self.store["singleMuTrigList"][trig]) )
          event_is_triggered = bool( trig in passed_triggers )
          if sublead_mu_is_matched and event_is_triggered: 
            if sublead_mu.tlv.Pt()>=self.store["singleMuTrigSlice"][trig][0] and sublead_mu.tlv.Pt()<self.store["singleMuTrigSlice"][trig][1]:
              return True
      return False
    
    #__________________________________________________________________________
    def cut_ThirdLeadIsMatchedPresc(self):
      required_triggers = self.store["reqTrig"]
      passed_triggers   = self.store["passTrig"].keys()
      
      thirdlead_mu = self.store['muons'][2]
      for trig in required_triggers:
        if trig in self.store["singleMuTrigList"].keys():
          thirdlead_mu_is_matched = bool( thirdlead_mu.isTrigMatchedToChain.at(self.store["singleMuTrigList"][trig]) )
          event_is_triggered = bool( trig in passed_triggers )
          if thirdlead_mu_is_matched and event_is_triggered: 
            if thirdlead_mu.tlv.Pt()>=self.store["singleMuTrigSlice"][trig][0] and thirdlead_mu.tlv.Pt()<self.store["singleMuTrigSlice"][trig][1]:
              return True
      return False
    """ 
    
    #__________________________________________________________________________
    def cut_LeadMuTruthFilter(self):
      muons = self.store['muons'] 
      if self.sampletype == "mc":
        return muons[0].isTrueIsoMuon()
      return True
    #__________________________________________________________________________
    def cut_LeadMuFakeFilter(self):
      muons = self.store['muons'] 
      if self.sampletype == "mc":
        return muons[0].isTrueNonIsoMuon()
      return True
    
    
    #__________________________________________________________________________
    def cut_ProbeTruthFilter(self):
      if self.sampletype == "mc":
        return self.store['probe'].isTrueIsoMuon()
      return True
    #__________________________________________________________________________
    def cut_ProbeMuFakeFilter(self):
      if self.sampletype == "mc":
        return self.store['probe'].isTrueNonIsoMuon()
      return True
    #__________________________________________________________________________
    def cut_ProbeMuFailTruthFilter(self):
      if self.sampletype == "mc":
        return not self.store['probe'].isTrueIsoMuon()
      return True
   

    #__________________________________________________________________________
    def cut_TagAndProbeExist(self):
      if "tag" in self.store.keys() and "probe" in self.store.keys():
        return True
      return False
    #__________________________________________________________________________
    def cut_TagisTight(self):
      return self.store['tag'].isIsolated_FixedCutTightTrackOnly and self.store['tag'].trkd0sig<3.
    #__________________________________________________________________________
    def cut_TagisLoose(self):
      return not self.store['tag'].isIsolated_FixedCutTightTrackOnly and self.store['tag'].trkd0sig<10.
    #__________________________________________________________________________
    def cut_ProbeisTight(self):
      return self.store['probe'].isIsolated_FixedCutTightTrackOnly and self.store['probe'].trkd0sig<3.
    #__________________________________________________________________________
    def cut_ProbeisLoose(self):
      return not self.store['probe'].isIsolated_FixedCutTightTrackOnly and self.store['probe'].trkd0sig<10.
   
    
    #__________________________________________________________________________
    def cut_LeadMuD0Sig2(self):
      muons = self.store['muons']
      return muons[0].trkd0sig<2. 
    #__________________________________________________________________________
    def cut_LeadMuD0Sig3(self):
      muons = self.store['muons']
      return muons[0].trkd0sig<3. 
    #__________________________________________________________________________
    def cut_LeadMuD0Sig4(self):
      muons = self.store['muons']
      return muons[0].trkd0sig<4. 
    #__________________________________________________________________________
    def cut_LeadMuD0Sig10(self):
      muons = self.store['muons']
      return muons[0].trkd0sig<10. 
    
    #__________________________________________________________________________
    def cut_LeadMuZ0SinTheta05(self):
      muons = self.store['muons']
      return abs(muons[0].trkz0sintheta)<0.5
    
    #__________________________________________________________________________
    def cut_METlow40(self):
      met = self.store["met_trk"]
      return met.tlv.Pt() < 40 * GeV
    #__________________________________________________________________________
    def cut_METlow50(self):
      met = self.store["met_trk"]
      return met.tlv.Pt() < 50 * GeV
    #__________________________________________________________________________
    def cut_METlow30(self):
      met = self.store["met_trk"]
      return met.tlv.Pt() < 30 * GeV
    #__________________________________________________________________________
    def cut_METhigh30(self):
      met = self.store["met_trk"]
      return met.tlv.Pt() > 30 * GeV
    
    #__________________________________________________________________________
    def cut_TauJetDphi282(self):
      lead_tau = self.store["taus"][0]
      lead_jet = self.store["jets"][0]
      if abs(lead_tau.tlv.DeltaPhi(lead_jet.tlv)) > 2.82: return True
      return False
    #__________________________________________________________________________
    def cut_TauJetDphi290(self):
      lead_tau = self.store["taus"][0]
      lead_jet = self.store["jets"][0]
      if abs(lead_tau.tlv.DeltaPhi(lead_jet.tlv)) > 2.90: return True
      return False   
    #__________________________________________________________________________
    def cut_TauJetDphi250(self):
      lead_tau = self.store["taus"][0]
      lead_jet = self.store["jets"][0]
      if abs(lead_tau.tlv.DeltaPhi(lead_jet.tlv)) > 2.50: return True
      return False 

    #__________________________________________________________________________
    def cut_MuJetDphi27(self):
      lead_mu = self.store["muons"][0]
      if self.store["jets_tight"]:
        for j in self.store["jets_tight"]:
          if abs(lead_mu.tlv.DeltaPhi(j.tlv)) > 2.7: return True
      return False
    #__________________________________________________________________________
    def cut_MuJetDphi28(self):
      lead_mu = self.store["muons"][0]
      if self.store["jets_tight"]:
        for j in self.store["jets_tight"]:
          if abs(lead_mu.tlv.DeltaPhi(j.tlv)) > 2.8: return True
      return False
    #__________________________________________________________________________
    def cut_MuJetDphi26(self):
      lead_mu = self.store["muons"][0]
      if self.store["jets_tight"]:
        for j in self.store["jets_tight"]:
          if abs(lead_mu.tlv.DeltaPhi(j.tlv)) > 2.6: return True
      return False

    #__________________________________________________________________________
    def cut_TightJetPt25(self):
      if self.store["jets_tight"]:
        jets = self.store["jets_tight"]
        for j in jets:
          if j.tlv.Pt() > 25 * GeV: return True
      return False
    #__________________________________________________________________________
    def cut_TightJetPt35(self):
      if self.store["jets_tight"]:
        jets = self.store["jets_tight"]
        for j in jets:
          if j.tlv.Pt() > 35 * GeV: return True
      return False
    #__________________________________________________________________________
    def cut_TightJetPt40(self):
      if self.store["jets_tight"]:
        jets = self.store["jets_tight"]
        for j in jets:
          if j.tlv.Pt() > 40 * GeV: return True
      return False
    #__________________________________________________________________________
    def cut_TightJetPt45(self):
      if self.store["jets_tight"]:
        jets = self.store["jets_tight"]
        for j in jets:
          if j.tlv.Pt() > 45 * GeV: return True
      return False
    #___________________________________________________________________________ 
    def cut_TauJetPtRatio(self):
	if 0.95 < self.store["taujet_ptratio"] < 1.05:
		return True
	return False
    #___________________________________________________________________________ 
    def cut_TauLeadTauSubleadDphi270(self):
      lead_tau = self.store["taus"][0]
      sublead_tau = self.store["taus"][1]
      if abs(lead_tau.tlv.DeltaPhi(sublead_tau.tlv)) > 2.70: return True
      return False
    #__________________________________________________________________________
    def cut_LeadTauOneTrack(self):
	ntrk = self.store["taus"][0].ntrk
	return ntrk == 1
    #_________________________________________________________________________
    def cut_LeadTauThreeTrack(self):
        ntrk = self.store["taus"][0].ntrk
        return ntrk == 3

#------------------------------------------------------------------------------
class PlotAlg(pyframe.algs.CutFlowAlg,CutAlg):
  
    #__________________________________________________________________________
    def __init__(self,
                 name          = 'PlotAlg',
                 region        = '',
                 hist_list     = [], # list of histograms to be filled
                 cut_flow      = None,
                 plot_all      = True,
                 do_var_check  = False,
                 ):
        pyframe.algs.CutFlowAlg.__init__(self,key=region)
        CutAlg.__init__(self,name,isfilter=False)
        self.cut_flow     = cut_flow
        self.region       = region
        self.plot_all     = plot_all
        self.hist_list    = hist_list
        self.do_var_check = do_var_check
    
    #_________________________________________________________________________
    def initialize(self):
        
        # remove eventual repetitions from list of histograms
        h_dict = {}
        for h in self.hist_list: h_dict[h.hname] = h
        self.hist_list = h_dict.values()

        pyframe.algs.CutFlowAlg.initialize(self)
    #_________________________________________________________________________
    def execute(self, weight):
   
        # next line fills in the cutflow hists
        # the first bin of the cutflow does not
        # take into account object weights
        pyframe.algs.CutFlowAlg.execute(self, weight)

        list_cuts = []
        for cut, list_weights in self.cut_flow:
            ## apply weights for this cut
            if list_weights:
              for w in list_weights: weight *= self.store[w]

            list_cuts.append(cut)
            passed = self.check_region(list_cuts)
            self.hists[self.region].count_if(passed, cut, weight)

            ## if plot_all is True, plot after each cut, 
            ## else only plot after full selection
            
            if (self.plot_all or len(list_cuts)==len(self.cut_flow)):
               region_name = os.path.join(self.region,'_'.join(list_cuts))
               region_name = region_name.replace('!', 'N')
               region = os.path.join('/regions/', region_name)
               
               self.plot(region, passed, list_cuts, cut, weight=weight)

        return True

    #__________________________________________________________________________
    def finalize(self):
        pyframe.algs.CutFlowAlg.finalize(self)

    #__________________________________________________________________________
    def plot(self, region, passed, list_cuts, cut, list_weights=None, weight=1.0):

        # -----------------
        # Create histograms
        # -----------------
        for h in self.hist_list:
            if h.get_name() == "Hist1D":
              h.instance = self.hist(h.hname, "ROOT.TH1F('$', ';%s;%s', %d, %lf, %lf)" % (h.xtitle,h.ytitle,h.nbins,h.xmin,h.xmax), dir=os.path.join(region, '%s'%h.dir))
            elif h.get_name() == "Hist2D": 
              h.instance = self.hist(h.hname, "ROOT.TH2F('$', ';%s;%s', %d, %lf, %lf, %d, %lf, %lf)" % (h.hname,h.hname,h.nbinsx,h.xmin,h.xmax,h.nbinsy,h.ymin,h.ymax), dir=os.path.join(region, '%s'%h.dir))
              h.set_axis_titles()

         
        # ---------------
        # Fill histograms
        # ---------------
        if passed:
          for h in self.hist_list:
            if self.do_var_check:
              exec ( "present = %s"%h.varcheck() )
              if not present: 
                sys.exit( "ERROR: variable %s  not found for hist %s"%(h.vexpr,h.hname) )
            
            if h.get_name() == "Hist1D":
              var = -999.
              
              # this all part gives me the shivers. But is just temporary. Don't panic
              if hasattr(self.chain,"njets") and "njets" in h.vexpr: exec( "var = self.chain.njets" ) 
              elif hasattr(self.chain,"njet") and "njet" in h.vexpr: exec( "var = self.chain.njet" ) 
              else: exec( "var = %s" % h.vexpr ) # so dirty !!!
              
              if h.instance and var!=-999.: h.fill(var, weight)
            
            elif h.get_name() == "Hist2D":
              varx = -999.
              vary = -999.
              exec( "varx,vary = %s" % h.vexpr ) # so dirty !!!
              if h.instance and varx!=-999. and vary!=-999.: h.fill(varx,vary, weight)


    #__________________________________________________________________________
    def check_region(self,cutnames):
        cut_passed = True
        for cn in cutnames:
            if cn == 'ALL': continue

            if cn.startswith('!'):
                cut_passed = not self.apply_cut(cn[1:])
            else:
                cut_passed = self.apply_cut(cn) and cut_passed
        return cut_passed
    
    
#__________________________________________________________________________
def log_bins(nbins,xmin,xmax):
    xmin_log = math.log(xmin)
    xmax_log = math.log(xmax)
    log_bins = [ float(i)/float(nbins)*(xmax_log-xmin_log) + xmin_log for i in xrange(nbins+1)]
    bins = [ math.exp(x) for x in log_bins ]
    return bins

#__________________________________________________________________________
def log_bins_str(nbins,xmin,xmax):
    bins = log_bins(nbins,xmin,xmax)
    bins_str = "%d, array.array('f',%s)" % (len(bins)-1, str(bins))
    return bins_str 


#EOF
