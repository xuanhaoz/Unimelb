# encoding: utf-8
'''
histmgr.py

description:

'''

## modules
import os 
import random
import ROOT
import copy
import math
from pyplot import histutils, fileio

from array import array

import logging
log = logging.getLogger(__name__)

# - - - - - - - - - - - class defs  - - - - - - - - - - - - #
#------------------------------------------------------------
class HistMgr():
    '''
    description of HistMgr 
    '''
    #____________________________________________________________
    def __init__(self,
            basedir = None,
            target_lumi = None,
            cutflow_histname = 'MetaData_EventCount', ### IMPORTANT: verify origin of the cutflow hist!!!
            ):
        self.basedir = basedir
        self.target_lumi = target_lumi
        self.cutflow_histname = cutflow_histname

    #____________________________________________________________
    def get_files_paths(self,samplename=None,sys=None,mode=None,get_slices=True,get_first_item=False):
        '''
        construct path to file for sample+systematic
        '''
        ## get systematics path
        syspath = 'nominal'
        if sys and not sys.flat_err:
            if mode == 'up': syspath = sys.var_up
            else:            syspath = sys.var_dn

        ## get file path
        paths_to_files = []
        common_file_path = os.path.join(self.basedir,syspath)
        
        for infile in os.listdir(common_file_path):
          if get_slices:
            if os.path.isfile(os.path.join(common_file_path,infile)) and samplename+"_slice" in infile:
              paths_to_files.append(os.path.join(common_file_path,infile))
          else: 
            if os.path.isfile(os.path.join(common_file_path,infile)) and samplename+"." in infile:
              paths_to_files.append(os.path.join(common_file_path,infile))
        
        if get_first_item:
          return paths_to_files[0]
        else:
          return paths_to_files

    #____________________________________________________________
    def hist(self, # retrieve folder with longer name
            histname   = None,
            samplename = None,
            region     = None,
            icut       = None, 
            sys        = None,
            mode       = None,
            ):

        assert histname,  'must define histname'
        assert samplename,    'must define samplename'
        if sys: 
            assert mode in ['up','dn'], "mode must be either 'up' or 'dn'"

        paths_to_files = self.get_files_paths(samplename,sys,mode,get_slices=True)

        ####

        h_list = []
        f_list = []

        for path in paths_to_files:
           #print "This is the path ", path
           f = ROOT.TFile.Open(path)
           #print "new appending %s to list of slices"%path
           f_list.append(f)
           assert f, 'Failed to open input file!'
           
           ## get hist path
           path_to_hist = ''
           
           if region != None:
              #print "looking for region %s"%region
              path_to_hist = os.path.join('regions',region)

              ## check region exists
              if not f.Get(path_to_hist):
                  f.Close()
                  return None
              cutflow = get_icut_path(path, path_to_hist, icut)
              
              if icut == 0: pass #cutflow = "ALL"
              if not cutflow: 
                  log.debug( '%s no cut: %s'% (samplename,icut) )
                  f.Close()
                  return None
              path_to_hist = os.path.join(path_to_hist,cutflow)
             
           path_to_hist = os.path.join(path_to_hist,histname)
           #print "found path to hist %s"%path_to_hist

           h = f.Get(path_to_hist)
           #print "got histogram %s"%h.GetName()
           
           if not h:
               f.Close()
               #print 'failed retrieveing hist: %s:%s'%(path_to_file,path_to_hist)
               return None
           
           h = h.Clone()
           #h.SetDirectory(0)
           #print "This is the histogram"
           #print h
           h_list.append(h)
           #print "This is the list inside"
           #print h_list
        
        #print "This is the list outside"
        #print h_list        
        h_sum = h_list[0]
        for h in h_list[1:]: h_sum.Add(h)

        #for f in f_list: f.Close()
        
        ## apply flat sys (if specified)
        if sys and sys.flat_err:
            if mode == 'up': h_sum.Scale(1.+sys.flat_err)
            else:            h_sum.Scale(1.-sys.flat_err)

        return h_sum
          
    #____________________________________________________________
    def get_nevents(self,samplename,sys=None,mode=None):
        '''
        retrieves cutflow hist for given sample 
        and given systematic (which contains the 
        total events before skim)
        '''
        assert samplename, 'must provide samplename'
    
        nevents = None 
        path_to_file = self.get_files_paths(samplename,sys,mode,get_slices=True,get_first_item=True)
        f = ROOT.TFile.Open(path_to_file)
        if f:
            h = f.Get(self.cutflow_histname)
            if h: nevents = h.GetBinContent(3)
            f.Close()
        
        return nevents


