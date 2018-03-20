# encoding: utf-8
'''
SubmitHist.py
'''

## modules
import os
import re
import subprocess
import time
import math
from   ssdilep.samples import samples

import ROOT

## environment variables
MAIN   = os.getenv('MAIN') # upper folder
USER   = os.getenv('USER')

## global config
# inputs
#NTUP='/coepp/cephfs/mel/fscutti/ssdilep/HIGG3D3_v12/merged' # input NTUP path

#NTUP='/coepp/cephfs/mel/fscutti/ssdilep/HIGG3D3_v7/merged' # input NTUP path
#NTUP='/coepp/cephfs/mel/fscutti/ssdilep/HIGG3D3_v8/merged' # input NTUP path
#NTUP='/coepp/cephfs/mel/fscutti/ssdilep/HIGG3D3_v12/merged' # input NTUP path
NTUPDATA='/coepp/cephfs/share/atlas/SSDiLep/SUSY11Data.v3.r1/merged'


JOBDIR = "/coepp/cephfs/mel/%s/jobdir" % USER # Alright this is twisted...
INTARBALL = os.path.join(JOBDIR,'histtarball_%s.tar.gz' % (time.strftime("d%d_m%m_y%Y_H%H_M%M_S%S")) )

AUTOBUILD = True                # auto-build tarball using Makefile.tarball

# outputs
#RUN = "VeryLoose"
#RUN = "AtLeastLoose"
#RUN = "ptRatio"
#RUN = "TwoSS"
#RUN = "TwoOS"
#RUN = "NotMedium"
#RUN = "NotMediumAtLeastLoose"
#RUN = "LeadTauPt65AtLeastLoose"
#RUN = "LeadTauPt65NotTight"
#RUN = "oneTrack"
#RUN = "threeTrack"

#RUN = "ptSlice"
RUN = "ptSlice.noUnpres"
#RUN = "noUnpresc"

OUTPATH="/coepp/cephfs/mel/%s/SSDiLep/jobs/SUSY11Data.v3.r1/Data/%s"%(USER,RUN) # 

# running
QUEUE="long"                        # length of pbs queue (short, long, extralong )

# pick your script!!!
SCRIPT="./ssdilep/run/j.plotter_TauFF.py"  
#SCRIPT="./ssdilep/run/j.plotter_TwoTauFF.py "
#SCRIPT="./ssdilep/run/j.plotter_TAndP.py"  
#SCRIPT="./ssdilep/run/j.plotter_VR_OneMuPair.py"  

#SCRIPT="./ssdilep/run/j.plotter_VR3.py"  

BEXEC="Hist.sh"                      # exec script (probably dont change) 

EVENT_BLOCK = 50000                 # number of events considered for each individual job
NJMAX       = 500                    # maximum number of jobs per train: should not exceed 600!!!

DO_NOM = True                        # submit the nominal job
DO_NTUP_SYS = False                  # submit the NTUP systematics jobs
DO_PLOT_SYS = False                 # submit the plot systematics jobs
TESTMODE = False                    # submit only 1 sub-job (for testing)

NCORES = 1

def main():
    """
    * configure the samples (input->output)
    * configure which samples to run for each systematic
    * prepare outdirs and build intarball
    * launch the jobs
    """
    global MAIN
    global USER
    global NTUPDATA
    global NTUPMC
    global INTARBALL
    global AUTOBUILD
    global RUN
    global OUTPATH
    global QUEUE
    global SCRIPT
    global BEXEC
    global DO_NOM
    global DO_NTUP_SYS
    global DO_PLOT_SYS
    global TESTMODE

    ## get lists of samples
    all_data = samples.all_data
    all_mc   = samples.all_mc

    nominal = all_data + all_mc 
    #nominal = all_data 
    #nominal = all_mc 

    
    ntup_sys = [
        ['SYS1_UP',                  all_mc],
        ['SYS1_DN',                  all_mc],
        ]    
    
    plot_sys = [
        ['FF_UP',        all_data + all_mc],
        ['FF_DN',        all_data + all_mc],
        ]    
    
    all_sys = ntup_sys + plot_sys

    ## ensure output path exists
    prepare_path(OUTPATH)
    
    ## auto-build tarball
    if AUTOBUILD:
        print 'building input tarball %s...'% (INTARBALL)
        cmd = 'cd %s; make -f Makefile.hist TARBALL=%s' % (MAIN,INTARBALL)
        m = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
        print m.communicate()[0]

    if DO_NOM: submit('nominal','nominal',nominal)
    if DO_NTUP_SYS: 
      for sys,samps in ntup_sys:
            submit(sys,sys,samps)
    if DO_PLOT_SYS:  
      for sys,samps in plot_sys:
            submit(sys,'nominal',samps,config={'sys':sys})


