#!/usr/bin/python

import os
import subprocess
import time
from ssdilep import plots

def make_tag(cat,var):
  return '_'.join([cat,var])

#---------------------
# Set environment
#---------------------
# Environment variables defined in batchsetup.sh

ana     = 'ssdilep'

#RUN = "ptSlice"
#RUN = "ptSlice.noUnpres"
#RUN = "noUnpresc"
#RUN 	= "VeryLoose"
#RUN 	= "AtLeastLoose"
#RUN 	= ""
#RUN 	= "TwoSS"
RUN 	= "TwoOS"
#RUN = "NotMedium"
#RUN = "NotMediumAtLeastLoose"
#RUN = "oneTrack"
#RUN = "threeTrack"

indir   = 'jobs/SUSY11Data.v3.r1/Data/%s'%(RUN)
outdir  = 'jobs/SUSY11Data.v3.r1/FF/%s'%(RUN)

USER    = os.getenv('USER')
MAIN    = os.getenv('MAIN')

inpath  = os.path.join("/coepp/cephfs/mel",USER,"SSDiLep")
INDIR   = os.path.join(inpath,indir)  
OUTDIR  = os.path.join(inpath,outdir)

if not os.path.isdir(OUTDIR): os.makedirs(OUTDIR)
if not os.path.isdir(OUTDIR+"/"+"log"): os.makedirs(OUTDIR+"/"+"log")

#---------------------
# Batch jobs options
#---------------------
AUTOBUILD = True
QUEUE     = 'short'
BEXEC     = 'Plots.sh'
JOBDIR    = "/coepp/cephfs/mel/%s/jobdir" % USER

#---------------------
# Batch jobs variables
#---------------------
INTARBALL = os.path.join(JOBDIR,'plotstarball_%s.tar.gz' % (time.strftime("d%d_m%m_y%Y_H%H_M%M_S%S")) )
SCRIPT    = os.path.join("./",ana,"scripts",'merge.py')

job_vars={}
job_vars['INTARBALL'] = INTARBALL
job_vars['OUTDIR']    = OUTDIR
job_vars['INDIR']     = INDIR
job_vars['SCRIPT']    = SCRIPT

#fake_estimate = "AllRegions"
fake_estimate = "Subtraction"

regions = {}
# use it as such:
#regions["FOLDERNAME"]     = [icut, "plot label"]

TAG = "r1"

#--------------------------------------------------
# Single Tau
#--------------------------------------------------
#"""
regions["FAKES_NUM_F1"]   = [4,  "tight", TAG]
regions["FAKES_DEN_F1"]   = [4,  "loose", TAG]

regions["FAKES_NUM_F2"]   = [4,  "tight", TAG]
regions["FAKES_DEN_F2"]   = [4,  "loose", TAG]

regions["FAKES_NUM_F3"]   = [4,  "tight", TAG]
regions["FAKES_DEN_F3"]   = [4,  "loose", TAG]

regions["FAKES_NUM_F4"]   = [4,  "tight", TAG]
regions["FAKES_DEN_F4"]   = [4,  "loose", TAG]

regions["FAKES_NUM_F5"]   = [4,  "tight", TAG]
regions["FAKES_DEN_F5"]   = [4,  "loose", TAG]

regions["FAKES_NUM_F6"]   = [5,  "tight", TAG]
regions["FAKES_DEN_F6"]   = [5,  "loose", TAG]

regions["FAKES_NUM_F7"]   = [5,  "tight", TAG]
regions["FAKES_DEN_F7"]   = [5,  "loose", TAG]

regions["FAKES_NUM_F8"]   = [6,  "tight", TAG]
regions["FAKES_DEN_F8"]   = [6,  "loose", TAG]
#"""
"""
regions["FAKES_NUM_F1"]   = [4,  "tight", "LeadTauPt30"]
regions["FAKES_DEN_F1"]   = [4,  "loose", "LeadTauPt30"]

regions["FAKES_NUM_F2"]   = [4,  "tight", "LeadJetPt170"]
regions["FAKES_DEN_F2"]   = [4,  "loose", "LeadJetPt170"]

regions["FAKES_NUM_F3"]   = [4,  "tight", "LeadJetPt130"]
regions["FAKES_DEN_F3"]   = [4,  "loose", "LeadJetPt130"]

regions["FAKES_NUM_F4"]   = [4,  "tight", "dphi290"]
regions["FAKES_DEN_F4"]   = [4,  "loose", "dphi290"]

regions["FAKES_NUM_F5"]   = [4,  "tight", "dphi250"]
regions["FAKES_DEN_F5"]   = [4,  "loose", "dphi250"]

regions["FAKES_NUM_F6"]   = [5,  "tight", "TwoJet"]
regions["FAKES_DEN_F6"]   = [5,  "loose", "TwoJet"]

regions["FAKES_NUM_F7"]   = [5,  "tight", "ThreeJet"]
regions["FAKES_DEN_F7"]   = [5,  "loose", "ThreeJet"]
"""