#------------------------------------------------------------
class BaseEstimator(object):
    '''
    TODO: put description of estimatior functionality here
    '''
    #____________________________________________________________
    def __init__(self,hm=None,sample=None):
        self.hm = hm
        self.sample = sample
        
        ## allowed systematics 
        self.allowed_systematics = []
        self.hist_store = {}

        assert self.sample, 'must provide sample to BaseEstimator'
    
    #____________________________________________________________
    def get_hist_tag(self,histname=None,region=None,icut=None,sys=None,mode=None):
      if isinstance(region,list): region = "_".join(region)
      htag = "_".join([str(s) for s in [histname,region,icut,sys,mode]])
      return htag
        
    #____________________________________________________________
    def hist(self,histname=None,region=None,icut=None,sys=None,mode=None):
        """
        Supports list of regions to be added
        """
        if not self.is_affected_by_systematic(sys): sys=mode=None
        htag = self.get_hist_tag(histname,region,icut,sys,mode)
        if not isinstance(region,list): region = [region]
        if not self.hist_store.has_key(htag):
          h_dict = {}
          for r in region:
             h_dict[r] = self.__hist__(
                     histname=histname,
                     region=r,
                     icut=icut,
                     sys=sys,
                     mode=mode,
                     )

          h = None
          if not all(v is None for v in h_dict.values()):
            h = histutils.add_hists(h_dict.values())
          if h: 
            self.sample.plotopts.configure(h)
            log.debug('%s: %s'%(self.sample.name,h.Integral()))
          
          self.hist_store[htag] = h
        return self.hist_store[htag]
    
    #__________________________________________________________________________
    def add_systematics(self, sys):
        if not isinstance(sys,list): sys = [sys]
        self.allowed_systematics += sys
    
    #__________________________________________________________________________
    def is_affected_by_systematic(self, sys):
        return sys in self.allowed_systematics

    #__________________________________________________________________________
    def flush_hists(self):
        for h in self.hist_store.values():
            if h: h.Delete()
        self.hist_store = {}


#------------------------------------------------------------
class Estimator(BaseEstimator):
    '''
    Standard Estimator class (for MC and data) 
    '''
    #____________________________________________________________
    def __init__(self,**kw):
        BaseEstimator.__init__(self,**kw)

        ## xsec / Ntotal, seperately for each systematic
        ## (set on first call to hist)
        self.mc_lumi_frac = {}
   

    #____________________________________________________________
    def __hist__(self,histname=None,region=None,icut=None,sys=None,mode=None):
        """
        implemenation of nominal hist getter
        """
        h = self.hm.hist(histname=histname,
                         samplename=self.sample.name,
                         region=region,
                         icut=icut,
                         sys=sys,
                         mode=mode,
                         )
        if h and self.sample.type == 'mc': 
            lumi_frac = self.get_mc_lumi_frac(sys,mode)
            h.Scale(self.hm.target_lumi * lumi_frac)

        return h    
    #____________________________________________________________
    def get_mc_lumi_frac(self,sys,mode):
        '''
        Gets the effective luminosity fraction of the mc sample. 
        This is done seperately for each sys, since the total 
        number of events can potentially be different for different 
        sys samples. Once retrieved, the value is stored for 
        further access. 
        '''
        if sys: 
            assert mode in ['up','dn'], "mode must be either 'up' or 'dn'"
        
        sysname = 'nominal'
        if sys:
            if mode == 'up': sysname = '%s_up'%(sys.name)
            else:            sysname = '%s_dn'%(sys.name)

        if not self.mc_lumi_frac.has_key(sysname): 
            xsec    = self.sample.xsec 
            feff    = self.sample.feff
            kfactor = self.sample.kfactor
            Ntotal  = self.hm.get_nevents(self.sample.name,sys,mode)
            
            self.mc_lumi_frac[sys] = (xsec * feff * kfactor) / Ntotal if Ntotal else 0.0
        return self.mc_lumi_frac[sys]