def submit(tag,job_sys,samps,config={}):
    """
    * construct config file 
    * prepare variable list to pass to job
    * submit job
    """
    global MAIN
    global USER
    global NTUPDATA
    global NTUPMC
    global INTARBALL
    global AUTOBUILD
    global RUN
    global OUTPATH
    global QUEUE
    global SCRIPT
    global BEXEC
    global DO_NOM
    global DO_NTUP_SYS
    global DO_PLOT_SYS
    global TESTMODE

    assert (NJMAX<=600), "Error: please, not more than 600 subjobs per array!"

    # configure output path 
    # ---------------------
    absoutpath = os.path.abspath(os.path.join(OUTPATH,tag))
    abslogpath = os.path.abspath(os.path.join(OUTPATH,'log_%s'%tag))
    
    ## construct config file
    # ----------------------
    
    nsubjobs = 0

    #cfg = os.path.join(JOBDIR,'Config%s.%s'%(RUN,tag))
    cfg = 'Config%s.%s'%(RUN,tag)
    cfg_dict = {}

    for s in samps:

        ## input & output
        sinput = input_file(s,job_sys) 
        soutput = output_file(s,job_sys) 

        #print sinput
        #print soutput

        finput   =  ROOT.TFile.Open(sinput,"READ")
        f_tree   = finput.Get("physics/nominal")
        f_events = f_tree.GetEntries()

        number_of_slices = int(math.ceil(f_events / float(EVENT_BLOCK)))

        ## sample type
        stype  = s.type

        ## config
        sconfig = {}
        sconfig.update(config)
        sconfig.update(s.config)
        sconfig_str = ",".join(["%s:%s"%(key,val) for key,val in sconfig.items()])
        
        
        for sl in xrange(number_of_slices):
          
          soutput_sliced = soutput.replace(".root","_slice%s"%sl)
          sname = s.name+"_slice%s"%sl
          line = ';'.join([sname,sinput,soutput_sliced+".root",stype, str(sl * EVENT_BLOCK + min(1,sl)), str((sl+1) * EVENT_BLOCK),sconfig_str])
          nsubjobs += 1
          
          cfg_name = cfg+".%s.%s"%(RUN,int(nsubjobs/NJMAX))

          if not cfg_name in cfg_dict.keys(): 
            cfg_dict[cfg_name] = {"nsubjobs":1,"sliced_sample":[soutput_sliced]}
          else: 
            cfg_dict[cfg_name]["nsubjobs"] += 1
            cfg_dict[cfg_name]["sliced_sample"] += [soutput_sliced]
          
          with open(os.path.join(JOBDIR,cfg_name),'a') as f:
            f.write('%s\n'%line)
            f.close()
          #if not file_exists(absoutpath,s.name+".root"): f.write('%s\n'%line) 
   

    # configure input path 
    # --------------------
    absintar   = os.path.abspath(INTARBALL)
    prepare_path(absoutpath)
    prepare_path(abslogpath)

    for cfg_file,cfg_listing in cfg_dict.iteritems():

       abscfg     = os.path.abspath(os.path.join(JOBDIR,cfg_file))
       nsubjobs   = cfg_listing["nsubjobs"]
       if TESTMODE: nsubjobs = 1
       
       vars=[]
       vars+=["CONFIG=%s"    % abscfg     ]
       vars+=["INTARBALL=%s" % absintar   ]
       vars+=["OUTPATH=%s"   % absoutpath ]
       vars+=["SCRIPT=%s"    % SCRIPT     ]
       vars+=["NCORES=%d"    % NCORES     ]
       
       VARS = ','.join(vars)
       
       cmd = 'qsub'
       cmd += ' -l nodes=1:ppn=%d'  % NCORES
       cmd += ' -q %s'              % QUEUE
       cmd += ' -v "%s"'            % VARS
       cmd += ' -N j.hist.%s.%s'    % (tag,cfg_file)
       cmd += ' -j oe -o %s/log_%s' % (abslogpath, cfg_file)
       cmd += ' -t1-%d'             % nsubjobs
       cmd += ' %s'                 % BEXEC
       print cmd
       m = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
       print m.communicate()[0]

def prepare_path(path):
    if not os.path.exists(path):
        print 'preparing outpath: %s'%(path)
        os.makedirs(path)

def input_file(sample,sys):
    global NTUPDATA
    global NTUPMC
    sinput = sample.infile
    
    if sys!='nominal': sys='sys_'+sys
    sinput += '.root'
    if sample.type == "mc":
      sinput = os.path.join(NTUPMC,sys,sinput) 
    if sample.type == "data":
      sinput = os.path.join(NTUPDATA,sys,sinput) 
    return sinput

def file_exists(path,file):
    if os.path.exists(path):
      return file in os.listdir(os.path.join(path))
    else: return False

def output_file(sample,sys):
    soutput = sample.name
    soutput += '.root'
    return soutput

if __name__=='__main__': main()


## EOF