#--------------------------------------------------
# Two Taus
#--------------------------------------------------
"""
regions["FAKES_NUM_F1"]   = [7,  "tight", TAG]
regions["FAKES_DEN_F1"]   = [7,  "loose", TAG]

regions["FAKES_NUM_F2"]   = [6,  "tight", TAG]
regions["FAKES_DEN_F2"]   = [6,  "loose", TAG]

regions["FAKES_NUM_F3"]   = [6,  "tight", TAG]
regions["FAKES_DEN_F3"]   = [6,  "loose", TAG]

regions["FAKES_NUM_F4"]   = [6,  "tight", TAG]
regions["FAKES_DEN_F4"]   = [6,  "loose", TAG]

regions["FAKES_NUM_F5"]   = [6,  "tight", TAG]
regions["FAKES_DEN_F5"]   = [6,  "loose", TAG]

regions["FAKES_NUM_F6"]   = [7,  "tight", TAG]
regions["FAKES_DEN_F6"]   = [7,  "loose", TAG]

regions["FAKES_NUM_F7"]   = [7,  "tight", TAG]
regions["FAKES_DEN_F7"]   = [7,  "loose", TAG]

regions["FAKES_NUM_F8"]   = [8,  "tight", TAG]
regions["FAKES_DEN_F8"]   = [8,  "loose", TAG]

"""
"""
regions["FAKES_NUM_F1"]   = [6,  "tight", "LeadTauPt30"]
regions["FAKES_DEN_F1"]   = [6,  "loose", "LeadTauPt30"]

regions["FAKES_NUM_F2"]   = [6,  "tight", "LeadJetPt170"]
regions["FAKES_DEN_F2"]   = [6,  "loose", "LeadJetPt170"]

regions["FAKES_NUM_F3"]   = [6,  "tight", "LeadJetPt130"]
regions["FAKES_DEN_F3"]   = [6,  "loose", "LeadJetPt130"]

regions["FAKES_NUM_F4"]   = [6,  "tight", "dphi290"]
regions["FAKES_DEN_F4"]   = [6,  "loose", "dphi290"]

regions["FAKES_NUM_F5"]   = [6,  "tight", "dphi250"]
regions["FAKES_DEN_F5"]   = [6,  "loose", "dphi250"]

regions["FAKES_NUM_F6"]   = [7,  "tight", "TwoJet"]
regions["FAKES_DEN_F6"]   = [7,  "loose", "TwoJet"]

regions["FAKES_NUM_F7"]   = [7,  "tight", "ThreeJet"]
regions["FAKES_DEN_F7"]   = [7,  "loose", "ThreeJet"]
"""

#---------------------
# Make input tarball
#---------------------
if os.path.exists(os.path.join(INTARBALL)):
  print 'removing existing tarball %s...'% (INTARBALL)
  cmd = 'rm %s' % (INTARBALL)
  m = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
  m.communicate()[0]

print 'building input tarball %s...'% (INTARBALL)
cmd = 'cd %s; make -f Makefile.plots TARBALL=%s' % (MAIN,INTARBALL)
m = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
m.communicate()[0]


for REG,OPT in regions.iteritems():
  vars_list = plots.vars_mumu.vars_list
  #vars_list = plots.vars_fakes.vars_list

  for var in vars_list:

    job_vars['VAR']      = var.name
    job_vars['REG']      = REG
    job_vars['ICUT']     = OPT[0]
    job_vars['LAB']      = OPT[1]
    job_vars['TAG']      = OPT[2]
    job_vars['MAKEPLOT'] = False
    job_vars['FAKEST']   = "Subtraction"
    
    VARS = []
    
    for vname in job_vars.keys(): VARS += ['%s=%s' % (vname,job_vars[vname])]
    
    cmd = 'qsub'
    cmd += " -q %s" % QUEUE
    cmd += ' -v "%s"' % (','.join(VARS))
    cmd += ' -N j.plots.%s' % (make_tag(REG,job_vars['VAR']))
    cmd += ' -o %s/log' % (OUTDIR)
    cmd += ' -e %s/log' % (OUTDIR)
    cmd += ' %s' % BEXEC
    print cmd
    m = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
    print m.communicate()[0]
 
 
## EOF