#------------------------------------------------------------
class DataBkgSubEstimator(BaseEstimator):
    '''
    DataBkgSub Estimator class 
    subtracts bkgs from data for estimate
    '''
    #____________________________________________________________
    def __init__(self,data_sample,mc_samples,mc_samples_rescales,**kw):
        BaseEstimator.__init__(self,**kw)
        self.data_sample         = data_sample
        self.mc_samples          = mc_samples
        self.mc_samples_rescales = mc_samples_rescales
    #____________________________________________________________
    def __hist__(self,histname=None,region=None,icut=None,sys=None,mode=None):
        h = self.data_sample.hist(histname=histname,region=region,icut=icut,sys=sys,mode=mode).Clone()
        if self.mc_samples: 
            for s in self.mc_samples: 
                hs = s.hist(histname=histname,region=region,icut=icut,sys=sys,mode=mode)
                mc_rescale = -1.0
                if self.mc_samples_rescales: 
                  if s in self.mc_samples_rescales.keys():
                    mc_rescale *= self.mc_samples_rescales[s]
                if hs: h.Add(hs, mc_rescale)
        return h
    #__________________________________________________________________________
    def is_affected_by_systematic(self, sys):
        """
        Override BaseEstimator implemenation.
        Check all daughter systematics
        """
        if sys in self.allowed_systematics: return True
        for s in self.mc_samples + [self.data_sample]: 
            if s.estimator.is_affected_by_systematic(sys): return True
        return False
    #__________________________________________________________________________
    def flush_hists(self):
        BaseEstimator.flush_hists(self)
        self.data_sample.estimator.flush_hists()
        for s in self.mc_samples: 
            s.estimator.flush_hists() 



#------------------------------------------------------------
class AddRegEstimator(BaseEstimator):
    '''
    AddOnEstimator Estimator class. It estimates histograms by 
    adding and subtracting contributions from a given set of regions. 
    For fakes this scheme has a preconfigured structure.
    '''
    #____________________________________________________________
    def __init__(self,
            data_sample,
            mc_samples,
            addition_regions = [],
            subtraction_regions = [],
            **kw
            ):

        BaseEstimator.__init__(self,**kw)
        self.data_sample         = data_sample
        self.mc_samples          = mc_samples
        self.data_minus_mc       = DataBkgSubEstimator(self.data_sample,self.mc_samples,None,**kw)
        self.addition_regions    = addition_regions 
        self.subtraction_regions = subtraction_regions 
        
        assert self.addition_regions, "ERROR: must provide addition regions"

    #____________________________________________________________
    def __hist__(self,region=None,histname=None,icut=None,sys=None,mode=None):
        
        # ----------------
        # addition regions
        # ----------------
        h_addition = []

        for reg in self.addition_regions:
          if "fakes" in self.sample.name:
            h_data_minus_mc = self.data_minus_mc.hist(region=reg,histname=histname,icut=icut,sys=sys,mode=mode)
            if h_data_minus_mc: h_addition.append(h_data_minus_mc.Clone())
          
          elif "data" in self.sample.name:
            h_data = self.data_sample.hist(region=reg,histname=histname,icut=icut,sys=sys,mode=mode)
            if h_data: h_addition.append(h_data.Clone())
          
          elif self.sample.type == "mc":
            for mcs in self.mc_samples:
              if mcs.name in self.sample.name:
                h_mcs = mcs.hist(region=reg,histname=histname,icut=icut,sys=sys,mode=mode)
                if h_mcs: h_addition.append(h_mcs.Clone())

        # -------------------
        # subtraction regions
        # -------------------
        h_subtraction = []

        for reg in self.subtraction_regions:
          if "fakes" in self.sample.name:
            h_data_minus_mc = self.data_minus_mc.hist(region=reg,histname=histname,icut=icut,sys=sys,mode=mode)
            if h_data_minus_mc: h_subtraction.append(h_data_minus_mc.Clone())
          
          elif "data" in self.sample.name:
            h_data = self.data_sample.hist(region=reg,histname=histname,icut=icut,sys=sys,mode=mode)
            if h_data: h_subtraction.append(h_data.Clone())
          
          elif self.sample.type == "mc":
            for mcs in self.mc_samples:
              if mcs.name in self.sample.name:
                h_mcs = mcs.hist(region=reg,histname=histname,icut=icut,sys=sys,mode=mode)
                if h_mcs: h_subtraction.append(h_mcs.Clone())
       
        h = histutils.add_hists(h_addition)
        if h_subtraction:
         h.Add(histutils.add_hists(h_subtraction), -1.0)
       
        return h
    
    #__________________________________________________________________________
    def add_systematics(self, sys):
        if not isinstance(sys,list): sys = [sys]
        self.allowed_systematics += sys
        self.data_sample.estimator.add_systematics(sys)
        for s in self.mc_samples:
          s.estimator.add_systematics(sys) 
    
    #__________________________________________________________________________
    def is_affected_by_systematic(self, sys):
        if sys in self.allowed_systematics: return True
        for s in self.mc_samples + [self.data_sample]: 
            if s.estimator.is_affected_by_systematic(sys): return True
        return False
    #__________________________________________________________________________
    def flush_hists(self):
        BaseEstimator.flush_hists(self)
        self.data_sample.estimator.flush_hists()
        for s in self.mc_samples:
          s.estimator.flush_hists()


#------------------------------------------------------------
class MergeEstimator(BaseEstimator):
    '''
    Merge Estimator class 
    '''
    #____________________________________________________________
    def __init__(self,samples,**kw):
        BaseEstimator.__init__(self,**kw)
        self.samples = samples
    #____________________________________________________________
    def __hist__(self,region=None,icut=None,histname=None,sys=None,mode=None):
        hists = []
        for s in self.samples: 
            h = s.hist(region=region,icut=icut,histname=histname,sys=sys,mode=mode)
            if h: hists.append(h)
        h = histutils.add_hists(hists)
        return h

    #__________________________________________________________________________
    def add_systematics(self, sys):
        '''
        Override BaseEstimator implementation.
        Pass systematics to daughters.
        '''
        for s in self.samples: 
            s.estimator.add_systematics(sys)

    #__________________________________________________________________________
    def is_affected_by_systematic(self, sys):
        """
        Override BaseEstimator implemenation.
        Check all daughter systematics
        """
        for s in self.samples: 
            if s.estimator.is_affected_by_systematic(sys): return True
        return False

    #__________________________________________________________________________
    def flush_hists(self):
        BaseEstimator.flush_hists(self)
        for s in self.samples:
            s.estimator.flush_hists()


# - - - - - - - - - - function defs - - - - - - - - - - - - #
#____________________________________________________________
def load_base_estimator(hm,input_sample):
    '''
    Sets a standard Estimator for samples of type "mc" or "data".
    If sample has daughters, sets the MergeEstimator.
    '''
    if input_sample.estimator == None:

        if input_sample.daughters: 
             input_sample.estimator = MergeEstimator(
                     input_sample.daughters,
                     sample=input_sample,
                     hm=hm,
                     )
             #print 'sample %s, assigned MergeEstimator' % (input_sample.name)
             for d in input_sample.daughters:
                 load_base_estimator(hm,d)

        else: 
             #load estimators
             if input_sample.type in ["data","mc"]: 
                    input_sample.estimator = Estimator(hm=hm,sample=input_sample)
                    #print 'sample %s, assigned Estimator' % (input_sample.name)


#____________________________________________________________
def dir_name_max(filename, dirpath):
    '''
    gets the longest subdirectory in dirpath
    '''
    #f = fileio.open_file( filename )
    f = ROOT.TFile.Open( filename )
    assert f, 'failed to open file %s'%(filename)

    temp = None
    dir = f.GetDirectory(dirpath)
    if not dir:  
        log.warn( '%s doesn\'t exist in %s' % (dirpath,filename) )
    else:
        list = dir.GetListOfKeys()
        next = ROOT.TIter(list)
        d = next()
        temp = ''
        while d != None:
            if len(temp) < len(d.GetName()) and d.IsFolder():
                temp = d.GetName()
            d = next()
    f.Close()  
    return temp 


#____________________________________________________________
def dir_cuts(filename, dirpath):
    '''
    split dir name into individual cuts
    '''
    name = dir_name_max(filename,dirpath)
    return name.split('_')


#____________________________________________________________
def get_ncuts(filename, dirpath):
    cuts = dir_cuts(filename,dirpath)
    return len(cuts)

#____________________________________________________________
def get_icut(filename, dirpath,i):
    cuts = dir_cuts(filename,dirpath)
    if i>= len(cuts): 
        return None
    return cuts[i]

#____________________________________________________________
def get_icut_path(filename, dirpath,i):
    cuts = dir_cuts(filename,dirpath)
    if i >= len(cuts):
      return None
    return '_'.join(cuts[:i+1])
    

## EOF
